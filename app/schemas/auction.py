"""
Auction Pydantic Schemas
These schemas define the structure for auction-related requests and responses.
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, field_validator
from enum import Enum


class AuctionStatusEnum(str, Enum):
    """Auction status enumeration"""
    UPCOMING = "upcoming"
    LIVE = "live"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class AuctionBase(BaseModel):
    """Base Auction schema with common fields"""
    title: str = Field(..., min_length=3, max_length=200, description="Auction title")
    description: Optional[str] = Field(None, max_length=1000, description="Auction description")
    total_budget_per_team: float = Field(..., gt=0, description="Budget per team (must be positive)")
    max_teams: int = Field(default=8, ge=2, le=16, description="Maximum teams allowed (2-16)")
    max_players_per_team: int = Field(default=15, ge=11, le=25, description="Max players per team (11-25)")
    start_time: Optional[datetime] = Field(None, description="Auction start time")
    end_time: Optional[datetime] = Field(None, description="Auction end time")

    @field_validator("total_budget_per_team")
    @classmethod
    def validate_budget(cls, v):
        """Validate that budget is reasonable"""
        if v <= 0:
            raise ValueError("Budget must be positive")
        if v > 10000000000:  # 1000 crore max
            raise ValueError("Budget cannot exceed 1000 crore")
        return v

    @field_validator("end_time")
    @classmethod
    def validate_end_time(cls, v, info):
        """Validate end time is after start time"""
        if v is not None and info.data.get('start_time') is not None:
            if v <= info.data['start_time']:
                raise ValueError("End time must be after start time")
        return v


class AuctionCreate(AuctionBase):
    """Schema for creating a new auction"""
    created_by: Optional[int] = Field(None, description="User ID who created the auction")


class AuctionUpdate(BaseModel):
    """Schema for updating auction information"""
    title: Optional[str] = Field(None, min_length=3, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[AuctionStatusEnum] = None
    total_budget_per_team: Optional[float] = Field(None, gt=0)
    max_teams: Optional[int] = Field(None, ge=2, le=16)
    max_players_per_team: Optional[int] = Field(None, ge=11, le=25)
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    is_active: Optional[bool] = None

    @field_validator("end_time")
    @classmethod
    def validate_end_time(cls, v, info):
        """Validate end time is after start time"""
        if v is not None and info.data.get('start_time') is not None:
            if v <= info.data['start_time']:
                raise ValueError("End time must be after start time")
        return v


class AuctionInDB(AuctionBase):
    """Schema for auction stored in database"""
    id: int
    status: AuctionStatusEnum
    is_active: bool
    created_by: Optional[int]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AuctionResponse(AuctionInDB):
    """Schema for auction API response"""
    pass


# ==========================================
# Bid Schemas
# ==========================================

class BidBase(BaseModel):
    """Base Bid schema with common fields"""
    auction_id: int = Field(..., description="Auction ID")
    player_id: int = Field(..., description="Player ID being bid on")
    team_id: int = Field(..., description="Team ID placing the bid")
    bid_amount: float = Field(..., gt=0, description="Bid amount (must be positive)")


class BidCreate(BidBase):
    """Schema for creating a new bid"""
    pass


class BidUpdate(BaseModel):
    """Schema for updating bid information"""
    is_winning_bid: Optional[bool] = None


class BidInDB(BidBase):
    """Schema for bid stored in database"""
    id: int
    is_winning_bid: bool
    created_at: datetime

    class Config:
        from_attributes = True


class BidResponse(BidInDB):
    """Schema for bid API response"""
    pass
