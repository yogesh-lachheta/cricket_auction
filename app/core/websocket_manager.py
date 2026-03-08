"""
WebSocket Connection Manager

Manages WebSocket connections for real-time auction updates.
"""

from typing import Dict, List, Set
from fastapi import WebSocket
import json
import logging

logger = logging.getLogger(__name__)


class ConnectionManager:
    """Manages WebSocket connections for auctions"""

    def __init__(self):
        # auction_id -> list of WebSocket connections
        self.active_connections: Dict[int, List[WebSocket]] = {}
        # websocket -> user_id mapping
        self.connection_users: Dict[WebSocket, int] = {}

    async def connect(self, websocket: WebSocket, auction_id: int, user_id: int):
        """
        Connect a user to an auction room.

        Args:
            websocket: WebSocket connection
            auction_id: Auction ID to join
            user_id: User ID connecting
        """
        await websocket.accept()

        if auction_id not in self.active_connections:
            self.active_connections[auction_id] = []

        self.active_connections[auction_id].append(websocket)
        self.connection_users[websocket] = user_id

        logger.info(f"User {user_id} connected to auction {auction_id}")
        logger.info(f"Total connections for auction {auction_id}: {len(self.active_connections[auction_id])}")

    def disconnect(self, websocket: WebSocket, auction_id: int):
        """
        Disconnect a user from an auction room.

        Args:
            websocket: WebSocket connection to remove
            auction_id: Auction ID to disconnect from
        """
        if auction_id in self.active_connections:
            if websocket in self.active_connections[auction_id]:
                self.active_connections[auction_id].remove(websocket)
                user_id = self.connection_users.get(websocket)
                logger.info(f"User {user_id} disconnected from auction {auction_id}")

                # Clean up empty auction rooms
                if not self.active_connections[auction_id]:
                    del self.active_connections[auction_id]

        # Remove from user mapping
        if websocket in self.connection_users:
            del self.connection_users[websocket]

    async def send_personal_message(self, message: dict, websocket: WebSocket):
        """
        Send a message to a specific connection.

        Args:
            message: Message dictionary to send
            websocket: Target WebSocket connection
        """
        try:
            await websocket.send_json(message)
        except Exception as e:
            logger.error(f"Error sending personal message: {e}")

    async def broadcast(self, auction_id: int, message: dict, exclude: WebSocket = None):
        """
        Broadcast a message to all connections in an auction room.

        Args:
            auction_id: Auction ID to broadcast to
            message: Message dictionary to broadcast
            exclude: Optional WebSocket to exclude from broadcast
        """
        if auction_id not in self.active_connections:
            logger.warning(f"No active connections for auction {auction_id}")
            return

        disconnected = []

        for connection in self.active_connections[auction_id]:
            if connection == exclude:
                continue

            try:
                await connection.send_json(message)
            except Exception as e:
                logger.error(f"Error broadcasting to connection: {e}")
                disconnected.append(connection)

        # Clean up disconnected connections
        for connection in disconnected:
            self.disconnect(connection, auction_id)

    async def broadcast_bid(
        self,
        auction_id: int,
        bid_data: dict,
        exclude: WebSocket = None
    ):
        """
        Broadcast a new bid to all users in the auction.

        Args:
            auction_id: Auction ID
            bid_data: Bid information
            exclude: Optional WebSocket to exclude
        """
        message = {
            "type": "new_bid",
            "data": bid_data
        }
        await self.broadcast(auction_id, message, exclude)

    async def broadcast_player_sold(
        self,
        auction_id: int,
        player_data: dict
    ):
        """
        Broadcast that a player has been sold.

        Args:
            auction_id: Auction ID
            player_data: Player and sale information
        """
        message = {
            "type": "player_sold",
            "data": player_data
        }
        await self.broadcast(auction_id, message)

    async def broadcast_player_unsold(
        self,
        auction_id: int,
        player_data: dict
    ):
        """
        Broadcast that a player is unsold.

        Args:
            auction_id: Auction ID
            player_data: Player information
        """
        message = {
            "type": "player_unsold",
            "data": player_data
        }
        await self.broadcast(auction_id, message)

    async def broadcast_auction_status(
        self,
        auction_id: int,
        status: str,
        current_player_id: int = None
    ):
        """
        Broadcast auction status change (started, paused, resumed, completed).

        Args:
            auction_id: Auction ID
            status: New status
            current_player_id: Current player being auctioned
        """
        message = {
            "type": "auction_status",
            "data": {
                "status": status,
                "current_player_id": current_player_id
            }
        }
        await self.broadcast(auction_id, message)

    async def broadcast_budget_update(
        self,
        auction_id: int,
        team_id: int,
        remaining_budget: float,
        current_players: int
    ):
        """
        Broadcast team budget update.

        Args:
            auction_id: Auction ID
            team_id: Team ID
            remaining_budget: Updated budget
            current_players: Updated player count
        """
        message = {
            "type": "budget_update",
            "data": {
                "team_id": team_id,
                "remaining_budget": remaining_budget,
                "current_players": current_players
            }
        }
        await self.broadcast(auction_id, message)

    def get_connection_count(self, auction_id: int) -> int:
        """Get number of active connections for an auction"""
        return len(self.active_connections.get(auction_id, []))


# Global instance
manager = ConnectionManager()
