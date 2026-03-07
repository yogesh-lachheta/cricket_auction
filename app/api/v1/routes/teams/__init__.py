"""
Team Routes Module

Combines all team-related endpoints.
"""

from fastapi import APIRouter
from app.api.v1.routes.teams import team_crud


router = APIRouter()

# Include team endpoints
router.include_router(team_crud.router, tags=["Teams"])
