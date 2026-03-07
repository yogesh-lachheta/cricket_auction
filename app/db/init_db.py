"""
Database Initialization Script

Run this script to create all database tables.
"""

from sqlalchemy import text
from app.db.base import Base
from app.db.session import engine
from app.models import User, Player, Team, Auction


def init_db():
    """Create all database tables"""
    print("=" * 60)
    print("🚀 Initializing Database Tables")
    print("=" * 60)
    print()

    try:
        # Create all tables
        print("⏳ Creating tables...")
        Base.metadata.create_all(bind=engine)

        print("✅ All tables created successfully!")
        print()

        # List created tables
        with engine.connect() as connection:
            result = connection.execute(text("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                ORDER BY table_name
            """))
            tables = result.fetchall()

            print(f"📁 Created Tables ({len(tables)}):")
            for table in tables:
                print(f"   ✓ {table[0]}")

        print()
        print("=" * 60)
        print("✅ Database initialization complete!")
        print("=" * 60)
        return True

    except Exception as e:
        print(f"❌ Error creating tables: {str(e)}")
        print()
        print("=" * 60)
        print("❌ Database initialization failed!")
        print("=" * 60)
        return False


def drop_all_tables():
    """Drop all database tables - USE WITH CAUTION!"""
    print("=" * 60)
    print("⚠️  WARNING: Dropping all tables!")
    print("=" * 60)
    print()

    try:
        print("⏳ Dropping all tables...")
        Base.metadata.drop_all(bind=engine)

        print("✅ All tables dropped successfully!")
        print()
        print("=" * 60)
        print("✅ Tables dropped!")
        print("=" * 60)
        return True

    except Exception as e:
        print(f"❌ Error dropping tables: {str(e)}")
        return False


def reset_db():
    """Reset database by dropping and recreating all tables"""
    print("=" * 60)
    print("🔄 Resetting Database")
    print("=" * 60)
    print()

    if drop_all_tables():
        print()
        return init_db()
    return False


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "drop":
            drop_all_tables()
        elif command == "reset":
            reset_db()
        else:
            print("Usage: python db/init_db.py [init|drop|reset]")
    else:
        init_db()
