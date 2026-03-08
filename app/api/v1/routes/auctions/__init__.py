"""
Auction Routes Module

Combines all auction-related endpoints.
"""

from fastapi import APIRouter
from app.api.v1.routes.auctions import auction_crud, auction_bidding, ws_auction


router = APIRouter()

# Include auction endpoints
router.include_router(auction_crud.router, tags=["Auctions"])

# Include bidding endpoints
router.include_router(auction_bidding.router, tags=["Auctions - Bidding"])

# Include WebSocket endpoints
router.include_router(ws_auction.router, tags=["Auctions - WebSocket"])
