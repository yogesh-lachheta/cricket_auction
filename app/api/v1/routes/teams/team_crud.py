"""
Team CRUD Endpoints
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user, get_current_admin
from app.schemas.team import TeamCreate, TeamUpdate, TeamResponse
from app.services.team_service import TeamService
from app.models.user import User


router = APIRouter()


@router.post(
    "/",
    response_model=TeamResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new team",
    description="Create a new team for an auction. Requires authentication."
)
def create_team(
    team_data: TeamCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Create a new team.

    Args:
        team_data: Team creation data
        db: Database session
        current_user: Authenticated user

    Returns:
        TeamResponse: Created team details

    Raises:
        HTTPException 400: If team name already exists in auction
    """
    team = TeamService.create_team(db, team_data, current_user)
    return team


@router.get(
    "/",
    response_model=List[TeamResponse],
    summary="Get list of teams",
    description="Get list of all teams with optional filters"
)
def get_teams(
    auction_id: Optional[int] = Query(None, description="Filter by auction ID"),
    user_id: Optional[int] = Query(None, description="Filter by owner/user ID"),
    is_active: Optional[bool] = Query(None, description="Filter by active status"),
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records"),
    db: Session = Depends(get_db)
):
    """
    Get list of teams with optional filters.

    Args:
        auction_id: Filter by auction ID
        user_id: Filter by owner/user ID
        is_active: Filter by active status
        skip: Number of records to skip (pagination)
        limit: Maximum number of records to return
        db: Database session

    Returns:
        List[TeamResponse]: List of teams
    """
    teams = TeamService.get_teams(
        db=db,
        auction_id=auction_id,
        user_id=user_id,
        is_active=is_active,
        skip=skip,
        limit=limit
    )
    return teams


@router.get(
    "/{team_id}",
    response_model=TeamResponse,
    summary="Get team by ID",
    description="Get detailed information about a specific team"
)
def get_team(
    team_id: int,
    db: Session = Depends(get_db)
):
    """
    Get team details by ID.

    Args:
        team_id: Team ID
        db: Database session

    Returns:
        TeamResponse: Team details

    Raises:
        HTTPException 404: If team not found
    """
    team = TeamService.get_team(db, team_id)

    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Team not found"
        )

    return team


@router.put(
    "/{team_id}",
    response_model=TeamResponse,
    summary="Update team",
    description="Update team details. Only team owner or admin can update."
)
def update_team(
    team_id: int,
    team_data: TeamUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Update team details.

    Args:
        team_id: Team ID to update
        team_data: Team update data
        db: Database session
        current_user: Authenticated user

    Returns:
        TeamResponse: Updated team details

    Raises:
        HTTPException 404: If team not found
        HTTPException 403: If user doesn't have permission
    """
    team = TeamService.update_team(db, team_id, team_data, current_user)
    return team


@router.delete(
    "/{team_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete team",
    description="Delete a team. Only admins can delete teams."
)
def delete_team(
    team_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """
    Delete a team.

    Args:
        team_id: Team ID to delete
        db: Database session
        current_user: Authenticated admin user

    Raises:
        HTTPException 404: If team not found
        HTTPException 403: If user is not admin
    """
    TeamService.delete_team(db, team_id, current_user)
    return None
