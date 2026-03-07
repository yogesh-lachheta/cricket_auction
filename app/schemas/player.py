"""
Player Pydantic Schemas

These schemas define the structure for player-related requests and responses.
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, field_validator
from enum import Enum


class PlayerRoleEnum(str, Enum):
    """Player role enumeration"""
    BATSMAN = "batsman"
    BOWLER = "bowler"
    ALL_ROUNDER = "all_rounder"
    WICKET_KEEPER = "wicket_keeper"


class PlayerStatusEnum(str, Enum):
    """Player status enumeration"""
    AVAILABLE = "available"
    SOLD = "sold"
    UNSOLD = "unsold"


class PlayerBase(BaseModel):
    """Base Player schema with common fields"""
    name: str = Field(..., min_length=3, max_length=200, description="Player full name")
    role: PlayerRoleEnum = Field(..., description="Player role")
    country: str = Field(..., min_length=2, max_length=100, description="Player's country")
    age: Optional[int] = Field(None, ge=18, le=45, description="Player age (18-45)")
    is_overseas: bool = Field(default=False, description="Is player overseas?")
    base_price: float = Field(..., gt=0, description="Base auction price")
    matches_played: int = Field(default=0, ge=0, description="Total matches played")
    batting_average: Optional[float] = Field(None, ge=0, description="Batting average")
    bowling_average: Optional[float] = Field(None, ge=0, description="Bowling average")

    @field_validator("age")
    @classmethod
    def validate_age(cls, v):
        """Validate player age is between 18-45"""
        if v is not None:
            if v < 18:
                raise ValueError("Player must be at least 18 years old")
            if v > 45:
                raise ValueError("Player age cannot exceed 45 years")
        return v

    @field_validator("base_price")
    @classmethod
    def validate_base_price(cls, v):
        """Validate base price is reasonable"""
        if v <= 0:
            raise ValueError("Base price must be positive")
        if v > 100000000:  # 10 crore max
            raise ValueError("Base price cannot exceed 10 crore")
        return v


class PlayerCreate(PlayerBase):
    """Schema for creating a new player"""
    auction_id: int = Field(..., description="Auction ID this player belongs to")


class PlayerUpdate(BaseModel):
    """Schema for updating player information"""
    name: Optional[str] = Field(None, min_length=3, max_length=200)
    role: Optional[PlayerRoleEnum] = None
    country: Optional[str] = Field(None, min_length=2, max_length=100)
    age: Optional[int] = Field(None, ge=18, le=45)
    is_overseas: Optional[bool] = None
    base_price: Optional[float] = Field(None, gt=0)
    current_price: Optional[float] = Field(None, ge=0)
    status: Optional[PlayerStatusEnum] = None
    team_id: Optional[int] = None
    matches_played: Optional[int] = Field(None, ge=0)
    batting_average: Optional[float] = Field(None, ge=0)
    bowling_average: Optional[float] = Field(None, ge=0)

    @field_validator("current_price")
    @classmethod
    def validate_current_price(cls, v):
        """Validate current price"""
        if v is not None and v < 0:
            raise ValueError("Current price cannot be negative")
        return v


class PlayerInDB(PlayerBase):
    """Schema for player stored in database"""
    id: int
    current_price: Optional[float]
    status: PlayerStatusEnum
    team_id: Optional[int]
    auction_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PlayerResponse(PlayerInDB):
    """Schema for player API response"""
    pass
