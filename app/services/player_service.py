"""
Player Service

Handles player management business logic.
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.player import Player
from app.models.user import User
from app.schemas.player import PlayerCreate, PlayerUpdate


class PlayerService:
    """Service class for player operations."""

    @staticmethod
    def create_player(db: Session, player_data: PlayerCreate, user: User) -> Player:
        """
        Create a new player.

        Args:
            db: Database session
            player_data: Player creation data
            user: User creating the player

        Returns:
            Player: Created player object

        Raises:
            HTTPException 403: If user is not admin/auctioneer
        """
        # Only admin or auctioneer can create players
        if user.role not in ["admin", "auctioneer"] and not user.is_superuser:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admins or auctioneers can add players"
            )

        # Create player
        player = Player(
            name=player_data.name,
            role=player_data.role,
            country=player_data.country,
            age=player_data.age,
            is_overseas=player_data.is_overseas,
            base_price=player_data.base_price,
            current_price=player_data.base_price,  # Initially same as base price
            status=player_data.status or "available",
            matches_played=player_data.matches_played or 0,
            batting_avg=player_data.batting_avg,
            bowling_avg=player_data.bowling_avg,
            team_id=None,  # Not assigned to team yet
            auction_id=player_data.auction_id
        )

        db.add(player)
        db.commit()
        db.refresh(player)

        return player

    @staticmethod
    def get_player(db: Session, player_id: int) -> Optional[Player]:
        """
        Get player by ID.

        Args:
            db: Database session
            player_id: Player ID

        Returns:
            Player: Player object if found, None otherwise
        """
        return db.query(Player).filter(Player.id == player_id).first()

    @staticmethod
    def get_players(
        db: Session,
        auction_id: Optional[int] = None,
        team_id: Optional[int] = None,
        role: Optional[str] = None,
        country: Optional[str] = None,
        is_overseas: Optional[bool] = None,
        status: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        skip: int = 0,
        limit: int = 100
    ) -> List[Player]:
        """
        Get list of players with filters.

        Args:
            db: Database session
            auction_id: Filter by auction ID
            team_id: Filter by team ID
            role: Filter by player role (batsman, bowler, all-rounder, wicket-keeper)
            country: Filter by country
            is_overseas: Filter by overseas status
            status: Filter by status (available, sold, unsold)
            min_price: Minimum base price
            max_price: Maximum base price
            skip: Number of records to skip
            limit: Maximum number of records to return

        Returns:
            List[Player]: List of players
        """
        query = db.query(Player)

        if auction_id is not None:
            query = query.filter(Player.auction_id == auction_id)

        if team_id is not None:
            query = query.filter(Player.team_id == team_id)

        if role is not None:
            query = query.filter(Player.role == role)

        if country is not None:
            query = query.filter(Player.country == country)

        if is_overseas is not None:
            query = query.filter(Player.is_overseas == is_overseas)

        if status is not None:
            query = query.filter(Player.status == status)

        if min_price is not None:
            query = query.filter(Player.base_price >= min_price)

        if max_price is not None:
            query = query.filter(Player.base_price <= max_price)

        return query.offset(skip).limit(limit).all()

    @staticmethod
    def update_player(
        db: Session,
        player_id: int,
        player_data: PlayerUpdate,
        user: User
    ) -> Player:
        """
        Update player details.

        Args:
            db: Database session
            player_id: Player ID to update
            player_data: Player update data
            user: User performing the update

        Returns:
            Player: Updated player object

        Raises:
            HTTPException 404: If player not found
            HTTPException 403: If user doesn't have permission
        """
        player = PlayerService.get_player(db, player_id)

        if not player:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Player not found"
            )

        # Only admin or auctioneer can update players
        if user.role not in ["admin", "auctioneer"] and not user.is_superuser:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admins or auctioneers can update players"
            )

        # Update fields
        update_data = player_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(player, field, value)

        db.commit()
        db.refresh(player)

        return player

    @staticmethod
    def delete_player(db: Session, player_id: int, user: User) -> bool:
        """
        Delete a player.

        Args:
            db: Database session
            player_id: Player ID to delete
            user: User performing the deletion

        Returns:
            bool: True if deleted successfully

        Raises:
            HTTPException 404: If player not found
            HTTPException 403: If user doesn't have permission
        """
        player = PlayerService.get_player(db, player_id)

        if not player:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Player not found"
            )

        # Only admin can delete players
        if not user.is_superuser and user.role != "admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admins can delete players"
            )

        db.delete(player)
        db.commit()

        return True

    @staticmethod
    def assign_player_to_team(
        db: Session,
        player_id: int,
        team_id: int,
        bid_amount: float
    ) -> Player:
        """
        Assign a player to a team after successful bid.

        Args:
            db: Database session
            player_id: Player ID
            team_id: Team ID
            bid_amount: Final bid amount

        Returns:
            Player: Updated player object

        Raises:
            HTTPException 404: If player not found
            HTTPException 400: If player is already sold
        """
        player = PlayerService.get_player(db, player_id)

        if not player:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Player not found"
            )

        if player.status == "sold":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Player is already sold"
            )

        player.team_id = team_id
        player.current_price = bid_amount
        player.status = "sold"

        db.commit()
        db.refresh(player)

        return player
