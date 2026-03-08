"""
Create test users for Cricket Auction Platform
"""
import sys
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User
from app.core.security import hash_password

def create_test_users():
    """Create test users: admin, owner1, owner2"""
    db: Session = SessionLocal()

    try:
        # Check if users already exist
        existing_admin = db.query(User).filter(User.username == "admin").first()
        if existing_admin:
            print("✅ Users already exist!")
            print("\n📋 Login Credentials:")
            print("=" * 50)

            users = db.query(User).all()
            for user in users:
                print(f"\nUsername: {user.username}")
                print(f"Email: {user.email}")
                print(f"Role: {user.role}")
                if user.username == "admin":
                    print(f"Password: Admin@123")
                elif user.username.startswith("owner"):
                    print(f"Password: Owner@123")
                else:
                    print(f"Password: Test@123")
            print("=" * 50)
            return

        # Create Admin User
        admin_user = User(
            email="admin@auction.com",
            username="admin",
            full_name="Admin User",
            hashed_password=hash_password("Admin@123"),
            role="admin",
            is_active=True,
            is_superuser=True,
            email_verified=True,
            mobile_verified=False
        )
        db.add(admin_user)

        # Create Team Owner 1
        owner1 = User(
            email="owner1@auction.com",
            username="owner1",
            full_name="Mumbai Owner",
            hashed_password=hash_password("Owner@123"),
            role="team_owner",
            is_active=True,
            is_superuser=False,
            email_verified=True,
            mobile_verified=False
        )
        db.add(owner1)

        # Create Team Owner 2
        owner2 = User(
            email="owner2@auction.com",
            username="owner2",
            full_name="Chennai Owner",
            hashed_password=hash_password("Owner@123"),
            role="team_owner",
            is_active=True,
            is_superuser=False,
            email_verified=True,
            mobile_verified=False
        )
        db.add(owner2)

        db.commit()

        print("✅ Test users created successfully!")
        print("\n📋 Login Credentials:")
        print("=" * 50)
        print("\n👨‍💼 ADMIN USER:")
        print("   URL: http://localhost:3001/login")
        print("   Username: admin")
        print("   Password: Admin@123")
        print("   Role: admin")

        print("\n👤 TEAM OWNER 1:")
        print("   URL: http://localhost:3001/login")
        print("   Username: owner1")
        print("   Password: Owner@123")
        print("   Role: team_owner")

        print("\n👤 TEAM OWNER 2:")
        print("   URL: http://localhost:3001/login")
        print("   Username: owner2")
        print("   Password: Owner@123")
        print("   Role: team_owner")
        print("=" * 50)

    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_test_users()
