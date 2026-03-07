"""
Team Service

Handles team management business logic.
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.team import Team
from app.models.user import User
from app.schemas.team import TeamCreate, TeamUpdate


class TeamService:
    """Service class for team operations."""

    @staticmethod
    def create_team(db: Session, team_data: TeamCreate, user: User) -> Team:
        """
        Create a new team.

        Args:
            db: Database session
            team_data: Team creation data
            user: User creating the team

        Returns:
            Team: Created team object

        Raises:
            HTTPException 400: If team name already exists in auction
        """
        # Check if team name already exists in this auction
        existing_team = db.query(Team).filter(
            Team.auction_id == team_data.auction_id,
            Team.name == team_data.name
        ).first()

        if existing_team:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Team '{team_data.name}' already exists in this auction"
            )

        # Create team
        team = Team(
            name=team_data.name,
            short_name=team_data.short_name,
            owner_name=team_data.owner_name or user.full_name,
            logo_url=team_data.logo_url,
            total_budget=team_data.total_budget,
            remaining_budget=team_data.total_budget,  # Initially full budget
            max_players=team_data.max_players or 15,
            current_players=0,
            overseas_count=0,
            user_id=user.id,
            auction_id=team_data.auction_id,
            is_active=True
        )

        db.add(team)
        db.commit()
        db.refresh(team)

        return team

    @staticmethod
    def get_team(db: Session, team_id: int) -> Optional[Team]:
        """
        Get team by ID.

        Args:
            db: Database session
            team_id: Team ID

        Returns:
            Team: Team object if found, None otherwise
        """
        return db.query(Team).filter(Team.id == team_id).first()

    @staticmethod
    def get_teams(
        db: Session,
        auction_id: Optional[int] = None,
        user_id: Optional[int] = None,
        is_active: Optional[bool] = None,
        skip: int = 0,
        limit: int = 100
    ) -> List[Team]:
        """
        Get list of teams with filters.

        Args:
            db: Database session
            auction_id: Filter by auction ID
            user_id: Filter by user/owner ID
            is_active: Filter by active status
            skip: Number of records to skip
            limit: Maximum number of records to return

        Returns:
            List[Team]: List of teams
        """
        query = db.query(Team)

        if auction_id is not None:
            query = query.filter(Team.auction_id == auction_id)

        if user_id is not None:
            query = query.filter(Team.user_id == user_id)

        if is_active is not None:
            query = query.filter(Team.is_active == is_active)

        return query.offset(skip).limit(limit).all()

    @staticmethod
    def update_team(
        db: Session,
        team_id: int,
        team_data: TeamUpdate,
        user: User
    ) -> Team:
        """
        Update team details.

        Args:
            db: Database session
            team_id: Team ID to update
            team_data: Team update data
            user: User performing the update

        Returns:
            Team: Updated team object

        Raises:
            HTTPException 404: If team not found
            HTTPException 403: If user is not the team owner
        """
        team = TeamService.get_team(db, team_id)

        if not team:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Team not found"
            )

        # Check if user is the team owner (or admin/superuser)
        if team.user_id != user.id and not user.is_superuser and user.role != "admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have permission to update this team"
            )

        # Update fields
        update_data = team_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(team, field, value)

        db.commit()
        db.refresh(team)

        return team

    @staticmethod
    def delete_team(db: Session, team_id: int, user: User) -> bool:
        """
        Delete a team.

        Args:
            db: Database session
            team_id: Team ID to delete
            user: User performing the deletion

        Returns:
            bool: True if deleted successfully

        Raises:
            HTTPException 404: If team not found
            HTTPException 403: If user doesn't have permission
        """
        team = TeamService.get_team(db, team_id)

        if not team:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Team not found"
            )

        # Only admin/superuser can delete teams
        if not user.is_superuser and user.role != "admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admins can delete teams"
            )

        db.delete(team)
        db.commit()

        return True

    @staticmethod
    def update_team_budget(
        db: Session,
        team_id: int,
        amount: float,
        operation: str = "subtract"
    ) -> Team:
        """
        Update team's remaining budget.

        Args:
            db: Database session
            team_id: Team ID
            amount: Amount to add or subtract
            operation: 'add' or 'subtract'

        Returns:
            Team: Updated team object

        Raises:
            HTTPException 400: If insufficient budget
        """
        team = TeamService.get_team(db, team_id)

        if not team:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Team not found"
            )

        if operation == "subtract":
            if team.remaining_budget < amount:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Insufficient budget. Available: {team.remaining_budget}, Required: {amount}"
                )
            team.remaining_budget -= amount
        elif operation == "add":
            team.remaining_budget += amount

        db.commit()
        db.refresh(team)

        return team
