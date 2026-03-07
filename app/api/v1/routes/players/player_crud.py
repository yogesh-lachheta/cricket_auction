"""
Player CRUD Endpoints
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user, get_current_admin
from app.schemas.player import PlayerCreate, PlayerUpdate, PlayerResponse
from app.services.player_service import PlayerService
from app.models.user import User


router = APIRouter()


@router.post("/", response_model=PlayerResponse, status_code=status.HTTP_201_CREATED)
def create_player(
    player_data: PlayerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new player (admin/auctioneer only)"""
    return PlayerService.create_player(db, player_data, current_user)


@router.get("/", response_model=List[PlayerResponse])
def get_players(
    auction_id: Optional[int] = Query(None),
    team_id: Optional[int] = Query(None),
    role: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    """Get list of players with filters"""
    return PlayerService.get_players(
        db, auction_id=auction_id, team_id=team_id,
        role=role, status=status, skip=skip, limit=limit
    )


@router.get("/{player_id}", response_model=PlayerResponse)
def get_player(player_id: int, db: Session = Depends(get_db)):
    """Get player by ID"""
    player = PlayerService.get_player(db, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@router.put("/{player_id}", response_model=PlayerResponse)
def update_player(
    player_id: int,
    player_data: PlayerUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update player (admin/auctioneer only)"""
    return PlayerService.update_player(db, player_id, player_data, current_user)


@router.delete("/{player_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_player(
    player_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """Delete player (admin only)"""
    PlayerService.delete_player(db, player_id, current_user)
    return None
