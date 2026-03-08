-- Create test users for Cricket Auction Platform

-- Insert Admin User
INSERT INTO users (email, username, full_name, hashed_password, role, is_active, is_superuser, email_verified, mobile_verified, created_at, updated_at)
VALUES (
    'admin@auction.com',
    'admin',
    'Admin User',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5O2.VY.KLNh8W', -- Password: Admin@123
    'admin',
    true,
    true,
    true,
    false,
    NOW(),
    NOW()
) ON CONFLICT (username) DO NOTHING;

-- Insert Team Owner 1
INSERT INTO users (email, username, full_name, hashed_password, role, is_active, is_superuser, email_verified, mobile_verified, created_at, updated_at)
VALUES (
    'owner1@auction.com',
    'owner1',
    'Mumbai Owner',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5O2.VY.KLNh8W', -- Password: Owner@123
    'team_owner',
    true,
    false,
    true,
    false,
    NOW(),
    NOW()
) ON CONFLICT (username) DO NOTHING;

-- Insert Team Owner 2
INSERT INTO users (email, username, full_name, hashed_password, role, is_active, is_superuser, email_verified, mobile_verified, created_at, updated_at)
VALUES (
    'owner2@auction.com',
    'owner2',
    'Chennai Owner',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5O2.VY.KLNh8W', -- Password: Owner@123
    'team_owner',
    true,
    false,
    true,
    false,
    NOW(),
    NOW()
) ON CONFLICT (username) DO NOTHING;

-- Display created users
SELECT id, username, email, role, is_active FROM users WHERE username IN ('admin', 'owner1', 'owner2');
