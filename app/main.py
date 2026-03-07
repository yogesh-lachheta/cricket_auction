from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.config import settings
from app.db.session import engine, get_db
from app.api.v1.routes.auth import router as auth_router
from app.api.v1.routes.teams import router as teams_router
from app.api.v1.routes.players import router as players_router
from app.api.v1.routes.auctions import router as auctions_router

app = FastAPI(
    title="Cricket Auction Platform",
    description="Real-time cricket player auction system",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routes
app.include_router(auth_router, prefix="/api/v1/auth")
app.include_router(teams_router, prefix="/api/v1/teams")
app.include_router(players_router, prefix="/api/v1/players")
app.include_router(auctions_router, prefix="/api/v1/auctions")


@app.on_event("startup")
async def startup_event():
    """Run on application startup"""
    print("🚀 Cricket Auction Platform starting up...")
    print(f"📊 Database: {settings.DB_NAME}")
    print(f"🔧 Debug Mode: {settings.DEBUG}")


@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown"""
    print("👋 Cricket Auction Platform shutting down...")
    engine.dispose()


@app.get("/")
def root():
    """Root endpoint"""
    return {
        "message": "Cricket Auction Platform API",
        "status": "running",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    """Health check endpoint with database status"""
    try:
        # Test database connection
        db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as e:
        db_status = f"disconnected: {str(e)}"

    return {
        "status": "healthy",
        "database": db_status,
        "version": "1.0.0"
    }