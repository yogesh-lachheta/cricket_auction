"""
Database Connection Status Checker
Run this script to check database connection and status
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from app.core.config import settings


def check_database_connection():
    """Check if database connection is working"""
    print("=" * 60)
    print("🔍 Cricket Auction - Database Connection Checker")
    print("=" * 60)
    print()

    # Print configuration
    print("📋 Configuration:")
    print(f"   Database URL: {settings.DATABASE_URL}")
    print(f"   Database Host: {settings.DB_HOST}")
    print(f"   Database Port: {settings.DB_PORT}")
    print(f"   Database Name: {settings.DB_NAME}")
    print(f"   Database User: {settings.DB_USER}")
    print()

    try:
        # Create engine
        print("⏳ Attempting to connect to database...")
        engine = create_engine(settings.DATABASE_URL)

        # Test connection
        with engine.connect() as connection:
            # Execute simple query
            result = connection.execute(text("SELECT version()"))
            version = result.fetchone()[0]

            print("✅ Database connection successful!")
            print()
            print("📊 Database Information:")
            print(f"   PostgreSQL Version: {version}")
            print()

            # Check if tables exist
            result = connection.execute(text("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                ORDER BY table_name
            """))
            tables = result.fetchall()

            if tables:
                print(f"📁 Existing Tables ({len(tables)}):")
                for table in tables:
                    print(f"   - {table[0]}")
            else:
                print("⚠️  No tables found in database")
                print("   Run 'python init_tables.py' to create tables")

            print()
            print("=" * 60)
            print("✅ Database Status: HEALTHY")
            print("=" * 60)
            return True

    except OperationalError as e:
        print("❌ Database connection failed!")
        print()
        print("Error Details:")
        print(f"   {str(e)}")
        print()
        print("📝 Possible Solutions:")
        print("   1. Check if PostgreSQL is running:")
        print("      pg_isready -h localhost -p 5432")
        print()
        print("   2. Create database and user:")
        print("      sudo -u postgres psql -f db_setup.sql")
        print()
        print("   3. Verify .env file configuration")
        print()
        print("=" * 60)
        print("❌ Database Status: UNAVAILABLE")
        print("=" * 60)
        return False

    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        print()
        print("=" * 60)
        print("❌ Database Status: ERROR")
        print("=" * 60)
        return False


if __name__ == "__main__":
    success = check_database_connection()
    sys.exit(0 if success else 1)
