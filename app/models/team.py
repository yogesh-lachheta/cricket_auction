"""
Team Database Model

This module defines the Team table structure for auction teams.
"""

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base


class Team(Base):
    """
    Team model for cricket auction platform.

    Attributes:
        id: Primary key
        name: Team name
        owner_name: Team owner's name
        total_budget: Total budget for auction
        remaining_budget: Remaining budget after purchases
        max_players: Maximum players allowed
        current_players: Current number of players
        user_id: Foreign key to user (team owner)
        auction_id: Foreign key to auction
        is_active: Team active status
        created_at: Record creation timestamp
        updated_at: Last update timestamp
    """

    __tablename__ = "teams"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Team Information
    name = Column(String(200), nullable=False, index=True)
    short_name = Column(String(50), nullable=False, index=True)
    owner_name = Column(String(200), nullable=True)
    logo_url = Column(String(500), nullable=True)

    # Budget Management
    total_budget = Column(Float, nullable=False)
    remaining_budget = Column(Float, nullable=False)

    # Player Limits
    max_players = Column(Integer, default=15, nullable=False)
    current_players = Column(Integer, default=0, nullable=False)
    overseas_count = Column(Integer, default=0, nullable=False)

    # Relationships
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    auction_id = Column(Integer, ForeignKey("auctions.id", ondelete="CASCADE"), nullable=False)

    # Status
    is_active = Column(Boolean, default=True, nullable=False)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # SQLAlchemy Relationships
    user = relationship("User", back_populates="teams")
    auction = relationship("Auction", back_populates="teams")
    players = relationship("Player", back_populates="team", cascade="all, delete-orphan")

    def __repr__(self):
        """String representation of Team object"""
        return f"<Team(id={self.id}, name='{self.name}', budget={self.remaining_budget}/{self.total_budget})>"
