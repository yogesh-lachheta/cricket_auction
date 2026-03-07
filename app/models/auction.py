"""
Auction Database Model

This module defines the Auction table structure for cricket auctions.
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.db.base import Base


class AuctionStatus(str, enum.Enum):
    """Enum for auction status"""
    UPCOMING = "upcoming"
    LIVE = "live"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Auction(Base):
    """
    Auction model for cricket auction platform.

    Attributes:
        id: Primary key
        title: Auction title/name
        description: Auction description
        status: Auction status (upcoming, live, completed, cancelled)
        start_time: Auction start time
        end_time: Auction end time
        total_budget_per_team: Budget allocated to each team
        max_teams: Maximum number of teams allowed
        max_players_per_team: Maximum players per team
        is_active: Auction active status
        created_by: User ID who created the auction
        created_at: Record creation timestamp
        updated_at: Last update timestamp
    """

    __tablename__ = "auctions"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Auction Information
    title = Column(String(200), nullable=False, index=True)
    description = Column(String(1000), nullable=True)

    # Status
    status = Column(Enum(AuctionStatus), default=AuctionStatus.UPCOMING, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    # Timing
    start_time = Column(DateTime(timezone=True), nullable=True)
    end_time = Column(DateTime(timezone=True), nullable=True)

    # Rules & Limits
    total_budget_per_team = Column(Float, nullable=False)
    max_teams = Column(Integer, default=8, nullable=False)
    max_players_per_team = Column(Integer, default=15, nullable=False)

    # Creator
    created_by = Column(Integer, nullable=True)  # User ID

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # SQLAlchemy Relationships
    # teams = relationship("Team", back_populates="auction")
    # players = relationship("Player", back_populates="auction")

    def __repr__(self):
        """String representation of Auction object"""
        return f"<Auction(id={self.id}, title='{self.title}', status='{self.status}')>"
