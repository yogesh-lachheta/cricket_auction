"""
Auction Routes Module

Combines all auction-related endpoints.
"""

from fastapi import APIRouter
from app.api.v1.routes.auctions import auction_crud


router = APIRouter()

# Include auction endpoints
router.include_router(auction_crud.router, tags=["Auctions"])
