"""
Bid Pydantic Schemas

These schemas define the structure for bid-related requests and responses.
"""

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field, field_validator


class BidBase(BaseModel):
    """Base Bid schema with common fields"""
    auction_id: int = Field(..., description="Auction ID")
    player_id: int = Field(..., description="Player ID being bid on")
    team_id: int = Field(..., description="Team ID placing the bid")
    bid_amount: float = Field(..., gt=0, description="Bid amount (must be positive)")

    @field_validator("bid_amount")
    @classmethod
    def validate_bid_amount(cls, v):
        """Validate that bid amount is reasonable"""
        if v <= 0:
            raise ValueError("Bid amount must be positive")
        if v > 1000000000:  # 100 crore max
            raise ValueError("Bid amount cannot exceed 100 crore")
        return v


class BidCreate(BidBase):
    """Schema for creating a new bid"""
    pass


class BidUpdate(BaseModel):
    """Schema for updating bid information"""
    is_winning_bid: Optional[bool] = None


class BidInDB(BidBase):
    """Schema for bid data as stored in database"""
    id: int
    is_winning_bid: bool
    created_at: datetime

    class Config:
        from_attributes = True


class BidResponse(BidInDB):
    """
    Schema for bid data in API responses.
    Includes related team and player information.
    """
    team: Optional[dict] = None
    player: Optional[dict] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "auction_id": 1,
                "player_id": 5,
                "team_id": 2,
                "bid_amount": 15000000.0,
                "is_winning_bid": True,
                "created_at": "2024-01-01T10:30:00Z",
                "team": {
                    "id": 2,
                    "name": "Mumbai Indians",
                    "short_name": "MI"
                },
                "player": {
                    "id": 5,
                    "name": "Virat Kohli",
                    "role": "Batsman"
                }
            }
        }


class PlaceBidRequest(BaseModel):
    """Schema for placing a bid via WebSocket or REST API"""
    player_id: int = Field(..., description="Player ID to bid on")
    bid_amount: float = Field(..., gt=0, description="Bid amount")

    @field_validator("bid_amount")
    @classmethod
    def validate_bid_amount(cls, v):
        """Validate bid amount"""
        if v <= 0:
            raise ValueError("Bid amount must be positive")
        if v > 1000000000:
            raise ValueError("Bid amount cannot exceed 100 crore")
        # Validate increment (must be multiple of 50000 - 50 lakh)
        if v % 500000 != 0:
            raise ValueError("Bid amount must be in multiples of ₹50 lakh")
        return v


class BidHistoryResponse(BaseModel):
    """Schema for bid history"""
    bids: List[BidResponse]
    total: int
    current_highest_bid: Optional[BidResponse] = None
