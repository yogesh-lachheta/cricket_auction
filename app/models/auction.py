"""
Auction Database Model

This module defines the Auction table structure for cricket auctions.
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, Enum, ForeignKey
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

    # Current Player Being Auctioned
    current_player_id = Column(Integer, ForeignKey("players.id", ondelete="SET NULL"), nullable=True, index=True)

    # Creator
    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # SQLAlchemy Relationships
    teams = relationship("Team", back_populates="auction")
    players = relationship("Player", back_populates="auction", foreign_keys="[Player.auction_id]")
    current_player = relationship("Player", foreign_keys=[current_player_id], lazy="joined")
    bids = relationship("Bid", back_populates="auction")

    def __repr__(self):
        """String representation of Auction object"""
        return f"<Auction(id={self.id}, title='{self.title}', status='{self.status}')>"


class Bid(Base):
    """
    Bid model for tracking auction bids.

    Attributes:
        id: Primary key
        auction_id: Foreign key to Auction
        player_id: Foreign key to Player being bid on
        team_id: Foreign key to Team placing the bid
        bid_amount: Amount of the bid
        is_winning_bid: Flag to indicate if this is the winning bid
        created_at: Bid timestamp
    """

    __tablename__ = "bids"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Foreign Keys
    auction_id = Column(Integer, ForeignKey("auctions.id", ondelete="CASCADE"), nullable=False)
    player_id = Column(Integer, ForeignKey("players.id", ondelete="CASCADE"), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id", ondelete="SET NULL"), nullable=True)

    # Bid Information
    bid_amount = Column(Float, nullable=False)
    is_winning_bid = Column(Boolean, default=False, nullable=False)

    # Timestamp
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # SQLAlchemy Relationships
    auction = relationship("Auction", back_populates="bids")
    player = relationship("Player", back_populates="bids")
    team = relationship("Team", back_populates="bids")

    def __repr__(self):
        """String representation of Bid object"""
        return f"<Bid(id={self.id}, player_id={self.player_id}, team_id={self.team_id}, amount={self.bid_amount})>"


