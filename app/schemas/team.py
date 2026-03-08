"""
Team Pydantic Schemas

These schemas define the structure for team-related requests and responses.
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, field_validator


class TeamBase(BaseModel):
    """Base Team schema with common fields"""
    name: str = Field(..., min_length=3, max_length=200, description="Team name")
    short_name: str = Field(..., min_length=2, max_length=50, description="Team short name (e.g., 'MI', 'CSK')")
    owner_name: Optional[str] = Field(None, max_length=200, description="Team owner's name")
    logo_url: Optional[str] = Field(None, description="Team logo URL or base64 encoded image")
    total_budget: float = Field(..., gt=0, description="Total budget (must be positive)")
    max_players: int = Field(default=15, ge=11, le=25, description="Maximum players allowed (11-25)")

    @field_validator("total_budget")
    @classmethod
    def validate_budget(cls, v):
        """Validate that budget is reasonable"""
        if v < 0:
            raise ValueError("Budget cannot be negative")
        if v > 1000000000:  # 100 crore max
            raise ValueError("Budget cannot exceed 100 crore")
        return v


class TeamCreate(TeamBase):
    """Schema for creating a new team"""
    auction_id: int = Field(..., description="Auction ID this team belongs to")
    user_id: Optional[int] = Field(None, description="User ID of team owner")


class TeamUpdate(BaseModel):
    """Schema for updating team information"""
    name: Optional[str] = Field(None, min_length=3, max_length=200)
    short_name: Optional[str] = Field(None, min_length=2, max_length=50)
    owner_name: Optional[str] = Field(None, max_length=200)
    logo_url: Optional[str] = Field(None, description="Team logo URL or base64 encoded image")
    total_budget: Optional[float] = Field(None, gt=0)
    remaining_budget: Optional[float] = Field(None, ge=0)
    current_players: Optional[int] = Field(None, ge=0)
    overseas_count: Optional[int] = Field(None, ge=0)
    max_players: Optional[int] = Field(None, ge=11, le=25)
    is_active: Optional[bool] = None

    @field_validator("remaining_budget")
    @classmethod
    def validate_remaining_budget(cls, v):
        """Validate remaining budget"""
        if v is not None and v < 0:
            raise ValueError("Remaining budget cannot be negative")
        return v

    @field_validator("current_players")
    @classmethod
    def validate_current_players(cls, v):
        """Validate current players count"""
        if v is not None and v > 25:
            raise ValueError("Cannot have more than 25 players")
        return v


class TeamInDB(TeamBase):
    """Schema for team stored in database"""
    id: int
    remaining_budget: float
    current_players: int
    overseas_count: int
    auction_id: int
    user_id: Optional[int]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TeamResponse(TeamInDB):
    """Schema for team API response"""
    pass
