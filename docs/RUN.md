# 🏏 Cricket Auction Backend - Complete Guide

<div align="center">

**🚀 Real-time Cricket Player Auction System**

Ye guide dekho aur ek ek step follow karo, sab kuch easily setup ho jayega!

[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-336791?style=for-the-badge&logo=postgresql)](https://www.postgresql.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)

</div>

---

## 🚀 Quick Start - Pehli Baar Setup Kaise Kare

> **Dhyan se padho aur ek ek command run karo. Agar koi error aaye toh neeche troubleshooting section dekho!**

### 📝 Step 1: PostgreSQL Check Karo (Database chal raha hai ya nahi)

```bash
pg_isready -h localhost -p 5432
```

**Agar ye dikhe:** `localhost:5432 - accepting connections` - Matlab sab theek hai! ✅

**Agar error aaye:**
```bash
# PostgreSQL start karo
sudo systemctl start postgresql

# Check karo ab chal raha hai ya nahi
sudo systemctl status postgresql
```

---

### 📝 Step 2: Database Aur User Banao

**2 tarike hain - koi bhi ek use karo:**

**🔹 Method 1: Script se (Easy way - Recommended)**
```bash
sudo -u postgres psql -f db_setup.sql
```

**🔹 Method 2: Manual (Agar script kaam nahi kare)**
```bash
sudo -u postgres psql << EOF
CREATE USER cricket_admin WITH PASSWORD 'cricket123';
CREATE DATABASE cricket_auction_db OWNER cricket_admin;
GRANT ALL PRIVILEGES ON DATABASE cricket_auction_db TO cricket_admin;
\c cricket_auction_db
GRANT ALL ON SCHEMA public TO cricket_admin;
EOF
```

**Kya hoga:** Database `cricket_auction_db` ban jayega aur user `cricket_admin` ban jayega

---

### 📝 Step 3: Check Karo Database Connect Ho Raha Hai Ya Nahi

```bash
python3 db_check.py
```

**Agar sab theek hai toh ye dikhega:**
```
✅ Database connection successful!
📊 Database Information:
   PostgreSQL Version: PostgreSQL 12.x
✅ Database Status: HEALTHY
```

**Agar error aaye:**
- Dekho PostgreSQL chal raha hai ya nahi
- `.env` file me username/password check karo
- Step 2 dobara karo

---

### 📝 Step 4: Tables Banao Database Me

```bash
python3 -m app.db.init_db
```

**Kya hoga:** 4 tables ban jayenge:
- ✓ users (Users ki info)
- ✓ auctions (Auction ki details)
- ✓ teams (Teams ki info)
- ✓ players (Players ki info)

---

### 📝 Step 5: Server Start Karo 🎉

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

**Agar ye dikhe toh server chal gaya:**
```
INFO: Uvicorn running on http://0.0.0.0:8001
🚀 Cricket Auction Platform starting up...
```

---

### 📝 Step 6: Browser Me Check Karo

**Ye URLs kholo browser me:**
- 🌐 API Docs: http://localhost:8001/docs
- 💚 Health Check: http://localhost:8001/health
- 🏠 Home: http://localhost:8001/

---

<div align="center">

## 🎊 Ho Gaya Setup Complete! 🎊

Ab aapka server chal raha hai port 8001 pe!

</div>

---

## 🖥️ Server Kaise Chalaye (Daily Use Commands)

### ▶️ Server Start Karne Ke Liye

```bash
# Development mode (code change hone pe auto-reload hoga)
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

**Kya milega:**
- 🔄 Code change karo, server auto-restart hoga
- 📝 Saare logs terminal me dikhenge
- 🐛 Development ke liye best hai

---

### ⏹️ Server Stop Karne Ke Liye

**Agar terminal me chal raha hai:**
```
Press CTRL+C
```

**Agar background me chal raha hai:**
```bash
pkill -f "uvicorn main:app"
```

---

### 🌙 Background Me Chalane Ke Liye (Bina Terminal Ke)

```bash
nohup uvicorn main:app --host 0.0.0.0 --port 8001 > server.log 2>&1 &
```

**Kya hoga:**
- Terminal band karne ke baad bhi server chalega
- Saare logs `server.log` file me jayenge
- Production testing ke liye best hai

**Logs dekhne ke liye:**
```bash
tail -f server.log
```

---

## 🔍 Status Check Kaise Kare

### 💚 Server Theek Se Chal Raha Hai Ya Nahi

```bash
curl http://localhost:8001/health
```

**Healthy response (sab theek hai):**
```json
{
  "status": "healthy",
  "database": "connected",
  "version": "1.0.0"
}
```

**Unhealthy response (problem hai):**
```json
{
  "status": "healthy",
  "database": "disconnected: error message",
  "version": "1.0.0"
}
```

---

### 🗄️ Database Status Check Karo

```bash
# Detailed check
python3 db_check.py

# Quick check
psql -U cricket_admin -d cricket_auction_db -h localhost -c "SELECT 'DB Connected!' as status;"
```

---

### 🔎 Server Chal Raha Hai Ya Nahi Pata Karo

```bash
# Process check karo
ps aux | grep "uvicorn main:app"

# Port check karo
lsof -i :8001

# Quick test
curl -I http://localhost:8001/
```

---

## 🔄 Database Reset/Management Kaise Kare

### 🔁 Pura Database Reset Karo (Saara data delete hoga!)

```bash
python3 -m app.db.init_db reset
```

**Kya hoga:**
1. Saare tables delete ho jayenge
2. Phir se naye tables ban jayenge
3. Saara data khatam ho jayega (fresh start)

**Kab use kare:** Jab testing ke liye fresh database chahiye

---

### 📦 Sirf Tables Banao (Pehli baar ya drop ke baad)

```bash
python3 -m app.db.init_db
```

**Kya hoga:**
- Agar tables nahi hai toh ban jayenge
- Agar already hain toh kuch nahi hoga

---

### 🗑️ Saare Tables Delete Karo (Danger Zone!)

```bash
python3 -m app.db.init_db drop
```

**⚠️ Warning:** Ye command se saare tables permanently delete ho jayenge!

---

### 💾 Database Backup Aur Restore

**Backup banao:**
```bash
pg_dump -U cricket_admin -d cricket_auction_db -h localhost > backup_$(date +%Y%m%d_%H%M%S).sql
```

**Backup se restore karo:**
```bash
psql -U cricket_admin -d cricket_auction_db -h localhost < backup_20260307_120000.sql
```

---

## 🌐 API Kaise Use Kare

<div align="center">

### 🔗 Important URLs

| Kya Hai | URL | Kiske Liye |
|---------|-----|-----------|
| 🏠 Home | http://localhost:8001 | Basic info dekhne ke liye |
| 💚 Health | http://localhost:8001/health | Server aur DB status check karne ke liye |
| 📚 API Docs | http://localhost:8001/docs | Saare APIs dekhne aur test karne ke liye |
| 📖 ReDoc | http://localhost:8001/redoc | Documentation padhne ke liye |

</div>

---

### 📚 API Documentation Kaise Dekhe (Swagger)

**Browser me kholo:** http://localhost:8001/docs

**Kya milega:**
- 📋 Saare API endpoints ki list
- 🧪 "Try it out" button - direct browser se test karo
- 📝 Request/Response ka format
- 🔐 Authentication setup
- 📊 Example data pre-filled

**Kab use kare:**
- API test karna hai
- Request/Response format dekhna hai
- Without Postman testing karni hai

---

### 📖 Documentation Padhne Ke Liye (ReDoc)

**Browser me kholo:** http://localhost:8001/redoc

**Kya milega:**
- 📱 Mobile-friendly clean interface
- 🔍 Search karke endpoints dhundho
- 📑 Better organization
- 📥 PDF export option

**Kab use kare:** Documentation padhni hai ya team ke saath share karni hai

---

## 🔌 Direct Database Me Kaise Jaye

### 💻 PostgreSQL Shell Me Connect Karo

```bash
# Interactive shell
psql -U cricket_admin -d cricket_auction_db -h localhost
```

**Ab SQL commands run kar sakte ho:**
```sql
-- Saare users dekho
SELECT * FROM users;

-- Players count karo
SELECT COUNT(*) FROM players;

-- Quit karne ke liye
\q
```

---

### 📋 Common Database Commands

```bash
# Saare tables ki list
psql -U cricket_admin -d cricket_auction_db -h localhost -c "\dt"

# Table structure dekho
psql -U cricket_admin -d cricket_auction_db -h localhost -c "\d users"

# Database size check karo
psql -U cricket_admin -d cricket_auction_db -h localhost -c "SELECT pg_size_pretty(pg_database_size('cricket_auction_db'));"

# Records count karo
psql -U cricket_admin -d cricket_auction_db -h localhost -c "SELECT 'Users: ' || COUNT(*) FROM users;"
```

---

## 📊 Database Me Kya Kya Tables Hain

| 🏷️ Table | 📝 Kya Hai | 🔑 Important Fields |
|----------|-----------|-------------------|
| 👤 **users** | Users ki information aur login details | email, username, role, password |
| 🏆 **auctions** | Auction ki details (kab, kitne players, budget) | title, status, start_time, budget |
| 👥 **teams** | Teams ki info (kiska team, kitna budget bacha) | name, remaining_budget, auction_id |
| 🏏 **players** | Players ki details (naam, role, price, status) | name, role, base_price, status |

---

## ⚙️ Settings/Configuration Kaise Change Kare

**File edit karo:** `.env`

```bash
nano .env
# ya
vim .env
# ya
code .env
```

**Important Settings:**

| Setting | Kya Hai | Default Value |
|---------|---------|---------------|
| `DATABASE_URL` | Database connection string | `postgresql://cricket_admin:...` |
| `DB_HOST` | Database host | `localhost` |
| `DB_PORT` | Database port | `5432` |
| `DB_NAME` | Database name | `cricket_auction_db` |
| `PORT` | Server port | `8001` |
| `DEBUG` | Debug mode on/off | `True` |
| `BACKEND_CORS_ORIGINS` | Frontend URLs (comma separated) | `http://localhost:3000,...` |

**Change karne ke baad:**
- Server restart karo
- Changes apply ho jayenge

---

## 🐛 Problems Aur Solutions

### ❌ Problem: Database Connect Nahi Ho Raha

**Error dikhega:**
```
psycopg2.OperationalError: connection refused
FATAL: password authentication failed
```

**Solution - Step by step:**

```bash
# 1. PostgreSQL chal raha hai ya nahi check karo
pg_isready -h localhost -p 5432
sudo systemctl status postgresql

# 2. Agar nahi chal raha toh start karo
sudo systemctl start postgresql

# 3. Database aur user banao (dubara)
sudo -u postgres psql -f db_setup.sql

# 4. .env file me credentials check karo
cat .env | grep DB_

# 5. Ab test karo
python3 db_check.py
```

---

### ❌ Problem: Port 8001 Already Use Ho Raha Hai

**Error dikhega:**
```
ERROR: [Errno 98] Address already in use
```

**Solution:**

```bash
# 1. Dekho kon use kar raha hai port ko
lsof -i :8001

# 2. Us process ko band karo
kill -9 <PID>

# Ya saare uvicorn processes band karo
pkill -f "uvicorn main:app"

# 3. Verify karo port free hai
lsof -i :8001

# 4. Ab server start karo
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

---

### ❌ Problem: Module Not Found (Import Error)

**Error dikhega:**
```
ModuleNotFoundError: No module named 'fastapi'
```

**Solution:**

```bash
# Saare dependencies install karo
cd /path/to/backend
pip install -r requirements.txt

# Ya individually install karo
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic-settings

# Check karo install hua ya nahi
pip list | grep -E "fastapi|uvicorn"
```

---

### ❌ Problem: Database Already Exists

**Error dikhega:**
```
ERROR: database "cricket_auction_db" already exists
```

**Solution - 2 options:**

**Option 1: Use existing database (safe)**
```bash
python3 -m app.db.init_db
```

**Option 2: Delete aur phir se banao (data loss hoga!)**
```bash
sudo -u postgres psql -c "DROP DATABASE IF EXISTS cricket_auction_db;"
sudo -u postgres psql -c "DROP USER IF EXISTS cricket_admin;"
sudo -u postgres psql -f db_setup.sql
```

---

### ❌ Problem: Permission Denied

**Error dikhega:**
```
FATAL: role "cricket_admin" does not exist
ERROR: permission denied
```

**Solution:**

```bash
sudo -u postgres psql << EOF
DROP USER IF EXISTS cricket_admin;
CREATE USER cricket_admin WITH PASSWORD 'cricket123';
ALTER USER cricket_admin CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE cricket_auction_db TO cricket_admin;
\c cricket_auction_db
GRANT ALL ON SCHEMA public TO cricket_admin;
GRANT ALL ON ALL TABLES IN SCHEMA public TO cricket_admin;
EOF
```

---

### ❌ Problem: CORS Error Browser Me

**Error dikhega:**
```
Access to fetch has been blocked by CORS policy
```

**Solution:**

```bash
# .env file edit karo
nano .env

# Apna frontend URL add karo
BACKEND_CORS_ORIGINS=http://localhost:3000,http://localhost:8000,http://your-url:3000

# Server restart karo (CTRL+C then start again)
```

---

## 🔍 Debugging - Agar Kuch Samajh Nahi Aa Raha

### Step 1: Saari Services Check Karo

```bash
# PostgreSQL
sudo systemctl status postgresql
pg_isready

# Server
ps aux | grep uvicorn

# Port
lsof -i :8001
```

### Step 2: Logs Dekho

```bash
# Server logs (agar background me hai)
tail -f server.log

# PostgreSQL logs
sudo tail -f /var/log/postgresql/postgresql-12-main.log
```

### Step 3: Ek Ek Karke Test Karo

```bash
# Database test
python3 db_check.py

# Server test
curl http://localhost:8001/health

# Python modules test
python3 -c "import fastapi; import sqlalchemy; print('Sab theek hai!')"
```

### Step 4: Complete Fresh Start

```bash
# 1. Server band karo
pkill -f uvicorn

# 2. Database reset karo
python3 -m app.db.init_db reset

# 3. Logs clear karo
> server.log

# 4. Fresh start
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

---

## 📚 Helpful Resources

### 🔗 Documentation Links
- 📘 [FastAPI Docs](https://fastapi.tiangolo.com/) - API framework
- 📗 [PostgreSQL Docs](https://www.postgresql.org/docs/) - Database
- 📙 [SQLAlchemy Docs](https://docs.sqlalchemy.org/) - ORM library
- 📕 [Uvicorn Docs](https://www.uvicorn.org/) - Web server

### 🛠️ Extra Tools Install Karo (Optional)

```bash
# PostgreSQL GUI
sudo apt install pgadmin4

# API Testing
sudo snap install postman

# Better PostgreSQL CLI
pip install pgcli
```

---

<div align="center">

## 🎉 Daily Use - Quick Commands

**Roz kaam aane wale commands:**

```bash
# ✅ Check karo sab theek hai
python3 db_check.py
curl http://localhost:8001/health

# 🚀 Server start karo
uvicorn main:app --reload --host 0.0.0.0 --port 8001

# ⏹️ Server stop karo
CTRL+C
# ya
pkill -f "uvicorn main:app"

# 🔄 Database reset (testing ke liye)
python3 -m app.db.init_db reset

# 📋 Logs dekho
tail -f server.log

# 🗄️ Database me jao
psql -U cricket_admin -d cricket_auction_db -h localhost

# 💾 Backup banao
pg_dump -U cricket_admin -d cricket_auction_db > backup.sql
```

---

### 📞 Help Chahiye?

- 🐛 **Bug mila:** Logs check karo (`server.log` ya terminal)
- ❌ **Error aa raha hai:** Troubleshooting section upar dekho
- 🔍 **Kuch samajh nahi aa raha:** Documentation links check karo
- 💡 **Idea chahiye:** FastAPI docs best hai

---

### 🌟 Bas! Ab Coding Shuru Karo! 🌟

**Agar koi problem aaye toh:**
1. Pehle troubleshooting section dekho
2. Logs check karo
3. Google pe error search karo
4. Documentation padho

**All the best!** 🏏🎉

---

**Made with ❤️ for Cricket Auction Platform**

*Agar ye guide helpful lagi toh apne teammates ko share karo!*

</div>
