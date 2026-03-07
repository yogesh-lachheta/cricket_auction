# 🏏 Cricket Auction Platform — Development Roadmap

---

> ### 📌 Project Stack
> | Layer | Technology |
> |-------|-----------|
> | 🐍 Backend | FastAPI + Python |
> | 🗄️ Database | PostgreSQL + SQLAlchemy + Alembic |
> | ⚛️ Frontend | React 18 + TypeScript + Vite |
> | 🎨 UI | Tailwind CSS + Shadcn UI |
> | 🔌 Realtime | WebSockets |
> | 🔐 Auth | JWT + Google OAuth |
>
> ⏱️ **Daily Commitment:** ~2 hours/day &nbsp;&nbsp; 📅 **Total:** 75 Days across 5 Phases

---

## 📋 Table of Contents

| Phase | Days | Topic | Status |
|-------|------|-------|--------|
| [🏗️ Phase 1](#-phase-1-foundation--setup) | 1–10 | Foundation & Setup | ✅ |
| [🔐 Phase 2](#-phase-2-authentication) | 11–25 | Authentication | 🔄 |
| [🧩 Phase 3](#-phase-3-team--player-crud) | 26–40 | Team & Player CRUD | 🔄 |
| [⚡ Phase 4](#-phase-4-auction-engine) | 41–65 | Auction Engine | 🔜 |
| [✨ Phase 5](#-phase-5-polish--complete) | 66–75 | Polish & Complete | 🔜 |

---

## 📚 Libraries & Concepts — Master Reference

> Ye section mein **har library** ka ek baar full explanation hai.
> Neeche jab bhi pehli baar use hogi, wahan short note milega aur yahan se full detail milegi.

| Library / Tool | Kya Hai | Kyu Use Kiya |
|----------------|---------|-------------|
| `fastapi` | Python web framework | Fast, auto Swagger docs, async support |
| `uvicorn` | ASGI server | FastAPI ko run karne ke liye |
| `sqlalchemy` | Python ORM | Python mein DB tables ko classes ki tarah use karo |
| `psycopg2-binary` | PostgreSQL driver | Python ko PostgreSQL se connect karta hai |
| `alembic` | DB migration tool | Schema changes track karta hai (Git for DB) |
| `pydantic` | Data validation | Request/response data validate karta hai |
| `pydantic-settings` | Config management | `.env` file ko Python class mein load karta hai |
| `python-dotenv` | `.env` loader | Environment variables `.env` file se load karta hai |
| `uuid` | Unique ID generator | Database IDs ke liye random unique IDs |
| `typing` | Type hints | Python mein `Optional`, `List`, `Generic` etc. |
| `brew` (Homebrew) | macOS package manager | macOS pe software ek command se install karo (jaise apt Ubuntu ke liye) |
| `venv` | Virtual environment | Project ka isolated Python environment |
| `vite` | Frontend build tool | React app fast reload ke saath run karta hai |
| `tailwindcss` | CSS utility framework | Inline classes se styling |
| `shadcn` | UI component library | Ready-made React components |
| `alembic revision` | Migration command | Naya migration file banata hai |
| `alembic upgrade head` | Migration command | Pending migrations database pe apply karta hai |
| `alembic current` | Migration command | Abhi database kis version pe hai ye batata hai |
| `alembic history` | Migration command | Saari migrations ki list dikhata hai |
| `Depends` | FastAPI dependency | Route mein automatically kuch inject karta hai |
| `Session` | SQLAlchemy DB session | Database se baat karne ka connection object |
| `get_db` | Custom dependency | Har request ko apna DB session deta hai |
| `BaseModel` | Pydantic class | Ye inherit karke data validation wali class banate hain |
| `BaseSettings` | Pydantic settings class | Environment variables ko typed class mein load karta hai |
| `Field()` | Pydantic validator | Schema field pe constraints lagate hain (min, max, regex) |
| `declarative_base` | SQLAlchemy function | DB model classes ka base banata hai |
| `create_engine` | SQLAlchemy function | Database se connection banata hai |
| `sessionmaker` | SQLAlchemy function | DB session factory banata hai |
| `passlib[bcrypt]` | Password hashing | User passwords ko securely hash karta hai |
| `python-jose` | JWT library | JWT tokens banao aur verify karo |
| `authlib` | OAuth 2.0 library | Google OAuth flow handle karta hai |
| `httpx` | Async HTTP client | Google API ko async requests bhejta hai |
| `Enum` | Python built-in | Fixed set of values (role: admin/team_owner/viewer) |
| `EmailStr` | Pydantic type | Email format automatically validate karta hai |
| `HTTPBearer` | FastAPI security | Authorization header se Bearer token extract karta hai |
| `SessionMiddleware` | Starlette middleware | OAuth state/CSRF protection ke liye session |
| `UserRepository` | Custom class | User ke saare DB queries ek jagah |
| `AuthService` | Custom class | Authentication business logic |
| `create_access_token` | Custom function | User ke liye JWT token generate karta hai |
| `get_current_user` | Custom dependency | Token verify karke current user return karta hai |
| `require_role` | Custom function | Role-based access control (RBAC) |
| `react-router-dom` | Frontend routing | URL change pe alag component render karo |
| `BrowserRouter` / `Routes` / `Route` | React Router | App mein routing setup karna |
| `Navigate` | React Router | Programmatic redirect component |
| `Outlet` | React Router | Nested routes ka placeholder |
| `useNavigate` | React Router hook | Code se route change karo |
| `useSearchParams` | React Router hook | URL query params read karo |
| `zustand` | State management | Global React state — lightweight Redux |
| `persist` (zustand) | Zustand middleware | Store ka data localStorage mein save karo |
| `axios` | HTTP client | API calls with interceptors (auto token add) |
| `relationship()` | SQLAlchemy | Models ke beech DB relations define karo |
| `ForeignKey` | SQLAlchemy | DB-level foreign key constraint |
| `joinedload` | SQLAlchemy | JOIN se related data ek query mein load karo |
| `back_populates` | SQLAlchemy | Bidirectional relationship define karna |
| `Query()` | FastAPI | URL query parameters validate karo |

---
---

# 🏗️ Phase 1: Foundation & Setup

### `Days 1 → 10` &nbsp;|&nbsp; Both Frontend & Backend setup

---

## 🗄️ Day 1: PostgreSQL Setup

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | PostgreSQL installed, DB created, connection string ready |

---

> ### 📖 PostgreSQL kya hai aur kyu use kiya?
>
> **Kya hai:** PostgreSQL ek **relational database** hai — matlab data tables mein store hota hai (rows aur columns), jaise Excel sheets hoti hain lekin bahut powerful.
>
> **Kyu use kiya:**
> - Free aur open-source hai
> - UUID, JSON, ARRAY jaise advanced data types support karta hai
> - High performance — lakho records handle kar sakta hai easily
> - SQLAlchemy (jo hum use karenge) ke saath perfectly kaam karta hai
>
> **Alternative kyun nahi:** MySQL bhi popular hai, lekin PostgreSQL more feature-rich hai aur modern apps ke liye better choice hai.
>
> **Kahan use hoga:** Poore project mein — users, teams, players, bids, auctions — sab kuch PostgreSQL mein store hoga.

---

### ✅ Tasks

---

#### `Task 1` — 📥 Download and install PostgreSQL 15+

**🐧 Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install -y postgresql postgresql-contrib

# Service start karo
sudo systemctl start postgresql
sudo systemctl enable postgresql   # system restart pe auto-start

# Status check karo
sudo systemctl status postgresql
```

**🍎 macOS (Homebrew):**

> ### 📖 `brew` (Homebrew) kya hai aur kyu use kiya?
>
> **Kya hai:**
> `brew` = **Homebrew** — macOS ka **package manager** hai.
>
> Package manager ka matlab: ek tool jisse tum software install, update, uninstall kar sakte ho — **ek command se** — bina manually website pe jaake installer download kiye.
>
> **Analogy:**
> | Platform | Package Manager | Example |
> |----------|----------------|---------|
> | 🐧 Ubuntu/Debian | `apt` | `sudo apt install postgresql` |
> | 🍎 macOS | `brew` | `brew install postgresql@15` |
> | 🪟 Windows | `winget` / `choco` | `choco install postgresql` |
> | 🐍 Python | `pip` | `pip install fastapi` |
> | ⚛️ Node.js | `npm` | `npm install react` |
>
> **Homebrew install kaise karein (agar pehle se nahi hai):**
> ```bash
> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
> ```
> Ye command Homebrew ko macOS pe install kar deti hai.
>
> **`brew services` kya hai?**
> Ye Homebrew ka ek sub-command hai jo **background services** manage karta hai (start / stop / restart).
> ```
> brew services start postgresql@15   → PostgreSQL background mein chalu karo
> brew services stop postgresql@15    → PostgreSQL band karo
> brew services restart postgresql@15 → Restart karo
> brew services list                  → Sab running services dekho
> ```
>
> **Kyu use kiya:**
> macOS pe PostgreSQL manually install karna complicated hai. `brew` se ek line mein ho jaata hai, aur `brew services` se hum usse background mein chala sakte hain system restart pe bhi.
>
> **Kahan use hoga:** Sirf macOS users ke liye — Day 1 PostgreSQL setup mein.

```bash
brew install postgresql@15
brew services start postgresql@15
```

**🪟 Windows:**
- Installer download: https://www.postgresql.org/download/windows/
- Version **15+** select karo
- Default port `5432` rakho
- Superuser password note karo (e.g., `postgres`)

**✔️ Verify installation:**
```bash
psql --version
# Output: psql (PostgreSQL) 15.x
```

> 💡 **Port 5432 kya hai?**
> Jaise website `80` port pe hoti hai, PostgreSQL `5432` port pe sunता है। Ye default port hai — change mat karo abhi.

---

#### `Task 2` — 🖥️ Install DBeaver CE

> 💡 **DBeaver kya hai?**
> DBeaver ek **GUI tool** hai PostgreSQL ke liye. Terminal mein SQL likhne ki jagah, graphical interface se tables dekh sakte ho, data browse kar sakte ho, queries run kar sakte ho.
> Visual Studio Code jo code ke liye hai, DBeaver wo database ke liye hai.
> **CE** = Community Edition (free version)

**🐧 Ubuntu:**
```bash
# Latest DBeaver CE download karo
wget -O /tmp/dbeaver.deb https://dbeaver.io/files/dbeaver-ce_latest_amd64.deb

# Install karo
sudo dpkg -i /tmp/dbeaver.deb

# Missing dependencies fix karo
sudo apt-get install -f

# Launch karo
dbeaver-ce &
```

**🍎 macOS / 🪟 Windows:**
- Download: https://dbeaver.io/download/
- Normal installer ki tarah install karo

---

#### `Task 3` — 🗃️ Create database `cricket_auction`

> 💡 **Database vs Schema vs Table — Fark kya hai?**
> - **Database** = Ek poora folder, jisme sab kuch hai (jaise ek company ka data)
> - **Schema** = Database ke andar ek namespace (default: `public`)
> - **Table** = Actual data store hota hai (jaise ek Excel sheet)
> Hum ek `cricket_auction` database banayenge jisme baad mein `users`, `teams`, `players` tables honge.

**Option A — psql terminal:**
```sql
-- postgres system user se login karo
sudo -u postgres psql

-- Database create karo
CREATE DATABASE cricket_auction;

-- Verify — list of all databases:
\l

-- Exit:
\q
```

**Option B — DBeaver GUI:**
1. Left panel → `Databases` → Right-click
2. `Create New Database`
3. Name: `cricket_auction` → OK

---

#### `Task 4` — 👤 Create user with password

> 💡 **Alag user kyu banaya? `postgres` use kyun nahi kiya?**
> `postgres` ek **superuser** hai — usse sab kuch access hai. Production mein superuser use karna dangerous hai.
> Isliye ek **limited user** `admin` banate hain jo sirf `cricket_auction` database access kar sake.
> Security best practice: **principle of least privilege** — sirf utna access do jitna zaroorat hai.

```sql
-- psql mein run karo
sudo -u postgres psql

-- User create karo
CREATE USER admin WITH PASSWORD 'admin';

-- DB pe full access do
GRANT ALL PRIVILEGES ON DATABASE cricket_auction TO admin;

-- PostgreSQL 15+ mein extra permission chahiye (schema level)
\c cricket_auction
GRANT ALL ON SCHEMA public TO admin;

-- Verify — list of users:
\du

-- Exit:
\q
```

---

#### `Task 5` — 🔗 Test connection from DBeaver

DBeaver mein new connection create karo:

| Field | Value |
|-------|-------|
| 📛 Name | `Cricket Auction Local` |
| 🖥️ Host | `localhost` |
| 🔌 Port | `5432` |
| 🗃️ Database | `cricket_auction` |
| 👤 Username | `admin` |
| 🔑 Password | `admin` |

**Terminal se verify:**
```bash
psql -h localhost -U admin -d cricket_auction -W
# -h = host, -U = username, -d = database, -W = password prompt
# Password: admin
\q
```

---

#### `Task 6` — 📝 Note down connection string

> 💡 **Connection String kya hota hai?**
> Ek single string jisme **sari DB connection info** hoti hai — host, port, user, password, database name.
> Python (SQLAlchemy) is string ko use karke database se connect karta hai.
> Format: `postgresql://user:password@host:port/database`

```bash
# Tumhara connection string:
postgresql://admin:admin@localhost:5432/cricket_auction
```

**`.env.example`** (Day 4 mein kaam aayega):
```env
DATABASE_URL=postgresql://admin:admin@localhost:5432/cricket_auction
DB_HOST=localhost
DB_PORT=5432
DB_NAME=cricket_auction
DB_USER=admin
DB_PASSWORD=admin
```

---

> ### 🏁 Expected Output — Day 1
> ```
> ✅ PostgreSQL 15+ running on localhost:5432
> ✅ DBeaver CE installed and connected
> ✅ Database 'cricket_auction' created
> ✅ User 'admin' created with privileges
> ✅ Connection string ready
> ```
> 🎯 **Goal Achieved:** PostgreSQL installed, DB created, connection string ready

---
---

## ⚡ Day 2: FastAPI Project Setup

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | FastAPI server running with Swagger docs |

---

> ### 📖 FastAPI kya hai aur kyu use kiya?
>
> **Kya hai:** FastAPI ek **modern Python web framework** hai API banane ke liye.
>
> **Kyu FastAPI (other options ke bajaye):**
> | Framework | Comparison |
> |-----------|-----------|
> | FastAPI | Fast, auto docs, type hints, async support ✅ |
> | Flask | Simple lekin manual kaam zyada, no auto docs ❌ |
> | Django | Bahut heavy, chota API ke liye overkill ❌ |
>
> **3 special features jo FastAPI mein hain:**
> 1. **Automatic Swagger UI** — code likhte hi `/docs` pe documentation ready
> 2. **Type hints se validation** — Pydantic ke saath automatic request validation
> 3. **Async support** — WebSockets ke liye zaroorat hogi (Phase 4 mein)

---

> ### 📖 `uvicorn` kya hai aur kyu use kiya?
>
> **Kya hai:** `uvicorn` ek **ASGI server** hai — FastAPI ke code ko actual HTTP server pe run karta hai.
>
> **Simple analogy:**
> - FastAPI = Recipe (how to handle requests)
> - uvicorn = Chef (actually runs the recipe, listens for connections)
>
> **`--reload` flag kya karta hai?**
> Code save karte hi server automatically restart ho jaata hai. Development mein bahut useful — manually restart nahi karna padta.
>
> **Production mein:** `--reload` nahi hoga, `gunicorn` ke saath `uvicorn` workers use hote hain.

---

### ✅ Tasks

---

#### `Task 1` — 📁 Create project folder `backend/`

```bash
mkdir cricket-auction-platform
cd cricket-auction-platform
mkdir backend
cd backend
```

---

#### `Task 2 & 3` — 🐍 Create + Activate virtual environment (`venv`)

> 💡 **`venv` (Virtual Environment) kya hai aur kyu zaroorat hai?**
>
> **Problem:** Agar globally Python packages install karo, toh different projects ke packages conflict kar sakte hain.
> For example: Project A needs `fastapi==0.100`, Project B needs `fastapi==0.115` — globally dono nahi reh sakte.
>
> **Solution:** `venv` — har project ka apna **isolated Python environment** jisme apne packages hote hain.
>
> ```
> System Python          venv (cricket-auction)
> ├── pip                ├── fastapi 0.115
> ├── python             ├── sqlalchemy 2.0
> └── (no packages)      └── pydantic 2.10
> ```

```bash
# Virtual environment banao (backend/ folder ke andar)
python3 -m venv venv
# `venv` folder ban jaayega — is mein isolated Python hoga

# ── Activate karo ─────────────────────────────────
# 🐧 Linux / 🍎 macOS:
source venv/bin/activate

# 🪟 Windows (Command Prompt):
venv\Scripts\activate.bat

# 🪟 Windows (PowerShell):
venv\Scripts\Activate.ps1
```

> ⚠️ **Important:** Har baar naya terminal kholo toh `source venv/bin/activate` chalana hoga. Prompt mein `(venv)` dikhne se pata chalega activated hai.

---

#### `Task 4` — 📦 Install FastAPI + uvicorn

```bash
# venv activated hona chahiye! (venv) dikhna chahiye prompt mein
pip install fastapi uvicorn[standard]
# uvicorn[standard] = uvicorn + extra features (websockets, http2 etc.)

pip show fastapi    # Version: 0.115.x
pip show uvicorn    # Version: 0.32.x
```

> 💡 **`pip` kya hai?**
> Python ka **package manager** — jaise `npm` JavaScript ke liye hai, `pip` Python ke liye hai. PyPI (Python Package Index) se packages download aur install karta hai.

---

#### `Task 5` — 📄 Create `app/main.py`

```bash
mkdir app
touch app/__init__.py   # Python ko batata hai ki 'app' ek package hai
touch app/main.py
```

> 💡 **`__init__.py` kyu banate hain?**
> Python mein kisi bhi folder ko "package" banana ho (matlab us folder se import ho sake), toh `__init__.py` file chahiye. Empty bhi ho sakti hai — sirf existence matter karti hai.
> ```python
> from app.main import app     # ye tab kaam karta hai jab app/__init__.py exist kare
> from app.config import settings
> ```

**`app/main.py`:**
```python
from fastapi import FastAPI
# FastAPI class import ki — is se app object banega

app = FastAPI(
    title="Cricket Auction Platform",
    description="Real-time cricket player auction system",
    version="1.0.0"
    # ye sab /docs pe Swagger UI mein dikhega
)


@app.get("/")
# @app.get = decorator — ye function ek GET HTTP endpoint ban jaata hai
def root():
    return {"message": "Cricket Auction Platform API", "status": "running"}
    # dict return karo — FastAPI automatically JSON mein convert kar deta hai


@app.get("/health")
def health_check():
    return {"status": "healthy"}
```

---

#### `Task 6` — 🚀 Run server

```bash
uvicorn app.main:app --reload
# uvicorn = server
# app.main = file path (app/main.py)
# :app = us file mein 'app' variable (FastAPI object)
# --reload = code change pe auto-restart
```

---

#### `Task 7 & 8` — 🌐 Test endpoints

```bash
curl http://localhost:8000
# {"message":"Cricket Auction Platform API","status":"running"}

curl http://localhost:8000/health
# {"status":"healthy"}
```

> 💡 **Swagger UI kya hai?** (`/docs`)
> FastAPI automatically ek **interactive documentation** page banata hai.
> - Har endpoint list hota hai
> - "Try it out" se directly browser se API test kar sakte ho
> - Request/response format dikhata hai
> Ye bahut kaam aata hai — Postman ki zaroorat nahi padti development mein.

**Browser mein:**
- 📖 Swagger UI → `http://localhost:8000/docs`
- 📘 ReDoc → `http://localhost:8000/redoc`

---

> ### 🏁 Expected Output — Day 2
> ```
> ✅ FastAPI running on localhost:8000
> ✅ Swagger docs at localhost:8000/docs
> ✅ GET / → JSON response
> ✅ GET /health → {"status":"healthy"}
> ```
> 🎯 **Goal Achieved:** FastAPI server running with Swagger docs

---
---

## 📚 Day 3: FastAPI Basics Learning

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Learning` |
| 🎯 **Goal** | Path params, query params, request body samajhna |

---

### ✅ Tasks

---

#### `Task 1` — 🛣️ Path Parameters

> 💡 **Path Parameter kya hai?**
> URL ka woh part jo **variable** hota hai — curly braces `{}` se define karte hain.
> ```
> /players/42      → player_id = 42
> /players/99      → player_id = 99
> /teams/MI        → team_name = "MI"
> ```
> URL ki path mein hi data pass hota hai.

```python
from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()


# Basic path parameter
@app.get("/players/{player_id}")
#                  ^^^^^^^^^^^ ye path parameter hai
def get_player(player_id: int):
#              ^^^^^^^^^^^
#              FastAPI automatically URL se value uthata hai
#              'int' type hint diya = automatically integer mein convert + validate
    return {"player_id": player_id, "message": f"Player #{player_id}"}


# Path parameter with validation using Path()
@app.get("/teams/{team_name}")
def get_team(
    team_name: str = Path(..., min_length=2, max_length=50)
    # Path(...) = required field, min/max length validation
):
    return {"team_name": team_name}


# Multiple path params
@app.get("/auctions/{auction_id}/bids/{bid_id}")
def get_bid(auction_id: int, bid_id: int):
    return {"auction_id": auction_id, "bid_id": bid_id}
```

```bash
curl http://localhost:8000/players/42
# {"player_id":42,"message":"Player #42"}

curl http://localhost:8000/players/abc
# 422 Unprocessable Entity — int chahiye tha, string diya
```

---

#### `Task 2` — 🔍 Query Parameters

> 💡 **Query Parameter kya hai?**
> URL mein `?` ke baad jo parameters aate hain — filtering, sorting, pagination ke liye.
> ```
> /players?skip=0&limit=10&role=BAT
>          ^^^^   ^^^^^    ^^^^^^^^
>          ye sab query parameters hain
> ```
> Path parameter **zaroorati** hota hai URL mein, query parameter **optional** hota hai.

```python
from typing import Optional
from enum import Enum


class PlayerRole(str, Enum):
    # str, Enum = string enum — value bhi string hai
    batsman      = "BAT"
    bowler       = "BOWL"
    allrounder   = "AR"
    wicketkeeper = "WK"


@app.get("/players")
def list_players(
    skip: int = 0,          # default = 0 (optional)
    limit: int = 10,        # default = 10 (optional)
    role: Optional[str] = None   # Optional = None bhi ho sakta hai
):
    return {"skip": skip, "limit": limit, "role": role}


# Enum type — sirf valid values accept karta hai
@app.get("/players/by-role")
def players_by_role(
    role: PlayerRole,           # sirf BAT/BOWL/AR/WK accept karega
    is_overseas: bool = False,
    min_price: int = 0
):
    return {"role": role, "is_overseas": is_overseas, "min_price": min_price}
```

> 💡 **`Optional` kya hai?** (`from typing import Optional`)
> `Optional[str]` ka matlab hai: ye value `str` ya `None` ho sakti hai.
> `Optional[str]` = `Union[str, None]` ka shortcut.
> Python 3.10+ mein `str | None` bhi likh sakte ho.
> Hum `typing` module se import karte hain kyunki Python mein built-in nahi hai (Python 3.9 se pehle).

```bash
curl "http://localhost:8000/players?skip=0&limit=5&role=BAT"
curl "http://localhost:8000/players/by-role?role=INVALID"
# 422 Error — only BAT/BOWL/AR/WK allowed
```

---

#### `Task 3` — 📦 Request Body

> 💡 **Request Body kya hai?**
> POST/PUT requests mein JSON data jo **body** mein bheja jaata hai — URL mein fit nahi hota bada data.
> ```
> POST /players
> Body: {"name": "Virat", "base_price": 20000000}
> ```
> Request body ke liye **Pydantic BaseModel** use karte hain.

> 💡 **Pydantic `BaseModel` kya hai?**
> Pydantic ek **data validation library** hai. `BaseModel` inherit karke ek class banao — Pydantic automatically:
> - Data validate karta hai (type check, constraints)
> - Error messages deta hai agar wrong data aaye
> - Dict se object aur object se dict convert karta hai
> FastAPI ke saath automatically request/response validation hoti hai.

```python
from pydantic import BaseModel


class PlayerCreate(BaseModel):
    name: str               # required field
    role: str               # required field
    base_price: int         # required field
    is_overseas: bool = False   # optional (default False)


@app.post("/players")
def create_player(player: PlayerCreate):
    # FastAPI automatically request body ko PlayerCreate mein convert karta hai
    # agar data galat ho → 422 error automatically
    return {"message": "Player created", "player": player.model_dump()}
    # .model_dump() = Pydantic object ko dict mein convert karo


@app.put("/players/{player_id}")
def update_player(player_id: int, player: PlayerCreate):
    # Path param + Body dono saath mein
    return {"player_id": player_id, "updated": player.model_dump()}
```

```bash
curl -X POST "http://localhost:8000/players" \
  -H "Content-Type: application/json" \
  -d '{"name": "Virat Kohli", "role": "BAT", "base_price": 20000000}'
```

---

#### `Task 4 & 5` — 🧪 Create 3 test endpoints + Swagger test

> 💡 **`APIRouter` kya hai?**
> FastAPI mein sab routes `main.py` mein likhna messy ho jaata hai jab project bade ho.
> `APIRouter` se alag files mein routes group kar sakte hain, phir `main.py` mein include karte hain.
> Jaise Express mein `router` hota hai, ye exactly wahi hai.

**`app/routers/test.py`:**
```python
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/test",     # har route pe automatically /test prefix lagega
    tags=["🧪 Test"]   # Swagger mein is group ka naam
)


@router.get("/")        # actual route: GET /test/
def test_get():
    return {"message": "GET working ✅", "data": ["item1", "item2"]}


@router.get("/{id}")    # actual route: GET /test/{id}
def test_get_by_id(id: int):
    fake_data = {
        1: {"id": 1, "name": "Test Item 1"},
        2: {"id": 2, "name": "Test Item 2"},
    }
    return fake_data.get(id, {"error": f"Item {id} not found"})


class TestCreate(BaseModel):
    name: str
    value: int

@router.post("/")       # actual route: POST /test/
def test_post(data: TestCreate):
    return {"message": "POST received ✅", "data": data.model_dump()}
```

**`app/main.py`** mein include karo:**
```python
from app.routers import test      # router import karo
app.include_router(test.router)   # main app mein register karo
```

```bash
curl http://localhost:8000/test/
curl http://localhost:8000/test/1
curl -X POST http://localhost:8000/test/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Cricket", "value": 42}'
```

---

> ### 🏁 Expected Output — Day 3
> ```
> ✅ Path params → URL se data uthana
> ✅ Query params → ?key=value filtering
> ✅ Request body → POST mein JSON data
> ✅ GET /test, GET /test/1, POST /test — working
> ✅ Swagger mein sab test kiye
> ```
> 🎯 **Goal Achieved:** Path params, query params, request body samajhna

---
---

## 🔌 Day 4: SQLAlchemy Setup

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | SQLAlchemy connected to PostgreSQL via `.env` config |

---

> ### 📖 SQLAlchemy kya hai aur kyu use kiya?
>
> **Kya hai:** SQLAlchemy ek **ORM (Object Relational Mapper)** hai Python ke liye.
>
> **ORM kya hota hai?**
> ORM = Database tables ko Python classes ki tarah use karo.
> ```
> WITHOUT ORM (raw SQL):          WITH SQLAlchemy (ORM):
> cursor.execute(                  player = Player(
>   "INSERT INTO players           name="Virat",
>    VALUES ('Virat', 20000000)"   base_price=20000000
> )                                )
>                                  db.add(player)
>                                  db.commit()
> ```
>
> **Kyu use kiya:**
> - SQL likhne ki zaroorat kam hoti hai
> - Python objects ki tarah kaam karta hai
> - Database change (SQLite → PostgreSQL) pe minimal code change
> - SQL injection se protection
>
> **Kahan use hoga:** Har jagah jahan database se data read/write hoga — users, teams, players, bids.

---

> ### 📖 `psycopg2-binary` kya hai?
>
> **Kya hai:** PostgreSQL ka **Python driver** — Python aur PostgreSQL ke beech ka translator.
>
> **Analogy:** SQLAlchemy ek manager hai jo orders deta hai, `psycopg2` woh worker hai jo actually PostgreSQL se baat karta hai.
>
> **`psycopg2` vs `psycopg2-binary`:**
> - `psycopg2` = Source se build hota hai (C compiler chahiye)
> - `psycopg2-binary` = Pre-compiled binary — development ke liye easy, bas install karo
> Production mein `psycopg2` better hai, development mein `psycopg2-binary` chalega.

---

### ✅ Tasks

---

#### `Task 1` — 📦 Install packages

```bash
pip install sqlalchemy psycopg2-binary pydantic-settings python-dotenv

pip show sqlalchemy       # 2.0.x
pip show psycopg2-binary  # 2.9.x
```

---

#### `Task 2 & 3` — 🗃️ Create `app/database.py`

```python
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings   # ye Day 4 Task 4 mein banayenge
```

> 💡 **`create_engine` kya karta hai?**
> SQLAlchemy ka entry point — database se connection establish karta hai.
> `engine` ek **connection pool** maintain karta hai — matlab ek sath multiple connections ready rehte hain. Har request pe naya connection nahi banana padta.
>
> **Parameters:**
> - `echo=True` → console mein generated SQL queries print hogi (debugging ke liye)
> - `pool_pre_ping=True` → connection use karne se pehle check karo ki alive hai
> - `pool_size=5` → maximum 5 connections simultaneously

> 💡 **`declarative_base()` kya karta hai?**
> Ek **Base class** banata hai. Saare database models (User, Team, Player etc.) is Base se inherit karenge.
> Base ke andar SQLAlchemy ka metadata store hota hai — kaun kaun si tables hain, unka structure kya hai.
> Alembic bhi is Base.metadata ko read karta hai migrations generate karne ke liye.

> 💡 **`sessionmaker` kya karta hai?**
> Ek **Session factory** banata hai — matlab `SessionLocal()` call karne pe ek naya DB session milega.
> Session = database ke saath ek conversation — queries execute karo, commit karo, rollback karo.
> `autocommit=False` = manually `.commit()` karna hoga (safety ke liye)
> `autoflush=False` = manually `.flush()` karna hoga

```python
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Database engine — connection pool maintain karta hai
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,     # Dev mein True: SQL queries console mein dikhegi
    pool_pre_ping=True,      # Stale connections detect karo
    pool_size=5,             # 5 connections pool mein
    max_overflow=10          # Extra 10 connections burst ke liye
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,   # Manually commit karna hoga
    autoflush=False,    # Manually flush karna hoga
    bind=engine         # Is engine ka use karo
)

# Sab models ka base class — is se inherit karenge
Base = declarative_base()


# ── FastAPI Dependency ──────────────────────────────────────
def get_db():
    """
    Har HTTP request ko apna DB session milega.
    Request complete hone pe automatically close hoga.
    FastAPI ke Depends() ke saath use hoga.
    """
    db = SessionLocal()   # Naya session banao
    try:
        yield db          # Request handler ko session do
    finally:
        db.close()        # Request ke baad close karo (error ho ya na ho)


def test_connection():
    """DB connection test karne ke liye — startup pe call karenge"""
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))   # Simple test query
        print("✅ Database connected successfully!")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False
```

> 💡 **`get_db()` mein `yield` kyu?**
> `yield` se ye function ek **generator** ban jaata hai.
> FastAPI `yield` se pehle ka code request ke pehle run karta hai (setup),
> aur `yield` ke baad ka code request complete hone ke baad run karta hai (cleanup).
> Ye **context manager** pattern hai — guaranteed cleanup (session close hogi chahe error ho ya na ho).

> 💡 **`Depends` (FastAPI) kya hai? — Concept Introduction**
> `Depends` ek FastAPI feature hai jo **dependency injection** karta hai.
> Matlab: route function automatically `get_db()` call karke db session milega — manually nahi karna padta.
> ```python
> @app.get("/players")
> def get_players(db: Session = Depends(get_db)):
> #                             ^^^^^^^^^^^^^^^^
> #   FastAPI automatically get_db() call karega
> #   aur db variable mein session inject karega
>     players = db.query(Player).all()
>     return players
> ```
> `Depends` ka full use Day 20 se shuru hoga jab Auth middleware banenge.

---

#### `Task 4` — 🔧 Create `app/config.py`

> ### 📖 `pydantic-settings` kya hai? `pydantic` se alag kyu?
>
> **Pydantic** = Data validation ke liye (request/response schemas)
> **pydantic-settings** = **Configuration management** ke liye — `.env` file ke variables ko typed Python class mein load karta hai
>
> **Problem:** Environment variables hamesha **strings** hoti hain
> ```bash
> DEBUG=True      # ye string "True" hai, boolean nahi
> PORT=8000       # ye string "8000" hai, int nahi
> ```
>
> **Solution:** `BaseSettings` automatically type conversion karta hai:
> ```python
> class Settings(BaseSettings):
>     DEBUG: bool    # "True" string → True boolean (automatic)
>     PORT: int      # "8000" string → 8000 int (automatic)
> ```
>
> **Kyu alag package?** `pydantic-settings` v2 mein alag package ban gaya (`pydantic` v1 mein included tha). Isliye `pip install pydantic-settings` separately karna padta hai.

> 💡 **`from pydantic_settings import BaseSettings` kyu?**
> ```python
> from pydantic_settings import BaseSettings
> # pydantic_settings = package name (underscore)
> # BaseSettings = class jo .env file read karti hai
> ```
> `BaseSettings` inherit karo → `Settings` class automatically `.env` file se values load karegi.

> 💡 **`from typing import Optional` kyu?**
> Python mein `Optional` type hint hai — `Optional[str]` matlab ye field `str` ya `None` ho sakta hai.
> `typing` module Python standard library mein hai — additional install nahi chahiye.
> Pydantic fields mein use karte hain jo **zaroorat nahi** hain (like Google OAuth keys — abhi empty hain).

```python
from pydantic_settings import BaseSettings
# BaseSettings = .env file se config load karne wali class

from typing import Optional
# Optional = value ya None — zaroorat nahi wale fields ke liye


class Settings(BaseSettings):
    # ── App Settings ──────────────────────────────
    APP_NAME: str = "Cricket Auction Platform"  # default value
    DEBUG: bool = True      # .env mein nahi hai toh True
    API_V1_PREFIX: str = "/api"

    # ── Database ──────────────────────────────────
    DATABASE_URL: str       # NO default — .env mein MUST hona chahiye
                            # nahi hoga toh startup pe error aayegi

    # ── JWT (Day 13 mein use hoga) ─────────────────
    SECRET_KEY: str = "changeme-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440   # 24 hours

    # ── Google OAuth (Day 15 mein use hoga) ────────
    GOOGLE_CLIENT_ID: Optional[str] = None      # Optional — abhi empty
    GOOGLE_CLIENT_SECRET: Optional[str] = None
    GOOGLE_REDIRECT_URI: Optional[str] = None

    class Config:
        env_file = ".env"        # is file se variables load karo
        case_sensitive = True    # DATABASE_URL aur database_url alag hain


# Global singleton — poore app mein ek hi instance hoga
settings = Settings()
# Ye line execute hote hi .env file read hogi aur sab values load hongi
```

---

#### `Task 5` — 📄 Create `.env` file

**`backend/.env`:**
```env
# Application
APP_NAME=Cricket Auction Platform
DEBUG=True

# Database — ye same connection string hai jo Day 1 mein banaya tha
DATABASE_URL=postgresql://admin:admin@localhost:5432/cricket_auction

# JWT — Day 13 mein use hoga
SECRET_KEY=super-secret-key-change-in-production-2024
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
```

> ⚠️ **`.env` file KABHI commit mat karna!**
> Isme passwords, secret keys hote hain. Agar GitHub pe chali gayi toh security breach ho sakta hai.
> `.gitignore` mein add karo: `backend/.env`
> Baaki developers ke liye `.env.example` banao (Day 10 mein).

---

#### `Task 6` — 🧪 Test DB connection

**`app/main.py`** update karo:**
```python
from fastapi import FastAPI
from app.config import settings      # config import karo
from app.database import test_connection  # test function import karo

app = FastAPI(title=settings.APP_NAME)


@app.on_event("startup")
async def startup_event():
    # App start hone pe ye automatically chalega
    print(f"🚀 {settings.APP_NAME} starting...")
    test_connection()   # DB connection check karo


@app.get("/")
def root():
    return {"app": settings.APP_NAME, "status": "running"}
```

```bash
uvicorn app.main:app --reload
# Terminal mein dikhega:
# 🚀 Cricket Auction Platform starting...
# ✅ Database connected successfully!
```

---

> ### 🏁 Expected Output — Day 4
> ```
> ✅ SQLAlchemy + psycopg2 installed
> ✅ app/database.py — engine, SessionLocal, get_db() ready
> ✅ app/config.py — pydantic-settings se .env load ho raha hai
> ✅ .env file created
> ✅ Startup mein "Database connected" log dikh raha hai
> ```
> 🎯 **Goal Achieved:** SQLAlchemy connected to PostgreSQL via `.env` config

---
---

## 📐 Day 5: Pydantic Basics

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | Pydantic validation samjhna, base schemas banana |

---

> ### 📖 Pydantic kya hai aur kyu use kiya?
>
> **Kya hai:** Python data validation library — data define karo, Pydantic validate karega.
>
> **Kyu use kiya:**
> ```python
> # WITHOUT Pydantic (manual validation — painful):
> def create_player(data: dict):
>     if "name" not in data:
>         raise ValueError("name required")
>     if not isinstance(data["name"], str):
>         raise ValueError("name must be string")
>     if len(data["name"]) < 2:
>         raise ValueError("name too short")
>     # ... baar baar yehi karo
>
> # WITH Pydantic (automatic):
> class PlayerCreate(BaseModel):
>     name: str = Field(..., min_length=2)
>     # Done! Automatic validation.
> ```
>
> **FastAPI ke saath:** FastAPI Pydantic use karta hai request/response automatically validate karne ke liye.

---

### ✅ Tasks

---

#### `Task 1` — 📦 Verify Pydantic

```bash
pip show pydantic           # Version: 2.x.x (FastAPI ke saath already aaya)
pip install pydantic[email] # Email validation ke liye extra dependency
```

> 💡 **Pydantic v1 vs v2:**
> Pydantic v2 (2023) mein bahut changes aaye — `.dict()` → `.model_dump()`, `.schema()` → `.model_json_schema()`. Hum v2 use kar rahe hain (modern way).

---

#### `Task 2` — 📚 Learn Pydantic models

```python
from pydantic import BaseModel
from typing import Optional, List
from enum import Enum


# ── Basic Model ────────────────────────────────────────────
class PlayerBase(BaseModel):
    name: str       # required, must be string
    age: int        # required, must be integer
    email: str      # required, must be string


# Usage:
player = PlayerBase(name="Virat", age=35, email="v@cricket.com")
print(player.name)                 # "Virat" — dot notation se access
print(player.model_dump())         # {"name": "Virat", "age": 35, "email": "..."}
print(player.model_json_schema())  # JSON Schema (Swagger mein use hoga)


# ── Model with Defaults ─────────────────────────────────────
class PlayerWithDefaults(BaseModel):
    name: str
    is_active: bool = True      # default = True
    score: float = 0.0          # default = 0.0
    tags: List[str] = []        # default = empty list


# ── Nested Models ───────────────────────────────────────────
class TeamInfo(BaseModel):
    team_name: str
    city: str

class PlayerWithTeam(BaseModel):
    name: str
    team: TeamInfo    # nested model — Pydantic recursively validate karega


# ── Enum with Pydantic ──────────────────────────────────────
class PlayerRole(str, Enum):
    # str inherit kiya — ye string bhi hai aur enum bhi
    # Pydantic automatically validate karega ki value valid hai
    BATSMAN      = "BAT"
    BOWLER       = "BOWL"
    ALL_ROUNDER  = "AR"
    WICKET_KEEPER = "WK"
```

---

#### `Task 3` — ✅ Schema with validators

> 💡 **`@field_validator` kya hai?**
> Specific field pe custom validation logic likhne ke liye.
> ```python
> @field_validator('name')
> @classmethod
> def clean_name(cls, v):
>     # v = value jo aaya hai
>     # kuch validate/transform karo
>     return v.strip().title()  # return karo transformed value
> ```
>
> 💡 **`@model_validator` kya hai?**
> Puri model pe validation — multiple fields ek saath check karne ke liye.
> For example: "Overseas marquee player ki price 1Cr+ honi chahiye" — ye 2 fields check karta hai.

```python
from pydantic import BaseModel, Field, field_validator, model_validator
from enum import Enum


class PlayerType(str, Enum):
    CAPPED   = "CAPPED"
    UNCAPPED = "UNCAPPED"
    OVERSEAS = "OVERSEAS"


class PlayerRole(str, Enum):
    BATSMAN       = "BAT"
    BOWLER        = "BOWL"
    ALL_ROUNDER   = "AR"
    WICKET_KEEPER = "WK"


class PlayerCreateTest(BaseModel):
    name: str        = Field(..., min_length=2, max_length=100)
    player_type: PlayerType
    role: PlayerRole
    base_price: int  = Field(..., ge=2_000_000)   # ge = greater than or equal = Min ₹20L
    age: int         = Field(..., ge=16, le=50)
    is_marquee: bool = False

    @field_validator('name')
    @classmethod
    def clean_name(cls, v: str) -> str:
        # Numbers allowed nahi hain name mein
        if any(char.isdigit() for char in v):
            raise ValueError('Name mein numbers nahi ho sakte')
        return v.strip().title()   # "virat kohli" → "Virat Kohli"

    @model_validator(mode='after')
    # mode='after' = sab fields validate hone ke baad chalega
    def overseas_price_check(self):
        # Do fields saath check kar rahe hain
        if self.player_type == PlayerType.OVERSEAS and self.is_marquee:
            if self.base_price < 10_000_000:
                raise ValueError('Overseas marquee ki base price 1Cr+ honi chahiye')
        return self
```

---

#### `Task 4` — 🔒 `Field()` constraints

> 💡 **`Field()` kya karta hai?**
> Pydantic field pe **constraints aur metadata** add karne ke liye.
> Default se zyada control milta hai.
>
> | Parameter | Matlab |
> |-----------|--------|
> | `...` | Field required hai (no default) |
> | `ge=5` | Greater than or Equal to 5 |
> | `le=100` | Less than or Equal to 100 |
> | `gt=0` | Greater Than 0 (strictly) |
> | `lt=10` | Less Than 10 (strictly) |
> | `min_length=2` | String minimum 2 characters |
> | `max_length=50` | String maximum 50 characters |
> | `pattern=r'^[A-Z]+'` | Regex pattern match hona chahiye |
> | `alias="teamId"` | Frontend different naam bhej sakta hai |
> | `description="..."` | Swagger mein description dikhegi |

```python
from pydantic import BaseModel, Field
from typing import Optional


class AuctionBidSchema(BaseModel):
    amount: int = Field(
        ...,                        # required
        ge=2_000_000,               # minimum ₹20 Lakh
        le=1_000_000_000,           # maximum ₹100 Crore
        description="Bid amount in rupees"
    )

    team_name: str = Field(..., min_length=2, max_length=50)

    team_code: str = Field(
        ...,
        pattern=r'^[A-Z]{2,4}$',   # 2-4 uppercase letters only: MI, CSK, RCB
        description="Team short code"
    )

    notes: Optional[str] = Field(default=None, max_length=200)

    auction_id: int = Field(
        ...,
        alias="auctionId"           # Frontend "auctionId" bhejega, Python mein "auction_id" milega
    )

    class Config:
        populate_by_name = True     # Original naam (auction_id) se bhi accept karo
```

---

#### `Task 5` — ❌ Test validation errors

> 💡 **`ValidationError` kya hai?**
> Jab Pydantic ka data invalid ho — ye exception raise hota hai.
> FastAPI automatically is error ko **422 Unprocessable Entity** HTTP response mein convert karta hai.
> Developer ko manually handle nahi karna padta.

```python
from pydantic import ValidationError


class TeamCreate(BaseModel):
    name: str        = Field(..., min_length=3, max_length=50)
    short_name: str  = Field(..., min_length=2, max_length=5)
    initial_purse: int = Field(..., ge=50_000_000)   # Min ₹5 Crore


test_cases = [
    {"name": "MI",            "short_name": "MI",          "initial_purse": 100_000_000},  # ❌ name too short
    {"name": "Mumbai Indians","short_name": "TOOLONGNAME",  "initial_purse": 100_000_000},  # ❌ short_name too long
    {"name": "Mumbai Indians","short_name": "MI",           "initial_purse": 1000},          # ❌ purse too low
    {"name": "Mumbai Indians","short_name": "MI",           "initial_purse": 100_000_000},   # ✅ valid
]

for data in test_cases:
    try:
        team = TeamCreate(**data)
        print(f"✅ Valid: {team.name}")
    except ValidationError as e:
        for err in e.errors():
            print(f"❌ Field '{err['loc'][0]}': {err['msg']}")
```

---

#### `Task 6 & 7` — 📂 Create `app/schemas/common.py`

> 💡 **`Generic` aur `TypeVar` kya hain?**
> ```python
> from typing import Generic, TypeVar
> DataT = TypeVar('DataT')     # Placeholder type — koi bhi type ho sakta hai
>
> class APIResponse(BaseModel, Generic[DataT]):
>     data: Optional[DataT]   # DataT = jo bhi type pass karein
>
> # Usage:
> APIResponse[PlayerResponse]    # data = PlayerResponse type ka hoga
> APIResponse[TeamResponse]      # data = TeamResponse type ka hoga
> ```
> Ek hi `APIResponse` class use karo — sab types ke saath. Code reuse!

```python
from pydantic import BaseModel, Field
from typing import Optional, Generic, TypeVar, List
from datetime import datetime
from uuid import UUID

DataT = TypeVar('DataT')   # Generic type placeholder


# ── Standard API Response Wrapper ──────────────────────────
class APIResponse(BaseModel, Generic[DataT]):
    """Poore API mein ek consistent response format"""
    success: bool = True
    message: str = "Success"
    data: Optional[DataT] = None    # DataT = koi bhi type


# ── Pagination ──────────────────────────────────────────────
class PaginationParams(BaseModel):
    page: int = Field(default=1, ge=1)
    limit: int = Field(default=10, ge=1, le=100)

    @property
    def skip(self) -> int:
        # @property = getter — db.query().offset(params.skip) mein use hoga
        return (self.page - 1) * self.limit


class PaginatedResponse(BaseModel, Generic[DataT]):
    items: List[DataT]
    total: int
    page: int
    limit: int
    total_pages: int


# ── Reusable Mixins ─────────────────────────────────────────
class TimestampMixin(BaseModel):
    """created_at + updated_at — jahan bhi chahiye inherit karo"""
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
        # SQLAlchemy model object ko directly Pydantic model mein convert karne deta hai
        # PlayerResponse(from_attributes=True).model_validate(db_player_object)


class IDMixin(BaseModel):
    id: UUID
    # UUID kyu? → Day 7 mein detail explanation milegi


# ── Error Response ──────────────────────────────────────────
class ErrorDetail(BaseModel):
    field: Optional[str] = None
    message: str


class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    errors: Optional[List[ErrorDetail]] = None
    error_code: Optional[str] = None
```

---

> ### 🏁 Expected Output — Day 5
> ```
> ✅ Pydantic v2 — BaseModel, Field(), validators samajh aaye
> ✅ Optional, List, Generic, TypeVar — typing concepts clear
> ✅ @field_validator aur @model_validator tested
> ✅ app/schemas/common.py ready — APIResponse, Pagination, ErrorResponse
> ✅ Phase 1 ka 50% complete 🎯
> ```
> 🎯 **Goal Achieved:** Pydantic validation samjhna, base schemas banana

---
---

## 📁 Day 6: Project Folder Structure

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | Complete scalable folder structure ready |

---

> ### 📖 Architecture Pattern — Layers kyu?
>
> Hum **layered architecture** follow kar rahe hain:
> ```
> HTTP Request
>      ↓
> 📡 Router (app/routers/)     ← Sirf request receive karo, validate karo
>      ↓
> 🧠 Service (app/services/)   ← Business logic — kya hona chahiye
>      ↓
> 🗄️ Repository (app/repositories/) ← Sirf DB queries — kaise hoga
>      ↓
> 💾 Database (PostgreSQL)
> ```
>
> **Kyu separate kiya?**
> - **Router** change karo bina service/DB touch kiye (e.g., REST → GraphQL)
> - **Service** change karo bina DB queries touch kiye
> - **Repository** change karo bina business logic touch kiye
> - Testing easy hoti hai (mock kar sakte ho)

---

### ✅ Tasks

---

#### `Task 1 & 2` — 📁 Create all folders + `__init__.py`

```bash
cd backend

mkdir -p app/models \
         app/schemas \
         app/routers \
         app/services \
         app/repositories \
         app/websockets \
         app/utils \
         app/middleware

# Har folder mein __init__.py banao (Python package banane ke liye)
touch app/models/__init__.py \
      app/schemas/__init__.py \
      app/routers/__init__.py \
      app/services/__init__.py \
      app/repositories/__init__.py \
      app/websockets/__init__.py \
      app/utils/__init__.py \
      app/middleware/__init__.py

find app -type d   # Verify — sab folders dikhne chahiye
```

> 💡 **Har folder ka kaam:**
>
> | Folder | Kya hoga | Example files |
> |--------|----------|---------------|
> | `models/` | SQLAlchemy ORM classes (= DB tables) | `user.py`, `team.py`, `player.py` |
> | `schemas/` | Pydantic validation classes | `user.py`, `team.py` |
> | `routers/` | API endpoints (routes) | `auth.py`, `teams.py`, `players.py` |
> | `services/` | Business logic | `auth_service.py`, `bid_service.py` |
> | `repositories/` | Database queries | `user_repo.py`, `team_repo.py` |
> | `websockets/` | WebSocket handlers | `manager.py`, `events.py` |
> | `utils/` | Helper functions | `security.py`, `oauth.py`, `timer.py` |
> | `middleware/` | Request/response processing | `auth.py` |

**Each `__init__.py` mein purpose comment karo:**

**`app/routers/__init__.py`:**
```python
"""
API Routers:
- auth.py       → /api/auth/*    (login, logout, google oauth)
- teams.py      → /api/teams/*   (CRUD)
- players.py    → /api/players/* (CRUD)
- auction.py    → /api/auction/* (start, pause, next-player)
- bids.py       → /api/bids/*    (place bid)
- users.py      → /api/users/*   (profile)
"""
```

**`app/services/__init__.py`:**
```python
"""
Business Logic Layer.
Request flow: Router → Service → Repository → Database
- Router: HTTP parse karo, validate karo
- Service: Business rules apply karo
- Repository: DB se data lao
"""
```

---

#### `Task 3` — 🔄 Update `main.py` with CORS

> 💡 **CORS kya hai aur kyu lagaya?**
>
> **Problem:** Browser security rule — ek origin (localhost:5173) dusre origin (localhost:8000) ko directly API call nahi kar sakta.
>
> **CORS (Cross-Origin Resource Sharing):** Backend batata hai ki "kaunse origins mujhe call kar sakte hain".
>
> ```
> Frontend: localhost:5173  ──────→  Backend: localhost:8000
>                           Blocked by browser! (CORS)
>
> With CORSMiddleware:
> Backend says: "localhost:5173 allowed hai" → Browser allow karta hai
> ```

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import test_connection

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ── CORS Middleware ──────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    # Production mein: ["https://yourdomain.com"]
    allow_credentials=True,    # Cookies/Auth headers allow
    allow_methods=["*"],       # GET, POST, PUT, DELETE sab allow
    allow_headers=["*"],       # Authorization, Content-Type sab allow
)

# ── Routers (baad mein uncomment karte rahenge) ──────────────
# from app.routers import auth, teams, players, auction, bids
# app.include_router(auth.router,    prefix=settings.API_V1_PREFIX)


@app.on_event("startup")
async def startup_event():
    print(f"🚀 Starting {settings.APP_NAME}...")
    test_connection()
    print("✅ Startup complete!")


@app.get("/", tags=["Root"])
def root():
    return {"app": settings.APP_NAME, "status": "running", "docs": "/docs"}

@app.get("/health", tags=["Root"])
def health():
    return {"status": "healthy"}
```

---

#### `Task 4` — 📄 `requirements.txt`

> 💡 **`requirements.txt` kyu banana?**
> Dusra developer tumhara project clone kare toh exactly same packages install kar sake.
> `pip install -r requirements.txt` = sab packages ek command mein install.
> Jaise `package.json` Node.js ke liye hai, `requirements.txt` Python ke liye hai.

```bash
pip freeze > requirements.txt
# pip freeze = installed packages ki list versions ke saath

# Future packages abhi install karo:
pip install python-jose[cryptography] passlib[bcrypt] authlib \
            httpx alembic python-multipart websockets cloudinary

pip freeze > requirements.txt
```

---

> ### 🏁 Expected Output — Day 6
> ```
> ✅ 8 folders created with purpose comments
> ✅ main.py updated with CORS middleware
> ✅ requirements.txt generated
> ✅ Architecture layers clear (Router → Service → Repository → DB)
> ```
> 🎯 **Goal Achieved:** Complete scalable folder structure ready

---
---

## 🔃 Day 7: Alembic Setup

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | DB migrations working, BaseModel with UUID ready |

---

> ### 📖 Alembic kya hai aur kyu use kiya?
>
> **Kya hai:** Database **migration tool** — database schema changes (tables add/modify/delete) ko track karta hai aur apply karta hai.
>
> **Simple Analogy:**
> - Git = Code changes track karta hai (commit history)
> - Alembic = Database schema changes track karta hai (migration history)
>
> **Problem without Alembic:**
> ```
> Dev 1: users table banaya manually in DBeaver
> Dev 2: Production pe manually users table banana pada
> Dev 3: Staging pe alag schema hai
> → Team mein DB sync nahi hai 😱
> ```
>
> **With Alembic:**
> ```
> Dev 1: alembic revision --autogenerate -m "add_users_table"
> Everyone: alembic upgrade head
> → Sab ka same DB schema ✅
> ```
>
> **Kahan use hoga:** Har baar naya model banate ho ya existing model mein column add/remove/modify karte ho.

---

### ✅ Tasks

---

#### `Task 1` — 📦 Install Alembic

```bash
pip install alembic

alembic --version   # alembic 1.13.x
pip freeze > requirements.txt
```

---

#### `Task 2` — 🚀 Initialize Alembic

```bash
# backend/ folder mein
alembic init alembic
```

> 💡 **`alembic init` kya banata hai?**
> ```
> alembic/
> ├── env.py          ← Main config file — yahan settings karte hain
> ├── script.py.mako  ← Migration file ka template
> └── versions/       ← Yahan sab migration files hongi
> alembic.ini         ← Global Alembic config (SQLAlchemy URL etc.)
> ```

---

#### `Task 3` — ⚙️ Configure `alembic.ini`

```ini
# alembic.ini mein ye line find karo aur comment out karo:
# sqlalchemy.url = driver://user:pass@localhost/dbname

# Kyu? Kyunki hum DATABASE_URL .env se load karenge (env.py mein)
# Hardcode karna insecure hai (password exposed)
```

---

#### `Task 4` — 🔧 Update `alembic/env.py`

> 💡 **`env.py` kyu configure karna hai?**
> `env.py` Alembic ka **brain** hai — migration run karte waqt ye file:
> 1. Database se connect karta hai
> 2. Tumhare models ka metadata read karta hai
> 3. Actual migration SQL generate aur run karta hai
>
> Hume 2 chizen add karni hain:
> - `sys.path` mein `backend/` add karo taaki `from app.config import settings` kaam kare
> - `settings.DATABASE_URL` se DB URL lo (hardcode mat karo)

```python
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import sys, os

# backend/ folder ko Python path mein add karo
# Is se 'from app.config import settings' kaam karega
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.config import settings    # .env se settings
from app.database import Base      # All models ka base (metadata yahan hai)

config = context.config

# .env se DATABASE_URL inject karo (hardcode nahi)
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ── Models import karo — IMPORTANT! ─────────────────────────
# Har naya model yahan import karna ZAROORAT hai
# Tabhi alembic --autogenerate kaam karega
# from app.models.user import User       # Day 11 pe uncomment karo
# from app.models.team import Team       # Day 26 pe uncomment karo
# from app.models.player import Player   # Day 30 pe uncomment karo

target_metadata = Base.metadata
# Base.metadata = sab imported models ki table info
# Alembic isko current DB se compare karke diff nikalega


def run_migrations_offline() -> None:
    """DB connection ke bina migration SQL generate karo"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata,
                      literal_binds=True, dialect_opts={"paramstyle": "named"})
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """DB se connect karke migration run karo (normal way)"""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,             # Column type changes detect karo
            compare_server_default=True,   # Default value changes detect karo
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

---

#### `Task 5` — 🧱 Create Base model class

> ### 📖 UUID kya hai aur kyu use kiya?
>
> **UUID (Universally Unique Identifier):** 128-bit random ID, format: `550e8400-e29b-41d4-a716-446655440000`
>
> **Integer ID (1, 2, 3...) vs UUID — kyu UUID:**
>
> | | Integer ID | UUID |
> |-|-----------|------|
> | Predictable | ✅ Haan (1, 2, 3...) | ❌ Nahi (random) |
> | Security | ❌ `/users/1` pe guess kar sakte | ✅ Impossible to guess |
> | Distributed | ❌ Multiple servers pe conflict | ✅ Global uniqueness |
> | Frontend generate | ❌ DB pe depend | ✅ Client bhi generate kar sakta |
>
> **Cricket Auction mein:** User IDs, Team IDs, Player IDs, Bid IDs — sab UUID honge.

**`app/models/base.py`:**
```python
from sqlalchemy import Column, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
# PostgreSQL specific UUID type — native UUID storage (efficient)
from app.database import Base
import uuid


class TimestampMixin:
    """
    created_at + updated_at columns — sab models mein chahiye.
    Mixin pattern: inherit karo, columns automatically milenge.
    """
    created_at = Column(
        DateTime(timezone=True),        # Timezone aware datetime
        server_default=func.now(),      # DB server se current time
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),    # Record update pe automatically current time
        nullable=True
    )


class UUIDMixin:
    """UUID primary key — sab models ko milega"""
    id = Column(
        UUID(as_uuid=True),     # Python mein uuid.UUID object milega
        primary_key=True,
        default=uuid.uuid4,     # Auto-generate UUID on creation
        nullable=False
    )


class BaseModel(UUIDMixin, TimestampMixin, Base):
    """
    Abstract base class — sab SQLAlchemy models yahan se inherit karenge.
    __abstract__ = True: Is class ka khud koi table nahi banega.
    """
    __abstract__ = True

    def to_dict(self):
        """Model object ko plain Python dict mein convert karo"""
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
```

---

#### `Task 6 & 7` — 🚦 Generate + Run migration + Commands

```bash
# Pehla (empty) migration banao
alembic revision -m "initial_setup"
# Ye alembic/versions/ mein ek file banata hai
```

> 💡 **`alembic revision` kya karta hai?**
> Ek naya **migration file** banata hai `alembic/versions/` mein.
> Is file mein 2 functions hote hain:
> - `upgrade()` → migration apply karo (tables banao)
> - `downgrade()` → migration rollback karo (tables hatao)

```bash
# Migration database pe apply karo
alembic upgrade head
# Output: INFO Running upgrade  -> abc123, initial_setup
```

> 💡 **`alembic upgrade head` kya karta hai?**
> `head` = latest migration tak upgrade karo.
> Sab pending migrations ek ek karke apply karta hai.
> Jab pehli baar run karo → `alembic_version` table banti hai DB mein jisme current version store hota hai.

---

> ### 📖 Alembic Commands — Poori Reference
>
> ```bash
> # ── GENERATE ────────────────────────────────────────────
> alembic revision -m "description"
> # Kya karta hai: Empty migration file banata hai
> # Kab use: Manually SQL likhni ho migration mein
>
> alembic revision --autogenerate -m "add_users_table"
> # Kya karta hai: Models dekh ke automatically migration generate karta hai
> # Kab use: Naya model banaya ya existing mein column add kiya
> # ⚠️  IMPORTANT: env.py mein model IMPORT hona chahiye tabhi kaam karega
>
> # ── RUN (Apply) ─────────────────────────────────────────
> alembic upgrade head
> # Kya karta hai: Sab pending migrations apply karta hai
> # Kab use: Fresh setup ya naya migration aane ke baad
>
> alembic upgrade +1
> # Kya karta hai: Sirf ek migration aage badhta hai
>
> # ── ROLLBACK ────────────────────────────────────────────
> alembic downgrade -1
> # Kya karta hai: Ek migration peeche jaata hai (undo)
> # Kab use: Galat migration apply ho gayi
>
> alembic downgrade base
> # Kya karta hai: Sab migrations rollback — fresh DB
>
> # ── INFO ────────────────────────────────────────────────
> alembic current
> # Kya karta hai: Database abhi kis migration version pe hai ye batata hai
> # Output: abc123def456 (head)
>
> alembic history
> # Kya karta hai: Sari migrations ki list (chronological order)
> # Output: abc123 -> def456 -> ghi789 (head)
>
> alembic history --verbose
> # Kya karta hai: Har migration ki detail — date, message, revision ID
> ```

---

> ### 🏁 Expected Output — Day 7
> ```
> ✅ Alembic installed and initialized
> ✅ env.py — .env se DATABASE_URL, Base.metadata connected
> ✅ BaseModel with UUID (auto-generate) + timestamps ready
> ✅ First migration created and applied
> ✅ alembic_version table visible in DBeaver
> ✅ All alembic commands samajh aaye
> ```
> 🎯 **Goal Achieved:** DB migrations working, BaseModel with UUID ready

---
---

## ⚛️ Day 8: Frontend Vite + React Setup

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Frontend` |
| 🎯 **Goal** | React + TypeScript app on localhost:5173 with proxy |

---

> ### 📖 Vite kya hai aur kyu use kiya?
>
> **Kya hai:** Modern **frontend build tool** — React app development server run karta hai aur production build banata hai.
>
> **Vite vs Create React App (CRA):**
> | | CRA | Vite |
> |-|-----|------|
> | Speed | ❌ Slow (webpack) | ✅ Fast (esbuild + native ESM) |
> | HMR (Hot reload) | ❌ Slow | ✅ Instant |
> | Config | ❌ Ejected, complex | ✅ Simple `vite.config.ts` |
>
> **TypeScript kyu?**
> JavaScript + Type safety = TypeScript. Compile time errors catch ho jaate hain. Player ID `string` hai ya `number` — TypeScript bata dega pehle hi.

---

### ✅ Tasks

---

#### `Task 1` — 📁 Create frontend folder

```bash
cd ..   # cricket-auction-platform/ root mein jao
mkdir frontend
cd frontend
```

---

#### `Task 2 & 3` — ⚡ Vite setup + Install dependencies

```bash
npm create vite@latest . -- --template react-ts
# . = current folder mein banao
# --template react-ts = React + TypeScript template

npm install              # package.json se sab dependencies install karo
npm install -D @types/node   # path alias ke liye Node.js types
```

---

#### `Task 4` — 🔧 Configure `vite.config.ts` with proxy

> 💡 **Proxy kyu lagaya?**
>
> **Problem:** Frontend `localhost:5173` pe hai, Backend `localhost:8000` pe hai.
> Browser CORS block karega agar directly `http://localhost:8000/api/...` call karo.
>
> **Solution:** Vite proxy — `/api/...` request aaye toh Vite automatically `http://localhost:8000/api/...` forward kar deta hai.
> Browser sirf `localhost:5173` se baat karta hai — CORS issue nahi hota.
>
> **WebSocket proxy bhi:** `/ws` path WebSocket connection ke liye forward hoga.

```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
      // @/components/ui/button = src/components/ui/button (short path)
    },
  },
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',  // Backend URL
        changeOrigin: true,               // Host header change karo
      },
      '/ws': {
        target: 'ws://localhost:8000',    // WebSocket backend
        ws: true,                         // WebSocket upgrade karo
      },
    },
  },
})
```

---

#### `Task 5 & 6` — 🧹 Clean up + Create structure

```bash
rm src/App.css      # nahi chahiye

mkdir -p src/pages \
         src/components/ui src/components/layout \
         src/components/auth src/components/auction \
         src/components/admin \
         src/hooks src/store src/services src/types src/utils
```

**`src/App.tsx`:**
```tsx
function App() {
  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>🏏 Cricket Auction Platform</h1>
      <p>Frontend setup complete!</p>
    </div>
  )
}
export default App
```

**`src/types/index.ts`** — shared TypeScript interfaces:
```typescript
// Ye types poore frontend mein use honge
// Backend ke Pydantic schemas se match karna chahiye

export interface User {
  id: string             // UUID string
  email: string
  name: string
  avatar_url?: string    // ? = optional
  role: 'admin' | 'captain' | 'member'   // Union type — sirf ye 3 values
  team_id?: string
  is_captain: boolean
}

export interface ApiResponse<T> {
  // Generic — T koi bhi type ho sakta hai
  success: boolean
  message: string
  data?: T
}

export interface PaginatedResponse<T> {
  items: T[]
  total: number
  page: number
  limit: number
  total_pages: number
}
```

---

#### `Task 7` — 🚀 Run dev server

```bash
npm run dev
# ➜  Local:   http://localhost:5173/
```

---

> ### 🏁 Expected Output — Day 8
> ```
> ✅ React + TypeScript on localhost:5173
> ✅ Vite proxy: /api → :8000, /ws → ws://:8000
> ✅ Folder structure ready
> ✅ TypeScript types defined
> ```
> 🎯 **Goal Achieved:** React + TypeScript app on localhost:5173 with proxy

---
---

## 🎨 Day 9: Tailwind + Shadcn Setup

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Frontend` |
| 🎯 **Goal** | Tailwind working, Shadcn components usable |

---

> ### 📖 Tailwind CSS kya hai?
>
> **Kya hai:** **Utility-first CSS framework** — pre-defined small CSS classes hain jo directly HTML mein lagate hain.
>
> ```jsx
> // Traditional CSS:
> <div className="card">  →  .card { padding: 1rem; border-radius: 0.5rem; }
>
> // Tailwind:
> <div className="p-4 rounded-lg bg-white shadow">  (no separate CSS file needed)
> ```
>
> **Kyu use kiya:** Custom CSS likhne ki zaroorat kam, design consistent rehta hai, responsive easily ho jaata hai.

---

> ### 📖 Shadcn UI kya hai?
>
> **Kya hai:** **Copy-paste component library** — Button, Card, Input jaise ready-made React components.
>
> **Shadcn vs Material UI / Ant Design:**
> - Material UI/Ant Design: npm package ke roop mein aate hain — override karna mushkil
> - Shadcn: Source code directly tumhare `src/components/ui/` mein aata hai — fully customizable
>
> **Kyu use kiya:** Quick UI, consistent design, Tailwind ke saath perfectly kaam karta hai.

---

### ✅ Tasks

---

#### `Task 1 & 2` — 📦 Install + Configure Tailwind

```bash
npm install -D tailwindcss postcss autoprefixer
# -D = devDependency (sirf development mein chahiye, production bundle mein nahi)
# postcss = CSS processing tool (Tailwind isko use karta hai)
# autoprefixer = browser vendor prefixes automatically add karta hai (-webkit-, -moz-)

npx tailwindcss init -p
# tailwind.config.js + postcss.config.js ban jaengi
```

**`tailwind.config.js`:**
```javascript
/** @type {import('tailwindcss').Config} */
export default {
  darkMode: ["class"],   // class="dark" add karne pe dark mode
  content: [
    "./index.html",
    "./src/**/*.{ts,tsx,js,jsx}",
    // Tailwind in files mein classes dhundega — unused classes remove karega (tree-shaking)
  ],
  theme: {
    extend: {
      colors: {
        // 🏏 Custom cricket theme colors
        cricket: {
          green: "#1a7a1a",
          pitch: "#4a7c59",
          gold:  "#f5c518",
          red:   "#cc0000",
        },
        // Shadcn UI ke liye CSS variable based colors
        border:     "hsl(var(--border))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT:    "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        // ... (baaki colors Day 9 ki file mein hain)
      },
    },
  },
  plugins: [],
}
```

> 💡 **`hsl(var(--primary))` kya hai?**
> CSS variables (`:root` mein define) + HSL color format.
> Dark mode mein sirf CSS variable ki value change karni hoti hai — ek jagah change, poora theme update.

---

#### `Task 3` — 🎨 Update `src/index.css`

```css
@tailwind base;        /* Tailwind reset styles */
@tailwind components;  /* Component classes */
@tailwind utilities;   /* Utility classes (p-4, flex, etc.) */

/* CSS Variables — Shadcn UI ke liye */
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --primary: 221.2 83.2% 53.3%;
    --primary-foreground: 210 40% 98%;
    /* ... baaki variables */
    --radius: 0.5rem;
  }

  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    /* Dark mode mein variables override ho jaate hain */
  }
}

@layer base {
  * { @apply border-border; }
  body { @apply bg-background text-foreground; }
}
```

---

#### `Task 4` — 🛠️ Init Shadcn

```bash
npx shadcn@latest init
# Style: Default | Color: Slate | CSS variables: yes
```

**`tsconfig.json`** mein paths (Shadcn ke liye zaroorat hai):
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": { "@/*": ["./src/*"] }
  }
}
```

---

#### `Task 5 & 6` — ➕ Add components + Test

```bash
npx shadcn@latest add button card input badge avatar
# Source code src/components/ui/ mein copy ho jaayega
```

**`src/App.tsx`** test:
```tsx
import { Button }                                          from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle }        from "@/components/ui/card"
import { Input }                                           from "@/components/ui/input"
import { Badge }                                           from "@/components/ui/badge"
// @ = src/ folder (vite.config.ts mein alias set kiya tha)

function App() {
  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center p-8">
      <Card className="w-full max-w-md shadow-lg">
        <CardHeader>
          <CardTitle className="text-2xl font-bold text-center">
            🏏 Cricket Auction Platform
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex gap-2 flex-wrap justify-center">
            <Badge variant="default">FastAPI ✅</Badge>
            <Badge variant="secondary">PostgreSQL ✅</Badge>
            <Badge className="bg-green-500 text-white">Tailwind ✅</Badge>
            <Badge className="bg-purple-500 text-white">Shadcn ✅</Badge>
          </div>
          <Input placeholder="🔍 Search players..." />
          <Button className="w-full bg-green-600 hover:bg-green-700 text-white">
            💰 Place Bid — ₹50 Lakhs
          </Button>
        </CardContent>
      </Card>
    </div>
  )
}
export default App
```

---

> ### 🏁 Expected Output — Day 9
> ```
> ✅ Tailwind CSS working — classes apply ho rahi hain
> ✅ Shadcn components installed (button, card, input, badge, avatar)
> ✅ Cricket-themed custom colors available
> ✅ Dark mode CSS variables ready
> ✅ Styled test page dikh raha hai
> ```
> 🎯 **Goal Achieved:** Tailwind working, Shadcn components usable

---
---

## 🐙 Day 10: Git Setup + First Commit

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Both` |
| 🎯 **Goal** | Git repo, first commit, both servers verified |

---

> ### 📖 Git kyu use kar rahe hain?
>
> **Kya hai:** **Version control system** — code history track karta hai.
>
> **3 main reasons:**
> 1. **History:** Kabhi bhi purana code dekh sako
> 2. **Collaboration:** Team mein kaam karo bina conflict ke
> 3. **Backup:** GitHub pe push karo — local delete ho toh bhi safe

---

### ✅ Tasks

---

#### `Task 1` — 🔧 Initialize git

```bash
cd ..   # cricket-auction-platform/ root

git init
# .git/ folder ban jaayega — ab ye folder tracked hai

git status   # kya tracked, kya nahi
```

---

#### `Task 2` — 📄 Create `.gitignore`

> 💡 **`.gitignore` kyu?**
> Kuch files kabhi commit nahi karni chahiye:
> - `venv/` — 100s of MBs, dusra developer apna install karega
> - `.env` — Passwords, secrets — public ho jaaye toh dangerous
> - `node_modules/` — 100s of MBs, `npm install` se generate hoga
> - `__pycache__/` — Compiled Python files — automatically bante hain

```gitignore
# ══════════════════════════════════════════
#   Cricket Auction Platform — .gitignore
# ══════════════════════════════════════════

# ── Python ──────────────────────────────
backend/venv/
backend/__pycache__/
backend/**/__pycache__/
backend/**/*.pyc
backend/.pytest_cache/

# ── Secrets (KABHI COMMIT MAT KARO!) ────
backend/.env
backend/.env.local
.env
.env.local

# ── Database ────────────────────────────
*.db
*.sqlite3

# ── Node ────────────────────────────────
frontend/node_modules/
frontend/dist/
frontend/dist-ssr/
frontend/.env

# ── IDE ─────────────────────────────────
.vscode/
.idea/
*.swp
.DS_Store
Thumbs.db

# ── Logs ────────────────────────────────
*.log
npm-debug.log*
```

---

#### `Task 3` — 📝 Create `README.md`

```markdown
# 🏏 Cricket Auction Platform

Real-time cricket player auction with live bidding, WebSockets, Google OAuth.

## 🛠️ Tech Stack
| Layer | Tech |
|-------|------|
| Backend | FastAPI + PostgreSQL + SQLAlchemy + Alembic |
| Frontend | React 18 + TypeScript + Tailwind + Shadcn UI |
| Realtime | WebSockets |
| Auth | JWT + Google OAuth |

## 🚀 Quick Start

### Backend
```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env    # apni values fill karo
alembic upgrade head
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend && npm install && npm run dev
```

## 📖 API Docs
- Swagger: http://localhost:8000/docs
```

---

#### `Task 4` — ✨ First commit

```bash
git add .           # Sab files staging mein add karo
git status          # Review — kya commit ho raha hai

git commit -m "feat: initial project setup (Phase 1)

- Backend: FastAPI + SQLAlchemy + Alembic + PostgreSQL configured
- Frontend: React + TypeScript + Tailwind + Shadcn UI setup
- Project folder structure (Router/Service/Repository pattern)
- BaseModel with UUID + timestamps
- CORS, proxy, environment config ready"

git log --oneline   # Commit history dekho
```

---

#### `Task 5 & 6` — ☁️ Push to GitHub (optional)

```bash
# GitHub pe naya private repo banao
git remote add origin https://github.com/YOUR_USERNAME/cricket-auction-platform.git
git branch -M main
git push -u origin main
```

---

#### `Task 7` — ✅ Verify both servers

**`backend/.env.example`** banao (commit karo, `.env` nahi):
```env
# cp .env.example .env  → phir apni values fill karo

APP_NAME=Cricket Auction Platform
DEBUG=True
DATABASE_URL=postgresql://admin:YOUR_PASSWORD@localhost:5432/cricket_auction
SECRET_KEY=your-super-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_REDIRECT_URI=http://localhost:8000/api/auth/google/callback
```

```bash
# Terminal 1 — Backend:
cd backend && source venv/bin/activate
uvicorn app.main:app --reload
# ✅ http://localhost:8000

# Terminal 2 — Frontend:
cd frontend && npm run dev
# ✅ http://localhost:5173

# Terminal 3 — Smoke test:
curl http://localhost:8000/health   # {"status":"healthy"}
```

```bash
# .env.example commit karo
git add backend/.env.example
git commit -m "docs: add .env.example for new developers"
```

---

> ### 🏁 Expected Output — Day 10
> ```
> ✅ Git repo initialized with .gitignore
> ✅ README.md with setup instructions
> ✅ First commit made
> ✅ .env.example committed (not .env!)
> ✅ Backend :8000 + Frontend :5173 — both running
> ✅ Phase 1 COMPLETE! 🎉
> ```
> 🎯 **Goal Achieved:** Git repo initialized, first commit done, both servers verified

---
---

## 🏆 Phase 1 — Complete Summary

| Day | 🎯 Topic | 🔧 Type | Key Libraries |
|-----|----------|---------|---------------|
| Day 1  | PostgreSQL Setup | Backend | `postgresql`, `DBeaver` |
| Day 2  | FastAPI Setup | Backend | `fastapi`, `uvicorn` |
| Day 3  | FastAPI Basics | Learning | `APIRouter`, `BaseModel` |
| Day 4  | SQLAlchemy Setup | Backend | `sqlalchemy`, `psycopg2`, `pydantic-settings` |
| Day 5  | Pydantic Basics | Backend | `pydantic`, `Field`, `field_validator` |
| Day 6  | Folder Structure | Backend | `CORSMiddleware`, `Depends` (concept) |
| Day 7  | Alembic Setup | Backend | `alembic`, `UUID`, `TimestampMixin` |
| Day 8  | Vite + React | Frontend | `vite`, `react`, `typescript` |
| Day 9  | Tailwind + Shadcn | Frontend | `tailwindcss`, `shadcn`, CSS variables |
| Day 10 | Git Setup | Both | `git`, `.gitignore`, `.env.example` |

---

### 📁 Final Folder Structure After Phase 1

```
cricket-auction-platform/
├── 📄 .gitignore
├── 📄 README.md
│
├── 🐍 backend/
│   ├── 📄 .env              ← gitignored (secrets)
│   ├── 📄 .env.example      ← committed (template)
│   ├── 📄 requirements.txt
│   ├── 📄 alembic.ini
│   ├── 📁 alembic/
│   │   ├── env.py           ← DB URL + models metadata
│   │   └── versions/        ← Migration files
│   └── 📁 app/
│       ├── main.py          ← FastAPI app + CORS
│       ├── config.py        ← pydantic-settings (.env loader)
│       ├── database.py      ← engine + SessionLocal + get_db()
│       ├── 📁 models/
│       │   └── base.py      ← BaseModel (UUID + timestamps)
│       ├── 📁 schemas/
│       │   └── common.py    ← APIResponse, Pagination, ErrorResponse
│       ├── 📁 routers/      ← API routes (Day 11+ se)
│       ├── 📁 services/     ← Business logic (Day 11+ se)
│       ├── 📁 repositories/ ← DB queries (Day 11+ se)
│       ├── 📁 websockets/   ← WebSocket (Day 43+ se)
│       ├── 📁 utils/        ← JWT, OAuth, Timer (Day 13+ se)
│       └── 📁 middleware/   ← Auth (Day 20 se)
│
└── ⚛️ frontend/
    ├── 📄 package.json
    ├── 📄 tailwind.config.js
    ├── 📄 vite.config.ts     ← Proxy config
    └── 📁 src/
        ├── App.tsx
        ├── index.css         ← Tailwind + CSS variables
        ├── 📁 types/
        │   └── index.ts      ← TypeScript interfaces
        ├── 📁 components/
        │   └── ui/           ← Shadcn components
        ├── 📁 pages/
        ├── 📁 hooks/
        ├── 📁 store/         ← Zustand (Day 23 se)
        └── 📁 services/      ← API calls (Day 24 se)
```

---

> ## 🔜 Next Up: Phase 2 — Authentication (Days 11–25)
>
> | Day | Topic | Key Concepts |
> |-----|-------|-------------|
> | Day 11 | User Model | SQLAlchemy model, Enum columns |
> | Day 12 | User Schemas | Pydantic UserCreate, UserResponse |
> | Day 13 | JWT Basics | `python-jose`, token generation |
> | Day 14 | JWT Token Flow | Payload, expiry, verification |
> | Day 15 | Google OAuth Setup | Google Cloud Console, credentials |
> | Day 16 | Authlib Setup | OAuth client configuration |
> | Day 17 | Google OAuth Routes | Redirect to Google |
> | Day 18 | Google Callback | Token exchange, user info |
> | Day 19 | Auto User Creation | DB upsert, JWT return |
> | Day 20 | Auth Middleware | `Depends`, `get_current_user` |
> | Day 21 | Protected Routes | `/api/auth/me` |
> | Day 22 | Login Page UI | React + Shadcn |
> | Day 23 | Auth Store | Zustand state management |
> | Day 24 | OAuth Integration | Frontend redirect + token save |
> | Day 25 | Protected Routes FE | React Router, ProtectedRoute |

---

---
---

# 🔐 Phase 2: Authentication

### `Days 11 → 25` &nbsp;|&nbsp; Backend Auth + Frontend Auth Flow

---

## 👤 Day 11: User Model (SQLAlchemy)

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | User table in DB with role-based access, migration applied |

---

> ### 📖 `Enum` kya hai aur kyu use kiya?
>
> **Kya hai:** `Enum` ek Python built-in type hai jo ek **fixed set of values** define karta hai. Jaise agar user ka role sirf `admin`, `team_owner`, ya `viewer` ho sakta hai — to Enum use karte hain.
>
> **Problem without Enum:**
> ```python
> # Bina Enum ke — koi bhi string store ho sakti hai
> user.role = "adminn"   # typo! DB mein galat value jaayegi
> user.role = "ADMIN"    # ya ye bhi chala jaayega
> ```
>
> **With Enum:**
> ```python
> class UserRole(str, Enum):
>     ADMIN = "admin"
>     TEAM_OWNER = "team_owner"
>     VIEWER = "viewer"
>
> user.role = UserRole.ADMIN      # ✅ valid
> user.role = "adminn"             # ❌ Error! invalid value
> ```
>
> **`str, Enum` kyu likha?** `str` inherit karne se ye Enum values JSON mein automatically string ke roop mein serialize hoti hain — FastAPI ke saath perfectly kaam karta hai.
>
> **Kahan use hoga:** User model mein `role` column ke liye, aur baad mein auction status ke liye bhi.

---

### ✅ Tasks

---

#### `Task 1` — 📦 Install dependencies

```bash
cd backend
pip install passlib[bcrypt]
pip freeze > requirements.txt
```

> ### 📖 `passlib[bcrypt]` kya hai aur kyu use kiya?
>
> **Kya hai:** `passlib` ek Python **password hashing library** hai. `bcrypt` ek hashing algorithm hai jo bahut secure hai.
>
> **Kyu password hash karte hain?**
> ```
> User ka actual password:  "mypassword123"
> Database mein store hoga: "$2b$12$eW5m8K.../hashed_value"
>
> Agar DB leak ho jaye → password nahi pata chalega hacker ko!
> ```
>
> **`passlib` vs plain `hashlib`:**
> | | `passlib[bcrypt]` | `hashlib` |
> |--|------------------|-----------|
> | Security | ✅ Industry standard | ⚠️ MD5/SHA — old, crackable |
> | Salt | ✅ Automatic | ❌ Manual add karna padega |
> | Verify | ✅ Easy `verify()` method | ❌ Manual re-hash |
>
> **Kahan use hoga:** Day 19 mein jab user registration add karenge — password store karne se pehle hash karenge. Google OAuth se aane wale users ke liye password nahi hoga (Google hi authenticate karta hai).

---

#### `Task 2` — 🗂️ Create User model

**`backend/app/models/user.py`** banao:

```python
import uuid
from enum import Enum
from sqlalchemy import Column, String, Boolean, Enum as SAEnum
from app.models.base import BaseModel  # Day 7 mein banaya tha (UUID + timestamps)


# ─── User Role Enum ──────────────────────────────────────────────────────────
class UserRole(str, Enum):
    """
    User ke teen roles hain:
    - ADMIN       → platform owner, sab kuch kar sakta hai
    - TEAM_OWNER  → apni team manage kar sakta hai, auction mein bid kar sakta hai
    - VIEWER      → sirf dekh sakta hai (read-only)
    """
    ADMIN = "admin"
    TEAM_OWNER = "team_owner"
    VIEWER = "viewer"


# ─── User SQLAlchemy Model ────────────────────────────────────────────────────
class User(BaseModel):
    """
    BaseModel se ye sab automatically milta hai (Day 7 se):
      - id          → UUID (auto-generated)
      - created_at  → timestamp
      - updated_at  → timestamp (auto-update)
    """
    __tablename__ = "users"

    email = Column(
        String(255),
        unique=True,     # ek email ek hi user ke paas ho sakta hai
        nullable=False,  # email required hai
        index=True       # email se fast search ke liye DB index
    )

    full_name = Column(
        String(255),
        nullable=False
    )

    google_id = Column(
        String(255),
        unique=True,     # Google ka unique user ID
        nullable=True    # nullable: sirf Google OAuth users ke paas hoga
    )

    profile_picture = Column(
        String(500),     # URL hai, isliye 500 chars
        nullable=True
    )

    role = Column(
        SAEnum(UserRole),         # SQLAlchemy ko batao ye Enum column hai
        default=UserRole.VIEWER,  # default role: viewer
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True,    # naya user by default active hota hai
        nullable=False
    )
```

> 💡 **`SAEnum` vs `Enum` — fark kya hai?**
> - `from enum import Enum` → Python ka built-in Enum (Python code mein use)
> - `from sqlalchemy import Enum as SAEnum` → SQLAlchemy ka Enum (database column ke liye)
> Dono ek saath use karte hain: Python Enum define karo, SQLAlchemy Enum column mein us Python Enum ko pass karo.

> 💡 **`index=True` kya karta hai?**
> Database mein ek special data structure banta hai (B-tree) jo `email` se search bahut fast karta hai.
> Bina index: DB har row scan karta hai (O(n))
> Index ke saath: Direct jump (O(log n))
> Email se frequently user dhundenge (login pe), isliye index lagaya.

---

#### `Task 3` — 🔗 Register model in Alembic

**`backend/alembic/env.py`** mein User model import karo:

```python
# env.py mein ye line dhundo:
from app.models.base import BaseModel     # ye pehle se hoga

# Neeche ye add karo (BaseModel ke baad):
from app.models.user import User          # ← ye add karo

# SQLAlchemy ko pata chalega User model ke liye table banani hai
target_metadata = BaseModel.metadata
```

> 💡 **Kyu import karna padta hai?**
> Alembic `BaseModel.metadata` dekhta hai — lekin metadata mein sirf wahi tables hoti hain jinke models Python memory mein import ho chuke hoon. Agar import nahi kiya → Alembic table nahi dekhega → migration nahi banega.

---

#### `Task 4` — 🚀 Create and run migration

```bash
cd backend

# Autogenerate migration (models dekhkar automatically SQL banayega)
alembic revision --autogenerate -m "create users table"

# Migration file versions/ folder mein banega — use review karo
# Phir apply karo:
alembic upgrade head
```

**Migration file kuch aisi dikhegi (`alembic/versions/xxxx_create_users_table.py`):**
```python
def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('full_name', sa.String(255), nullable=False),
        sa.Column('google_id', sa.String(255), nullable=True),
        sa.Column('profile_picture', sa.String(500), nullable=True),
        sa.Column('role', sa.Enum('admin','team_owner','viewer'), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('google_id'),
    )
    op.create_index('ix_users_email', 'users', ['email'])
```

---

> ### 🏁 Expected Output — Day 11
> ```
> ✅ passlib[bcrypt] installed
> ✅ app/models/user.py created — User model with UserRole enum
> ✅ alembic/env.py updated — User imported
> ✅ Migration created in versions/ folder
> ✅ alembic upgrade head — users table in PostgreSQL
> ✅ DBeaver mein "users" table visible with all columns
> ```
> 🎯 **Goal Achieved:** User table in DB with role-based access, migration applied

---
---

## 📝 Day 12: User Schemas (Pydantic)

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | Request/Response schemas for User — type-safe API |

---

> ### 📖 Schema vs Model — fark kya hai?
>
> Ye confusion bahut common hai naye developers mein:
>
> | | SQLAlchemy **Model** | Pydantic **Schema** |
> |--|---------------------|---------------------|
> | File | `app/models/user.py` | `app/schemas/user.py` |
> | Kya hai | Database table ka Python representation | API request/response ka shape |
> | Kab use | DB se read/write karte waqt | Route mein input validate ya output serialize karte waqt |
> | Example | `User` class with columns | `UserResponse` class with fields |
>
> **Analogy:** Model = database ka blueprint. Schema = API ka contract (kya bhejo, kya milega).

---

### ✅ Tasks

---

#### `Task 1` — 📄 Create User schemas

**`backend/app/schemas/user.py`** banao:

```python
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from app.models.user import UserRole


# ─── Base schema (shared fields) ─────────────────────────────────────────────
class UserBase(BaseModel):
    """
    Ye schema sirf shared fields define karta hai.
    UserCreate aur UserResponse dono isko inherit karenge.
    """
    email: EmailStr           # Pydantic automatically email format validate karta hai
    full_name: str = Field(..., min_length=2, max_length=255)


# ─── Create schema (request body) ────────────────────────────────────────────
class UserCreate(UserBase):
    """
    Naya user banane ke liye request body.
    Abhi Google OAuth use karenge, to password nahi hai.
    google_id Google se milega.
    """
    google_id: Optional[str] = None
    profile_picture: Optional[str] = None


# ─── Update schema ────────────────────────────────────────────────────────────
class UserUpdate(BaseModel):
    """
    Partial update — sab fields optional hain.
    Sirf jo bhejo, wohi update hoga.
    """
    full_name: Optional[str] = Field(None, min_length=2, max_length=255)
    profile_picture: Optional[str] = None


# ─── Response schema (what API returns) ──────────────────────────────────────
class UserResponse(UserBase):
    """
    API response mein yahi shape return hogi.
    Password, google_id — sensitive fields yahan NAHI hain (intentional!).
    """
    id: str              # UUID string
    role: UserRole
    is_active: bool
    profile_picture: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
    # ↑ Pydantic v2 mein ye likhna padta hai taaki SQLAlchemy object
    #   directly Pydantic schema mein convert ho sake


# ─── Token schemas ────────────────────────────────────────────────────────────
class TokenResponse(BaseModel):
    """
    Login ke baad client ko ye milega.
    """
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


class TokenPayload(BaseModel):
    """
    JWT token ke andar jo data hoga (payload).
    """
    sub: str             # "subject" — user ka UUID
    email: str
    role: str
    exp: Optional[int] = None   # expiry timestamp
```

> 💡 **`EmailStr` kya hai?**
> Ye Pydantic ka built-in type hai jo **email format validate** karta hai automatically.
> ```python
> email: EmailStr
> # "user@example.com"  → ✅ valid
> # "notanemail"        → ❌ ValidationError
> # "user@"            → ❌ ValidationError
> ```
> Install karo agar error aaye: `pip install pydantic[email]`

> 💡 **`model_config = {"from_attributes": True}` kya karta hai?**
> SQLAlchemy objects ke attributes normally Pydantic directly nahi read kar sakta.
> Ye config Pydantic ko batata hai: "dict ki jagah object ke `.attribute` se bhi values lelo."
> ```python
> # Bina from_attributes:
> UserResponse(**user.__dict__)  # manually convert karna padta
>
> # With from_attributes:
> UserResponse.model_validate(user)  # ✅ directly SQLAlchemy object pass karo
> ```

---

#### `Task 2` — 🔄 Update common schemas

**`backend/app/schemas/common.py`** mein import add karo:

```python
# common.py mein ye already hoga (Day 5 se):
from typing import TypeVar, Generic, Optional, List
from pydantic import BaseModel

T = TypeVar("T")

class APIResponse(BaseModel, Generic[T]):
    success: bool
    message: str
    data: Optional[T] = None

# Usage example (reference ke liye):
# return APIResponse(success=True, message="User fetched", data=UserResponse.model_validate(user))
```

---

> ### 🏁 Expected Output — Day 12
> ```
> ✅ app/schemas/user.py created
> ✅ UserBase, UserCreate, UserUpdate, UserResponse defined
> ✅ TokenResponse, TokenPayload schemas ready
> ✅ EmailStr validation working
> ✅ model_config from_attributes=True set
> ```
> 🎯 **Goal Achieved:** Request/Response schemas for User — type-safe API

---
---

## 🔑 Day 13: JWT Basics

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | JWT token generate aur verify karna — `python-jose` se |

---

> ### 📖 JWT kya hai aur kyu use kiya?
>
> **Kya hai:** JWT = **JSON Web Token** — ek standard tarika hai **user ki identity prove karne ka** — bina baar baar database check kiye.
>
> **Problem without JWT:**
> ```
> User login karta hai → DB mein session store karo → har request pe DB check karo
> ❌ Slow, ❌ DB pe load, ❌ Horizontal scaling mushkil
> ```
>
> **JWT ke saath:**
> ```
> User login karta hai → Token generate karo (signed) → Client ke paas store hota hai
> Har request → Token verify karo (math se, DB touch nahi) → User identify
> ✅ Fast, ✅ Stateless, ✅ Scalable
> ```
>
> **JWT ka structure (3 parts, `.` se separated):**
> ```
> eyJhbGciOiJIUzI1NiJ9 . eyJzdWIiOiJ1c2VyMTIzIn0 . SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
>      HEADER                      PAYLOAD                           SIGNATURE
>   (algorithm)              (user data — visible)            (secret se sign kiya)
> ```
>
> **Signature kyu important hai?**
> Token mein data **visible** hota hai (base64 encoded, encrypted nahi) — lekin signature ke bina koi tamper nahi kar sakta. Agar payload change karo → signature invalid ho jaata hai.
>
> **Kahan use hoga:** Har protected API route pe — user logged in hai ya nahi verify karne ke liye.

> ### 📖 `python-jose` kya hai aur kyu use kiya?
>
> **Kya hai:** `python-jose` ek Python library hai JWT tokens **encode** (create) aur **decode** (verify) karne ke liye.
>
> **Alternatives:**
> | Library | Status |
> |---------|--------|
> | `python-jose` | ✅ Popular, FastAPI docs mein recommended |
> | `PyJWT` | ✅ Also good, simpler |
> | `authlib` | ✅ Full OAuth + JWT (Day 16 mein use karenge) |
>
> **`[cryptography]` extra kyu?** Kuch algorithms (RS256, ES256) ke liye cryptography backend chahiye. `python-jose[cryptography]` dono saath install karta hai.

---

### ✅ Tasks

---

#### `Task 1` — 📦 Install JWT library

```bash
cd backend
pip install "python-jose[cryptography]"
pip freeze > requirements.txt
```

---

#### `Task 2` — ⚙️ Add JWT config in `.env`

```bash
# backend/.env mein ye add karo:
SECRET_KEY=your-super-secret-key-change-this-in-production-must-be-long
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080   # 7 days (7 * 24 * 60)
```

> ⚠️ **`SECRET_KEY` production mein strong hona chahiye:**
> ```bash
> # Terminal mein ye command se strong key generate karo:
> openssl rand -hex 32
> # Output: a9f3d8c2... (64 char random hex string)
> ```

**`backend/app/config.py`** update karo:

```python
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str               # ← ye add karo
    ALGORITHM: str = "HS256"      # ← ye add karo
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080  # ← ye add karo

    class Config:
        env_file = ".env"
```

---

#### `Task 3` — 🛠️ Create JWT utility

**`backend/app/utils/jwt.py`** banao:

```python
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from app.config import settings


# ─── Create Token ─────────────────────────────────────────────────────────────
def create_access_token(
    user_id: str,
    email: str,
    role: str,
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    JWT access token banata hai.

    Parameters:
        user_id  → User ka UUID (string)
        email    → User ka email
        role     → User ka role (admin/team_owner/viewer)
        expires_delta → Token kitne time mein expire ho (default: settings se)

    Returns:
        JWT token string
    """
    # Expiry time calculate karo
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    # Token ka payload (data jo token ke andar encode hoga)
    payload = {
        "sub": user_id,       # "subject" — JWT standard field, user ID
        "email": email,
        "role": role,
        "exp": expire,        # "expiry" — JWT standard field
        "iat": datetime.now(timezone.utc),  # "issued at" — kab banaya
    }

    # Token encode karo (SECRET_KEY se sign hoga)
    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return token


# ─── Verify & Decode Token ────────────────────────────────────────────────────
def decode_access_token(token: str) -> Optional[dict]:
    """
    JWT token verify karta hai aur payload return karta hai.

    Returns:
        dict (payload) → agar token valid hai
        None           → agar token invalid/expired hai
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        # JWTError tab aata hai jab:
        # - Token tampered ho
        # - Token expired ho
        # - Signature match na kare
        return None
```

> 💡 **`sub` (subject) field kya hai?**
> JWT mein kuch **reserved claims** hain (standard fields):
> - `sub` → subject (usually user ID)
> - `exp` → expiry timestamp
> - `iat` → issued at timestamp
> - `iss` → issuer (kise ne banaya)
> Hum `sub` mein user UUID store karte hain taaki token se user identify kar sakein.

> 💡 **`timezone.utc` kyu use kiya?**
> `datetime.now()` local timezone mein time deta hai — server ka timezone alag ho sakta hai.
> `datetime.now(timezone.utc)` → always UTC time → consistent across all servers.

---

#### `Task 4` — 🧪 Test JWT in Python shell

```bash
cd backend
python3 -c "
from app.utils.jwt import create_access_token, decode_access_token
import uuid

# Token banao
token = create_access_token(
    user_id=str(uuid.uuid4()),
    email='test@example.com',
    role='viewer'
)
print('Token:', token[:50], '...')

# Token decode karo
payload = decode_access_token(token)
print('Payload:', payload)
"
```

---

> ### 🏁 Expected Output — Day 13
> ```
> ✅ python-jose[cryptography] installed
> ✅ SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES in .env + config.py
> ✅ app/utils/jwt.py created
> ✅ create_access_token() working
> ✅ decode_access_token() working
> ✅ Python shell test successful — token encode + decode ✓
> ```
> 🎯 **Goal Achieved:** JWT token generate aur verify karna — `python-jose` se

---
---

## 🔐 Day 14: JWT Token Flow (Protected Routes)

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | `get_current_user` dependency — har protected route pe user inject hoga |

---

### ✅ Tasks

---

#### `Task 1` — 🗃️ User Repository banao

**`backend/app/repositories/user_repository.py`** banao:

```python
from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User


class UserRepository:
    """
    User ke saare database operations yahan hain.
    Service layer directly DB touch nahi karta — sirf repository se baat karta hai.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: str) -> Optional[User]:
        """UUID se user dhundo."""
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str) -> Optional[User]:
        """Email se user dhundo (login ke liye)."""
        return self.db.query(User).filter(User.email == email).first()

    def get_by_google_id(self, google_id: str) -> Optional[User]:
        """Google ID se user dhundo (OAuth callback pe)."""
        return self.db.query(User).filter(User.google_id == google_id).first()

    def create(self, email: str, full_name: str, google_id: Optional[str] = None,
               profile_picture: Optional[str] = None) -> User:
        """Naya user banao aur DB mein save karo."""
        user = User(
            email=email,
            full_name=full_name,
            google_id=google_id,
            profile_picture=profile_picture,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)  # DB se latest data wapas lo (id, timestamps etc.)
        return user

    def update(self, user: User, **kwargs) -> User:
        """User ke fields update karo."""
        for key, value in kwargs.items():
            if hasattr(user, key) and value is not None:
                setattr(user, key, value)
        self.db.commit()
        self.db.refresh(user)
        return user
```

> 💡 **`self.db.refresh(user)` kyu?**
> `.commit()` ke baad Python object ke paas `id`, `created_at` etc. nahi hote (DB ne generate kiye hain).
> `.refresh(user)` DB se latest data reload karta hai Python object mein.

---

#### `Task 2` — 🔒 Create `get_current_user` dependency

**`backend/app/utils/dependencies.py`** banao:

```python
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils.jwt import decode_access_token
from app.repositories.user_repository import UserRepository
from app.models.user import User, UserRole


# HTTPBearer: Authorization header se "Bearer <token>" extract karta hai
bearer_scheme = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
) -> User:
    """
    Protected routes ke liye dependency.
    Request header se token uthata hai, verify karta hai, user return karta hai.

    Usage in routes:
        @router.get("/me")
        def get_me(current_user: User = Depends(get_current_user)):
            return current_user
    """
    # 401 error ka template
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Token decode karo
    token = credentials.credentials   # "Bearer <token>" se sirf token part
    payload = decode_access_token(token)

    if payload is None:
        raise credentials_exception

    # Payload se user ID nikalo
    user_id: Optional[str] = payload.get("sub")
    if user_id is None:
        raise credentials_exception

    # DB se actual user fetch karo
    user_repo = UserRepository(db)
    user = user_repo.get_by_id(user_id)

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is deactivated"
        )

    return user


def require_role(*roles: UserRole):
    """
    Role-based access control ke liye helper.

    Usage:
        @router.delete("/user/{id}")
        def delete_user(
            _: User = Depends(require_role(UserRole.ADMIN))
        ):
            ...
    """
    async def role_checker(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Required role: {[r.value for r in roles]}"
            )
        return current_user
    return role_checker
```

> ### 📖 `HTTPBearer` kya hai aur kyu use kiya?
>
> **Kya hai:** `HTTPBearer` FastAPI ka built-in security helper hai jo **Authorization header** se Bearer token automatically extract karta hai.
>
> **Request header kuch aisa hoti hai:**
> ```
> GET /api/auth/me HTTP/1.1
> Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIi...
> ```
>
> `HTTPBearer()` ye `Authorization` header check karta hai aur `Bearer ` prefix hata ke sirf token string deta hai.
>
> **Agar header nahi hai?** Automatically `401 Unauthorized` return karta hai — hume manually check nahi karna.

> 💡 **`require_role(*roles)` kya karta hai?**
> Ye ek **function jo function return kare** hai (higher-order function). Jab tum likhte ho:
> ```python
> Depends(require_role(UserRole.ADMIN))
> ```
> Pehle `require_role(UserRole.ADMIN)` call hota hai → `role_checker` function return hota hai → FastAPI `role_checker` ko dependency ki tarah use karta hai.

---

#### `Task 3` — 🧪 Test with a protected route

**`backend/app/routers/auth.py`** mein ek test route banao:

```python
from fastapi import APIRouter, Depends
from app.models.user import User
from app.utils.dependencies import get_current_user
from app.schemas.user import UserResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(
    current_user: User = Depends(get_current_user)
):
    """
    Logged in user ki info return karta hai.
    Token valid hona chahiye Authorization header mein.
    """
    return current_user
```

**`backend/app/main.py`** mein router register karo:

```python
from app.routers.auth import router as auth_router
app.include_router(auth_router, prefix="/api")
```

---

> ### 🏁 Expected Output — Day 14
> ```
> ✅ app/repositories/user_repository.py created
> ✅ app/utils/dependencies.py created — get_current_user + require_role
> ✅ app/routers/auth.py created — /api/auth/me route
> ✅ Swagger UI mein /api/auth/me visible (with lock icon 🔒)
> ✅ Without token → 401 Unauthorized
> ✅ With invalid token → 401 Unauthorized
> ```
> 🎯 **Goal Achieved:** `get_current_user` dependency — har protected route pe user inject hoga

---
---

## 🌐 Day 15: Google OAuth Setup (Google Cloud Console)

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend + Config` |
| 🎯 **Goal** | Google OAuth credentials ready, project configured in Google Cloud |

---

> ### 📖 OAuth 2.0 kya hai aur kyu use kiya?
>
> **Kya hai:** OAuth 2.0 ek **authorization protocol** hai. Iska matlab hai: user apni Google (ya GitHub, Facebook) identity use karke tumhari app mein login kar sakta hai — **bina naya password banaye**.
>
> **Flow (simple version):**
> ```
> 1. User clicks "Login with Google"
> 2. Humari app user ko Google ke login page pe redirect karti hai
> 3. User Google pe login karta hai (Google ka page, not ours)
> 4. Google ek "code" ke saath user ko wapas redirect karta hai
> 5. Humari app wo "code" Google ko deti hai → Google access token deta hai
> 6. Hum access token se user ki info (email, name, photo) Google se lete hain
> 7. Hum apna JWT token banate hain aur client ko dete hain
> ```
>
> **Kyu Google OAuth?**
> - User ko password yaad nahi rakhna
> - Email verification automatic (Google ne already verify ki hai)
> - Security Google handle karta hai
> - Cricket auction jaisi app ke liye perfect (social login preferred)

---

### ✅ Tasks

---

#### `Task 1` — ☁️ Google Cloud Console setup

> 💡 **Google Cloud Console kya hai?**
> Google ka developer dashboard hai jahan tum Google ke APIs use karne ke liye register karte ho. Jaise tum Google Maps, Gmail, OAuth — sab ke liye credentials yahan se milte hain.

**Step-by-step:**

```
1. Browser mein jao: https://console.cloud.google.com

2. New Project banao:
   - Top bar mein "Select a project" → "New Project"
   - Name: "cricket-auction-platform"
   - Create karo

3. OAuth Consent Screen setup:
   - Left menu → APIs & Services → OAuth consent screen
   - User Type: External (testing ke liye)
   - App name: "Cricket Auction Platform"
   - User support email: apna email
   - Developer contact: apna email
   - Save & Continue (baaki sab skip karo for now)

4. Credentials banao:
   - Left menu → APIs & Services → Credentials
   - + CREATE CREDENTIALS → OAuth client ID
   - Application type: Web application
   - Name: "Cricket Auction Web Client"

5. Authorized redirect URIs add karo:
   - http://localhost:8000/api/auth/google/callback  ← development
   (Production ke liye baad mein add karenge)

6. Create karo → Client ID aur Client Secret milenge → Copy karo!
```

---

#### `Task 2` — 🔑 Update `.env` with Google credentials

```bash
# backend/.env mein add karo:
GOOGLE_CLIENT_ID=your-client-id-from-google.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-client-secret-from-google
GOOGLE_REDIRECT_URI=http://localhost:8000/api/auth/google/callback
FRONTEND_URL=http://localhost:5173
```

> ⚠️ **`.env` file NEVER commit karo!** Client ID aur Secret gitignore mein hai (Day 10 se). `.env.example` mein placeholder add karo:
> ```bash
> # backend/.env.example mein add karo:
> GOOGLE_CLIENT_ID=your-google-client-id-here
> GOOGLE_CLIENT_SECRET=your-google-client-secret-here
> GOOGLE_REDIRECT_URI=http://localhost:8000/api/auth/google/callback
> FRONTEND_URL=http://localhost:5173
> ```

---

#### `Task 3` — ⚙️ Update `config.py`

```python
# backend/app/config.py
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080

    # Google OAuth — ye add karo
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str
    FRONTEND_URL: str = "http://localhost:5173"

    class Config:
        env_file = ".env"

settings = Settings()
```

---

> ### 🏁 Expected Output — Day 15
> ```
> ✅ Google Cloud project created: "cricket-auction-platform"
> ✅ OAuth consent screen configured
> ✅ OAuth credentials created — Client ID + Secret copied
> ✅ Redirect URI added: http://localhost:8000/api/auth/google/callback
> ✅ .env updated with Google credentials
> ✅ .env.example updated with placeholders
> ✅ config.py updated — no errors on app startup
> ```
> 🎯 **Goal Achieved:** Google OAuth credentials ready, project configured in Google Cloud

---
---

## 🔧 Day 16: Authlib Setup (OAuth Client)

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | `authlib` configure karo — Google OAuth redirect URL generate kar sake |

---

> ### 📖 `authlib` kya hai aur kyu use kiya?
>
> **Kya hai:** `authlib` ek Python library hai jo **OAuth 1.0, OAuth 2.0, OpenID Connect** implement karna easy banati hai.
>
> **`python-jose` aur `authlib` mein fark:**
> | | `python-jose` | `authlib` |
> |--|-------------|-----------|
> | Kya karta hai | JWT encode/decode | Full OAuth 2.0 flow |
> | Use case | Token banao/verify karo | Google se redirect, code exchange, user info |
> | Hum use karte hain | Day 13 — JWT tokens ke liye | Day 16-19 — Google OAuth flow ke liye |
>
> **`httpx` kyu?** Google ke API ko HTTP requests bhejne ke liye (access token ke badle user info maangne ke liye). `requests` library bhi kaam karti hai but `httpx` async support deta hai jo FastAPI ke saath better hai.

---

### ✅ Tasks

---

#### `Task 1` — 📦 Install authlib and httpx

```bash
cd backend
pip install authlib httpx
pip freeze > requirements.txt
```

---

#### `Task 2` — 🔧 Create OAuth utility

**`backend/app/utils/oauth.py`** banao:

```python
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config as StarletteConfig
from app.config import settings


# Starlette config object banao (authlib isko expect karta hai)
starlette_config = StarletteConfig(
    environ={
        "GOOGLE_CLIENT_ID": settings.GOOGLE_CLIENT_ID,
        "GOOGLE_CLIENT_SECRET": settings.GOOGLE_CLIENT_SECRET,
    }
)

# OAuth instance banao
oauth = OAuth(starlette_config)

# Google OAuth register karo
oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    # ↑ Google ka OpenID configuration URL — authlib yahan se sab endpoints discover karta hai
    #   (authorization URL, token URL, userinfo URL sab yahan se milta hai automatically)
    client_kwargs={
        "scope": "openid email profile",
        # scope matlab: Google se kya info maangte hain
        # openid  → basic authentication
        # email   → user ka email address
        # profile → name, photo, etc.
    },
)
```

> 💡 **`openid-configuration` URL kya hai?**
> Google ka ek public JSON file hai jisme unke OAuth server ke saare endpoints listed hain:
> ```json
> {
>   "authorization_endpoint": "https://accounts.google.com/o/oauth2/v2/auth",
>   "token_endpoint": "https://oauth2.googleapis.com/token",
>   "userinfo_endpoint": "https://openidconnect.googleapis.com/v1/userinfo",
>   ...
> }
> ```
> `authlib` is URL se automatically sab discover kar leta hai — hume manually hardcode nahi karna.

> 💡 **`scope` kya hai?**
> OAuth mein scope = "permission request". Jab user Google login screen dekhta hai, wahan likha hota hai "This app wants to access: your email, your profile". Scope se ye decide hota hai.

---

#### `Task 3` — 🔗 Register OAuth in main app

**`backend/app/main.py`** update karo:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware  # ← add karo
from app.config import settings
from app.routers.auth import router as auth_router

app = FastAPI(title="Cricket Auction API")

# Session middleware — OAuth flow ke liye zaroori hai
# authlib state parameter (CSRF protection) session mein store karta hai
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api")

@app.get("/health")
async def health():
    return {"status": "healthy"}
```

> 💡 **`SessionMiddleware` kyu?**
> OAuth mein ek **CSRF attack prevention** mechanism hai: server ek random `state` parameter banata hai, Google ke paas bhejta hai, aur jab callback aata hai to verify karta hai ki same `state` wapas aaya.
> Ye `state` server-side session mein store hona chahiye — `SessionMiddleware` ye session provide karta hai.

---

> ### 🏁 Expected Output — Day 16
> ```
> ✅ authlib + httpx installed
> ✅ app/utils/oauth.py created — Google OAuth registered
> ✅ SessionMiddleware added in main.py
> ✅ uvicorn restart → no errors
> ✅ Google OAuth config loading from .env
> ```
> 🎯 **Goal Achieved:** `authlib` configure karo — Google OAuth redirect URL generate kar sake

---
---

## 🚀 Day 17: Google OAuth Routes (Login Redirect)

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | `/api/auth/google/login` route — browser ko Google ke login page pe redirect kare |

---

### ✅ Tasks

---

#### `Task 1` — 🛣️ Add Google login routes

**`backend/app/routers/auth.py`** update karo:

```python
from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from app.models.user import User
from app.utils.dependencies import get_current_user
from app.utils.oauth import oauth
from app.schemas.user import UserResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(
    current_user: User = Depends(get_current_user)
):
    """Logged in user ki info."""
    return current_user


@router.get("/google/login")
async def google_login(request: Request):
    """
    User ko Google login page pe redirect karo.

    Flow:
    1. Client browser mein /api/auth/google/login kholega
    2. Ye route Google ka authorization URL generate karta hai
    3. User Google pe redirect ho jaata hai
    4. Google login ke baad /api/auth/google/callback pe wapas aata hai
    """
    redirect_uri = request.url_for("google_callback")
    # ↑ automatically http://localhost:8000/api/auth/google/callback banata hai

    return await oauth.google.authorize_redirect(request, redirect_uri)
    # ↑ authlib Google ka authorization URL banata hai + state set karta hai
    #   aur RedirectResponse return karta hai


@router.get("/google/callback", name="google_callback")
async def google_callback(request: Request):
    """
    Google callback — placeholder for now.
    Day 18 mein implement karenge.
    """
    # Abhi ke liye sirf confirm karo ki Google wapas aa raha hai
    return {"message": "Google callback received — Day 18 mein implement karenge"}
```

> 💡 **`request.url_for("google_callback")` kya karta hai?**
> FastAPI/Starlette ka `url_for` function route ka naam le ke us route ka URL automatically generate karta hai.
> `name="google_callback"` → route ka naam hai (decorator mein define kiya)
> Ye hardcoded URL se better hai kyunki development vs production URL automatically change ho jaata hai.

> 💡 **`await` kyu lagaya?**
> `oauth.google.authorize_redirect(...)` ek async function hai (HTTP request Google ke server pe bhi jaata hai discovery ke liye).
> FastAPI async functions ke andar `await` lagana zaroori hai — warna function actually execute nahi hoga.

---

#### `Task 2` — 🧪 Test the login redirect

```bash
# Backend chalu hai to:
# Browser mein ye URL kholo:
http://localhost:8000/api/auth/google/login

# Expected: Browser automatically Google login page pe redirect ho jaayega!
# Google login page dikhega with "Cricket Auction Platform wants access to:"
```

> ⚠️ **Agar "This app isn't verified" warning aaye:**
> Development mode mein Google ye warning deta hai. "Advanced" click karo → "Go to cricket-auction-platform (unsafe)" → normal hai development ke liye.

---

> ### 🏁 Expected Output — Day 17
> ```
> ✅ /api/auth/google/login route added
> ✅ /api/auth/google/callback route (placeholder) added
> ✅ Browser → http://localhost:8000/api/auth/google/login → Google login page!
> ✅ Google login ke baad → callback URL pe wapas aata hai
> ✅ {"message": "Google callback received..."} dikhta hai
> ```
> 🎯 **Goal Achieved:** `/api/auth/google/login` route — browser Google login page pe redirect ho raha hai

---
---

## 🔄 Day 18: Google Callback (Token Exchange)

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | Google se user info fetch karo — email, name, photo |

---

### ✅ Tasks

---

#### `Task 1` — 📋 Google user info schema

**`backend/app/schemas/user.py`** mein add karo (file ke end mein):

```python
class GoogleUserInfo(BaseModel):
    """
    Google se milne wali user info ka schema.
    Google yahi fields return karta hai userinfo endpoint se.
    """
    sub: str          # Google ka unique user ID (subject)
    email: EmailStr
    name: str
    picture: Optional[str] = None
    email_verified: bool = False
```

---

#### `Task 2` — 🔄 Implement callback route

**`backend/app/routers/auth.py`** mein callback route update karo:

```python
import httpx
from fastapi import APIRouter, Depends, Request, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.utils.dependencies import get_current_user
from app.utils.oauth import oauth
from app.utils.jwt import create_access_token
from app.schemas.user import UserResponse, GoogleUserInfo
from app.repositories.user_repository import UserRepository

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/google/login")
async def google_login(request: Request):
    redirect_uri = request.url_for("google_callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/google/callback", name="google_callback")
async def google_callback(request: Request, db: Session = Depends(get_db)):
    """
    Google login ke baad Google yahan redirect karta hai.

    Steps:
    1. Google ka authorization code → access token mein exchange karo
    2. Access token se Google userinfo endpoint pe jaao → user info lo
    3. User info validate karo
    4. DB mein user dhundo ya banao (Day 19 mein)
    5. Apna JWT token banao
    6. Frontend pe redirect karo with token
    """
    try:
        # Step 1: Code → Token exchange (authlib automatically karta hai)
        token_data = await oauth.google.authorize_access_token(request)
        # token_data mein: access_token, id_token, expires_in etc.

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"OAuth error: {str(e)}"
        )

    # Step 2: User info fetch karo Google se
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://openidconnect.googleapis.com/v1/userinfo",
                headers={"Authorization": f"Bearer {token_data['access_token']}"}
            )
            response.raise_for_status()
            raw_user_info = response.json()

    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Failed to fetch user info from Google"
        )

    # Step 3: Validate
    google_user = GoogleUserInfo(**raw_user_info)

    if not google_user.email_verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Google email not verified"
        )

    # Step 4 + 5: User upsert + JWT token (Day 19 mein implement karenge)
    # Abhi ke liye sirf user info return karo (testing ke liye)
    return {
        "google_user": google_user.model_dump(),
        "message": "Day 19 mein JWT return karenge"
    }
```

> ### 📖 `httpx` kya hai aur kyu use kiya?
>
> **Kya hai:** `httpx` ek modern Python HTTP client library hai. `requests` library ka async-capable replacement hai.
>
> **`requests` vs `httpx`:**
> | | `requests` | `httpx` |
> |--|-----------|---------|
> | Async | ❌ No | ✅ Yes (`async with httpx.AsyncClient()`) |
> | FastAPI ke saath | ⚠️ Works but blocks event loop | ✅ Native async |
> | API | Same style | Same style (familiar) |
>
> **`async with httpx.AsyncClient()` kya hai?**
> Ek async context manager hai — HTTP connection open karta hai, kaam karta hai, phir properly close karta hai.
> `async with` → `await __aenter__()` aur `await __aexit__()` automatically call hota hai.

> 💡 **`response.raise_for_status()` kya karta hai?**
> Agar HTTP response 4xx ya 5xx status code hai → automatically exception raise karta hai.
> 200-299 → koi error nahi.
> Ye manual `if response.status_code != 200` check se better hai.

---

> ### 🏁 Expected Output — Day 18
> ```
> ✅ GoogleUserInfo schema added
> ✅ Callback route — Google se access token exchange working
> ✅ userinfo endpoint se email, name, picture fetch ho raha hai
> ✅ email_verified check implemented
> ✅ Browser flow: Login → Google → Callback → JSON with user info
> ```
> 🎯 **Goal Achieved:** Google se user info fetch karo — email, name, photo

---
---

## 💾 Day 19: Auto User Creation (DB Upsert + JWT Return)

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | Google callback pe user DB mein save ho, JWT token frontend pe jaaye |

---

> ### 📖 Upsert kya hai?
>
> **Kya hai:** "Upsert" = **Update + Insert** — pehle check karo user exist karta hai ya nahi:
> - Exist karta hai → **Update** (latest info sync karo)
> - Exist nahi karta → **Insert** (naya banao)
>
> **Kyu zaroori hai:**
> Agar user pehle kabhi login kiya hai → DB mein hai → dobara user banane ki zaroorat nahi, existing user use karo.
> Agar pehli baar login → naya user banao.
>
> ```python
> # Upsert logic:
> user = db.get_by_google_id(google_id)
> if user:
>     user = db.update(user, full_name=..., picture=...)  # update
> else:
>     user = db.create(email=..., full_name=..., ...)      # insert
> ```

---

### ✅ Tasks

---

#### `Task 1` — 🔧 Create Auth Service

**`backend/app/services/auth_service.py`** banao:

```python
from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import GoogleUserInfo
from app.utils.jwt import create_access_token


class AuthService:
    """
    Authentication business logic yahan hai.
    Repository sirf DB queries karta hai — logic yahan hoti hai.
    """

    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)

    def get_or_create_google_user(self, google_user: GoogleUserInfo) -> User:
        """
        Google user info se DB mein user dhundo ya banao (upsert).

        Steps:
        1. Google ID se dhundo (returning user)
        2. Nahi mila → email se dhundo (existing user with different login method)
        3. Phir bhi nahi mila → naya user banao
        4. Profile info sync karo (name, photo update ho sakti hai)
        """
        # Step 1: Google ID se dhundo
        user = self.user_repo.get_by_google_id(google_user.sub)

        if user:
            # Returning user — profile sync karo
            user = self.user_repo.update(
                user,
                full_name=google_user.name,
                profile_picture=google_user.picture,
            )
            return user

        # Step 2: Email se dhundo (same email, different method)
        user = self.user_repo.get_by_email(google_user.email)

        if user:
            # Existing user — google_id link karo
            user = self.user_repo.update(
                user,
                google_id=google_user.sub,
                full_name=google_user.name,
                profile_picture=google_user.picture,
            )
            return user

        # Step 3: Bilkul naya user
        user = self.user_repo.create(
            email=google_user.email,
            full_name=google_user.name,
            google_id=google_user.sub,
            profile_picture=google_user.picture,
        )
        return user

    def create_token_for_user(self, user: User) -> str:
        """User ke liye JWT access token banao."""
        return create_access_token(
            user_id=str(user.id),
            email=user.email,
            role=user.role.value,
        )
```

---

#### `Task 2` — 🔄 Complete callback route

**`backend/app/routers/auth.py`** mein callback route update karo:

```python
@router.get("/google/callback", name="google_callback")
async def google_callback(request: Request, db: Session = Depends(get_db)):
    from app.config import settings

    try:
        token_data = await oauth.google.authorize_access_token(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"OAuth error: {str(e)}")

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://openidconnect.googleapis.com/v1/userinfo",
                headers={"Authorization": f"Bearer {token_data['access_token']}"}
            )
            response.raise_for_status()
            raw_user_info = response.json()
    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail="Failed to fetch Google user info")

    google_user = GoogleUserInfo(**raw_user_info)

    if not google_user.email_verified:
        raise HTTPException(status_code=400, detail="Google email not verified")

    # Auth service — user upsert + token generate
    auth_service = AuthService(db)
    user = auth_service.get_or_create_google_user(google_user)
    jwt_token = auth_service.create_token_for_user(user)

    # Frontend pe redirect karo with token
    # Frontend URL: http://localhost:5173/auth/callback?token=xxx
    frontend_callback = f"{settings.FRONTEND_URL}/auth/callback?token={jwt_token}"
    return RedirectResponse(url=frontend_callback)
```

> 💡 **Token ko query param se kyun bhejte hain?**
> Google ka callback server-side (backend) hit karta hai — browser directly nahi jaata. Isliye hum backend se frontend pe redirect karte hain aur token URL mein attach karte hain.
> Frontend ye URL parameter se token read karke localStorage mein save karega (Day 24 mein).
>
> **Production mein better approach:** Token ko URL mein nahi, ek short-lived one-time code mein exchange karo — security ke liye. Abhi ke liye ye approach development mein theek hai.

---

> ### 🏁 Expected Output — Day 19
> ```
> ✅ app/services/auth_service.py created — get_or_create_google_user()
> ✅ Callback route complete — Google login → user DB mein save → JWT token
> ✅ Browser flow: Login with Google → JWT token milta hai
> ✅ DBeaver mein users table mein naya user visible
> ✅ Token decode karo (jwt.io) → email, role, sub sab dikh rahe hain
> ```
> 🎯 **Goal Achieved:** Google callback pe user DB mein save ho, JWT token frontend pe jaaye

---
---

## 🛡️ Day 20: Auth Middleware & Protected Routes Test

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | End-to-end auth flow test karo, Swagger mein JWT auth setup karo |

---

### ✅ Tasks

---

#### `Task 1` — 🔒 Swagger mein JWT auth setup karo

Abhi Swagger UI mein JWT token test karna easy nahi hai. Swagger ko batao ki Bearer token accept kare:

**`backend/app/main.py`** update karo:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from fastapi.openapi.utils import get_openapi
from starlette.middleware.sessions import SessionMiddleware
from app.config import settings
from app.routers.auth import router as auth_router

app = FastAPI(
    title="Cricket Auction API",
    version="1.0.0",
    description="Cricket Auction Platform — Phase 2: Authentication"
)

app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api")

@app.get("/health")
async def health():
    return {"status": "healthy"}


# Swagger mein "Authorize" button ke liye — JWT Bearer token input field deta hai
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
```

> 💡 **`custom_openapi()` kya karta hai?**
> FastAPI ka Swagger UI automatically generate hota hai OpenAPI spec se.
> Hum us spec mein `BearerAuth` security scheme add kar rahe hain taaki Swagger UI mein top-right mein "Authorize 🔒" button aaye — jahan tum JWT token paste kar sako aur phir protected routes test kar sako.

---

#### `Task 2` — 🧪 End-to-end auth flow test

```bash
# 1. Backend start karo
cd backend && uvicorn app.main:app --reload

# 2. Browser mein Google login:
http://localhost:8000/api/auth/google/login
# → Google login → callback → Frontend redirect → URL mein token dikhega

# 3. Token copy karo URL se:
# http://localhost:5173/auth/callback?token=eyJhbGc...

# 4. Swagger pe jaao:
http://localhost:8000/docs
# → "Authorize" button click karo
# → Token paste karo (without "Bearer " prefix)

# 5. /api/auth/me route test karo:
# → Execute karo → 200 OK → User info milegi
```

---

#### `Task 3` — 📝 Full auth flow verify karo

```python
# Quick test script — backend/test_auth.py (temporary file)
import requests

BASE_URL = "http://localhost:8000"

# Health check
r = requests.get(f"{BASE_URL}/health")
print("Health:", r.json())   # {"status": "healthy"}

# Protected route without token
r = requests.get(f"{BASE_URL}/api/auth/me")
print("No token:", r.status_code)   # 403 (HTTPBearer returns 403 if no header)

# Protected route with fake token
r = requests.get(
    f"{BASE_URL}/api/auth/me",
    headers={"Authorization": "Bearer fake_token"}
)
print("Fake token:", r.status_code)   # 401 Unauthorized
```

---

> ### 🏁 Expected Output — Day 20
> ```
> ✅ Swagger UI mein "Authorize 🔒" button visible
> ✅ JWT token paste karke /api/auth/me → 200 + User info
> ✅ Bina token → 403 Forbidden
> ✅ Fake/expired token → 401 Unauthorized
> ✅ Google login flow end-to-end: Login → DB mein user → JWT token ✓
> ✅ DBeaver mein users table — Google se aaya user stored hai
> ✅ Phase 2 Backend auth COMPLETE! 🎉
> ```
> 🎯 **Goal Achieved:** End-to-end auth flow test karo, Swagger mein JWT auth setup karo

---
---

## 🏆 Phase 2 — Days 11–20 Summary

| Day | 🎯 Topic | 🔧 Type | Key Libraries / Concepts |
|-----|----------|---------|--------------------------|
| Day 11 | User Model | Backend | `sqlalchemy`, `Enum`, `passlib[bcrypt]`, migration |
| Day 12 | User Schemas | Backend | `Pydantic`, `EmailStr`, `model_config`, `from_attributes` |
| Day 13 | JWT Basics | Backend | `python-jose`, `create_access_token`, `SECRET_KEY` |
| Day 14 | JWT Token Flow | Backend | `get_current_user`, `HTTPBearer`, `require_role`, `Depends` |
| Day 15 | Google OAuth Setup | Config | Google Cloud Console, credentials, redirect URI |
| Day 16 | Authlib Setup | Backend | `authlib`, `httpx`, `SessionMiddleware`, OAuth scope |
| Day 17 | Google OAuth Routes | Backend | `authorize_redirect`, `url_for`, `await`, redirect |
| Day 18 | Google Callback | Backend | Token exchange, `httpx.AsyncClient`, `raise_for_status` |
| Day 19 | Auto User Creation | Backend | Upsert pattern, `AuthService`, JWT + redirect |
| Day 20 | Auth Middleware Test | Backend | Swagger BearerAuth, end-to-end flow verification |

---

> ### 📚 New Libraries Added — Days 11–20
>
> | Library | Install Command | Kya Karta Hai |
> |---------|----------------|---------------|
> | `passlib[bcrypt]` | `pip install passlib[bcrypt]` | Password hashing (bcrypt algorithm) |
> | `python-jose[cryptography]` | `pip install "python-jose[cryptography]"` | JWT encode/decode |
> | `authlib` | `pip install authlib` | Full OAuth 2.0 flow (Google login) |
> | `httpx` | `pip install httpx` | Async HTTP client (Google API calls) |

---

> ## 🔜 Next Up: Phase 2 Days 21–25 — Frontend Auth
>
> | Day | Topic | Key Concepts |
> |-----|-------|-------------|
> | Day 21 | Protected Routes (more) | Admin-only routes, role checking |
> | Day 22 | Login Page UI | React + Shadcn Button, Google sign-in button |
> | Day 23 | Auth Store (Zustand) | State management, token persistence |
> | Day 24 | OAuth Integration FE | Frontend redirect + token save |
> | Day 25 | Protected Routes FE | React Router, ProtectedRoute component |

---

---
---

## 🛡️ Day 21: More Protected Routes (Admin + Role-based)

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | Admin-only routes, role-based API access, user management endpoints |

---

> ### 📖 RBAC (Role-Based Access Control) kya hai?
>
> **Kya hai:** RBAC = ek security pattern jisme **user ke role ke hisaab se** decide hota hai ki wo kya kar sakta hai.
>
> **Hamare 3 roles:**
> ```
> VIEWER     → sirf read karo (GET)
> TEAM_OWNER → apni team manage karo (GET + POST/PUT apni team)
> ADMIN      → sab kuch (GET + POST + PUT + DELETE — kisi bhi user/team)
> ```
>
> **Kyu zaroori hai:**
> Bina RBAC ke koi bhi user kisi bhi aur ka data delete kar sakta hai. Real app mein ye critical hai.

---

### ✅ Tasks

---

#### `Task 1` — 👑 Admin user management routes

**`backend/app/routers/admin.py`** banao:

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User, UserRole
from app.schemas.user import UserResponse
from app.utils.dependencies import require_role
from app.repositories.user_repository import UserRepository
from typing import List

router = APIRouter(prefix="/admin", tags=["Admin"])

# Shortcut — sirf ADMIN role wale access kar sakte hain
AdminOnly = Depends(require_role(UserRole.ADMIN))


@router.get("/users", response_model=List[UserResponse])
async def list_all_users(
    db: Session = Depends(get_db),
    _: User = AdminOnly    # sirf admin
):
    """Saare users ki list — sirf admin dekh sakta hai."""
    repo = UserRepository(db)
    return repo.get_all()


@router.put("/users/{user_id}/role", response_model=UserResponse)
async def change_user_role(
    user_id: str,
    role: UserRole,
    db: Session = Depends(get_db),
    _: User = AdminOnly
):
    """Kisi bhi user ka role change karo — sirf admin."""
    repo = UserRepository(db)
    user = repo.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return repo.update(user, role=role)


@router.put("/users/{user_id}/deactivate", response_model=UserResponse)
async def deactivate_user(
    user_id: str,
    db: Session = Depends(get_db),
    current_admin: User = AdminOnly
):
    """User ko deactivate karo (ban)."""
    if str(current_admin.id) == user_id:
        raise HTTPException(status_code=400, detail="Apne aap ko deactivate nahi kar sakte")
    repo = UserRepository(db)
    user = repo.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return repo.update(user, is_active=False)
```

**`UserRepository`** mein `get_all` method add karo:

```python
# backend/app/repositories/user_repository.py mein add karo:
def get_all(self, skip: int = 0, limit: int = 100) -> list[User]:
    """Saare users fetch karo (pagination ke saath)."""
    return self.db.query(User).offset(skip).limit(limit).all()
```

> 💡 **`_: User = AdminOnly` — underscore kyu?**
> `_` ek convention hai Python mein — "ye variable mujhe result mein nahi chahiye, sirf side effect chahiye" (dependency run ho, role check ho).
> Agar current admin ki info chahiye hoti to likhte: `current_admin: User = AdminOnly`

---

#### `Task 2` — 📝 Register admin router

**`backend/app/main.py`** mein add karo:

```python
from app.routers.admin import router as admin_router
app.include_router(admin_router, prefix="/api")
```

---

#### `Task 3` — 🧪 Test role-based access

```bash
# 1. Pehle apna user ADMIN banao (DBeaver se ya psql se):
UPDATE users SET role = 'admin' WHERE email = 'your-email@gmail.com';

# 2. Google se login karo → JWT token lo

# 3. Swagger → Authorize → token paste karo

# 4. Test karo:
# GET /api/admin/users → ADMIN = 200 ✅, VIEWER = 403 ❌
# PUT /api/admin/users/{id}/role → ADMIN only
```

---

> ### 🏁 Expected Output — Day 21
> ```
> ✅ app/routers/admin.py created
> ✅ GET /api/admin/users — admin only
> ✅ PUT /api/admin/users/{id}/role — role change
> ✅ PUT /api/admin/users/{id}/deactivate — ban user
> ✅ Viewer token se admin routes → 403 Forbidden ✓
> ✅ Admin token se admin routes → 200 OK ✓
> ```
> 🎯 **Goal Achieved:** Admin-only routes, role-based API access, user management endpoints

---
---

## 🎨 Day 22: Login Page UI (React + Shadcn)

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Frontend` |
| 🎯 **Goal** | Beautiful login page with Google sign-in button — Tailwind + Shadcn |

---

> ### 📖 React Router DOM kya hai aur kyu use kiya?
>
> **Kya hai:** `react-router-dom` React ka **client-side routing** library hai. Matlab browser URL change hone par page reload hue bina alag component render hoga.
>
> **Kyu zaroori hai:**
> ```
> Without Router:
>   localhost:5173/login  → always same component
>   localhost:5173/dashboard → same component (URL change ka koi effect nahi)
>
> With Router:
>   localhost:5173/login     → <LoginPage />
>   localhost:5173/dashboard → <DashboardPage />
>   localhost:5173/profile   → <ProfilePage />
> ```
>
> **`BrowserRouter` vs `HashRouter`:**
> | | `BrowserRouter` | `HashRouter` |
> |--|----------------|-------------|
> | URL format | `/dashboard` | `/#/dashboard` |
> | Server config | Server ko `/*` → `index.html` serve karna chahiye | Nahi chahiye |
> | Modern? | ✅ Yes | ❌ Old style |
> Hum `BrowserRouter` use karenge — Vite dev server already handle karta hai.

---

### ✅ Tasks

---

#### `Task 1` — 📦 Install React Router

```bash
cd frontend
npm install react-router-dom
npm install -D @types/react-router-dom   # TypeScript types
```

---

#### `Task 2` — 🗺️ Setup routes in App.tsx

**`frontend/src/App.tsx`** update karo:

```tsx
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import DashboardPage from "./pages/DashboardPage";
import AuthCallbackPage from "./pages/AuthCallbackPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Public routes */}
        <Route path="/login" element={<LoginPage />} />
        <Route path="/auth/callback" element={<AuthCallbackPage />} />

        {/* Default redirect */}
        <Route path="/" element={<Navigate to="/login" replace />} />

        {/* Protected routes — Day 25 mein add karenge */}
        <Route path="/dashboard" element={<DashboardPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

> 💡 **`<Navigate to="/login" replace />` kya karta hai?**
> `replace` prop ke saath ye browser history mein naya entry nahi banata — "replace" karta hai.
> Matlab user agar `/` pe tha aur `/login` pe gaya, Back button press karne pe `/` nahi jaayega (infinite redirect loop avoid hoga).

---

#### `Task 3` — 🎨 Create Login Page

**`frontend/src/pages/LoginPage.tsx`** banao:

```tsx
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";

export default function LoginPage() {
  const handleGoogleLogin = () => {
    // Backend ka Google login URL — ye backend pe redirect karega
    // Backend phir Google pe, Google phir callback pe, callback phir yahan
    window.location.href = "http://localhost:8000/api/auth/google/login";
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-900 to-slate-800">
      <Card className="w-full max-w-md shadow-2xl border-slate-700 bg-slate-800 text-white">
        <CardHeader className="text-center space-y-4 pb-2">
          {/* Logo / Icon */}
          <div className="mx-auto w-16 h-16 bg-emerald-500 rounded-2xl flex items-center justify-center text-3xl">
            🏏
          </div>

          <CardTitle className="text-3xl font-bold text-white">
            Cricket Auction
          </CardTitle>

          <CardDescription className="text-slate-400 text-base">
            Sign in to manage your team and participate in live auctions
          </CardDescription>
        </CardHeader>

        <CardContent className="pt-6 space-y-4">
          {/* Google Sign-in Button */}
          <Button
            onClick={handleGoogleLogin}
            variant="outline"
            className="w-full h-12 text-base font-medium border-slate-600 bg-white text-slate-800 hover:bg-slate-100 flex items-center gap-3"
          >
            {/* Google SVG Icon */}
            <svg className="w-5 h-5" viewBox="0 0 24 24">
              <path
                fill="#4285F4"
                d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
              />
              <path
                fill="#34A853"
                d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
              />
              <path
                fill="#FBBC05"
                d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"
              />
              <path
                fill="#EA4335"
                d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
              />
            </svg>
            Continue with Google
          </Button>

          {/* Divider */}
          <div className="relative">
            <div className="absolute inset-0 flex items-center">
              <div className="w-full border-t border-slate-700" />
            </div>
            <div className="relative flex justify-center text-xs text-slate-500">
              <span className="bg-slate-800 px-2">Secure login via Google OAuth 2.0</span>
            </div>
          </div>

          {/* Info text */}
          <p className="text-center text-xs text-slate-500">
            By signing in, you agree to our Terms of Service.
            <br />
            We never store your Google password.
          </p>
        </CardContent>
      </Card>
    </div>
  );
}
```

---

#### `Task 4` — 📄 Create placeholder pages

**`frontend/src/pages/DashboardPage.tsx`:**
```tsx
export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-slate-900 text-white flex items-center justify-center">
      <h1 className="text-3xl font-bold">🏏 Dashboard — Day 23+ mein complete karenge</h1>
    </div>
  );
}
```

**`frontend/src/pages/AuthCallbackPage.tsx`** (placeholder — Day 24 mein complete karenge):
```tsx
export default function AuthCallbackPage() {
  return (
    <div className="min-h-screen bg-slate-900 text-white flex items-center justify-center">
      <p className="text-slate-400">Processing login...</p>
    </div>
  );
}
```

---

> ### 🏁 Expected Output — Day 22
> ```
> ✅ react-router-dom installed
> ✅ App.tsx — BrowserRouter + Routes setup
> ✅ LoginPage.tsx — beautiful dark login card
> ✅ Google SVG icon button
> ✅ http://localhost:5173/login → Login page visible
> ✅ "Continue with Google" button → redirects to Google login
> ```
> 🎯 **Goal Achieved:** Beautiful login page with Google sign-in button — Tailwind + Shadcn

---
---

## 🐻 Day 23: Auth Store (Zustand)

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Frontend` |
| 🎯 **Goal** | Global auth state — token aur user info store karo, persist karo localStorage mein |

---

> ### 📖 Zustand kya hai aur kyu use kiya?
>
> **Kya hai:** Zustand ek **lightweight state management library** hai React ke liye.
>
> **State management kyu chahiye?**
> ```
> Problem:
>   LoginPage → token milta hai
>   DashboardPage → token chahiye
>   Navbar → user name dikhana hai
>   ProfilePage → user info chahiye
>
>   Bina state management ke: har component separately localStorage read kare → messy
>   With Zustand: ek central store → sab components us store se read karein
> ```
>
> **Zustand vs Redux:**
> | | Redux | Zustand |
> |--|-------|---------|
> | Setup | ❌ Boilerplate bahut zyada | ✅ Minimal — 10 lines mein store |
> | Bundle size | ❌ Large | ✅ Tiny (1KB) |
> | Learning curve | ❌ Actions, reducers, selectors | ✅ Simple object + functions |
> | React 18 | ✅ | ✅ |
>
> **Kyu Zustand aur Redux nahi:** Cricket auction app ke liye Zustand sufficient hai. Redux overkill hoga.
>
> **Kahan use hoga:** Auth token, user info, aur baad mein auction state (current bids, timer) ke liye.

---

### ✅ Tasks

---

#### `Task 1` — 📦 Install Zustand

```bash
cd frontend
npm install zustand
```

---

#### `Task 2` — 📝 Define TypeScript types

**`frontend/src/types/index.ts`** update karo:

```typescript
// User roles
export type UserRole = "admin" | "team_owner" | "viewer";

// User object (API se milne wala)
export interface User {
  id: string;
  email: string;
  full_name: string;
  role: UserRole;
  is_active: boolean;
  profile_picture: string | null;
  created_at: string;
  updated_at: string;
}

// Auth store ka shape
export interface AuthState {
  token: string | null;          // JWT token
  user: User | null;             // Logged in user
  isAuthenticated: boolean;      // Computed: token exists?
  isLoading: boolean;            // API call chal raha hai?

  // Actions
  setAuth: (token: string, user: User) => void;
  logout: () => void;
  setLoading: (loading: boolean) => void;
}
```

> 💡 **TypeScript `interface` vs `type` — kab kya?**
> - `interface` → object shapes ke liye (preferred for objects)
> - `type` → union types, primitives, computed types ke liye
> ```typescript
> type UserRole = "admin" | "team_owner" | "viewer";  // union → type
> interface User { id: string; ... }                   // object shape → interface
> ```
> Practically dono kaam karte hain — `interface` objects ke liye zyada readable hai.

---

#### `Task 3` — 🏪 Create Auth Store

**`frontend/src/store/authStore.ts`** banao:

```typescript
import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";
import { AuthState, User } from "../types";

// Zustand store with persist middleware
// persist → store ka data localStorage mein save hota hai
// Page refresh pe bhi login state rehta hai
export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      // ─── Initial State ──────────────────────────────────────
      token: null,
      user: null,
      isAuthenticated: false,
      isLoading: false,

      // ─── Actions ─────────────────────────────────────────────

      setAuth: (token: string, user: User) => {
        set({
          token,
          user,
          isAuthenticated: true,
          isLoading: false,
        });
      },

      logout: () => {
        set({
          token: null,
          user: null,
          isAuthenticated: false,
        });
        // localStorage se bhi hata do (persist middleware handle karega)
      },

      setLoading: (loading: boolean) => {
        set({ isLoading: loading });
      },
    }),
    {
      name: "cricket-auth",           // localStorage key
      storage: createJSONStorage(() => localStorage),
      // Sirf token aur user persist karo (isLoading nahi)
      partialize: (state) => ({
        token: state.token,
        user: state.user,
        isAuthenticated: state.isAuthenticated,
      }),
    }
  )
);
```

> 💡 **`persist` middleware kya karta hai?**
> ```
> Without persist:
>   Login → token store hua → Page refresh → Store reset → Logout ho gaya!
>
> With persist:
>   Login → token store hua → localStorage mein bhi save → Page refresh →
>   Store localStorage se reload → Still logged in ✅
> ```
>
> `partialize` se decide karte hain kya persist karna hai — `isLoading` persist nahi karna (page load pe loading false hona chahiye).

> 💡 **`create<AuthState>()(...)` — double parentheses kyu?**
> Zustand mein `persist` middleware use karne ke liye curried pattern hai.
> `create<AuthState>()` → TypeScript generic, phir `(persist(...))` → actual store definition.
> Ye TypeScript inference ke liye necessary hai.

---

#### `Task 4` — 🔧 Create API service (axios setup)

> ### 📖 `axios` kya hai aur kyu use kiya?
>
> **Kya hai:** `axios` ek popular HTTP client library hai JavaScript ke liye.
>
> **`fetch` vs `axios`:**
> | | `fetch` (built-in) | `axios` |
> |--|-------------------|---------|
> | Error handling | ❌ 4xx/5xx pe error nahi throw karta | ✅ Auto throw |
> | Request interceptors | ❌ Manual | ✅ Built-in |
> | JSON auto-parse | ❌ `.json()` manually | ✅ Automatic |
> | Request cancellation | ✅ AbortController | ✅ Built-in |
>
> **Interceptor kyu important hai:** Har request mein `Authorization: Bearer <token>` header automatically add ho jaye — manually har jagah likhne ki zaroorat nahi.

**Install karo:**
```bash
cd frontend
npm install axios
```

**`frontend/src/services/api.ts`** banao:

```typescript
import axios from "axios";
import { useAuthStore } from "../store/authStore";

// Base API instance
const api = axios.create({
  baseURL: "/api",     // Vite proxy use hoga: /api → http://localhost:8000/api
  headers: {
    "Content-Type": "application/json",
  },
});

// Request interceptor — har request se pehle token add karo
api.interceptors.request.use(
  (config) => {
    // Zustand store se token lo (localStorage se)
    const token = useAuthStore.getState().token;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor — 401 pe logout karo
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token expired ya invalid → logout
      useAuthStore.getState().logout();
      window.location.href = "/login";
    }
    return Promise.reject(error);
  }
);

export default api;
```

> 💡 **`interceptors.request.use(...)` kya hai?**
> Ye ek middleware hai axios mein. Har HTTP request **bhejne se pehle** ye function run hoga.
> ```
> Component → api.get("/users") → interceptor adds token → actual HTTP request → server
> ```
> Bina interceptor: har `api.get(...)` call mein manually token add karna padta.

---

> ### 🏁 Expected Output — Day 23
> ```
> ✅ zustand installed
> ✅ frontend/src/types/index.ts — User, AuthState interfaces
> ✅ frontend/src/store/authStore.ts — persist ke saath
> ✅ axios installed, frontend/src/services/api.ts created
> ✅ Request interceptor — auto token add
> ✅ Response interceptor — 401 pe auto logout
> ✅ Browser refresh ke baad bhi login state persist ✓
> ```
> 🎯 **Goal Achieved:** Global auth state — token aur user info store karo, persist karo localStorage mein

---
---

## 🔗 Day 24: OAuth Integration Frontend (Token Save)

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Frontend` |
| 🎯 **Goal** | Google callback token URL se read karo, store mein save karo, dashboard pe jaao |

---

### ✅ Tasks

---

#### `Task 1` — 📄 Complete AuthCallbackPage

**`frontend/src/pages/AuthCallbackPage.tsx`** update karo:

```tsx
import { useEffect } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import { useAuthStore } from "../store/authStore";
import api from "../services/api";
import { User } from "../types";

export default function AuthCallbackPage() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const { setAuth, logout } = useAuthStore();

  useEffect(() => {
    const handleCallback = async () => {
      // URL se token lo: /auth/callback?token=eyJhbGc...
      const token = searchParams.get("token");

      if (!token) {
        // Token nahi mila — login pe wapas
        navigate("/login", { replace: true });
        return;
      }

      try {
        // Token ko temporarily axios header mein set karo
        // Taaki /auth/me call kar sakein
        api.defaults.headers.common["Authorization"] = `Bearer ${token}`;

        // Backend se user info lo
        const response = await api.get<User>("/auth/me");
        const user = response.data;

        // Store mein save karo (localStorage persist bhi hoga)
        setAuth(token, user);

        // Dashboard pe redirect
        navigate("/dashboard", { replace: true });

      } catch (error) {
        // Token invalid ya API error → logout + login pe
        delete api.defaults.headers.common["Authorization"];
        logout();
        navigate("/login", { replace: true });
      }
    };

    handleCallback();
  }, []); // sirf mount pe ek baar run karo

  return (
    <div className="min-h-screen bg-slate-900 text-white flex items-center justify-center">
      <div className="text-center space-y-4">
        {/* Loading spinner */}
        <div className="w-12 h-12 border-4 border-emerald-500 border-t-transparent rounded-full animate-spin mx-auto" />
        <p className="text-slate-400">Logging you in...</p>
      </div>
    </div>
  );
}
```

> 💡 **`useSearchParams` kya hai?**
> React Router ka hook hai jo URL ke query parameters read karta hai.
> ```
> URL: /auth/callback?token=eyJhbGc...&foo=bar
>
> const [searchParams] = useSearchParams();
> searchParams.get("token")  → "eyJhbGc..."
> searchParams.get("foo")    → "bar"
> ```

> 💡 **`useEffect(() => {...}, [])` — empty array kyu?**
> Empty dependency array `[]` matlab: **sirf component mount pe ek baar run karo**.
> Bina `[]`: har render pe run hoga → infinite loop!
> `[]` ke saath: page load pe ek baar callback process hoga.

> 💡 **`navigate("/dashboard", { replace: true })` kyu `replace`?**
> `replace: true` → browser history mein `/auth/callback` replace hoga → user Back button press kare to `/login` pe jaayega, `/auth/callback` pe nahi (jo dobara token read karne ki koshish karega).

---

#### `Task 2` — 🧪 Complete auth flow test

```bash
# 1. Backend aur Frontend dono start karo:
# Terminal 1:
cd backend && uvicorn app.main:app --reload

# Terminal 2:
cd frontend && npm run dev

# 2. Browser mein:
http://localhost:5173/login
→ "Continue with Google" click karo
→ Google login karo
→ http://localhost:5173/auth/callback?token=eyJ... pe redirect hoga
→ AuthCallbackPage token read karega
→ /api/auth/me call → user info milegi
→ Store mein save hoga
→ http://localhost:5173/dashboard pe redirect

# 3. Refresh karo → still logged in (localStorage persist)

# 4. Browser DevTools → Application → Local Storage → "cricket-auth" key dekhega
```

---

> ### 🏁 Expected Output — Day 24
> ```
> ✅ AuthCallbackPage.tsx — token URL se read, /auth/me call, store save
> ✅ Loading spinner during callback processing
> ✅ Complete Google OAuth flow: Login → Google → Callback → Dashboard ✓
> ✅ Page refresh → still logged in (Zustand persist) ✓
> ✅ localStorage mein "cricket-auth" key visible ✓
> ✅ Invalid token → /login redirect ✓
> ```
> 🎯 **Goal Achieved:** Google callback token URL se read karo, store mein save karo, dashboard pe jaao

---
---

## 🔒 Day 25: Protected Routes (React Router)

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Frontend` |
| 🎯 **Goal** | `ProtectedRoute` component — bina login ke dashboard access nahi hoga |

---

### ✅ Tasks

---

#### `Task 1` — 🔐 Create ProtectedRoute component

**`frontend/src/components/ProtectedRoute.tsx`** banao:

```tsx
import { Navigate, Outlet } from "react-router-dom";
import { useAuthStore } from "../store/authStore";
import { UserRole } from "../types";

interface ProtectedRouteProps {
  requiredRole?: UserRole;   // Optional: specific role required
}

export default function ProtectedRoute({ requiredRole }: ProtectedRouteProps) {
  const { isAuthenticated, user } = useAuthStore();

  // 1. Logged in nahi hai → login pe bhejo
  if (!isAuthenticated || !user) {
    return <Navigate to="/login" replace />;
  }

  // 2. Role check (agar required role specify kiya hai)
  if (requiredRole && user.role !== requiredRole && user.role !== "admin") {
    return <Navigate to="/dashboard" replace />;
    // Note: admin har jagah ja sakta hai
  }

  // 3. Sab theek hai → child routes render karo
  return <Outlet />;
  // Outlet = nested routes ka placeholder (React Router v6)
}
```

> 💡 **`<Outlet />` kya hai?**
> React Router v6 mein jab tum routes nest karte ho, `Outlet` wo jagah hai jahan child route render hogi.
> ```tsx
> <Route element={<ProtectedRoute />}>           // parent
>   <Route path="/dashboard" element={<Dashboard />} />  // child → Outlet mein render
>   <Route path="/profile" element={<Profile />} />      // child → Outlet mein render
> </Route>
> ```

---

#### `Task 2` — 🗺️ Update App.tsx with protected routes

**`frontend/src/App.tsx`** update karo:

```tsx
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import ProtectedRoute from "./components/ProtectedRoute";
import LoginPage from "./pages/LoginPage";
import AuthCallbackPage from "./pages/AuthCallbackPage";
import DashboardPage from "./pages/DashboardPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* ─── Public Routes ────────────────────────── */}
        <Route path="/login" element={<LoginPage />} />
        <Route path="/auth/callback" element={<AuthCallbackPage />} />

        {/* ─── Protected Routes (login required) ────── */}
        <Route element={<ProtectedRoute />}>
          <Route path="/dashboard" element={<DashboardPage />} />
          {/* Day 26+ se more routes add honge */}
        </Route>

        {/* ─── Admin Only Routes ────────────────────── */}
        <Route element={<ProtectedRoute requiredRole="admin" />}>
          {/* Day 21+ admin pages yahan */}
        </Route>

        {/* ─── Default ──────────────────────────────── */}
        <Route path="/" element={<Navigate to="/dashboard" replace />} />
        <Route path="*" element={<Navigate to="/dashboard" replace />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

---

#### `Task 3` — 🧭 Navbar component banao (basic)

**`frontend/src/components/Navbar.tsx`** banao:

```tsx
import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { useAuthStore } from "../store/authStore";

export default function Navbar() {
  const { user, logout } = useAuthStore();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login", { replace: true });
  };

  return (
    <nav className="h-16 bg-slate-900 border-b border-slate-800 px-6 flex items-center justify-between">
      {/* Logo */}
      <div className="flex items-center gap-2">
        <span className="text-2xl">🏏</span>
        <span className="text-white font-bold text-lg">Cricket Auction</span>
      </div>

      {/* User info + logout */}
      {user && (
        <div className="flex items-center gap-4">
          {/* Profile picture */}
          {user.profile_picture && (
            <img
              src={user.profile_picture}
              alt={user.full_name}
              className="w-8 h-8 rounded-full border-2 border-emerald-500"
            />
          )}

          {/* Name + Role badge */}
          <div className="text-right hidden sm:block">
            <p className="text-white text-sm font-medium">{user.full_name}</p>
            <p className="text-emerald-400 text-xs capitalize">{user.role.replace("_", " ")}</p>
          </div>

          {/* Logout button */}
          <Button
            variant="outline"
            size="sm"
            onClick={handleLogout}
            className="border-slate-700 text-slate-300 hover:text-white hover:bg-slate-800"
          >
            Logout
          </Button>
        </div>
      )}
    </nav>
  );
}
```

**`frontend/src/pages/DashboardPage.tsx`** update karo:

```tsx
import Navbar from "../components/Navbar";
import { useAuthStore } from "../store/authStore";

export default function DashboardPage() {
  const { user } = useAuthStore();

  return (
    <div className="min-h-screen bg-slate-900">
      <Navbar />
      <main className="container mx-auto px-6 py-8">
        <div className="text-white">
          <h1 className="text-3xl font-bold mb-2">
            Welcome back, {user?.full_name?.split(" ")[0]}! 👋
          </h1>
          <p className="text-slate-400">
            Role: <span className="text-emerald-400 capitalize">{user?.role?.replace("_", " ")}</span>
          </p>

          {/* Placeholder cards — Day 26+ se real data */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8">
            {[
              { icon: "🏟️", title: "Auctions", count: "Coming Soon" },
              { icon: "👥", title: "Teams", count: "Coming Soon" },
              { icon: "🏃", title: "Players", count: "Coming Soon" },
            ].map((card) => (
              <div
                key={card.title}
                className="bg-slate-800 border border-slate-700 rounded-2xl p-6"
              >
                <div className="text-4xl mb-3">{card.icon}</div>
                <h3 className="text-white font-semibold text-lg">{card.title}</h3>
                <p className="text-slate-400 text-sm mt-1">{card.count}</p>
              </div>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
}
```

---

> ### 🏁 Expected Output — Day 25
> ```
> ✅ ProtectedRoute.tsx — auth + role check
> ✅ App.tsx — nested protected routes
> ✅ Navbar.tsx — user photo + name + role badge + logout
> ✅ DashboardPage.tsx — welcome message + placeholder cards
> ✅ Bina login ke /dashboard → /login redirect ✓
> ✅ Logout → /login + localStorage cleared ✓
> ✅ Phase 2 COMPLETE! 🎉 Full auth flow end-to-end working!
> ```
> 🎯 **Goal Achieved:** `ProtectedRoute` component — bina login ke dashboard access nahi hoga

---
---

## 🏆 Phase 2 — Days 21–25 Summary

| Day | 🎯 Topic | 🔧 Type | Key Libraries / Concepts |
|-----|----------|---------|--------------------------|
| Day 21 | Admin Routes | Backend | `require_role`, RBAC, admin-only endpoints |
| Day 22 | Login Page UI | Frontend | `react-router-dom`, `BrowserRouter`, Shadcn `Card`, `Button` |
| Day 23 | Auth Store | Frontend | `zustand`, `persist`, `axios` interceptors |
| Day 24 | OAuth Integration | Frontend | `useSearchParams`, token save, `useEffect` |
| Day 25 | Protected Routes | Frontend | `ProtectedRoute`, `Outlet`, `Navbar`, full flow |

---
---

# 🧩 Phase 3: Team & Player CRUD

### `Days 26 → 40` &nbsp;|&nbsp; Backend + Frontend — Team/Player management

---

## 🏟️ Day 26: Team Model (SQLAlchemy)

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | Team table with owner relationship, migration applied |

---

> ### 📖 SQLAlchemy Relationships kya hain?
>
> **Kya hai:** SQLAlchemy mein `relationship()` se ek model dusre model se link hota hai — jaise SQL ka `JOIN` but Python objects ke roop mein.
>
> **Hamare case mein:**
> ```
> User (1) ──────────── (many) Team
> Ek user ke paas      ek user ke paas
> sirf ek team ho      multiple teams ho
> sakti hai            sakti hain
> (team_owner)
> ```
>
> **`ForeignKey` vs `relationship`:**
> ```python
> # ForeignKey → database mein actual column (owner_id)
> owner_id = Column(UUID, ForeignKey("users.id"))
>
> # relationship → Python mein object access (team.owner → User object)
> owner = relationship("User", back_populates="teams")
> ```
> `ForeignKey` DB-level constraint hai. `relationship` Python-level convenience hai.

---

### ✅ Tasks

---

#### `Task 1` — 🗂️ Create Team model

**`backend/app/models/team.py`** banao:

```python
import uuid
from enum import Enum
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Enum as SAEnum, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class TeamStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    ELIMINATED = "eliminated"


class Team(BaseModel):
    __tablename__ = "teams"

    name = Column(String(100), unique=True, nullable=False, index=True)
    short_name = Column(String(10), nullable=False)   # e.g., "MI", "CSK"
    city = Column(String(100), nullable=True)
    logo_url = Column(String(500), nullable=True)
    description = Column(Text, nullable=True)

    # Budget fields
    total_budget = Column(Integer, default=1000, nullable=False)
    # Crores mein (e.g., 1000 = 100 crore purse)
    remaining_budget = Column(Integer, default=1000, nullable=False)

    status = Column(
        SAEnum(TeamStatus),
        default=TeamStatus.ACTIVE,
        nullable=False
    )

    # ─── Foreign Key (owner = team_owner user) ───────────────────────────────
    owner_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        # ondelete="SET NULL" → agar owner delete ho jaye to team null ho jaaye
        # (team delete mat ho — data preserve karo)
        nullable=True
    )

    # ─── Relationships ────────────────────────────────────────────────────────
    owner = relationship(
        "User",
        back_populates="teams",
        lazy="select"   # owner sirf jab explicitly access karo tab DB hit ho
    )

    players = relationship(
        "Player",
        back_populates="team",
        lazy="select"
    )
```

> 💡 **`ondelete="SET NULL"` kya karta hai?**
> Ye **referential integrity** rule hai database ke liye.
> Agar `users` table se koi user delete ho jaye aur us user ki teams hain to:
> - `ondelete="SET NULL"` → `owner_id` NULL ho jaayega (team exist karti rahegi)
> - `ondelete="CASCADE"` → Team bhi delete ho jaati (data loss!)
> - `ondelete="RESTRICT"` → User delete nahi hoga jab tak team hai (error)
> Humne SET NULL choose kiya taaki teams survive karein even if owner deletes account.

> 💡 **`lazy="select"` kya hai?**
> SQLAlchemy mein relationships "lazy" ya "eager" hoti hain:
> ```python
> # lazy="select" (default):
> team = db.query(Team).first()
> # team.owner → ab DB query hogi (sirf jab access karo)
>
> # lazy="joined":
> team = db.query(Team).first()
> # team.owner → already loaded (JOIN ke saath pehli query mein)
> ```
> `lazy="select"` better hai jab owner har time nahi chahiye.

---

#### `Task 2` — 🔗 Update User model with back_populates

**`backend/app/models/user.py`** mein `teams` relationship add karo:

```python
# User class ke andar, imports ke baad:
from sqlalchemy.orm import relationship

class User(BaseModel):
    # ... existing fields ...

    # Relationship — User ke saare teams
    teams = relationship(
        "Team",
        back_populates="owner",
        lazy="select"
    )
```

> 💡 **`back_populates` kya hai?**
> Dono sides pe relationship define karna padta hai:
> ```python
> # Team model:
> owner = relationship("User", back_populates="teams")
>
> # User model:
> teams = relationship("Team", back_populates="owner")
> ```
> `back_populates` dono ko link karta hai: `team.owner` aur `user.teams` — dono updated rehte hain.

---

#### `Task 3` — 🔃 Register model + Migration

**`backend/alembic/env.py`** mein add karo:
```python
from app.models.user import User
from app.models.team import Team   # ← add karo
```

```bash
cd backend
alembic revision --autogenerate -m "create teams table"
alembic upgrade head
```

---

> ### 🏁 Expected Output — Day 26
> ```
> ✅ app/models/team.py — Team model with TeamStatus enum
> ✅ User model updated — teams relationship
> ✅ ForeignKey: teams.owner_id → users.id
> ✅ Migration generated + applied
> ✅ DBeaver → teams table visible with all columns
> ✅ teams.owner_id → users.id foreign key constraint ✓
> ```
> 🎯 **Goal Achieved:** Team table with owner relationship, migration applied

---
---

## 📋 Day 27: Team Schemas (Pydantic)

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | Team request/response schemas with nested owner info |

---

### ✅ Tasks

---

#### `Task 1` — 📄 Create Team schemas

**`backend/app/schemas/team.py`** banao:

```python
from typing import Optional
from pydantic import BaseModel, Field
from app.models.team import TeamStatus
from app.schemas.user import UserResponse   # nested owner info ke liye


# ─── Base ─────────────────────────────────────────────────────────────────────
class TeamBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    short_name: str = Field(..., min_length=2, max_length=10)
    city: Optional[str] = Field(None, max_length=100)
    logo_url: Optional[str] = None
    description: Optional[str] = None
    total_budget: int = Field(default=1000, ge=100, le=10000)
    # ge=100 → minimum 100 crore budget, le=10000 → max 10000 crore


# ─── Create ───────────────────────────────────────────────────────────────────
class TeamCreate(TeamBase):
    pass
    # TeamBase se sab inherit ho gaya
    # owner_id route se milega (logged in user ka id)


# ─── Update ───────────────────────────────────────────────────────────────────
class TeamUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    short_name: Optional[str] = Field(None, min_length=2, max_length=10)
    city: Optional[str] = None
    logo_url: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TeamStatus] = None


# ─── Response ─────────────────────────────────────────────────────────────────
class TeamResponse(TeamBase):
    id: str
    remaining_budget: int
    status: TeamStatus
    owner_id: Optional[str] = None
    created_at: str
    updated_at: str

    model_config = {"from_attributes": True}


# ─── Response with Owner details (nested) ─────────────────────────────────────
class TeamWithOwner(TeamResponse):
    owner: Optional[UserResponse] = None
    # Nested object: team response ke saath owner ka full info
    # Example response:
    # {
    #   "id": "...", "name": "Mumbai Indians",
    #   "owner": { "id": "...", "email": "owner@gmail.com", ... }
    # }
```

> 💡 **`TeamWithOwner` vs `TeamResponse` kyu alag?**
> Har endpoint pe owner ki full info nahi chahiye (extra DB query + larger response).
> - `GET /teams` (list) → `TeamResponse` (owner_id only — fast)
> - `GET /teams/{id}` (detail) → `TeamWithOwner` (owner full info — one team)
> Ye "N+1 query problem" avoid karta hai.

---

> ### 🏁 Expected Output — Day 27
> ```
> ✅ app/schemas/team.py created
> ✅ TeamBase, TeamCreate, TeamUpdate, TeamResponse, TeamWithOwner
> ✅ Field validations: budget range, name length
> ✅ Nested owner: TeamWithOwner → owner: UserResponse
> ```
> 🎯 **Goal Achieved:** Team request/response schemas with nested owner info

---
---

## 🏗️ Day 28: Team Repository + Service

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | Team ke CRUD operations — repository pattern + service layer |

---

### ✅ Tasks

---

#### `Task 1` — 🗃️ Create Team Repository

**`backend/app/repositories/team_repository.py`** banao:

```python
from typing import Optional, List
from sqlalchemy.orm import Session, joinedload
from app.models.team import Team, TeamStatus


class TeamRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(
        self,
        skip: int = 0,
        limit: int = 20,
        status: Optional[TeamStatus] = None
    ) -> List[Team]:
        """Saari teams — optional status filter ke saath."""
        query = self.db.query(Team)
        if status:
            query = query.filter(Team.status == status)
        return query.offset(skip).limit(limit).all()

    def get_by_id(self, team_id: str) -> Optional[Team]:
        """ID se team dhundo."""
        return self.db.query(Team).filter(Team.id == team_id).first()

    def get_by_id_with_owner(self, team_id: str) -> Optional[Team]:
        """Team + owner info — single DB query (JOIN)."""
        return (
            self.db.query(Team)
            .options(joinedload(Team.owner))
            # joinedload → JOIN ke saath owner bhi load karo (N+1 avoid)
            .filter(Team.id == team_id)
            .first()
        )

    def get_by_owner(self, owner_id: str) -> List[Team]:
        """Ek user ki saari teams."""
        return self.db.query(Team).filter(Team.owner_id == owner_id).all()

    def get_by_name(self, name: str) -> Optional[Team]:
        """Name se team dhundo (uniqueness check ke liye)."""
        return self.db.query(Team).filter(Team.name == name).first()

    def create(self, owner_id: str, **kwargs) -> Team:
        """Naya team banao."""
        team = Team(owner_id=owner_id, **kwargs)
        self.db.add(team)
        self.db.commit()
        self.db.refresh(team)
        return team

    def update(self, team: Team, **kwargs) -> Team:
        """Team update karo."""
        for key, value in kwargs.items():
            if hasattr(team, key) and value is not None:
                setattr(team, key, value)
        self.db.commit()
        self.db.refresh(team)
        return team

    def delete(self, team: Team) -> None:
        """Team delete karo."""
        self.db.delete(team)
        self.db.commit()

    def deduct_budget(self, team: Team, amount: int) -> Team:
        """Auction mein player khareedne ke baad budget deduct karo."""
        team.remaining_budget -= amount
        self.db.commit()
        self.db.refresh(team)
        return team
```

> 💡 **`joinedload` kya karta hai?**
> ```python
> # Bina joinedload (N+1 problem):
> team = db.query(Team).filter(...).first()  # Query 1
> team.owner  # SQLAlchemy ab owner ke liye DOOSRI query karta hai  # Query 2
>
> # joinedload ke saath:
> team = db.query(Team).options(joinedload(Team.owner)).filter(...).first()
> # Ek hi query: SELECT teams.*, users.* FROM teams JOIN users ON ...
> # team.owner  # Already loaded — no extra query
> ```
> "N+1 problem" tab hota hai jab N teams hain aur har team ke liye alag owner query hoti hai.

---

#### `Task 2` — 🔧 Create Team Service

**`backend/app/services/team_service.py`** banao:

```python
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.team import Team
from app.models.user import User, UserRole
from app.repositories.team_repository import TeamRepository
from app.schemas.team import TeamCreate, TeamUpdate


class TeamService:
    """Business logic for teams."""

    def __init__(self, db: Session):
        self.db = db
        self.repo = TeamRepository(db)

    def create_team(self, data: TeamCreate, current_user: User) -> Team:
        """Naya team banao."""
        # Check: team name already exist karta hai?
        if self.repo.get_by_name(data.name):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Team '{data.name}' already exists"
            )

        # Team owner sirf apni ek team bana sakta hai (business rule)
        if current_user.role == UserRole.TEAM_OWNER:
            existing = self.repo.get_by_owner(str(current_user.id))
            if existing:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Team owner can only have one team"
                )

        return self.repo.create(
            owner_id=str(current_user.id),
            name=data.name,
            short_name=data.short_name.upper(),   # always uppercase
            city=data.city,
            logo_url=data.logo_url,
            description=data.description,
            total_budget=data.total_budget,
            remaining_budget=data.total_budget,   # initially same as total
        )

    def get_team_or_404(self, team_id: str) -> Team:
        """Team ID se team lo, nahi mila to 404."""
        team = self.repo.get_by_id(team_id)
        if not team:
            raise HTTPException(status_code=404, detail="Team not found")
        return team

    def update_team(self, team_id: str, data: TeamUpdate, current_user: User) -> Team:
        """Team update karo — sirf owner ya admin kar sakta hai."""
        team = self.get_team_or_404(team_id)

        # Authorization check
        if current_user.role != UserRole.ADMIN and str(team.owner_id) != str(current_user.id):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only team owner or admin can update this team"
            )

        return self.repo.update(team, **data.model_dump(exclude_none=True))

    def delete_team(self, team_id: str, current_user: User) -> None:
        """Team delete karo — sirf admin kar sakta hai."""
        if current_user.role != UserRole.ADMIN:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admin can delete teams"
            )
        team = self.get_team_or_404(team_id)
        self.repo.delete(team)
```

> 💡 **`data.model_dump(exclude_none=True)` kya karta hai?**
> Pydantic v2 mein `.model_dump()` schema ko dict mein convert karta hai.
> `exclude_none=True` → `None` values wale fields skip ho jaate hain.
> ```python
> # TeamUpdate(name="Mumbai Indians", city=None)
> data.model_dump()                      # {"name": "Mumbai Indians", "city": None}
> data.model_dump(exclude_none=True)     # {"name": "Mumbai Indians"}
>
> # Repository mein: sirf "name" update hoga, "city" unchanged rahegi
> ```

---

> ### 🏁 Expected Output — Day 28
> ```
> ✅ app/repositories/team_repository.py — full CRUD + joinedload
> ✅ app/services/team_service.py — business logic + auth checks
> ✅ Duplicate team name check (409 Conflict)
> ✅ team_owner sirf ek team create kar sakta hai
> ✅ Update — sirf owner/admin kar sakta hai (403 otherwise)
> ✅ Delete — sirf admin kar sakta hai
> ```
> 🎯 **Goal Achieved:** Team ke CRUD operations — repository pattern + service layer

---
---

## 🛣️ Day 29: Team CRUD Routes (API)

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | RESTful Team API endpoints — full CRUD |

---

### ✅ Tasks

---

#### `Task 1` — 🛣️ Create Team router

**`backend/app/routers/teams.py`** banao:

```python
from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User, UserRole
from app.models.team import TeamStatus
from app.schemas.team import TeamCreate, TeamUpdate, TeamResponse, TeamWithOwner
from app.schemas.common import APIResponse
from app.services.team_service import TeamService
from app.repositories.team_repository import TeamRepository
from app.utils.dependencies import get_current_user, require_role

router = APIRouter(prefix="/teams", tags=["Teams"])


@router.get("", response_model=List[TeamResponse])
async def list_teams(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    status: Optional[TeamStatus] = Query(default=None),
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user)   # login required
):
    """Saari teams ki list — public (logged in users)."""
    repo = TeamRepository(db)
    return repo.get_all(skip=skip, limit=limit, status=status)


@router.post("", response_model=TeamResponse, status_code=201)
async def create_team(
    data: TeamCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Naya team banao — sirf team_owner ya admin."""
    service = TeamService(db)
    return service.create_team(data, current_user)


@router.get("/{team_id}", response_model=TeamWithOwner)
async def get_team(
    team_id: str,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user)
):
    """Team detail — owner info ke saath."""
    repo = TeamRepository(db)
    team = repo.get_by_id_with_owner(team_id)
    if not team:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Team not found")
    return team


@router.put("/{team_id}", response_model=TeamResponse)
async def update_team(
    team_id: str,
    data: TeamUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Team update karo — sirf owner ya admin."""
    service = TeamService(db)
    return service.update_team(team_id, data, current_user)


@router.delete("/{team_id}", status_code=204)
async def delete_team(
    team_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN))
):
    """Team delete karo — sirf admin."""
    service = TeamService(db)
    service.delete_team(team_id, current_user)
    # 204 No Content — response body nahi hota
```

> 💡 **`status_code=201` kyu create ke liye?**
> HTTP status codes:
> - `200 OK` → generic success
> - `201 Created` → naya resource create hua ✅ (POST ke liye correct)
> - `204 No Content` → success but koi response body nahi (DELETE ke liye correct)
>
> RESTful conventions follow karna professional practice hai.

> 💡 **`Query(default=0, ge=0)` kya hai?**
> FastAPI `Query` se URL query parameters validate karo:
> ```
> GET /api/teams?skip=0&limit=20&status=active
> skip=0  → ge=0 check (0 ya usse zyada)
> limit=20 → ge=1, le=100 check (1 se 100 ke beech)
> ```

---

#### `Task 2` — 📝 Register team router

**`backend/app/main.py`** mein add karo:

```python
from app.routers.teams import router as teams_router
app.include_router(teams_router, prefix="/api")
```

---

> ### 🏁 Expected Output — Day 29
> ```
> ✅ GET    /api/teams          → teams list (with pagination)
> ✅ POST   /api/teams          → team create (201)
> ✅ GET    /api/teams/{id}     → team detail with owner
> ✅ PUT    /api/teams/{id}     → team update
> ✅ DELETE /api/teams/{id}     → team delete (admin only, 204)
> ✅ Swagger UI mein saare routes visible
> ✅ Unauthorized access → 401/403 correctly
> ```
> 🎯 **Goal Achieved:** RESTful Team API endpoints — full CRUD

---
---

## 🧪 Day 30: Team API Testing + Player Model Start

| | |
|---|---|
| ⏱️ **Duration** | 2 hours |
| 🔧 **Type** | `Backend` |
| 🎯 **Goal** | Sare team endpoints test karo, Player model banana shuru karo |

---

### ✅ Tasks

---

#### `Task 1` — 🧪 Test all team endpoints (Swagger)

```bash
# Backend start karo:
uvicorn app.main:app --reload

# Swagger kholo: http://localhost:8000/docs

# Step 1: Google se login karo, token lo
# Step 2: Swagger → Authorize → token paste karo

# Step 3: Test karo:

# POST /api/teams — team banao
{
  "name": "Mumbai Indians",
  "short_name": "MI",
  "city": "Mumbai",
  "total_budget": 1000
}
# Expected: 201 Created ✅

# GET /api/teams — list dekho
# Expected: [{"id":"...","name":"Mumbai Indians",...}]

# GET /api/teams/{id} — detail with owner
# Expected: {..., "owner": {"email": "your@gmail.com", ...}}

# PUT /api/teams/{id} — update
{ "city": "Mumbai, Maharashtra" }
# Expected: 200 OK with updated city

# POST /api/teams again — same name
# Expected: 409 Conflict ✅

# DELETE /api/teams/{id} — admin se
# Expected: 204 No Content
```

---

#### `Task 2` — 🏃 Start Player Model

**`backend/app/models/player.py`** banao:

```python
from enum import Enum
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Enum as SAEnum, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class PlayerRole(str, Enum):
    BATSMAN = "batsman"
    BOWLER = "bowler"
    ALL_ROUNDER = "all_rounder"
    WICKET_KEEPER = "wicket_keeper"


class PlayerStatus(str, Enum):
    AVAILABLE = "available"    # Auction mein available
    SOLD = "sold"              # Khareed liya gaya
    UNSOLD = "unsold"          # Koi nahi kharida
    RETAINED = "retained"      # Team ne retain kiya


class Player(BaseModel):
    __tablename__ = "players"

    name = Column(String(200), nullable=False, index=True)
    country = Column(String(100), nullable=False)
    age = Column(Integer, nullable=True)
    player_role = Column(SAEnum(PlayerRole), nullable=False)
    base_price = Column(Integer, nullable=False)    # Lakhs mein
    image_url = Column(String(500), nullable=True)
    bio = Column(Text, nullable=True)

    # Stats (simple for now)
    batting_avg = Column(Integer, nullable=True)    # Integer percent
    bowling_avg = Column(Integer, nullable=True)
    matches_played = Column(Integer, default=0)

    status = Column(
        SAEnum(PlayerStatus),
        default=PlayerStatus.AVAILABLE,
        nullable=False
    )

    # Final sold price (auction mein kitne mein bika)
    final_price = Column(Integer, nullable=True)

    # Which team bought this player
    team_id = Column(
        UUID(as_uuid=True),
        ForeignKey("teams.id", ondelete="SET NULL"),
        nullable=True
    )

    team = relationship("Team", back_populates="players")
```

**`backend/alembic/env.py`** mein add karo:
```python
from app.models.player import Player
```

```bash
alembic revision --autogenerate -m "create players table"
alembic upgrade head
```

---

> ### 🏁 Expected Output — Day 30
> ```
> ✅ All team endpoints tested — 200/201/204/404/409/403 all working correctly
> ✅ app/models/player.py created — PlayerRole + PlayerStatus enums
> ✅ Player model: name, country, role, base_price, status, team_id FK
> ✅ Migration created + applied
> ✅ DBeaver → players table visible
> ✅ Phase 3 foundation laid! 🎉
> ```
> 🎯 **Goal Achieved:** Sare team endpoints test karo, Player model banana shuru karo

---
---

## 🏆 Phase 3 Start — Days 26–30 Summary

| Day | 🎯 Topic | 🔧 Type | Key Concepts |
|-----|----------|---------|--------------|
| Day 26 | Team Model | Backend | `relationship`, `ForeignKey`, `ondelete`, `back_populates` |
| Day 27 | Team Schemas | Backend | Nested schemas, `TeamWithOwner`, `exclude_none` |
| Day 28 | Team Repo + Service | Backend | `joinedload`, N+1 problem, business rules |
| Day 29 | Team CRUD API | Backend | REST conventions, `Query()`, status codes 201/204 |
| Day 30 | Testing + Player Model | Backend | End-to-end API test, Player model with enums |

---

> ### 📚 New Libraries Added — Days 21–30
>
> | Library | Install Command | Kya Karta Hai |
> |---------|----------------|---------------|
> | `react-router-dom` | `npm install react-router-dom` | Frontend routing (URL → Component) |
> | `zustand` | `npm install zustand` | Global state management (lightweight Redux) |
> | `axios` | `npm install axios` | HTTP client with interceptors |

---

> ## 🔜 Next Up: Phase 3 Days 31–40 — Player CRUD + Team Management UI
>
> | Day | Topic | Key Concepts |
> |-----|-------|-------------|
> | Day 31 | Player Schemas | Pydantic Player schemas, filtering |
> | Day 32 | Player Repository | Player CRUD + team assignment |
> | Day 33 | Player Routes | RESTful Player API |
> | Day 34 | Player Import | Bulk CSV/JSON player import |
> | Day 35 | Teams UI (Frontend) | React team list + create form |
> | Day 36 | Team Detail UI | Team page with player list |
> | Day 37 | Players UI | Player cards, filter by role/country |
> | Day 38 | Player Detail UI | Player profile page |
> | Day 39 | Admin Dashboard | User management + team management UI |
> | Day 40 | Phase 3 Polish | Error handling, loading states, tests |

---

*Days 31–40 documentation coming soon...*
