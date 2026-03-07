"""
Auction CRUD Endpoints
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user, get_current_admin
from app.schemas.auction import AuctionCreate, AuctionUpdate, AuctionResponse
from app.services.auction_service import AuctionService
from app.models.user import User


router = APIRouter()


@router.post(
    "/",
    response_model=AuctionResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new auction",
    description="Create a new auction. Requires admin or auctioneer role."
)
def create_auction(
    auction_data: AuctionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Create a new auction.

    Args:
        auction_data: Auction creation data
        db: Database session
        current_user: Authenticated user

    Returns:
        AuctionResponse: Created auction details

    Raises:
        HTTPException 403: If user is not admin/auctioneer
        HTTPException 400: If validation fails
    """
    auction = AuctionService.create_auction(db, auction_data, current_user)
    return auction


@router.get(
    "/",
    response_model=List[AuctionResponse],
    summary="Get list of auctions",
    description="Get list of all auctions with optional filters"
)
def get_auctions(
    status: Optional[str] = Query(None, description="Filter by status (upcoming, live, completed, cancelled)"),
    is_active: Optional[bool] = Query(None, description="Filter by active status"),
    created_by: Optional[int] = Query(None, description="Filter by creator user ID"),
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records"),
    db: Session = Depends(get_db)
):
    """
    Get list of auctions with optional filters.

    Args:
        status: Filter by auction status
        is_active: Filter by active status
        created_by: Filter by creator user ID
        skip: Number of records to skip (pagination)
        limit: Maximum number of records to return
        db: Database session

    Returns:
        List[AuctionResponse]: List of auctions
    """
    auctions = AuctionService.get_auctions(
        db=db,
        status=status,
        is_active=is_active,
        created_by=created_by,
        skip=skip,
        limit=limit
    )
    return auctions


@router.get(
    "/{auction_id}",
    response_model=AuctionResponse,
    summary="Get auction by ID",
    description="Get detailed information about a specific auction"
)
def get_auction(
    auction_id: int,
    db: Session = Depends(get_db)
):
    """
    Get auction details by ID.

    Args:
        auction_id: Auction ID
        db: Database session

    Returns:
        AuctionResponse: Auction details

    Raises:
        HTTPException 404: If auction not found
    """
    auction = AuctionService.get_auction(db, auction_id)

    if not auction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Auction not found"
        )

    return auction


@router.put(
    "/{auction_id}",
    response_model=AuctionResponse,
    summary="Update auction",
    description="Update auction details. Requires admin or auctioneer role."
)
def update_auction(
    auction_id: int,
    auction_data: AuctionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Update auction details.

    Args:
        auction_id: Auction ID to update
        auction_data: Auction update data
        db: Database session
        current_user: Authenticated user

    Returns:
        AuctionResponse: Updated auction details

    Raises:
        HTTPException 404: If auction not found
        HTTPException 403: If user doesn't have permission
        HTTPException 400: If validation fails
    """
    auction = AuctionService.update_auction(db, auction_id, auction_data, current_user)
    return auction


@router.delete(
    "/{auction_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete auction",
    description="Delete an auction. Only admins can delete auctions."
)
def delete_auction(
    auction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """
    Delete an auction.

    Args:
        auction_id: Auction ID to delete
        db: Database session
        current_user: Authenticated admin user

    Raises:
        HTTPException 404: If auction not found
        HTTPException 403: If user is not admin
        HTTPException 400: If auction is live or has teams
    """
    AuctionService.delete_auction(db, auction_id, current_user)
    return None


@router.post(
    "/{auction_id}/start",
    response_model=AuctionResponse,
    summary="Start auction",
    description="Start an auction (change status to LIVE). Requires admin or auctioneer role."
)
def start_auction(
    auction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Start an auction.

    Args:
        auction_id: Auction ID to start
        db: Database session
        current_user: Authenticated user

    Returns:
        AuctionResponse: Updated auction details

    Raises:
        HTTPException 404: If auction not found
        HTTPException 403: If user doesn't have permission
        HTTPException 400: If auction cannot be started
    """
    auction = AuctionService.start_auction(db, auction_id, current_user)
    return auction


@router.post(
    "/{auction_id}/end",
    response_model=AuctionResponse,
    summary="End auction",
    description="End an auction (change status to COMPLETED). Requires admin or auctioneer role."
)
def end_auction(
    auction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    End an auction.

    Args:
        auction_id: Auction ID to end
        db: Database session
        current_user: Authenticated user

    Returns:
        AuctionResponse: Updated auction details

    Raises:
        HTTPException 404: If auction not found
        HTTPException 403: If user doesn't have permission
        HTTPException 400: If auction cannot be ended
    """
    auction = AuctionService.end_auction(db, auction_id, current_user)
    return auction


@router.post(
    "/{auction_id}/cancel",
    response_model=AuctionResponse,
    summary="Cancel auction",
    description="Cancel an auction (change status to CANCELLED). Only admins can cancel auctions."
)
def cancel_auction(
    auction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """
    Cancel an auction.

    Args:
        auction_id: Auction ID to cancel
        db: Database session
        current_user: Authenticated admin user

    Returns:
        AuctionResponse: Updated auction details

    Raises:
        HTTPException 404: If auction not found
        HTTPException 403: If user is not admin
        HTTPException 400: If auction is already completed
    """
    auction = AuctionService.cancel_auction(db, auction_id, current_user)
    return auction
