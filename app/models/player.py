"""
Player Database Model

This module defines the Player table structure for cricket players.
"""

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.db.base import Base


class PlayerRole(str, enum.Enum):
    """Enum for player roles"""
    BATSMAN = "batsman"
    BOWLER = "bowler"
    ALL_ROUNDER = "all_rounder"
    WICKET_KEEPER = "wicket_keeper"


class PlayerStatus(str, enum.Enum):
    """Enum for player status"""
    AVAILABLE = "available"
    SOLD = "sold"
    UNSOLD = "unsold"


class Player(Base):
    """
    Player model for cricket auction platform.

    Attributes:
        id: Primary key
        name: Player full name
        role: Player role (batsman, bowler, all-rounder, wicket-keeper)
        base_price: Starting bid price
        current_price: Current bid price (if sold)
        status: Player status (available, sold, unsold)
        country: Player's country
        age: Player's age
        matches_played: Total matches played
        batting_average: Batting average
        bowling_average: Bowling average
        team_id: Foreign key to team (if sold)
        auction_id: Foreign key to auction
        created_at: Record creation timestamp
        updated_at: Last update timestamp
    """

    __tablename__ = "players"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Basic Information
    name = Column(String(200), nullable=False, index=True)
    role = Column(Enum(PlayerRole), nullable=False)
    country = Column(String(100), nullable=False)
    age = Column(Integer, nullable=True)
    is_overseas = Column(Boolean, default=False, nullable=False)

    # Pricing
    base_price = Column(Float, nullable=False)
    current_price = Column(Float, nullable=True)
    status = Column(Enum(PlayerStatus), default=PlayerStatus.AVAILABLE, nullable=False)

    # Statistics
    matches_played = Column(Integer, default=0)
    batting_average = Column(Float, nullable=True)
    bowling_average = Column(Float, nullable=True)

    # Relationships
    team_id = Column(Integer, ForeignKey("teams.id", ondelete="SET NULL"), nullable=True)
    auction_id = Column(Integer, ForeignKey("auctions.id", ondelete="CASCADE"), nullable=False)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # SQLAlchemy Relationships
    team = relationship("Team", back_populates="players")
    auction = relationship("Auction", back_populates="players", foreign_keys=[auction_id])
    bids = relationship("Bid", back_populates="player")

    def __repr__(self):
        """String representation of Player object"""
        return f"<Player(id={self.id}, name='{self.name}', role='{self.role}', status='{self.status}')>"
