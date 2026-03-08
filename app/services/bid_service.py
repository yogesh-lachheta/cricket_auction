"""
Bid Service

Business logic for handling auction bids.
"""

from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import and_, desc
from fastapi import HTTPException, status

from app.models.auction import Bid, Auction, AuctionStatus
from app.models.team import Team
from app.models.player import Player
from app.models.user import User
from app.schemas.bid import BidCreate, BidUpdate, PlaceBidRequest


class BidService:
    """Service class for bid operations"""

    @staticmethod
    def validate_bid(
        db: Session,
        auction_id: int,
        player_id: int,
        team_id: int,
        bid_amount: float,
        current_user: User
    ) -> dict:
        """
        Validate if a bid can be placed.

        Returns dict with validation result:
        {
            "valid": bool,
            "error": str (if invalid),
            "team": Team,
            "player": Player,
            "auction": Auction,
            "current_bid": Bid
        }
        """
        # 1. Check if auction exists and is LIVE
        auction = db.query(Auction).filter(Auction.id == auction_id).first()
        if not auction:
            return {"valid": False, "error": "Auction not found"}

        if auction.status != AuctionStatus.LIVE:
            return {"valid": False, "error": f"Auction is not live (status: {auction.status})"}

        # 2. Check if player exists and belongs to this auction
        player = db.query(Player).filter(
            and_(
                Player.id == player_id,
                Player.auction_id == auction_id
            )
        ).first()

        if not player:
            return {"valid": False, "error": "Player not found in this auction"}

        if player.is_sold:
            return {"valid": False, "error": "Player is already sold"}

        # 3. Check if team exists and belongs to this auction
        team = db.query(Team).filter(
            and_(
                Team.id == team_id,
                Team.auction_id == auction_id
            )
        ).first()

        if not team:
            return {"valid": False, "error": "Team not found in this auction"}

        if not team.is_active:
            return {"valid": False, "error": "Team is not active"}

        # 4. Verify user owns this team
        if team.user_id != current_user.id and current_user.role != "admin":
            return {"valid": False, "error": "You don't own this team"}

        # 5. Get current highest bid for this player
        current_bid = db.query(Bid).filter(
            and_(
                Bid.player_id == player_id,
                Bid.auction_id == auction_id
            )
        ).order_by(desc(Bid.bid_amount)).first()

        # 6. Validate bid amount
        min_bid = player.base_price
        if current_bid:
            min_bid = current_bid.bid_amount + 500000  # Minimum increment 50 lakh

        if bid_amount < min_bid:
            return {
                "valid": False,
                "error": f"Bid must be at least ₹{min_bid/10000000:.1f} cr (current: ₹{bid_amount/10000000:.1f} cr)"
            }

        # 7. Check team budget
        if team.remaining_budget < bid_amount:
            return {
                "valid": False,
                "error": f"Insufficient budget. Available: ₹{team.remaining_budget/10000000:.1f} cr, Required: ₹{bid_amount/10000000:.1f} cr"
            }

        # 8. Check if team has reached max players
        if team.current_players >= team.max_players:
            return {
                "valid": False,
                "error": f"Team has reached maximum players limit ({team.max_players})"
            }

        return {
            "valid": True,
            "team": team,
            "player": player,
            "auction": auction,
            "current_bid": current_bid
        }

    @staticmethod
    def place_bid(
        db: Session,
        auction_id: int,
        bid_data: PlaceBidRequest,
        team_id: int,
        current_user: User
    ) -> Bid:
        """
        Place a bid on a player.

        Args:
            db: Database session
            auction_id: Auction ID
            bid_data: Bid request data
            team_id: Team ID placing the bid
            current_user: User placing the bid

        Returns:
            Created Bid object

        Raises:
            HTTPException if validation fails
        """
        # Validate bid
        validation = BidService.validate_bid(
            db=db,
            auction_id=auction_id,
            player_id=bid_data.player_id,
            team_id=team_id,
            bid_amount=bid_data.bid_amount,
            current_user=current_user
        )

        if not validation["valid"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=validation["error"]
            )

        # Mark previous winning bid as not winning
        if validation["current_bid"]:
            validation["current_bid"].is_winning_bid = False
            db.add(validation["current_bid"])

        # Create new bid
        new_bid = Bid(
            auction_id=auction_id,
            player_id=bid_data.player_id,
            team_id=team_id,
            bid_amount=bid_data.bid_amount,
            is_winning_bid=True
        )

        db.add(new_bid)
        db.commit()
        db.refresh(new_bid)

        return new_bid

    @staticmethod
    def get_bid_history(
        db: Session,
        auction_id: int,
        player_id: Optional[int] = None,
        team_id: Optional[int] = None,
        limit: int = 50
    ) -> List[Bid]:
        """Get bid history for an auction/player/team"""
        query = db.query(Bid).filter(Bid.auction_id == auction_id)

        if player_id:
            query = query.filter(Bid.player_id == player_id)

        if team_id:
            query = query.filter(Bid.team_id == team_id)

        return query.order_by(desc(Bid.created_at)).limit(limit).all()

    @staticmethod
    def get_current_bid(
        db: Session,
        auction_id: int,
        player_id: int
    ) -> Optional[Bid]:
        """Get current highest bid for a player"""
        return db.query(Bid).filter(
            and_(
                Bid.auction_id == auction_id,
                Bid.player_id == player_id,
                Bid.is_winning_bid == True
            )
        ).first()

    @staticmethod
    def mark_player_sold(
        db: Session,
        auction_id: int,
        player_id: int,
        current_user: User
    ) -> dict:
        """
        Mark a player as sold to the highest bidder.
        Only admin/auctioneer can do this.
        """
        if current_user.role not in ["admin", "auctioneer"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admin/auctioneer can mark players as sold"
            )

        # Get winning bid
        winning_bid = BidService.get_current_bid(db, auction_id, player_id)

        if not winning_bid:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No bids found for this player"
            )

        # Get player and team
        player = db.query(Player).filter(Player.id == player_id).first()
        team = db.query(Team).filter(Team.id == winning_bid.team_id).first()

        if not player or not team:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Player or team not found"
            )

        # Update player
        player.is_sold = True
        player.final_price = winning_bid.bid_amount
        player.team_id = winning_bid.team_id

        # Update team
        team.remaining_budget -= winning_bid.bid_amount
        team.current_players += 1

        # Update overseas count if applicable
        if player.country.upper() != "INDIA":
            team.overseas_count += 1

        db.commit()
        db.refresh(player)
        db.refresh(team)

        return {
            "player": player,
            "team": team,
            "final_price": winning_bid.bid_amount
        }

    @staticmethod
    def mark_player_unsold(
        db: Session,
        auction_id: int,
        player_id: int,
        current_user: User
    ) -> Player:
        """
        Mark a player as unsold.
        Only admin/auctioneer can do this.
        """
        if current_user.role not in ["admin", "auctioneer"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admin/auctioneer can mark players as unsold"
            )

        player = db.query(Player).filter(Player.id == player_id).first()

        if not player:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Player not found"
            )

        player.is_sold = False
        player.final_price = None
        player.team_id = None

        db.commit()
        db.refresh(player)

        return player
