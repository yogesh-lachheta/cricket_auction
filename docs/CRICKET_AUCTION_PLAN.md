# 🏏 IPL-Style Cricket Auction Platform - Complete Plan

---

> ```
> ╔═══════════════════════════════════════════════════════════════════════════╗
> ║  📋 Complete Project Plan for Cricket Auction Platform                    ║
> ║  📅 Version: 1.0  |  Created: February 2026                               ║
> ║  ⏱️  Duration: 75 Days (2 hrs/day)  |  🎓 Level: Beginner Friendly        ║
> ╚═══════════════════════════════════════════════════════════════════════════╝
> ```

---

## 📋 Table of Contents

1. [Project Overview](#1-project-overview)
2. [Tech Stack](#2-tech-stack)
3. [IPL-Style Categories & Rules](#3-ipl-style-categories--rules)
4. [Database Schema](#4-database-schema)
5. [API Endpoints](#5-api-endpoints)
6. [WebSocket Events](#6-websocket-events)
7. [Folder Structure](#7-folder-structure)
8. [Frontend Pages & Components](#8-frontend-pages--components)
9. [User Roles & Permissions](#9-user-roles--permissions)
10. [75-Day Roadmap](#10-75-day-roadmap)
11. [Daily Task Breakdown](#11-daily-task-breakdown)
12. [Beginner Resources](#12-beginner-resources)

---

## 1. Project Overview

> ```
> ┌─────────────────────────────────────────────────────────────────────────────┐
> │  🎯 PROJECT OVERVIEW - What, Why, and How                                   │
> └─────────────────────────────────────────────────────────────────────────────┘
> ```

### 1.1 What We're Building

A real-time IPL-style cricket auction platform where:
- Teams bid for players in live auction
- Only team captains can place bids
- Admin controls the entire auction
- Everything updates in real-time (no page refresh)
- Google authentication for secure login

### 1.2 Key Features

| Feature | Description |
|---------|-------------|
| **Google Login** | Secure OAuth2 authentication |
| **Auto Profile** | User profile created on first login |
| **3 Teams** | Each with captain, members, and purse |
| **IPL Categories** | Capped, Uncapped, Overseas players |
| **Player Roles** | Batter, Bowler, All-rounder, Wicket-keeper |
| **Live Auction** | Real-time bidding with timer |
| **Purse Management** | Auto deduction on player sold |
| **Notifications** | Real-time alerts for all events |
| **Admin Controls** | Start, pause, correction, force-sell |

### 1.3 Project Timeline

```
┌─────────────────────────────────────────────────────────────┐
│                    PROJECT TIMELINE                         │
├─────────────────────────────────────────────────────────────┤
│   Total Duration      : 75 days                             │
│   Daily Effort        : 2 hours                             │
│   Total Hours         : 150 hours                           │
│   Weekly Days         : 7 days                              │
│   Total Weeks         : ~11 weeks                           │
│   Total Months        : ~2.5 months                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Tech Stack

> ```
> ┌─────────────────────────────────────────────────────────────────────────────┐
> │  🛠️ TECH STACK - Technologies Used in This Project                         │
> └─────────────────────────────────────────────────────────────────────────────┘
> ```

### 2.1 Backend

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.11+ | Programming Language |
| FastAPI | 0.109+ | API Framework |
| PostgreSQL | 15+ | Database |
| SQLAlchemy | 2.0+ | ORM (Object Relational Mapper) |
| Alembic | 1.13+ | Database Migrations |
| Pydantic | 2.0+ | Data Validation |
| PyJWT | 2.8+ | JWT Token Authentication |
| Authlib | 1.3+ | Google OAuth |
| python-multipart | 0.0.6+ | File Upload |
| Cloudinary | 1.36+ | Image Storage |
| WebSockets | Built-in | Real-time Communication |
| Uvicorn | 0.27+ | ASGI Server |

### 2.2 Frontend

| Technology | Version | Purpose |
|------------|---------|---------|
| React | 18.2+ | UI Library |
| Vite | 5.0+ | Build Tool |
| TypeScript | 5.3+ | Type Safety |
| Tailwind CSS | 3.4+ | Styling |
| Shadcn UI | Latest | UI Components |
| Zustand | 4.5+ | State Management |
| React Query | 5.0+ | Data Fetching & Caching |
| React Router | 6.22+ | Routing |
| Socket.io Client | 4.7+ | WebSocket Client |
| Axios | 1.6+ | HTTP Client |
| Lucide React | Latest | Icons |

### 2.3 Development Tools

| Tool | Purpose |
|------|---------|
| VS Code | Code Editor |
| DBeaver CE | Database GUI |
| Postman | API Testing |
| Git | Version Control |
| npm/pnpm | Package Manager |

---

## 3. IPL-Style Categories & Rules

> ```
> ┌─────────────────────────────────────────────────────────────────────────────┐
> │  🏏 IPL-STYLE RULES - Player Types, Roles, and Auction Rules               │
> └─────────────────────────────────────────────────────────────────────────────┘
> ```

### 3.1 Player Types

| Type | Code | Description |
|------|------|-------------|
| **Capped** | `CAPPED` | Played international cricket (any country) |
| **Uncapped** | `UNCAPPED` | Only domestic cricket experience |
| **Overseas** | `OVERSEAS` | Foreign players (non-Indian) |

### 3.2 Player Roles

| Role | Code | Description |
|------|------|-------------|
| **Batter** | `BAT` | Specialist batsman |
| **Bowler** | `BOWL` | Specialist bowler |
| **All-rounder** | `AR` | Both batting & bowling |
| **Wicket-keeper** | `WK` | Keeper with batting ability |

### 3.3 Base Price Slabs (IPL Style)

| Slab | Amount | Typical Players |
|------|--------|-----------------|
| **Slab 1** | ₹2,00,00,000 | Star international players |
| **Slab 2** | ₹1,50,00,000 | Proven performers |
| **Slab 3** | ₹1,00,00,000 | Experienced players |
| **Slab 4** | ₹75,00,000 | Good domestic record |
| **Slab 5** | ₹50,00,000 | Promising players |
| **Slab 6** | ₹40,00,000 | Decent performers |
| **Slab 7** | ₹30,00,000 | Young talents |
| **Slab 8** | ₹20,00,000 | New entrants |

### 3.4 Auction Rules

```
┌─────────────────────────────────────────────────────────────┐
│                    AUCTION RULES                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Team Purse              : ₹100,00,00,000 (100 Crore)      │
│   Maximum Squad Size      : 25 players                      │
│   Minimum Squad Size      : 18 players                      │
│   Maximum Overseas        : 8 players in squad              │
│   Overseas in Playing XI  : 4 maximum                       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Bid Timer               : 15 seconds                      │
│   Timer Reset             : On every new bid                │
│   Minimum Increment       : ₹5,00,000 (5 Lakhs)             │
│   Quick Increments        : +5L, +10L, +25L, +50L, +1Cr     │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Player Sold When        : Timer reaches 0                 │
│   Unsold                  : No bids at base price           │
│   Re-auction              : Unsold players in final round   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.5 Auction Sets (Player Groups)

| Set | Name | Players |
|-----|------|---------|
| **Set 1** | Marquee Batters | Capped BAT (₹2Cr base) |
| **Set 2** | Marquee All-rounders | Capped AR (₹2Cr base) |
| **Set 3** | Marquee Bowlers | Capped BOWL (₹2Cr base) |
| **Set 4** | Marquee Wicket-keepers | Capped WK (₹2Cr base) |
| **Set 5** | Capped Batters | ₹1Cr - ₹1.5Cr base |
| **Set 6** | Capped Bowlers | ₹1Cr - ₹1.5Cr base |
| **Set 7** | Capped All-rounders | ₹1Cr - ₹1.5Cr base |
| **Set 8** | Overseas Players | Various base prices |
| **Set 9** | Uncapped Batters | ₹20L - ₹75L base |
| **Set 10** | Uncapped Bowlers | ₹20L - ₹75L base |
| **Set 11** | Uncapped All-rounders | ₹20L - ₹75L base |
| **Set 12** | Uncapped Wicket-keepers | ₹20L - ₹75L base |
| **Set 13** | Accelerated Round | Unsold players |

### 3.6 Bid Validation Rules

```python
# Bid is VALID only if ALL conditions are TRUE:

1. user.role == "captain"                    # Only captain can bid
2. bid_amount > current_bid                  # Must be higher than current
3. bid_amount >= base_price                  # Must meet base price
4. bid_amount <= team.current_purse          # Must have enough money
5. team.squad_count < team.max_squad_size    # Squad not full
6. if player.type == "OVERSEAS":
       team.overseas_count < team.max_overseas   # Overseas limit check
7. auction.status == "live"                  # Auction must be live
8. player.status == "live"                   # Player must be on block
```

---

## 4. Database Schema

> ```
> ┌─────────────────────────────────────────────────────────────────────────────┐
> │  🗄️ DATABASE SCHEMA - Tables, Relationships, and SQL                       │
> └─────────────────────────────────────────────────────────────────────────────┘
> ```

### 4.1 ER Diagram (Text)

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│    USERS    │       │    TEAMS    │       │   PLAYERS   │
├─────────────┤       ├─────────────┤       ├─────────────┤
│ id (PK)     │──┐    │ id (PK)     │──┐    │ id (PK)     │
│ email       │  │    │ name        │  │    │ name        │
│ name        │  │    │ short_name  │  │    │ photo_url   │
│ avatar_url  │  │    │ logo_url    │  │    │ player_type │
│ provider    │  │    │ color       │  │    │ role        │
│ provider_id │  │    │ purse       │  │    │ base_price  │
│ role        │  │    │ max_squad   │  │    │ set_number  │
│ team_id(FK) │──┼────│ max_overseas│  │    │ is_marquee  │
│ is_captain  │  │    │ captain_id  │──┘    │ status      │
│ created_at  │  │    │ created_at  │       │ sold_price  │
└─────────────┘  │    └─────────────┘       │ sold_to(FK) │──┐
                 │                          │ created_at  │  │
                 │                          └─────────────┘  │
                 │                                           │
                 │    ┌─────────────┐       ┌─────────────┐  │
                 │    │   AUCTIONS  │       │    BIDS     │  │
                 │    ├─────────────┤       ├─────────────┤  │
                 │    │ id (PK)     │       │ id (PK)     │  │
                 │    │ status      │       │ auction_id  │──┤
                 │    │ curr_player │───────│ player_id   │  │
                 │    │ curr_bid    │       │ team_id     │──┤
                 │    │ curr_team   │───────│ user_id     │──┤
                 │    │ timer_end   │       │ amount      │  │
                 │    │ created_at  │       │ created_at  │  │
                 │    └─────────────┘       └─────────────┘  │
                 │                                           │
                 │    ┌─────────────┐       ┌─────────────┐  │
                 │    │AUCTION_SETS │       │NOTIFICATIONS│  │
                 │    ├─────────────┤       ├─────────────┤  │
                 │    │ id (PK)     │       │ id (PK)     │  │
                 │    │ set_number  │       │ user_id(FK) │──┘
                 │    │ name        │       │ title       │
                 │    │ description │       │ message     │
                 │    │ status      │       │ type        │
                 │    │ order       │       │ is_read     │
                 │    │ created_at  │       │ created_at  │
                 │    └─────────────┘       └─────────────┘
```

### 4.2 Detailed Table Definitions

#### Table: `users`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | UUID | PK, DEFAULT uuid_generate_v4() | Unique identifier |
| `email` | VARCHAR(255) | UNIQUE, NOT NULL | User email |
| `name` | VARCHAR(100) | NOT NULL | Display name |
| `avatar_url` | VARCHAR(500) | NULL | Profile photo URL |
| `provider` | VARCHAR(20) | NOT NULL | 'google' or 'microsoft' |
| `provider_id` | VARCHAR(255) | NOT NULL | OAuth provider user ID |
| `role` | ENUM | NOT NULL, DEFAULT 'member' | 'admin', 'captain', 'member' |
| `team_id` | UUID | FK → teams.id, NULL | Assigned team |
| `is_captain` | BOOLEAN | DEFAULT FALSE | Is team captain |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Creation timestamp |
| `updated_at` | TIMESTAMP | DEFAULT NOW() | Last update timestamp |

#### Table: `teams`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | UUID | PK | Unique identifier |
| `name` | VARCHAR(100) | UNIQUE, NOT NULL | Team full name |
| `short_name` | VARCHAR(5) | UNIQUE, NOT NULL | Short code (MI, CSK) |
| `logo_url` | VARCHAR(500) | NULL | Team logo URL |
| `primary_color` | VARCHAR(7) | NOT NULL | Hex color (#004BA0) |
| `secondary_color` | VARCHAR(7) | NULL | Secondary hex color |
| `initial_purse` | BIGINT | NOT NULL | Starting purse amount |
| `current_purse` | BIGINT | NOT NULL | Remaining purse |
| `max_squad_size` | INTEGER | DEFAULT 25 | Maximum players allowed |
| `max_overseas` | INTEGER | DEFAULT 8 | Maximum overseas players |
| `captain_id` | UUID | FK → users.id, NULL | Team captain |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Creation timestamp |
| `updated_at` | TIMESTAMP | DEFAULT NOW() | Last update timestamp |

#### Table: `players`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | UUID | PK | Unique identifier |
| `name` | VARCHAR(100) | NOT NULL | Player name |
| `photo_url` | VARCHAR(500) | NULL | Player photo URL |
| `player_type` | ENUM | NOT NULL | 'CAPPED', 'UNCAPPED', 'OVERSEAS' |
| `role` | ENUM | NOT NULL | 'BAT', 'BOWL', 'AR', 'WK' |
| `base_price` | BIGINT | NOT NULL | Base auction price |
| `set_number` | INTEGER | NOT NULL | Auction set number |
| `is_marquee` | BOOLEAN | DEFAULT FALSE | Marquee player flag |
| `status` | ENUM | DEFAULT 'upcoming' | 'upcoming', 'live', 'sold', 'unsold' |
| `sold_price` | BIGINT | NULL | Final sold price |
| `sold_to_team_id` | UUID | FK → teams.id, NULL | Winning team |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Creation timestamp |
| `updated_at` | TIMESTAMP | DEFAULT NOW() | Last update timestamp |

#### Table: `auctions`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | UUID | PK | Unique identifier |
| `status` | ENUM | DEFAULT 'not_started' | 'not_started', 'live', 'paused', 'completed' |
| `current_player_id` | UUID | FK → players.id, NULL | Player on auction block |
| `current_bid` | BIGINT | DEFAULT 0 | Current highest bid |
| `current_team_id` | UUID | FK → teams.id, NULL | Current highest bidder team |
| `current_set_id` | UUID | FK → auction_sets.id, NULL | Current auction set |
| `timer_end_at` | TIMESTAMP | NULL | When timer expires |
| `bid_increment` | BIGINT | DEFAULT 500000 | Current bid increment |
| `started_at` | TIMESTAMP | NULL | Auction start time |
| `ended_at` | TIMESTAMP | NULL | Auction end time |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Creation timestamp |
| `updated_at` | TIMESTAMP | DEFAULT NOW() | Last update timestamp |

#### Table: `auction_sets`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | UUID | PK | Unique identifier |
| `set_number` | INTEGER | UNIQUE, NOT NULL | Set order number |
| `name` | VARCHAR(100) | NOT NULL | Set name |
| `description` | VARCHAR(255) | NULL | Set description |
| `status` | ENUM | DEFAULT 'pending' | 'pending', 'active', 'completed' |
| `display_order` | INTEGER | NOT NULL | Display sequence |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Creation timestamp |

#### Table: `bids`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | UUID | PK | Unique identifier |
| `auction_id` | UUID | FK → auctions.id, NOT NULL | Auction reference |
| `player_id` | UUID | FK → players.id, NOT NULL | Player being bid on |
| `team_id` | UUID | FK → teams.id, NOT NULL | Bidding team |
| `user_id` | UUID | FK → users.id, NOT NULL | User who placed bid |
| `amount` | BIGINT | NOT NULL | Bid amount |
| `is_valid` | BOOLEAN | DEFAULT TRUE | Was bid valid |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Bid timestamp |

#### Table: `notifications`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | UUID | PK | Unique identifier |
| `user_id` | UUID | FK → users.id, NOT NULL | Recipient user |
| `title` | VARCHAR(100) | NOT NULL | Notification title |
| `message` | VARCHAR(500) | NOT NULL | Notification body |
| `type` | ENUM | DEFAULT 'info' | 'info', 'success', 'warning', 'error' |
| `is_read` | BOOLEAN | DEFAULT FALSE | Read status |
| `metadata` | JSONB | NULL | Additional data |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Creation timestamp |

### 4.3 Indexes

```sql
-- Performance indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_team_id ON users(team_id);
CREATE INDEX idx_players_status ON players(status);
CREATE INDEX idx_players_set_number ON players(set_number);
CREATE INDEX idx_players_sold_to ON players(sold_to_team_id);
CREATE INDEX idx_bids_player_id ON bids(player_id);
CREATE INDEX idx_bids_team_id ON bids(team_id);
CREATE INDEX idx_notifications_user_id ON notifications(user_id);
CREATE INDEX idx_notifications_is_read ON notifications(is_read);
```

### 4.4 Enums

```sql
-- User roles
CREATE TYPE user_role AS ENUM ('admin', 'captain', 'member');

-- Player types
CREATE TYPE player_type AS ENUM ('CAPPED', 'UNCAPPED', 'OVERSEAS');

-- Player roles
CREATE TYPE player_role AS ENUM ('BAT', 'BOWL', 'AR', 'WK');

-- Player status
CREATE TYPE player_status AS ENUM ('upcoming', 'live', 'sold', 'unsold');

-- Auction status
CREATE TYPE auction_status AS ENUM ('not_started', 'live', 'paused', 'completed');

-- Auction set status
CREATE TYPE set_status AS ENUM ('pending', 'active', 'completed');

-- Notification type
CREATE TYPE notification_type AS ENUM ('info', 'success', 'warning', 'error');
```

---

## 5. API Endpoints

> ```
> ┌─────────────────────────────────────────────────────────────────────────────┐
> │  🔌 API ENDPOINTS - All REST APIs with Request/Response                    │
> └─────────────────────────────────────────────────────────────────────────────┘
> ```

### 5.1 Authentication APIs

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| `GET` | `/api/auth/google` | Redirect to Google OAuth | Public |
| `GET` | `/api/auth/google/callback` | Google OAuth callback | Public |
| `GET` | `/api/auth/me` | Get current user info | Authenticated |
| `POST` | `/api/auth/logout` | Logout user | Authenticated |
| `POST` | `/api/auth/refresh` | Refresh JWT token | Authenticated |

### 5.2 User APIs

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| `GET` | `/api/users` | List all users | Admin |
| `GET` | `/api/users/{id}` | Get user by ID | Authenticated |
| `PUT` | `/api/users/{id}` | Update user profile | Self/Admin |
| `POST` | `/api/users/{id}/avatar` | Upload avatar | Self/Admin |
| `DELETE` | `/api/users/{id}/avatar` | Remove avatar | Self/Admin |

### 5.3 Team APIs

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| `GET` | `/api/teams` | List all teams | Authenticated |
| `POST` | `/api/teams` | Create new team | Admin |
| `GET` | `/api/teams/{id}` | Get team details | Authenticated |
| `PUT` | `/api/teams/{id}` | Update team | Admin |
| `DELETE` | `/api/teams/{id}` | Delete team | Admin |
| `GET` | `/api/teams/{id}/players` | Get team's players | Authenticated |
| `GET` | `/api/teams/{id}/members` | Get team members | Authenticated |
| `POST` | `/api/teams/{id}/captain` | Assign captain | Admin |
| `DELETE` | `/api/teams/{id}/captain` | Remove captain | Admin |
| `POST` | `/api/teams/{id}/members` | Add member to team | Admin |
| `DELETE` | `/api/teams/{id}/members/{userId}` | Remove member | Admin |

### 5.4 Player APIs

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| `GET` | `/api/players` | List all players | Authenticated |
| `POST` | `/api/players` | Create player | Admin |
| `GET` | `/api/players/{id}` | Get player details | Authenticated |
| `PUT` | `/api/players/{id}` | Update player | Admin |
| `DELETE` | `/api/players/{id}` | Delete player | Admin |
| `POST` | `/api/players/{id}/photo` | Upload player photo | Admin |
| `GET` | `/api/players/by-set/{setNumber}` | Get players by set | Authenticated |
| `GET` | `/api/players/sold` | Get sold players | Authenticated |
| `GET` | `/api/players/unsold` | Get unsold players | Authenticated |

### 5.5 Auction Set APIs

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| `GET` | `/api/auction-sets` | List all sets | Authenticated |
| `POST` | `/api/auction-sets` | Create auction set | Admin |
| `PUT` | `/api/auction-sets/{id}` | Update set | Admin |
| `DELETE` | `/api/auction-sets/{id}` | Delete set | Admin |
| `PUT` | `/api/auction-sets/reorder` | Reorder sets | Admin |

### 5.6 Auction APIs

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| `GET` | `/api/auction` | Get auction state | Authenticated |
| `POST` | `/api/auction/start` | Start auction | Admin |
| `POST` | `/api/auction/pause` | Pause auction | Admin |
| `POST` | `/api/auction/resume` | Resume auction | Admin |
| `POST` | `/api/auction/end` | End auction | Admin |
| `POST` | `/api/auction/next-player` | Bring next player | Admin |
| `POST` | `/api/auction/next-set` | Move to next set | Admin |
| `POST` | `/api/auction/force-sell` | Force sell player | Admin |
| `POST` | `/api/auction/mark-unsold` | Mark player unsold | Admin |
| `POST` | `/api/auction/correction` | Correct last bid | Admin |
| `POST` | `/api/auction/undo-sell` | Undo player sell | Admin |

### 5.7 Bid APIs

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| `POST` | `/api/bids` | Place a bid | Captain |
| `GET` | `/api/bids/history` | Get all bid history | Authenticated |
| `GET` | `/api/bids/player/{playerId}` | Get bids for player | Authenticated |
| `GET` | `/api/bids/team/{teamId}` | Get team's bids | Authenticated |

### 5.8 Notification APIs

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| `GET` | `/api/notifications` | Get user's notifications | Authenticated |
| `GET` | `/api/notifications/unread-count` | Get unread count | Authenticated |
| `PUT` | `/api/notifications/{id}/read` | Mark as read | Authenticated |
| `PUT` | `/api/notifications/read-all` | Mark all as read | Authenticated |
| `DELETE` | `/api/notifications/{id}` | Delete notification | Authenticated |

### 5.9 Dashboard/Stats APIs

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| `GET` | `/api/stats/auction` | Auction statistics | Authenticated |
| `GET` | `/api/stats/teams` | Team-wise stats | Authenticated |
| `GET` | `/api/stats/top-buys` | Top expensive players | Authenticated |

---

## 6. WebSocket Events

> ```
> ┌─────────────────────────────────────────────────────────────────────────────┐
> │  🌐 WEBSOCKET EVENTS - Real-time Communication Events                      │
> └─────────────────────────────────────────────────────────────────────────────┘
> ```

### 6.1 Connection

```javascript
// Client connects to WebSocket
ws://localhost:8000/ws/auction?token=JWT_TOKEN
```

### 6.2 Server → Client Events

| Event | Payload | Description |
|-------|---------|-------------|
| `auction:started` | `{ auction_id, started_at }` | Auction has started |
| `auction:paused` | `{ auction_id, paused_at }` | Auction paused |
| `auction:resumed` | `{ auction_id, resumed_at }` | Auction resumed |
| `auction:ended` | `{ auction_id, ended_at }` | Auction completed |
| `set:changed` | `{ set_id, set_name, set_number }` | New set started |
| `player:live` | `{ player }` | New player on block |
| `bid:new` | `{ bid_id, team_id, team_name, amount, bidder }` | New bid placed |
| `timer:tick` | `{ seconds_remaining }` | Timer countdown (every second) |
| `timer:warning` | `{ seconds_remaining }` | Timer < 5 seconds |
| `player:sold` | `{ player, team, amount }` | Player sold |
| `player:unsold` | `{ player }` | Player unsold |
| `purse:updated` | `{ team_id, new_purse }` | Team purse changed |
| `team:updated` | `{ team }` | Team info updated |
| `captain:assigned` | `{ team_id, user_id }` | New captain assigned |
| `notification:new` | `{ notification }` | New notification |
| `correction:made` | `{ details }` | Admin made correction |
| `error` | `{ message, code }` | Error occurred |

### 6.3 Client → Server Events

| Event | Payload | Description |
|-------|---------|-------------|
| `bid:place` | `{ amount }` | Place a bid (captain only) |
| `ping` | `{}` | Keep connection alive |

### 6.4 Event Flow Example

```
┌─────────────────────────────────────────────────────────────┐
│                    AUCTION EVENT FLOW                       │
└─────────────────────────────────────────────────────────────┘

Admin clicks "Start Auction"
    │
    ▼
Server: auction:started → All clients
    │
    ▼
Server: set:changed (Set 1) → All clients
    │
    ▼
Server: player:live (Player 1) → All clients
    │
    ▼
Server: timer:tick (15, 14, 13...) → All clients
    │
    ▼
Captain clicks "Bid ₹2.5 Cr"
    │
    ▼
Client: bid:place { amount: 25000000 } → Server
    │
    ▼
Server validates bid (role, amount, purse)
    │
    ▼
Server: bid:new → All clients
Server: timer:tick (reset to 15) → All clients
Server: purse:updated → All clients
    │
    ▼
... more bids ...
    │
    ▼
Timer reaches 0
    │
    ▼
Server: player:sold → All clients
Server: purse:updated → All clients
Server: notification:new → Winner team members
    │
    ▼
Server: player:live (next player) → All clients
```

---

## 7. Folder Structure

> ```
> ┌─────────────────────────────────────────────────────────────────────────────┐
> │  📁 FOLDER STRUCTURE - Project Organization                                │
> └─────────────────────────────────────────────────────────────────────────────┘
> ```

### 7.1 Backend Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                      # FastAPI app entry point
│   ├── config.py                    # Settings & env variables
│   ├── database.py                  # Database connection
│   │
│   ├── models/                      # SQLAlchemy Models
│   │   ├── __init__.py
│   │   ├── base.py                  # Base model class
│   │   ├── user.py
│   │   ├── team.py
│   │   ├── player.py
│   │   ├── auction.py
│   │   ├── auction_set.py
│   │   ├── bid.py
│   │   └── notification.py
│   │
│   ├── schemas/                     # Pydantic Schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── team.py
│   │   ├── player.py
│   │   ├── auction.py
│   │   ├── auction_set.py
│   │   ├── bid.py
│   │   ├── notification.py
│   │   └── common.py                # Common response schemas
│   │
│   ├── routers/                     # API Routes
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── teams.py
│   │   ├── players.py
│   │   ├── auction.py
│   │   ├── auction_sets.py
│   │   ├── bids.py
│   │   ├── notifications.py
│   │   └── stats.py
│   │
│   ├── services/                    # Business Logic
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── team_service.py
│   │   ├── player_service.py
│   │   ├── auction_service.py
│   │   ├── bid_service.py
│   │   ├── notification_service.py
│   │   └── upload_service.py        # Cloudinary upload
│   │
│   ├── repositories/                # Database Operations
│   │   ├── __init__.py
│   │   ├── base_repo.py             # Base repository class
│   │   ├── user_repo.py
│   │   ├── team_repo.py
│   │   ├── player_repo.py
│   │   ├── auction_repo.py
│   │   ├── bid_repo.py
│   │   └── notification_repo.py
│   │
│   ├── websockets/                  # WebSocket Handlers
│   │   ├── __init__.py
│   │   ├── manager.py               # Connection Manager
│   │   ├── auction_ws.py            # Auction WebSocket
│   │   └── events.py                # Event definitions
│   │
│   ├── utils/                       # Utilities
│   │   ├── __init__.py
│   │   ├── security.py              # JWT, hashing
│   │   ├── oauth.py                 # Google/Microsoft OAuth
│   │   ├── timer.py                 # Auction timer
│   │   └── helpers.py               # Helper functions
│   │
│   ├── middleware/                  # Custom Middleware
│   │   ├── __init__.py
│   │   ├── auth.py                  # Auth middleware
│   │   └── logging.py               # Request logging
│   │
│   └── exceptions/                  # Custom Exceptions
│       ├── __init__.py
│       └── handlers.py              # Exception handlers
│
├── alembic/                         # Database Migrations
│   ├── versions/
│   │   └── 001_initial.py
│   ├── env.py
│   └── script.py.mako
│
├── tests/                           # Unit Tests
│   ├── __init__.py
│   ├── conftest.py                  # Test fixtures
│   ├── test_auth.py
│   ├── test_teams.py
│   ├── test_players.py
│   ├── test_auction.py
│   └── test_bids.py
│
├── scripts/                         # Utility Scripts
│   ├── seed_data.py                 # Seed initial data
│   └── create_admin.py              # Create admin user
│
├── .env.example                     # Environment template
├── .gitignore
├── alembic.ini                      # Alembic config
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Docker config
└── README.md
```

### 7.2 Frontend Structure

```
frontend/
├── public/
│   ├── favicon.ico
│   ├── logo.png
│   └── teams/                       # Team logos
│       ├── mi.png
│       ├── csk.png
│       └── rcb.png
│
├── src/
│   ├── main.tsx                     # App entry point
│   ├── App.tsx                      # Root component
│   ├── index.css                    # Global styles
│   ├── vite-env.d.ts
│   │
│   ├── components/
│   │   ├── ui/                      # Shadcn UI Components
│   │   │   ├── button.tsx
│   │   │   ├── card.tsx
│   │   │   ├── input.tsx
│   │   │   ├── badge.tsx
│   │   │   ├── avatar.tsx
│   │   │   ├── dialog.tsx
│   │   │   ├── dropdown-menu.tsx
│   │   │   ├── select.tsx
│   │   │   ├── table.tsx
│   │   │   ├── tabs.tsx
│   │   │   ├── toast.tsx
│   │   │   ├── skeleton.tsx
│   │   │   └── ... (more shadcn)
│   │   │
│   │   ├── layout/
│   │   │   ├── Header.tsx
│   │   │   ├── Sidebar.tsx
│   │   │   ├── Layout.tsx
│   │   │   ├── AdminLayout.tsx
│   │   │   └── Footer.tsx
│   │   │
│   │   ├── auth/
│   │   │   ├── GoogleLoginButton.tsx
│   │   │   ├── ProtectedRoute.tsx
│   │   │   ├── AdminRoute.tsx
│   │   │   └── CaptainRoute.tsx
│   │   │
│   │   ├── auction/
│   │   │   ├── PlayerCard.tsx       # Big player display
│   │   │   ├── PlayerCardSmall.tsx  # List item
│   │   │   ├── BidPanel.tsx         # Bidding controls
│   │   │   ├── BidButton.tsx
│   │   │   ├── Timer.tsx            # Countdown timer
│   │   │   ├── TimerCircular.tsx    # Circular timer
│   │   │   ├── CurrentBid.tsx
│   │   │   ├── LeadingTeam.tsx
│   │   │   ├── TeamPurseCard.tsx
│   │   │   ├── TeamPurseList.tsx
│   │   │   ├── BidHistory.tsx
│   │   │   ├── SoldOverlay.tsx      # Sold animation
│   │   │   ├── UnsoldOverlay.tsx
│   │   │   ├── SetIndicator.tsx
│   │   │   └── AuctionStatus.tsx
│   │   │
│   │   ├── admin/
│   │   │   ├── TeamForm.tsx
│   │   │   ├── TeamList.tsx
│   │   │   ├── PlayerForm.tsx
│   │   │   ├── PlayerList.tsx
│   │   │   ├── PlayerImport.tsx     # Bulk import
│   │   │   ├── SetForm.tsx
│   │   │   ├── SetList.tsx
│   │   │   ├── CaptainAssign.tsx
│   │   │   ├── MemberAssign.tsx
│   │   │   ├── AuctionControl.tsx   # Start/pause/etc
│   │   │   ├── CorrectionPanel.tsx
│   │   │   └── StatsCard.tsx
│   │   │
│   │   ├── team/
│   │   │   ├── TeamCard.tsx
│   │   │   ├── TeamDetail.tsx
│   │   │   ├── TeamSquad.tsx
│   │   │   ├── TeamMembers.tsx
│   │   │   └── PurseDisplay.tsx
│   │   │
│   │   ├── player/
│   │   │   ├── PlayerDetail.tsx
│   │   │   ├── PlayerStats.tsx
│   │   │   ├── PlayerBadge.tsx      # Role/type badge
│   │   │   └── PlayerFilter.tsx
│   │   │
│   │   ├── notification/
│   │   │   ├── NotificationBell.tsx
│   │   │   ├── NotificationList.tsx
│   │   │   ├── NotificationItem.tsx
│   │   │   └── NotificationToast.tsx
│   │   │
│   │   └── common/
│   │       ├── Loader.tsx
│   │       ├── Spinner.tsx
│   │       ├── EmptyState.tsx
│   │       ├── ErrorState.tsx
│   │       ├── ConfirmDialog.tsx
│   │       ├── PriceDisplay.tsx     # Format ₹ amounts
│   │       ├── RoleBadge.tsx
│   │       └── Avatar.tsx
│   │
│   ├── pages/
│   │   ├── LoginPage.tsx
│   │   ├── DashboardPage.tsx
│   │   ├── AuctionPage.tsx
│   │   ├── ProfilePage.tsx
│   │   ├── TeamsPage.tsx
│   │   ├── TeamDetailPage.tsx
│   │   ├── PlayersPage.tsx
│   │   ├── BidHistoryPage.tsx
│   │   ├── NotificationsPage.tsx
│   │   ├── admin/
│   │   │   ├── AdminDashboard.tsx
│   │   │   ├── AdminTeams.tsx
│   │   │   ├── AdminPlayers.tsx
│   │   │   ├── AdminSets.tsx
│   │   │   ├── AdminAuction.tsx
│   │   │   └── AdminUsers.tsx
│   │   └── NotFoundPage.tsx
│   │
│   ├── hooks/
│   │   ├── useAuth.ts
│   │   ├── useWebSocket.ts
│   │   ├── useAuction.ts
│   │   ├── useTimer.ts
│   │   ├── useNotifications.ts
│   │   ├── useTeams.ts
│   │   ├── usePlayers.ts
│   │   └── useDebounce.ts
│   │
│   ├── services/
│   │   ├── api.ts                   # Axios instance
│   │   ├── authService.ts
│   │   ├── userService.ts
│   │   ├── teamService.ts
│   │   ├── playerService.ts
│   │   ├── auctionService.ts
│   │   ├── bidService.ts
│   │   ├── notificationService.ts
│   │   └── uploadService.ts
│   │
│   ├── store/
│   │   ├── authStore.ts
│   │   ├── auctionStore.ts
│   │   ├── teamStore.ts
│   │   ├── notificationStore.ts
│   │   └── uiStore.ts               # UI state (sidebar, etc)
│   │
│   ├── types/
│   │   ├── index.ts                 # Export all types
│   │   ├── user.ts
│   │   ├── team.ts
│   │   ├── player.ts
│   │   ├── auction.ts
│   │   ├── bid.ts
│   │   ├── notification.ts
│   │   └── api.ts                   # API response types
│   │
│   ├── lib/
│   │   ├── utils.ts                 # Shadcn utils
│   │   ├── formatters.ts            # Price, date formatters
│   │   └── validators.ts            # Form validation
│   │
│   ├── constants/
│   │   ├── index.ts
│   │   ├── routes.ts                # Route paths
│   │   ├── api.ts                   # API endpoints
│   │   └── auction.ts               # Auction constants
│   │
│   └── config/
│       └── env.ts                   # Environment config
│
├── .env.example
├── .gitignore
├── components.json                  # Shadcn config
├── tailwind.config.js
├── postcss.config.js
├── tsconfig.json
├── tsconfig.node.json
├── vite.config.ts
├── package.json
└── README.md
```

---

## 8. Frontend Pages & Components

> ```
> ┌─────────────────────────────────────────────────────────────────────────────┐
> │  🖥️ FRONTEND PAGES - React Components and UI Design                       │
> └─────────────────────────────────────────────────────────────────────────────┘
> ```

### 8.1 Page List

| Page | Route | Access | Description |
|------|-------|--------|-------------|
| Login | `/login` | Public | Google login button |
| Dashboard | `/` | All | Overview, quick stats |
| Auction | `/auction` | All | Live auction view |
| Teams | `/teams` | All | List all teams |
| Team Detail | `/teams/:id` | All | Team squad & info |
| Players | `/players` | All | All players list |
| Bid History | `/history` | All | All bids log |
| Profile | `/profile` | All | User profile |
| Notifications | `/notifications` | All | All notifications |
| Admin Dashboard | `/admin` | Admin | Admin overview |
| Admin Teams | `/admin/teams` | Admin | Manage teams |
| Admin Players | `/admin/players` | Admin | Manage players |
| Admin Sets | `/admin/sets` | Admin | Manage auction sets |
| Admin Auction | `/admin/auction` | Admin | Control auction |
| Admin Users | `/admin/users` | Admin | Manage users |
| 404 | `*` | Public | Not found |

### 8.2 Auction Page Layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│  HEADER: Logo | Navigation | NotificationBell | UserMenu               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────────────────────┐  ┌───────────────────────────────┐ │
│  │                                 │  │  SET 1: MARQUEE BATTERS       │ │
│  │       PLAYER CARD (Large)       │  │  Player 3 of 12               │ │
│  │                                 │  ├───────────────────────────────┤ │
│  │  ┌─────────────────────────┐    │  │                               │ │
│  │  │                         │    │  │   CURRENT BID                 │ │
│  │  │      PLAYER PHOTO       │    │  │   ₹15,25,00,000               │ │
│  │  │                         │    │  │                               │ │
│  │  └─────────────────────────┘    │  │   LEADING: MUMBAI INDIANS     │ │
│  │                                 │  │   [MI Logo]                   │ │
│  │  VIRAT KOHLI                    │  │                               │ │
│  │  [CAPPED] [BATTER]              │  ├───────────────────────────────┤ │
│  │                                 │  │                               │ │
│  │  Base Price: ₹2,00,00,000       │  │      ┌─────────────┐          │ │
│  │                                 │  │      │     08      │          │ │
│  │                                 │  │      │   seconds   │          │ │
│  │                                 │  │      └─────────────┘          │ │
│  │                                 │  │                               │ │
│  └─────────────────────────────────┘  └───────────────────────────────┘ │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐│
│  │  BID PANEL (Captain Only)                                          ││
│  │                                                                     ││
│  │  [+5L] [+10L] [+25L] [+50L] [+1Cr]     [ BID ₹15,30,00,000 ]       ││
│  │                                                                     ││
│  └─────────────────────────────────────────────────────────────────────┘│
│                                                                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐           │
│  │ MUMBAI INDIANS  │ │ CHENNAI SK      │ │ ROYAL CB        │           │
│  │ ────────────────│ │ ────────────────│ │ ────────────────│           │
│  │ Purse: ₹45.5 Cr │ │ Purse: ₹38.2 Cr │ │ Purse: ₹52.1 Cr │           │
│  │ Squad: 12/25    │ │ Squad: 10/25    │ │ Squad: 8/25     │           │
│  │ OS: 4/8         │ │ OS: 3/8         │ │ OS: 5/8         │           │
│  │ ▓▓▓▓▓▓▓░░░ 45%  │ │ ▓▓▓▓░░░░░░ 38%  │ │ ▓▓▓▓▓▓▓▓░░ 52%  │           │
│  └─────────────────┘ └─────────────────┘ └─────────────────┘           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 8.3 Admin Auction Control

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ADMIN AUCTION CONTROL                                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Auction Status: [LIVE]              Current Set: Set 1 - Marquee       │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  CONTROLS                                                         │  │
│  │                                                                   │  │
│  │  [▶ START]  [⏸ PAUSE]  [⏭ NEXT PLAYER]  [⏭ NEXT SET]            │  │
│  │                                                                   │  │
│  │  [🔨 FORCE SELL]  [❌ MARK UNSOLD]  [↩ UNDO LAST]                │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  CORRECTION PANEL                                                 │  │
│  │                                                                   │  │
│  │  Player: [Virat Kohli    ▼]                                       │  │
│  │  Team:   [Mumbai Indians ▼]                                       │  │
│  │  Amount: [₹ 15,00,00,000   ]                                      │  │
│  │                                                                   │  │
│  │  [APPLY CORRECTION]                                               │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  UPCOMING PLAYERS (Drag to reorder)                               │  │
│  │                                                                   │  │
│  │  1. ☰ Rohit Sharma    [BAT] [CAPPED]   ₹2Cr                      │  │
│  │  2. ☰ KL Rahul        [WK]  [CAPPED]   ₹2Cr                      │  │
│  │  3. ☰ Hardik Pandya   [AR]  [CAPPED]   ₹2Cr                      │  │
│  │  4. ☰ Jasprit Bumrah  [BOWL][CAPPED]   ₹2Cr                      │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 9. User Roles & Permissions

> ```
> ┌─────────────────────────────────────────────────────────────────────────────┐
> │  👥 USER ROLES - Admin, Captain, and Member Permissions                    │
> └─────────────────────────────────────────────────────────────────────────────┘
> ```

### 9.1 Role Definitions

| Role | Code | Description |
|------|------|-------------|
| **Admin** | `admin` | Full system control |
| **Captain** | `captain` | Team leader, can bid |
| **Member** | `member` | Team member, view only |

### 9.2 Permission Matrix

| Action | Admin | Captain | Member |
|--------|:-----:|:-------:|:------:|
| **Authentication** |
| Login with Google | ✅ | ✅ | ✅ |
| View own profile | ✅ | ✅ | ✅ |
| Edit own profile | ✅ | ✅ | ✅ |
| Upload avatar | ✅ | ✅ | ✅ |
| **Team Management** |
| View all teams | ✅ | ✅ | ✅ |
| Create team | ✅ | ❌ | ❌ |
| Edit team | ✅ | ❌ | ❌ |
| Delete team | ✅ | ❌ | ❌ |
| Assign captain | ✅ | ❌ | ❌ |
| Add/remove members | ✅ | ❌ | ❌ |
| **Player Management** |
| View all players | ✅ | ✅ | ✅ |
| Create player | ✅ | ❌ | ❌ |
| Edit player | ✅ | ❌ | ❌ |
| Delete player | ✅ | ❌ | ❌ |
| **Auction Control** |
| Start auction | ✅ | ❌ | ❌ |
| Pause/Resume | ✅ | ❌ | ❌ |
| Next player | ✅ | ❌ | ❌ |
| Force sell | ✅ | ❌ | ❌ |
| Make corrections | ✅ | ❌ | ❌ |
| End auction | ✅ | ❌ | ❌ |
| **Bidding** |
| View live auction | ✅ | ✅ | ✅ |
| Place bid | ❌ | ✅ | ❌ |
| View bid history | ✅ | ✅ | ✅ |
| **Notifications** |
| View notifications | ✅ | ✅ | ✅ |
| Receive bid alerts | ✅ | ✅ | ✅ |

### 9.3 Route Protection

```typescript
// Frontend route protection example
const routes = [
  { path: '/login', element: <LoginPage />, public: true },
  { path: '/', element: <DashboardPage />, auth: true },
  { path: '/auction', element: <AuctionPage />, auth: true },
  { path: '/profile', element: <ProfilePage />, auth: true },
  { path: '/admin/*', element: <AdminLayout />, role: 'admin' },
];
```

---

## 10. 75-Day Roadmap

> ```
> ┌─────────────────────────────────────────────────────────────────────────────┐
> │  🗺️ 75-DAY ROADMAP - Phase-wise Project Timeline                           │
> └─────────────────────────────────────────────────────────────────────────────┘
> ```

### 10.1 Phase Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         75-DAY ROADMAP                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  PHASE 1: Foundation & Setup                                            │
│  ══════════════════════════════════════════════════                     │
│  Days 1-10 (20 hours)                                                   │
│  • PostgreSQL setup                                                     │
│  • FastAPI project structure                                            │
│  • Frontend setup (Vite + React + Tailwind + Shadcn)                   │
│                                                                         │
│  PHASE 2: Authentication                                                │
│  ══════════════════════════════════════════════════                     │
│  Days 11-25 (30 hours)                                                  │
│  • User model & JWT                                                     │
│  • Google OAuth integration                                             │
│  • Frontend login flow                                                  │
│                                                                         │
│  PHASE 3: Team & Player CRUD                                            │
│  ══════════════════════════════════════════════════                     │
│  Days 26-40 (30 hours)                                                  │
│  • Team APIs & UI                                                       │
│  • Player APIs & UI                                                     │
│  • Admin dashboard                                                      │
│                                                                         │
│  PHASE 4: Auction Engine                                                │
│  ══════════════════════════════════════════════════                     │
│  Days 41-65 (50 hours)                                                  │
│  • WebSocket setup                                                      │
│  • Bidding logic                                                        │
│  • Timer system                                                         │
│  • Real-time UI                                                         │
│                                                                         │
│  PHASE 5: Polish & Complete                                             │
│  ══════════════════════════════════════════════════                     │
│  Days 66-75 (20 hours)                                                  │
│  • Notifications                                                        │
│  • Profile & upload                                                     │
│  • Testing & fixes                                                      │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 10.2 Milestone Checkpoints

| Day | Milestone | What Should Work |
|-----|-----------|------------------|
| **10** | Setup Complete | Both servers run, DB connected |
| **25** | Auth Complete | Google login works end-to-end |
| **40** | CRUD Complete | Admin can manage teams/players |
| **55** | Auction Core | Live bidding with timer works |
| **65** | Real-time Complete | All WebSocket events work |
| **75** | Project Complete | Full MVP ready |

---

## 11. Daily Task Breakdown

> ```
> ┌─────────────────────────────────────────────────────────────────────────────┐
> │  📅 DAILY TASKS - Day-by-Day Implementation Guide                          │
> └─────────────────────────────────────────────────────────────────────────────┘
> ```

### Phase 1: Foundation & Setup (Days 1-10)

#### Day 1: PostgreSQL Setup
```
Duration: 2 hours
Type: Backend

Tasks:
□ Download and install PostgreSQL 15+
□ Install DBeaver 4
□ Create database: cricket_auction
□ Create user with password
□ Test connection from DBeaver
□ Note down connection string

Expected Output:
- PostgreSQL running on localhost:5432
- Database 'cricket_auction' created
- Connection string ready
```

#### Day 2: FastAPI Project Setup
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create project folder: backend/
□ Create virtual environment: python -m venv venv
□ Activate venv
□ Install FastAPI: pip install fastapi uvicorn
□ Create app/main.py with hello world
□ Run server: uvicorn app.main:app --reload
□ Test http://localhost:8000
□ Test http://localhost:8000/docs

Expected Output:
- FastAPI running on localhost:8000
- Swagger docs accessible
- "Hello World" API working
```

#### Day 3: FastAPI Basics Learning
```
Duration: 2 hours
Type: Learning

Tasks:
□ Read FastAPI docs: First Steps
□ Understand path parameters
□ Understand query parameters
□ Understand request body
□ Create test endpoints:
  - GET /test
  - GET /test/{id}
  - POST /test
□ Test all in Swagger

Expected Output:
- Understanding of FastAPI basics
- 3 test endpoints working
```

#### Day 4: SQLAlchemy Setup
```
Duration: 2 hours
Type: Backend

Tasks:
□ Install: pip install sqlalchemy psycopg2-binary
□ Create app/database.py
□ Setup database connection
□ Create engine and SessionLocal
□ Test connection to PostgreSQL
□ Create app/config.py for env variables
□ Install python-dotenv
□ Create .env file with DB_URL

Expected Output:
- SQLAlchemy connected to PostgreSQL
- Config management working
```

#### Day 5: Pydantic Basics
```
Duration: 2 hours
Type: Backend

Tasks:
□ Install: pip install pydantic
□ Learn Pydantic models
□ Create test schema with validation
□ Understand Field() constraints
□ Test validation errors
□ Create app/schemas/ folder
□ Create common.py with base schemas

Expected Output:
- Understanding of Pydantic validation
- Base schemas created
```

#### Day 6: Project Folder Structure
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create all folders as per structure:
  - app/models/
  - app/schemas/
  - app/routers/
  - app/services/
  - app/repositories/
  - app/websockets/
  - app/utils/
  - app/middleware/
□ Create __init__.py in each folder
□ Update main.py to import routers
□ Create requirements.txt

Expected Output:
- Complete folder structure ready
- All __init__.py files created
```

#### Day 7: Alembic Setup
```
Duration: 2 hours
Type: Backend

Tasks:
□ Install: pip install alembic
□ Initialize: alembic init alembic
□ Configure alembic.ini
□ Update alembic/env.py for async
□ Create base model class
□ Generate first migration (empty)
□ Run migration: alembic upgrade head

Expected Output:
- Alembic configured
- Migrations working
```

#### Day 8: Frontend Vite + React Setup
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Create frontend folder
□ Run: npm create vite@latest . -- --template react-ts
□ Install dependencies: npm install
□ Run: npm run dev
□ Test http://localhost:5173
□ Clean up default files
□ Create folder structure

Expected Output:
- React app running on localhost:5173
- TypeScript configured
```

#### Day 9: Tailwind + Shadcn Setup
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Install Tailwind: npm install -D tailwindcss postcss autoprefixer
□ Init Tailwind: npx tailwindcss init -p
□ Configure tailwind.config.js
□ Update index.css with Tailwind directives
□ Init Shadcn: npx shadcn-ui@latest init
□ Add components: button, card, input
□ Test components in App.tsx

Expected Output:
- Tailwind working
- Shadcn components available
```

#### Day 10: Git Setup + First Commit
```
Duration: 2 hours
Type: Both

Tasks:
□ Initialize git in root folder
□ Create .gitignore (Python + Node)
□ Create README.md
□ First commit: "Initial project setup"
□ Create GitHub repository (optional)
□ Push to remote (optional)
□ Verify both servers still work

Expected Output:
- Git repository initialized
- First commit made
- Phase 1 complete! ✅
```

---

### Phase 2: Authentication (Days 11-25)

#### Day 11: User Model
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/models/user.py
□ Define User model with SQLAlchemy:
  - id (UUID)
  - email (unique)
  - name
  - avatar_url
  - provider
  - provider_id
  - role (enum)
  - team_id (FK, nullable)
  - is_captain
  - created_at, updated_at
□ Create enum for user_role
□ Generate migration: alembic revision --autogenerate
□ Run migration: alembic upgrade head
□ Verify table in DBeaver

Expected Output:
- users table created in database
```

#### Day 12: User Schemas
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/schemas/user.py
□ Define schemas:
  - UserBase
  - UserCreate
  - UserUpdate
  - UserResponse
  - UserInDB
□ Add validation rules
□ Test schemas with sample data

Expected Output:
- User schemas ready for API
```

#### Day 13: JWT Basics
```
Duration: 2 hours
Type: Backend

Tasks:
□ Install: pip install python-jose[cryptography]
□ Create app/utils/security.py
□ Generate SECRET_KEY
□ Create function: create_access_token()
  - Takes user data
  - Returns JWT token
□ Create function: verify_token()
  - Takes token
  - Returns user data or error
□ Add JWT settings to config
□ Test token creation/verification

Expected Output:
- JWT token generation working
- Token verification working
```

#### Day 14: JWT Token Flow
```
Duration: 2 hours
Type: Backend

Tasks:
□ Define token expiry (24 hours)
□ Add token payload structure:
  - sub (user_id)
  - email
  - role
  - exp
□ Create TokenResponse schema
□ Test expired token handling
□ Test invalid token handling

Expected Output:
- Complete JWT flow working
```

#### Day 15: Google OAuth Credentials
```
Duration: 2 hours
Type: Backend

Tasks:
□ Go to Google Cloud Console
□ Create new project: "Cricket Auction"
□ Enable Google+ API
□ Create OAuth 2.0 credentials
□ Set authorized redirect URI:
  http://localhost:8000/api/auth/google/callback
□ Download credentials
□ Add to .env:
  - GOOGLE_CLIENT_ID
  - GOOGLE_CLIENT_SECRET
  - GOOGLE_REDIRECT_URI

Expected Output:
- Google OAuth credentials ready
```

#### Day 16: Authlib Setup
```
Duration: 2 hours
Type: Backend

Tasks:
□ Install: pip install authlib httpx
□ Create app/utils/oauth.py
□ Configure Google OAuth client
□ Create OAuth instance
□ Test OAuth configuration

Expected Output:
- Authlib configured for Google
```

#### Day 17: Google OAuth Routes
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/routers/auth.py
□ Create GET /api/auth/google
  - Redirect to Google login page
□ Test endpoint - should redirect to Google
□ Login with Google account
□ Note the callback URL with code

Expected Output:
- Google redirect working
- Can see Google login page
```

#### Day 18: Google Callback Handler
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create GET /api/auth/google/callback
□ Exchange code for token
□ Get user info from Google
□ Extract: email, name, picture, google_id
□ Log user info to console
□ Test full OAuth flow

Expected Output:
- Callback receives user data from Google
```

#### Day 19: Auto User Creation
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/repositories/user_repo.py
□ Create functions:
  - get_by_email()
  - get_by_provider_id()
  - create_user()
□ Create app/services/auth_service.py
□ Create function: google_login()
  - Check if user exists
  - Create new user if not
  - Return user
□ Update callback to create/get user
□ Generate JWT token for user
□ Return token in response

Expected Output:
- New users auto-created on first login
- JWT token returned after login
```

#### Day 20: Auth Middleware
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/middleware/auth.py
□ Create get_current_user dependency:
  - Extract token from header
  - Verify token
  - Get user from database
  - Return user
□ Create get_current_active_user
□ Handle invalid/expired tokens

Expected Output:
- Auth middleware ready
```

#### Day 21: Protected Routes
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create GET /api/auth/me
  - Requires authentication
  - Returns current user info
□ Test with valid token
□ Test with invalid token
□ Test with no token
□ Create POST /api/auth/logout (optional)

Expected Output:
- /api/auth/me working with token
- Proper error for invalid tokens
```

#### Day 22: Frontend Login Page UI
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Create src/pages/LoginPage.tsx
□ Design login card:
  - Logo
  - Title
  - Google login button
□ Add Shadcn Button component
□ Style with Tailwind
□ Add cricket-themed design

Expected Output:
- Beautiful login page UI
```

#### Day 23: Frontend Auth Store
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Install: npm install zustand
□ Create src/store/authStore.ts
□ Define state:
  - user
  - token
  - isAuthenticated
  - isLoading
□ Define actions:
  - setUser
  - setToken
  - logout
  - checkAuth
□ Persist token in localStorage

Expected Output:
- Auth state management ready
```

#### Day 24: Frontend OAuth Integration
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Create src/services/api.ts (Axios instance)
□ Create src/services/authService.ts
□ On Google button click:
  - Redirect to backend /api/auth/google
□ Create callback page to receive token
□ Save token to store
□ Redirect to dashboard

Expected Output:
- Google login button works
- Token saved after login
```

#### Day 25: Frontend Protected Routes
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Install: npm install react-router-dom
□ Create src/components/auth/ProtectedRoute.tsx
□ Check authentication status
□ Redirect to login if not authenticated
□ Setup router in App.tsx
□ Test full login flow end-to-end

Expected Output:
- Complete login flow working
- Phase 2 complete! ✅
```

---

### Phase 3: Team & Player CRUD (Days 26-40)

#### Day 26: Team Model
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/models/team.py
□ Define Team model:
  - id, name, short_name
  - logo_url, primary_color, secondary_color
  - initial_purse, current_purse
  - max_squad_size, max_overseas
  - captain_id (FK to users)
  - created_at, updated_at
□ Generate migration
□ Run migration
□ Verify in DBeaver

Expected Output:
- teams table created
```

#### Day 27: Team Schemas
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/schemas/team.py
□ Define schemas:
  - TeamBase
  - TeamCreate
  - TeamUpdate
  - TeamResponse
  - TeamWithPlayers
  - TeamWithMembers
□ Add validation (purse > 0, etc.)

Expected Output:
- Team schemas ready
```

#### Day 28: Team CRUD APIs
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/repositories/team_repo.py
□ Create app/services/team_service.py
□ Create app/routers/teams.py
□ Implement:
  - GET /api/teams
  - POST /api/teams (admin only)
□ Test in Swagger

Expected Output:
- List and create teams working
```

#### Day 29: Team APIs Complete
```
Duration: 2 hours
Type: Backend

Tasks:
□ Implement:
  - GET /api/teams/{id}
  - PUT /api/teams/{id} (admin)
  - DELETE /api/teams/{id} (admin)
□ Add admin role check
□ Test all endpoints

Expected Output:
- All team CRUD APIs working
```

#### Day 30: Player Model
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/models/player.py
□ Define Player model:
  - id, name, photo_url
  - player_type (enum: CAPPED/UNCAPPED/OVERSEAS)
  - role (enum: BAT/BOWL/AR/WK)
  - base_price, set_number, is_marquee
  - status (enum)
  - sold_price, sold_to_team_id
  - created_at, updated_at
□ Generate and run migration

Expected Output:
- players table created
```

#### Day 31: Player Schemas
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/schemas/player.py
□ Define schemas:
  - PlayerBase
  - PlayerCreate
  - PlayerUpdate
  - PlayerResponse
  - PlayerList
□ Add enums for types and roles
□ Add validation (base_price >= 2000000)

Expected Output:
- Player schemas ready
```

#### Day 32: Player CRUD APIs
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/repositories/player_repo.py
□ Create app/services/player_service.py
□ Create app/routers/players.py
□ Implement:
  - GET /api/players (with filters)
  - POST /api/players (admin)

Expected Output:
- List and create players working
```

#### Day 33: Player APIs Complete
```
Duration: 2 hours
Type: Backend

Tasks:
□ Implement:
  - GET /api/players/{id}
  - PUT /api/players/{id}
  - DELETE /api/players/{id}
  - GET /api/players/by-set/{setNumber}
□ Test all endpoints

Expected Output:
- All player CRUD APIs working
```

#### Day 34: Captain Assignment API
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create POST /api/teams/{id}/captain
  - Validate user exists
  - Validate user not captain of another team
  - Update team.captain_id
  - Update user.is_captain = true
  - Update user.role = 'captain'
□ Create DELETE /api/teams/{id}/captain
□ Test captain assignment

Expected Output:
- Captain assignment working
```

#### Day 35: Team Member APIs
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create POST /api/teams/{id}/members
  - Add user to team
  - Update user.team_id
  - Update user.role = 'member'
□ Create DELETE /api/teams/{id}/members/{userId}
□ Create GET /api/teams/{id}/members
□ Test member management

Expected Output:
- Team member management working
```

#### Day 36: Role-Based Access
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create decorators/dependencies:
  - require_admin
  - require_captain
  - require_team_member
□ Apply to existing routes
□ Test access control:
  - Admin can access admin routes
  - Captain cannot access admin routes
  - Member cannot bid

Expected Output:
- Role-based access working
```

#### Day 37: Frontend Admin Layout
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Create src/components/layout/AdminLayout.tsx
□ Create sidebar with navigation:
  - Dashboard
  - Teams
  - Players
  - Auction Sets
  - Auction Control
  - Users
□ Style with Tailwind
□ Add active state to nav items

Expected Output:
- Admin layout with sidebar ready
```

#### Day 38: Frontend Team Management
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Create src/pages/admin/AdminTeams.tsx
□ Create src/components/admin/TeamList.tsx
□ Create src/components/admin/TeamForm.tsx
□ Install react-query: npm install @tanstack/react-query
□ Fetch and display teams
□ Create team form with validation

Expected Output:
- Team list and create form working
```

#### Day 39: Frontend Player Management
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Create src/pages/admin/AdminPlayers.tsx
□ Create src/components/admin/PlayerList.tsx
□ Create src/components/admin/PlayerForm.tsx
□ Add filters: by type, role, status
□ Implement create/edit player
□ Add category badges

Expected Output:
- Player management UI working
```

#### Day 40: Frontend Captain/Member UI
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Create src/components/admin/CaptainAssign.tsx
□ Create src/components/admin/MemberAssign.tsx
□ Add captain badge to team card
□ Show team members list
□ Test full CRUD flow

Expected Output:
- Captain and member assignment UI working
- Phase 3 complete! ✅
```

---

### Phase 4: Auction Engine (Days 41-65)

#### Day 41: Auction Model
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/models/auction.py
□ Define Auction model:
  - id, status (enum)
  - current_player_id (FK)
  - current_bid
  - current_team_id (FK)
  - current_set_id (FK)
  - timer_end_at
  - bid_increment
  - started_at, ended_at
  - created_at, updated_at
□ Generate and run migration

Expected Output:
- auctions table created
```

#### Day 42: Bid Model
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/models/bid.py
□ Define Bid model:
  - id
  - auction_id (FK)
  - player_id (FK)
  - team_id (FK)
  - user_id (FK)
  - amount
  - is_valid
  - created_at
□ Generate and run migration

Expected Output:
- bids table created
```

#### Day 43: WebSocket Basics
```
Duration: 2 hours
Type: Backend

Tasks:
□ Read FastAPI WebSocket documentation
□ Create simple WebSocket endpoint
□ Test with browser console:
  - Connect to ws://localhost:8000/ws
  - Send message
  - Receive response
□ Understand connection lifecycle

Expected Output:
- Basic WebSocket working
```

#### Day 44: Connection Manager
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/websockets/manager.py
□ Implement ConnectionManager class:
  - active_connections: dict
  - connect(websocket, user_id)
  - disconnect(user_id)
  - broadcast(message)
  - send_to_user(user_id, message)
  - send_to_team(team_id, message)
□ Test with multiple browser tabs

Expected Output:
- Connection manager handling multiple clients
```

#### Day 45: WebSocket Events Setup
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/websockets/events.py
□ Define event types:
  - AUCTION_STARTED
  - AUCTION_PAUSED
  - PLAYER_LIVE
  - BID_NEW
  - TIMER_TICK
  - PLAYER_SOLD
  - etc.
□ Create event helper functions
□ Create app/websockets/auction_ws.py

Expected Output:
- Event system ready
```

#### Day 46: Auction Start API
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/routers/auction.py
□ Create POST /api/auction/start:
  - Check admin role
  - Create auction record
  - Set status = 'live'
  - Broadcast auction:started event
□ Test auction start

Expected Output:
- Auction start API working
- WebSocket event broadcasted
```

#### Day 47: Next Player API
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create POST /api/auction/next-player:
  - Get next player from current set
  - Update auction.current_player_id
  - Update player.status = 'live'
  - Set auction.current_bid = base_price
  - Broadcast player:live event
□ Test next player

Expected Output:
- Next player API working
```

#### Day 48: WebSocket Broadcast
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create auction WebSocket endpoint
□ Authenticate WebSocket connection
□ On auction:started, send to all
□ On player:live, send with player data
□ Test events in browser console

Expected Output:
- Events broadcasting to all clients
```

#### Day 49: Bid Validation Logic
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/services/bid_service.py
□ Implement validate_bid():
  - Check user is captain
  - Check bid > current_bid
  - Check bid >= base_price
  - Check bid <= team_purse
  - Check squad not full
  - Check overseas limit
□ Return validation result with error message

Expected Output:
- Bid validation logic complete
```

#### Day 50: Bid API
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create POST /api/bids:
  - Validate bid
  - Save bid to database
  - Update auction.current_bid
  - Update auction.current_team_id
  - Broadcast bid:new event
□ Test bidding

Expected Output:
- Bid API working
```

#### Day 51: Race Condition Handling
```
Duration: 2 hours
Type: Backend

Tasks:
□ Learn database transactions
□ Learn SELECT FOR UPDATE
□ Wrap bid logic in transaction:
  - Lock auction row
  - Validate bid
  - Update auction
  - Save bid
  - Commit
□ Test concurrent bids (two tabs)

Expected Output:
- Race conditions handled
```

#### Day 52: Bid Broadcast
```
Duration: 2 hours
Type: Backend

Tasks:
□ On successful bid:
  - Broadcast bid:new to all
  - Include: team_name, amount, bidder_name
  - Broadcast purse:updated to team
□ Test real-time bid updates

Expected Output:
- Bids showing in real-time
```

#### Day 53: Timer Concept
```
Duration: 2 hours
Type: Backend

Tasks:
□ Learn asyncio basics
□ Learn background tasks in FastAPI
□ Plan timer implementation:
  - Start timer on player:live
  - Tick every second
  - Reset on new bid
  - Trigger sold on zero
□ Create app/utils/timer.py

Expected Output:
- Timer plan ready
```

#### Day 54: Timer Implementation
```
Duration: 2 hours
Type: Backend

Tasks:
□ Implement AuctionTimer class:
  - start(duration)
  - stop()
  - reset()
  - on_tick callback
  - on_complete callback
□ Test timer in isolation

Expected Output:
- Timer class working
```

#### Day 55: Timer Reset on Bid
```
Duration: 2 hours
Type: Backend

Tasks:
□ On new bid:
  - Cancel current timer
  - Start new timer (15 seconds)
□ On timer tick:
  - Broadcast timer:tick with seconds
□ Test timer reset

Expected Output:
- Timer resets on each bid
```

#### Day 56: Timer Tick Broadcast
```
Duration: 2 hours
Type: Backend

Tasks:
□ Every second broadcast timer:tick
□ When timer < 5s, add warning flag
□ Update auction.timer_end_at
□ Test countdown in browser

Expected Output:
- Timer countdown visible in real-time
```

#### Day 57: Player Sold Logic
```
Duration: 2 hours
Type: Backend

Tasks:
□ On timer complete (0 seconds):
  - Update player.status = 'sold'
  - Update player.sold_price = current_bid
  - Update player.sold_to_team_id
  - Broadcast player:sold event
□ Test player sold

Expected Output:
- Player sold when timer ends
```

#### Day 58: Purse Deduction
```
Duration: 2 hours
Type: Backend

Tasks:
□ On player sold:
  - Deduct from team.current_purse
  - Validate purse doesn't go negative
  - Broadcast purse:updated
□ Update team squad count
□ If overseas, update overseas count
□ Test purse deduction

Expected Output:
- Purse auto-deducted on sale
```

#### Day 59: Admin Controls
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create POST /api/auction/pause
□ Create POST /api/auction/resume
□ Create POST /api/auction/force-sell
□ Create POST /api/auction/mark-unsold
□ Broadcast events for each action

Expected Output:
- Admin auction controls working
```

#### Day 60: More Admin Controls
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create POST /api/auction/correction
  - Update bid amount
  - Adjust purse
  - Broadcast correction event
□ Create POST /api/auction/undo-sell
□ Test all admin controls

Expected Output:
- All admin controls working
```

#### Day 61: Frontend Auction Page Layout
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Create src/pages/AuctionPage.tsx
□ Layout:
  - Player card (large)
  - Bid info panel
  - Timer
  - Team purse cards
□ Use CSS Grid for layout
□ Style with team colors

Expected Output:
- Auction page layout ready
```

#### Day 62: Frontend WebSocket Hook
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Install: npm install socket.io-client
□ Create src/hooks/useWebSocket.ts
□ Connect to backend WebSocket
□ Handle events:
  - auction:started
  - player:live
  - bid:new
  - timer:tick
  - player:sold
□ Update Zustand store on events

Expected Output:
- WebSocket connected and receiving events
```

#### Day 63: Frontend Timer Component
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Create src/components/auction/Timer.tsx
□ Display seconds remaining
□ Circular progress (optional)
□ Color change:
  - Green > 10s
  - Yellow 5-10s
  - Red < 5s
□ Pulse animation on warning

Expected Output:
- Timer component working
```

#### Day 64: Frontend Bid Button
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Create src/components/auction/BidPanel.tsx
□ Show increment buttons: +5L, +10L, +25L, +50L, +1Cr
□ Show current bid amount
□ BID button (captain only)
□ Disable if not captain
□ Call bid API on click
□ Show loading state

Expected Output:
- Bid panel working for captains
```

#### Day 65: Frontend Polish
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Create sold animation/overlay
□ Create unsold animation
□ Add confetti on sold (optional)
□ Test full auction flow:
  - Admin starts auction
  - Player goes live
  - Captain bids
  - Timer countdown
  - Player sold
□ Fix any bugs

Expected Output:
- Complete auction flow working
- Phase 4 complete! ✅
```

---

### Phase 5: Polish & Complete (Days 66-75)

#### Day 66: Notification Model
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create app/models/notification.py
□ Define Notification model
□ Create migration
□ Create notification service
□ Create notification APIs

Expected Output:
- Notification system ready
```

#### Day 67: Notification Events
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create notifications on:
  - Captain assigned
  - Player sold (to team members)
  - Auction started
  - Admin correction
□ Broadcast notification:new event
□ Test notifications

Expected Output:
- Notifications being created
```

#### Day 68: Frontend Notifications
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Create NotificationBell component
□ Show unread count badge
□ Dropdown with notification list
□ Mark as read on click
□ Real-time new notifications

Expected Output:
- Notification bell working
```

#### Day 69: Profile API
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create GET /api/users/me
□ Create PUT /api/users/me
□ Allow updating: name, avatar_url
□ Test profile update

Expected Output:
- Profile API working
```

#### Day 70: Photo Upload
```
Duration: 2 hours
Type: Backend

Tasks:
□ Create Cloudinary account
□ Install: pip install cloudinary
□ Configure Cloudinary
□ Create POST /api/users/me/avatar
□ Upload to Cloudinary
□ Save URL to database

Expected Output:
- Photo upload working
```

#### Day 71: Frontend Profile Page
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Create src/pages/ProfilePage.tsx
□ Show user info
□ Show team info
□ Captain badge if captain
□ Edit name form

Expected Output:
- Profile page working
```

#### Day 72: Frontend Avatar Upload
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Create avatar upload component
□ Preview before upload
□ Upload to backend
□ Show new avatar after upload

Expected Output:
- Avatar upload working
```

#### Day 73: Bid History Page
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Create src/pages/BidHistoryPage.tsx
□ List all bids
□ Filter by player/team
□ Show bid details

Expected Output:
- Bid history page working
```

#### Day 74: Responsive Design
```
Duration: 2 hours
Type: Frontend

Tasks:
□ Test on mobile viewport
□ Fix auction page for mobile
□ Fix admin sidebar for mobile
□ Add mobile menu toggle
□ Test all pages

Expected Output:
- Mobile responsive design
```

#### Day 75: Final Testing & Fixes
```
Duration: 2 hours
Type: Both

Tasks:
□ Test complete flow:
  1. Admin creates teams
  2. Admin adds players
  3. Admin assigns captains
  4. Admin starts auction
  5. Captains bid
  6. Players sold
  7. Notifications received
□ Fix any bugs found
□ Update documentation

Expected Output:
- Project complete! 🎉
- Phase 5 complete! ✅
```

---

## 12. Beginner Resources

> ```
> ┌─────────────────────────────────────────────────────────────────────────────┐
> │  📚 BEGINNER RESOURCES - Learning Materials and Links                      │
> └─────────────────────────────────────────────────────────────────────────────┘
> ```

### 12.1 Essential Learning

| Topic | Resource | Time |
|-------|----------|------|
| **Python Basics** | Python Official Tutorial | 2-3 hours |
| **FastAPI** | FastAPI Official Tutorial | 3-4 hours |
| **SQLAlchemy** | SQLAlchemy 2.0 Tutorial | 2-3 hours |
| **Pydantic** | Pydantic Documentation | 1-2 hours |
| **React** | React Official Tutorial | 3-4 hours |
| **TypeScript** | TypeScript Handbook | 2-3 hours |
| **Tailwind** | Tailwind CSS Docs | 1-2 hours |

### 12.2 Video Tutorials (Hindi)

| Topic | Channel | Link |
|-------|---------|------|
| FastAPI | CodeWithHarry | YouTube |
| React | Thapa Technical | YouTube |
| PostgreSQL | Geeky Shows | YouTube |

### 12.3 Documentation Links

```
FastAPI:      https://fastapi.tiangolo.com/
SQLAlchemy:   https://docs.sqlalchemy.org/
Pydantic:     https://docs.pydantic.dev/
React:        https://react.dev/
Tailwind:     https://tailwindcss.com/
Shadcn:       https://ui.shadcn.com/
Zustand:      https://zustand-demo.pmnd.rs/
React Query:  https://tanstack.com/query/
```

### 12.4 Troubleshooting Tips

| Problem | Solution |
|---------|----------|
| **Import error** | Check file paths, __init__.py files |
| **Database connection failed** | Verify PostgreSQL running, check credentials |
| **CORS error** | Add CORS middleware in FastAPI |
| **Token invalid** | Check token expiry, SECRET_KEY |
| **WebSocket not connecting** | Check URL, authentication |
| **Migration failed** | Delete versions, recreate migration |

### 12.5 Daily Checklist Template

```
┌────────────────────────────────────────┐
│           DAILY CHECKLIST              │
├────────────────────────────────────────┤
│ Day: ___  Date: ___________            │
│ Phase: ___  Task: _______________      │
├────────────────────────────────────────┤
│ □ Read previous day's code             │
│ □ Understand today's task              │
│ □ Write code                           │
│ □ Test locally                         │
│ □ Commit to git                        │
│ □ Note blockers/questions              │
├────────────────────────────────────────┤
│ Time spent: ___ hrs                    │
│ Completed: Yes / No / Partial          │
│ Notes: _________________________       │
└────────────────────────────────────────┘
```

---

## 🎯 Quick Reference

### Commands Cheatsheet

```bash
# Backend
cd backend
source venv/bin/activate          # Activate virtual environment
uvicorn app.main:app --reload     # Run server
alembic revision --autogenerate -m "message"  # Create migration
alembic upgrade head              # Run migrations
pip freeze > requirements.txt     # Save dependencies

# Frontend
cd frontend
npm run dev                       # Run dev server
npm install <package>             # Install package
npm run build                     # Production build

# Git
git add .
git commit -m "message"
git push origin main
```

### Price Formatting (Frontend)

```typescript
// Format price in Indian style
const formatPrice = (amount: number): string => {
  if (amount >= 10000000) {
    return `₹${(amount / 10000000).toFixed(2)} Cr`;
  } else if (amount >= 100000) {
    return `₹${(amount / 100000).toFixed(2)} L`;
  }
  return `₹${amount.toLocaleString('en-IN')}`;
};

// Examples:
// 20000000 → ₹2.00 Cr
// 5000000  → ₹50.00 L
// 50000    → ₹50,000
```

---

## ✅ Project Summary

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         PROJECT SUMMARY                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   Project Name    : IPL-Style Cricket Auction Platform                  │
│   Duration        : 75 days (2 hrs/day)                                 │
│   Total Hours     : 150 hours                                           │
│   Difficulty      : Beginner to Intermediate                            │
│                                                                         │
│   Backend         : FastAPI + PostgreSQL + WebSocket                    │
│   Frontend        : React + Tailwind + Shadcn                           │
│                                                                         │
│   Key Features    :                                                     │
│   • Google OAuth Login                                                  │
│   • 3 Teams with Captains                                               │
│   • IPL-style Player Categories                                         │
│   • Real-time Live Auction                                              │
│   • Bidding with Timer                                                  │
│   • Auto Purse Management                                               │
│   • Admin Controls                                                      │
│   • Notifications                                                       │
│                                                                         │
│   Expected Completion: Early May 2026                                   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

**Best of luck bhai! 🏏 Happy Coding!**

*Document created for Cricket Auction Project - February 2026*
