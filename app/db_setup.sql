-- Cricket Auction Database Setup Script
-- Run this file to create database and user

-- Create database user
CREATE USER cricket_admin WITH PASSWORD 'cricket123';

-- Create database
CREATE DATABASE cricket_auction_db OWNER cricket_admin;

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE cricket_auction_db TO cricket_admin;

-- Connect to the new database
\c cricket_auction_db

-- Grant schema privileges
GRANT ALL ON SCHEMA public TO cricket_admin;
