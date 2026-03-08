"""
Auction Bidding REST API Endpoints

REST endpoints for bid operations (non-WebSocket).
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.core.dependencies import get_db, get_current_user
from app.models.user import User
from app.schemas.bid import BidResponse, BidHistoryResponse, PlaceBidRequest
from app.services.bid_service import BidService

router = APIRouter()


@router.get("/auctions/{auction_id}/bids", response_model=List[BidResponse])
def get_auction_bids(
    auction_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(50, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get all bids for an auction.

    Returns bid history ordered by most recent first.
    """
    bids = BidService.get_bid_history(
        db=db,
        auction_id=auction_id,
        limit=limit
    )
    return bids


@router.get("/auctions/{auction_id}/players/{player_id}/bids", response_model=BidHistoryResponse)
def get_player_bids(
    auction_id: int,
    player_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(50, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get bid history for a specific player in an auction.

    Returns:
    - List of all bids for the player
    - Total bid count
    - Current highest bid
    """
    bids = BidService.get_bid_history(
        db=db,
        auction_id=auction_id,
        player_id=player_id,
        limit=limit
    )

    current_bid = BidService.get_current_bid(
        db=db,
        auction_id=auction_id,
        player_id=player_id
    )

    return BidHistoryResponse(
        bids=bids,
        total=len(bids),
        current_highest_bid=current_bid
    )


@router.get("/auctions/{auction_id}/teams/{team_id}/bids", response_model=List[BidResponse])
def get_team_bids(
    auction_id: int,
    team_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(50, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get all bids placed by a specific team in an auction.

    Useful for team owners to see their bidding history.
    """
    bids = BidService.get_bid_history(
        db=db,
        auction_id=auction_id,
        team_id=team_id,
        limit=limit
    )
    return bids


@router.get("/auctions/{auction_id}/players/{player_id}/current-bid", response_model=Optional[BidResponse])
def get_current_bid_for_player(
    auction_id: int,
    player_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get the current winning bid for a player.

    Returns None if no bids have been placed yet.
    """
    current_bid = BidService.get_current_bid(
        db=db,
        auction_id=auction_id,
        player_id=player_id
    )
    return current_bid


@router.post("/auctions/{auction_id}/players/{player_id}/mark-sold")
def mark_player_sold(
    auction_id: int,
    player_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Mark a player as sold to the highest bidder.

    Only admin/auctioneer can perform this action.
    Updates:
    - Player: is_sold, final_price, team_id
    - Team: remaining_budget, current_players, overseas_count
    """
    result = BidService.mark_player_sold(
        db=db,
        auction_id=auction_id,
        player_id=player_id,
        current_user=current_user
    )

    # Broadcast to WebSocket clients
    from app.core.websocket_manager import manager
    import asyncio

    async def broadcast_sold():
        await manager.broadcast_player_sold(
            auction_id=auction_id,
            player_data={
                "player_id": result["player"].id,
                "player_name": result["player"].name,
                "team_id": result["team"].id,
                "team_name": result["team"].name,
                "final_price": result["final_price"]
            }
        )

        # Also broadcast budget update
        await manager.broadcast_budget_update(
            auction_id=auction_id,
            team_id=result["team"].id,
            remaining_budget=result["team"].remaining_budget,
            current_players=result["team"].current_players
        )

    # Run broadcast in background
    asyncio.create_task(broadcast_sold())

    return {
        "message": "Player marked as sold successfully",
        "player": {
            "id": result["player"].id,
            "name": result["player"].name,
            "final_price": result["final_price"]
        },
        "team": {
            "id": result["team"].id,
            "name": result["team"].name,
            "remaining_budget": result["team"].remaining_budget,
            "current_players": result["team"].current_players
        }
    }


@router.post("/auctions/{auction_id}/players/{player_id}/mark-unsold")
def mark_player_unsold(
    auction_id: int,
    player_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Mark a player as unsold.

    Only admin/auctioneer can perform this action.
    Clears player's team assignment and final price.
    """
    player = BidService.mark_player_unsold(
        db=db,
        auction_id=auction_id,
        player_id=player_id,
        current_user=current_user
    )

    # Broadcast to WebSocket clients
    from app.core.websocket_manager import manager
    import asyncio

    async def broadcast_unsold():
        await manager.broadcast_player_unsold(
            auction_id=auction_id,
            player_data={
                "player_id": player.id,
                "player_name": player.name
            }
        )

    # Run broadcast in background
    asyncio.create_task(broadcast_unsold())

    return {
        "message": "Player marked as unsold",
        "player": {
            "id": player.id,
            "name": player.name,
            "is_sold": player.is_sold
        }
    }


@router.post("/auctions/{auction_id}/teams/{team_id}/place-bid", response_model=BidResponse)
def place_bid_rest(
    auction_id: int,
    team_id: int,
    bid_data: PlaceBidRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Place a bid via REST API (alternative to WebSocket).

    This endpoint is provided for compatibility, but WebSocket
    is recommended for real-time bidding experience.
    """
    new_bid = BidService.place_bid(
        db=db,
        auction_id=auction_id,
        bid_data=bid_data,
        team_id=team_id,
        current_user=current_user
    )

    # Broadcast to WebSocket clients
    from app.core.websocket_manager import manager
    import asyncio

    async def broadcast_bid():
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

        await manager.broadcast_bid(
            auction_id=auction_id,
            bid_data=bid_response
        )

    # Run broadcast in background
    asyncio.create_task(broadcast_bid())

    return new_bid
