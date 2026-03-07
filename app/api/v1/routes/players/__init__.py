"""
Player Routes Module
"""

from fastapi import APIRouter
from app.api.v1.routes.players import player_crud

router = APIRouter()
router.include_router(player_crud.router, tags=["Players"])
