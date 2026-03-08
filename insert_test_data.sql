-- ========================================
-- Cricket Auction - Sample Test Data
-- ========================================
-- Run this after creating auction "47Billion2026" (ID: 2)
-- Command: PGPASSWORD=admin psql -h localhost -U postgres -d auction_db -f insert_test_data.sql

-- ========================================
-- STEP 1: Insert Sample Players
-- ========================================

-- Clear existing players for auction 2 (optional)
-- DELETE FROM players WHERE auction_id = 2;

-- Insert 15 sample players for auction ID 2
INSERT INTO players (name, role, country, age, is_overseas, base_price, current_price, status, matches_played, batting_average, bowling_average, auction_id, created_at, updated_at)
VALUES
-- Star Batsmen (5 players)
('Virat Kohli', 'batsman', 'India', 35, false, 20000000, NULL, 'available', 254, 50.5, NULL, 2, NOW(), NOW()),
('Rohit Sharma', 'batsman', 'India', 36, false, 18000000, NULL, 'available', 243, 48.2, NULL, 2, NOW(), NOW()),
('Steve Smith', 'batsman', 'Australia', 34, true, 15000000, NULL, 'available', 178, 51.8, NULL, 2, NOW(), NOW()),
('Kane Williamson', 'batsman', 'New Zealand', 33, true, 16000000, NULL, 'available', 156, 47.9, NULL, 2, NOW(), NOW()),
('Shubman Gill', 'batsman', 'India', 24, false, 12000000, NULL, 'available', 45, 42.3, NULL, 2, NOW(), NOW()),

-- Premium Bowlers (5 players)
('Jasprit Bumrah', 'bowler', 'India', 30, false, 17000000, NULL, 'available', 120, NULL, 23.4, 2, NOW(), NOW()),
('Pat Cummins', 'bowler', 'Australia', 30, true, 16000000, NULL, 'available', 132, NULL, 21.8, 2, NOW(), NOW()),
('Kagiso Rabada', 'bowler', 'South Africa', 28, true, 14000000, NULL, 'available', 98, NULL, 22.1, 2, NOW(), NOW()),
('Mohammed Shami', 'bowler', 'India', 33, false, 13000000, NULL, 'available', 115, NULL, 24.7, 2, NOW(), NOW()),
('Trent Boult', 'bowler', 'New Zealand', 34, true, 13500000, NULL, 'available', 145, NULL, 25.3, 2, NOW(), NOW()),

-- All-rounders (3 players)
('Hardik Pandya', 'all_rounder', 'India', 30, false, 19000000, NULL, 'available', 95, 31.2, 28.5, 2, NOW(), NOW()),
('Ben Stokes', 'all_rounder', 'England', 32, true, 17000000, NULL, 'available', 156, 36.8, 31.4, 2, NOW(), NOW()),
('Ravindra Jadeja', 'all_rounder', 'India', 35, false, 15000000, NULL, 'available', 178, 33.4, 24.2, 2, NOW(), NOW()),

-- Wicket Keepers (2 players)
('Rishabh Pant', 'wicket_keeper', 'India', 26, false, 16000000, NULL, 'available', 87, 42.1, NULL, 2, NOW(), NOW()),
('Jos Buttler', 'wicket_keeper', 'England', 33, true, 15000000, NULL, 'available', 156, 39.8, NULL, 2, NOW(), NOW());

-- Verify insertion
SELECT COUNT(*) as total_players FROM players WHERE auction_id = 2;

-- ========================================
-- STEP 2: Get User IDs for Team Owners
-- ========================================

-- Check existing users
SELECT id, email, username, full_name, role FROM users WHERE email IN ('owner1@auction.com', 'owner2@auction.com');

-- Note: Replace user_id values below with actual IDs from above query

-- ========================================
-- STEP 3: Insert Teams
-- ========================================

-- Clear existing teams for auction 2 (optional)
-- DELETE FROM teams WHERE auction_id = 2;

-- Insert 2 teams (update user_id after checking users table)
INSERT INTO teams (name, short_name, owner_name, logo_url, total_budget, remaining_budget, current_players, overseas_count, max_players, auction_id, user_id, is_active, created_at, updated_at)
VALUES
-- Team 1: Mumbai Indians
-- Replace user_id 10 with actual owner1 user_id
('Mumbai Indians', 'MI', 'Akash Ambani', NULL, 1000000000, 1000000000, 0, 0, 15, 2, 10, true, NOW(), NOW()),

-- Team 2: Chennai Super Kings
-- Replace user_id 11 with actual owner2 user_id
('Chennai Super Kings', 'CSK', 'N. Srinivasan', NULL, 1000000000, 1000000000, 0, 0, 15, 2, 11, true, NOW(), NOW());

-- Verify insertion
SELECT * FROM teams WHERE auction_id = 2;

-- ========================================
-- STEP 4: Verification Queries
-- ========================================

-- Check all data for auction 2
SELECT
    'Players' as entity,
    COUNT(*) as count
FROM players
WHERE auction_id = 2

UNION ALL

SELECT
    'Teams' as entity,
    COUNT(*) as count
FROM teams
WHERE auction_id = 2;

-- Player breakdown by role
SELECT
    role,
    COUNT(*) as count,
    AVG(base_price) as avg_base_price,
    MIN(base_price) as min_price,
    MAX(base_price) as max_price
FROM players
WHERE auction_id = 2
GROUP BY role
ORDER BY role;

-- ========================================
-- NOTES:
-- ========================================
-- 1. Auction ID 2 is for "47Billion2026"
-- 2. Update user_id in teams INSERT after running SELECT query
-- 3. All prices are in rupees (₹)
-- 4. Base prices range from ₹12 Cr to ₹20 Cr
-- 5. All players start with status 'available'
-- 6. Each team gets ₹100 Cr total budget

-- ========================================
-- Manual Steps to Find User IDs:
-- ========================================
-- Run this query first:
/*
SELECT id, email FROM users WHERE email IN ('owner1@auction.com', 'owner2@auction.com');

-- Example output:
--  id  |        email
-- -----+---------------------
--  10  | owner1@auction.com
--  11  | owner2@auction.com

-- Then use these IDs in the teams INSERT above
*/
