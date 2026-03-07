"""
Auction Service

Handles auction management business logic.
"""

from typing import List, Optional
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.auction import Auction, AuctionStatus
from app.models.user import User
from app.schemas.auction import AuctionCreate, AuctionUpdate


class AuctionService:
    """Service class for auction operations."""

    @staticmethod
    def create_auction(db: Session, auction_data: AuctionCreate, user: User) -> Auction:
        """
        Create a new auction.

        Args:
            db: Database session
            auction_data: Auction creation data
            user: User creating the auction

        Returns:
            Auction: Created auction object

        Raises:
            HTTPException 403: If user is not admin/auctioneer
            HTTPException 400: If validation fails
        """
        # Only admin or auctioneer can create auctions
        if user.role not in ["admin", "auctioneer"] and not user.is_superuser:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admins or auctioneers can create auctions"
            )

        # Validate times if provided
        if auction_data.start_time and auction_data.end_time:
            if auction_data.end_time <= auction_data.start_time:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="End time must be after start time"
                )

        # Check for duplicate auction title
        existing_auction = db.query(Auction).filter(
            Auction.title == auction_data.title,
            Auction.is_active == True
        ).first()

        if existing_auction:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"An active auction with title '{auction_data.title}' already exists"
            )

        # Create auction
        auction = Auction(
            title=auction_data.title,
            description=auction_data.description,
            status=AuctionStatus.UPCOMING,
            total_budget_per_team=auction_data.total_budget_per_team,
            max_teams=auction_data.max_teams,
            max_players_per_team=auction_data.max_players_per_team,
            start_time=auction_data.start_time,
            end_time=auction_data.end_time,
            is_active=True,
            created_by=user.id
        )

        db.add(auction)
        db.commit()
        db.refresh(auction)

        return auction

    @staticmethod
    def get_auction(db: Session, auction_id: int) -> Optional[Auction]:
        """
        Get auction by ID.

        Args:
            db: Database session
            auction_id: Auction ID

        Returns:
            Auction: Auction object if found, None otherwise
        """
        return db.query(Auction).filter(Auction.id == auction_id).first()

    @staticmethod
    def get_auctions(
        db: Session,
        status: Optional[str] = None,
        is_active: Optional[bool] = None,
        created_by: Optional[int] = None,
        skip: int = 0,
        limit: int = 100
    ) -> List[Auction]:
        """
        Get list of auctions with filters.

        Args:
            db: Database session
            status: Filter by status (upcoming, live, completed, cancelled)
            is_active: Filter by active status
            created_by: Filter by creator user ID
            skip: Number of records to skip
            limit: Maximum number of records to return

        Returns:
            List[Auction]: List of auctions
        """
        query = db.query(Auction)

        if status is not None:
            query = query.filter(Auction.status == status)

        if is_active is not None:
            query = query.filter(Auction.is_active == is_active)

        if created_by is not None:
            query = query.filter(Auction.created_by == created_by)

        # Order by created_at descending (newest first)
        query = query.order_by(Auction.created_at.desc())

        return query.offset(skip).limit(limit).all()

    @staticmethod
    def update_auction(
        db: Session,
        auction_id: int,
        auction_data: AuctionUpdate,
        user: User
    ) -> Auction:
        """
        Update auction details.

        Args:
            db: Database session
            auction_id: Auction ID to update
            auction_data: Auction update data
            user: User performing the update

        Returns:
            Auction: Updated auction object

        Raises:
            HTTPException 404: If auction not found
            HTTPException 403: If user doesn't have permission
            HTTPException 400: If validation fails
        """
        auction = AuctionService.get_auction(db, auction_id)

        if not auction:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Auction not found"
            )

        # Only admin or auctioneer can update auctions
        if user.role not in ["admin", "auctioneer"] and not user.is_superuser:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admins or auctioneers can update auctions"
            )

        # Prevent updating live or completed auctions (except status and is_active)
        if auction.status in [AuctionStatus.LIVE, AuctionStatus.COMPLETED]:
            update_data = auction_data.model_dump(exclude_unset=True)
            restricted_fields = ['title', 'total_budget_per_team', 'max_teams', 'max_players_per_team']

            if any(field in update_data for field in restricted_fields):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Cannot modify critical fields for {auction.status} auctions"
                )

        # Validate time changes if provided
        if auction_data.start_time or auction_data.end_time:
            new_start = auction_data.start_time if auction_data.start_time else auction.start_time
            new_end = auction_data.end_time if auction_data.end_time else auction.end_time

            if new_start and new_end and new_end <= new_start:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="End time must be after start time"
                )

        # Update fields
        update_data = auction_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(auction, field, value)

        db.commit()
        db.refresh(auction)

        return auction

    @staticmethod
    def delete_auction(db: Session, auction_id: int, user: User) -> bool:
        """
        Delete an auction.

        Args:
            db: Database session
            auction_id: Auction ID to delete
            user: User performing the deletion

        Returns:
            bool: True if deleted successfully

        Raises:
            HTTPException 404: If auction not found
            HTTPException 403: If user doesn't have permission
            HTTPException 400: If auction is live or has teams
        """
        auction = AuctionService.get_auction(db, auction_id)

        if not auction:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Auction not found"
            )

        # Only admin can delete auctions
        if not user.is_superuser and user.role != "admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admins can delete auctions"
            )

        # Prevent deletion of live auctions
        if auction.status == AuctionStatus.LIVE:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot delete a live auction. End it first."
            )

        # Check if auction has teams registered
        if auction.teams and len(auction.teams) > 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot delete auction with registered teams. Remove teams first."
            )

        db.delete(auction)
        db.commit()

        return True

    @staticmethod
    def start_auction(db: Session, auction_id: int, user: User) -> Auction:
        """
        Start an auction (change status to LIVE).

        Args:
            db: Database session
            auction_id: Auction ID
            user: User starting the auction

        Returns:
            Auction: Updated auction object

        Raises:
            HTTPException 404: If auction not found
            HTTPException 403: If user doesn't have permission
            HTTPException 400: If auction cannot be started
        """
        auction = AuctionService.get_auction(db, auction_id)

        if not auction:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Auction not found"
            )

        # Only admin or auctioneer can start auctions
        if user.role not in ["admin", "auctioneer"] and not user.is_superuser:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admins or auctioneers can start auctions"
            )

        # Check if auction can be started
        if auction.status != AuctionStatus.UPCOMING:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Cannot start auction with status: {auction.status}"
            )

        # Verify auction has teams
        if not auction.teams or len(auction.teams) < 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Auction must have at least 2 teams registered before starting"
            )

        # Verify auction has players
        if not auction.players or len(auction.players) < 1:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Auction must have at least 1 player before starting"
            )

        # Update auction status and start time
        auction.status = AuctionStatus.LIVE
        if not auction.start_time:
            auction.start_time = datetime.now(timezone.utc)

        db.commit()
        db.refresh(auction)

        return auction

    @staticmethod
    def end_auction(db: Session, auction_id: int, user: User) -> Auction:
        """
        End an auction (change status to COMPLETED).

        Args:
            db: Database session
            auction_id: Auction ID
            user: User ending the auction

        Returns:
            Auction: Updated auction object

        Raises:
            HTTPException 404: If auction not found
            HTTPException 403: If user doesn't have permission
            HTTPException 400: If auction cannot be ended
        """
        auction = AuctionService.get_auction(db, auction_id)

        if not auction:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Auction not found"
            )

        # Only admin or auctioneer can end auctions
        if user.role not in ["admin", "auctioneer"] and not user.is_superuser:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admins or auctioneers can end auctions"
            )

        # Check if auction can be ended
        if auction.status != AuctionStatus.LIVE:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Cannot end auction with status: {auction.status}"
            )

        # Update auction status and end time
        auction.status = AuctionStatus.COMPLETED
        if not auction.end_time:
            auction.end_time = datetime.now(timezone.utc)

        db.commit()
        db.refresh(auction)

        return auction

    @staticmethod
    def cancel_auction(db: Session, auction_id: int, user: User) -> Auction:
        """
        Cancel an auction (change status to CANCELLED).

        Args:
            db: Database session
            auction_id: Auction ID
            user: User cancelling the auction

        Returns:
            Auction: Updated auction object

        Raises:
            HTTPException 404: If auction not found
            HTTPException 403: If user doesn't have permission
            HTTPException 400: If auction is already completed
        """
        auction = AuctionService.get_auction(db, auction_id)

        if not auction:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Auction not found"
            )

        # Only admin can cancel auctions
        if not user.is_superuser and user.role != "admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admins can cancel auctions"
            )

        # Cannot cancel completed auctions
        if auction.status == AuctionStatus.COMPLETED:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot cancel a completed auction"
            )

        # Update auction status
        auction.status = AuctionStatus.CANCELLED
        auction.is_active = False

        db.commit()
        db.refresh(auction)

        return auction
