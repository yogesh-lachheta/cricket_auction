"""
WebSocket Auction Endpoints

Real-time WebSocket endpoints for live auction bidding.
"""

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
import logging
from typing import Optional

from app.core.dependencies import get_db
from app.core.websocket_manager import manager
from app.core.security import get_current_user_ws
from app.models.user import User
from app.models.auction import Auction, AuctionStatus
from app.services.bid_service import BidService
from app.schemas.bid import PlaceBidRequest
import json

logger = logging.getLogger(__name__)

router = APIRouter()


@router.websocket("/auctions/{auction_id}/ws")
async def websocket_auction_endpoint(
    websocket: WebSocket,
    auction_id: int,
    token: str = Query(...),
    db: Session = Depends(get_db)
):
    """
    WebSocket endpoint for real-time auction updates.

    Clients connect with their JWT token and receive:
    - New bids from other teams
    - Player sold/unsold notifications
    - Auction status changes
    - Budget updates

    Message Types (Server -> Client):
    - new_bid: {"type": "new_bid", "data": {...}}
    - player_sold: {"type": "player_sold", "data": {...}}
    - player_unsold: {"type": "player_unsold", "data": {...}}
    - auction_status: {"type": "auction_status", "data": {...}}
    - budget_update: {"type": "budget_update", "data": {...}}
    - error: {"type": "error", "message": "..."}

    Message Types (Client -> Server):
    - place_bid: {"action": "place_bid", "player_id": 1, "team_id": 2, "bid_amount": 15000000}
    - ping: {"action": "ping"} -> responds with {"type": "pong"}
    """
    # Authenticate user via token
    try:
        current_user = await get_current_user_ws(token, db)
    except Exception as e:
        logger.error(f"WebSocket authentication failed: {e}")
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    # Verify auction exists
    auction = db.query(Auction).filter(Auction.id == auction_id).first()
    if not auction:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    # Connect to auction room
    await manager.connect(websocket, auction_id, current_user.id)

    try:
        # Send connection success message
        await manager.send_personal_message({
            "type": "connected",
            "message": f"Connected to auction {auction.name}",
            "auction_id": auction_id,
            "user_id": current_user.id,
            "user_name": current_user.full_name,
            "auction_status": auction.status.value
        }, websocket)

        # Broadcast user joined (optional - can be removed if not needed)
        # await manager.broadcast(auction_id, {
        #     "type": "user_joined",
        #     "user_name": current_user.full_name
        # }, exclude=websocket)

        # Listen for messages from client
        while True:
            data = await websocket.receive_json()

            action = data.get("action")

            if action == "ping":
                await manager.send_personal_message({"type": "pong"}, websocket)

            elif action == "place_bid":
                # Handle bid placement
                try:
                    player_id = data.get("player_id")
                    team_id = data.get("team_id")
                    bid_amount = data.get("bid_amount")

                    if not all([player_id, team_id, bid_amount]):
                        await manager.send_personal_message({
                            "type": "error",
                            "message": "Missing required fields: player_id, team_id, bid_amount"
                        }, websocket)
                        continue

                    # Create bid request
                    bid_data = PlaceBidRequest(
                        player_id=player_id,
                        bid_amount=bid_amount
                    )

                    # Place bid using service
                    new_bid = BidService.place_bid(
                        db=db,
                        auction_id=auction_id,
                        bid_data=bid_data,
                        team_id=team_id,
                        current_user=current_user
                    )

                    # Prepare bid response
                    bid_response = {
                        "id": new_bid.id,
                        "auction_id": new_bid.auction_id,
                        "player_id": new_bid.player_id,
                        "team_id": new_bid.team_id,
                        "bid_amount": new_bid.bid_amount,
                        "is_winning_bid": new_bid.is_winning_bid,
                        "created_at": new_bid.created_at.isoformat(),
                        "team": {
                            "id": new_bid.team.id,
                            "name": new_bid.team.name,
                            "short_name": new_bid.team.short_name
                        } if new_bid.team else None,
                        "player": {
                            "id": new_bid.player.id,
                            "name": new_bid.player.name,
                            "role": new_bid.player.role
                        } if new_bid.player else None
                    }

                    # Send success to bidder
                    await manager.send_personal_message({
                        "type": "bid_placed",
                        "message": "Bid placed successfully",
                        "data": bid_response
                    }, websocket)

                    # Broadcast to all other users
                    await manager.broadcast_bid(
                        auction_id=auction_id,
                        bid_data=bid_response,
                        exclude=websocket
                    )

                except HTTPException as e:
                    await manager.send_personal_message({
                        "type": "error",
                        "message": e.detail
                    }, websocket)
                except Exception as e:
                    logger.error(f"Error placing bid: {e}")
                    await manager.send_personal_message({
                        "type": "error",
                        "message": "Failed to place bid"
                    }, websocket)

            else:
                await manager.send_personal_message({
                    "type": "error",
                    "message": f"Unknown action: {action}"
                }, websocket)

    except WebSocketDisconnect:
        manager.disconnect(websocket, auction_id)
        logger.info(f"User {current_user.id} disconnected from auction {auction_id}")
        # Optionally broadcast user left
        # await manager.broadcast(auction_id, {
        #     "type": "user_left",
        #     "user_name": current_user.full_name
        # })
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        manager.disconnect(websocket, auction_id)
