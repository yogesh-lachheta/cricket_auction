<div align="center">

# 🏏 Cricket Auction Platform
## 🚀 Complete Development Guide

![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12-blue?style=for-the-badge&logo=postgresql)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge&logo=python)

**Environment:** Ubuntu 20.04 | PostgreSQL 12 | Python 3.8+ | FastAPI | DBeaver CE

---

</div>

## 📑 Table of Contents

1. [🎯 Quick Start](#-quick-start-3-commands)
2. [📊 Current System Status](#-current-system-status)
3. [🎛️ Service Control Commands](#️-service-control-commands)
4. [⚔️ Kill Commands Guide](#️-kill-commands-guide)
5. [✅ Required Services Setup](#-required-services-setup)
6. [🔄 Daily Workflow](#-daily-workflow)
7. [🔥 Troubleshooting](#-troubleshooting)
8. [🌐 Important URLs](#-important-urls)
9. [📂 Project Structure](#-project-structure)
10. [💡 Pro Tips](#-pro-tips)

---

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; color: white;">

## 🎯 Quick Start - Manual Commands

</div>

> **⚠️ IMPORTANT:** Har command ko separately run karein. Ek ek step follow karein for better control!

### 📋 Step-by-Step Startup (Recommended)

#### **Step 1: Check/Start PostgreSQL**

```bash
# Check if PostgreSQL is running
pg_lsclusters
```

**Expected Output:**
```
Ver Cluster Port Status Owner
12  main    5432 online postgres  ✅
```

**If status shows "down", start it:**
```bash
sudo systemctl start postgresql@12-main
```

**Verify again:**
```bash
pg_lsclusters
# Status: online ✅
```

---

#### **Step 2: Navigate to Backend Folder**

```bash
cd ~/Documents/R\&D/Cricket\ Auctions/cricket-auction-platform/backend
```

**Verify location:**
```bash
pwd
# Output: /home/billion/Documents/R&D/Cricket Auctions/cricket-auction-platform/backend
```

---

#### **Step 3: Activate Virtual Environment**

```bash
source venv/bin/activate
```

**Verify activation:**
```bash
# Check 1: Prompt shows (venv)
# Terminal: (venv) user@hostname:~/path$

# Check 2: VIRTUAL_ENV variable set
echo $VIRTUAL_ENV
# Output: /home/billion/Documents/R&D/Cricket Auctions/cricket-auction-platform/backend/venv ✅

# Check 3: Python path
which python
# Output: .../backend/venv/bin/python ✅
```

---

#### **Step 4: Start FastAPI Development Server**

```bash
uvicorn app.main:app --reload
```

**Expected Output:**
```
INFO:     Will watch for changes in these directories: ['/home/billion/Documents/R&D/Cricket Auctions/cricket-auction-platform/backend']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using WatchFiles
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete. ✅
```

**⚠️ Note:**
- Ye terminal ab server run kar raha hai
- Logs yahan dikhenge
- Ctrl+C se stop hoga
- Dusre commands ke liye naya terminal open karo

---

### ⚡ Advanced: One-Command Version (Optional)

**For experienced users only:**
```bash
cd ~/Documents/R\&D/Cricket\ Auctions/cricket-auction-platform/backend && source venv/bin/activate && uvicorn app.main:app --reload
```

**⚠️ Recommendation:** Use step-by-step commands above for:
- Better control
- Easy debugging
- Understanding each step
- Troubleshooting issues

### ✅ Expected Output

```
INFO:     Will watch for changes in these directories: ['/home/billion/Documents/R&D/Cricket Auctions/cricket-auction-platform/backend']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using WatchFiles
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### ✅ Verify Server Running

```bash
# Test API
curl http://localhost:8000
# Response: {"message":"Cricket Auction Platform API","status":"running"}

# Or open in browser
# http://localhost:8000/docs
```

---

<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 20px; border-radius: 10px; color: white;">

## 📊 Current System Status

</div>

### 🎯 Live Status Table

| # | Component | Status | Port | Required? | Action |
|:-:|-----------|:------:|:----:|:---------:|--------|
| 1️⃣ | **PostgreSQL Service** | ![Online](https://img.shields.io/badge/-ONLINE-success) | 5432 | 🔴 MUST | ✅ No action needed |
| 2️⃣ | **PostgreSQL Auto-Start** | ![Enabled](https://img.shields.io/badge/-ENABLED-success) | - | 🟡 RECOMMENDED | ✅ No action needed |
| 3️⃣ | **Database: cricket_auction** | ![Exists](https://img.shields.io/badge/-EXISTS-success) | - | 🔴 MUST | ✅ No action needed |
| 4️⃣ | **Database User: admin** | ![Active](https://img.shields.io/badge/-ACTIVE-success) | - | 🔴 MUST | ✅ No action needed |
| 5️⃣ | **Project Structure** | ![Ready](https://img.shields.io/badge/-READY-success) | - | 🔴 MUST | ✅ No action needed |
| 6️⃣ | **Virtual Environment** | ![Available](https://img.shields.io/badge/-AVAILABLE-yellow) | - | 🔴 MUST | ⚠️ Activate: `source venv/bin/activate` |
| 7️⃣ | **FastAPI Server** | ![Running](https://img.shields.io/badge/-RUNNING-success) | 8000 | 🔴 MUST | ✅ Currently running (PID: 361061) |
| 8️⃣ | **DBeaver CE** | ![Optional](https://img.shields.io/badge/-OPTIONAL-inactive) | - | 🟢 OPTIONAL | ℹ️ Launch when needed |

**Legend:**
- 🔴 **MUST** = Required for code to run
- 🟡 **RECOMMENDED** = Should be enabled
- 🟢 **OPTIONAL** = Nice to have

### 📊 Quick Status Check Command

```bash
echo "=== PostgreSQL ===" && pg_lsclusters && \
echo -e "\n=== Virtual Environment ===" && \
([ -n "$VIRTUAL_ENV" ] && echo "✅ Active: $VIRTUAL_ENV" || echo "❌ Not Active") && \
echo -e "\n=== FastAPI Server ===" && \
(lsof -i:8000 > /dev/null 2>&1 && echo "✅ Running on port 8000" || echo "❌ Not Running")
```

---

<div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 20px; border-radius: 10px; color: white;">

## 🎛️ Service Control Commands

</div>

### 📊 Complete Service Control Table

| Service | Action | Command | Description |
|---------|:------:|---------|-------------|
| **🐘 PostgreSQL** | ![Start](https://img.shields.io/badge/-START-brightgreen) | `sudo systemctl start postgresql@12-main` | Service start karo |
| | ![Stop](https://img.shields.io/badge/-STOP-red) | `sudo systemctl stop postgresql@12-main` | Service stop karo |
| | ![Restart](https://img.shields.io/badge/-RESTART-orange) | `sudo systemctl restart postgresql@12-main` | Service restart karo |
| | ![Status](https://img.shields.io/badge/-STATUS-blue) | `pg_lsclusters` | Quick status check |
| | ![Status](https://img.shields.io/badge/-STATUS-blue) | `sudo systemctl status postgresql@12-main` | Detailed status |
| | ![Enable](https://img.shields.io/badge/-ENABLE-green) | `sudo systemctl enable postgresql@12-main` | Boot pe auto-start |
| | ![Disable](https://img.shields.io/badge/-DISABLE-gray) | `sudo systemctl disable postgresql@12-main` | Auto-start disable |
| | ![Reload](https://img.shields.io/badge/-RELOAD-yellow) | `sudo systemctl reload postgresql@12-main` | Config reload |
| | ![Logs](https://img.shields.io/badge/-LOGS-lightblue) | `sudo journalctl -u postgresql@12-main -n 50` | Last 50 logs |
| | ![Live Logs](https://img.shields.io/badge/-LIVE_LOGS-lightblue) | `sudo journalctl -u postgresql@12-main -f` | Live logs (Ctrl+C to exit) |
| **🐍 Virtual Env** | ![Activate](https://img.shields.io/badge/-ACTIVATE-brightgreen) | `source venv/bin/activate` | Activate venv |
| | ![Deactivate](https://img.shields.io/badge/-DEACTIVATE-red) | `deactivate` | Deactivate venv |
| | ![Status](https://img.shields.io/badge/-STATUS-blue) | `echo $VIRTUAL_ENV` | Check if active |
| | ![Status](https://img.shields.io/badge/-STATUS-blue) | `which python` | Active Python path |
| **🚀 FastAPI** | ![Start](https://img.shields.io/badge/-START-brightgreen) | `uvicorn app.main:app --reload` | Dev server start |
| | ![Start Port](https://img.shields.io/badge/-START_PORT-green) | `uvicorn app.main:app --reload --port 8001` | Custom port |
| | ![Start BG](https://img.shields.io/badge/-START_BG-green) | `uvicorn app.main:app --reload &` | Background mode |
| | ![Stop](https://img.shields.io/badge/-STOP-red) | `Ctrl + C` | Stop foreground server |
| | ![Force Stop](https://img.shields.io/badge/-FORCE_STOP-darkred) | `kill -9 $(lsof -ti:8000)` | Force kill |
| | ![Status](https://img.shields.io/badge/-STATUS-blue) | `lsof -i:8000` | Port 8000 status |
| | ![Test](https://img.shields.io/badge/-TEST-yellow) | `curl http://localhost:8000` | API test |
| **💾 DBeaver** | ![Start](https://img.shields.io/badge/-START-brightgreen) | `dbeaver-ce &` | Launch GUI |
| | ![Stop](https://img.shields.io/badge/-STOP-red) | `pkill -f dbeaver` | Close DBeaver |
| | ![Status](https://img.shields.io/badge/-STATUS-blue) | `pgrep -f dbeaver` | Check running |
| **🗄️ Database** | ![Connect](https://img.shields.io/badge/-CONNECT-brightgreen) | `PGPASSWORD=admin psql -h localhost -U admin -d cricket_auction` | Connect to DB |
| | ![List DBs](https://img.shields.io/badge/-LIST-blue) | `PGPASSWORD=admin psql -h localhost -U admin -d cricket_auction -c "\l"` | List databases |
| | ![List Tables](https://img.shields.io/badge/-TABLES-blue) | `PGPASSWORD=admin psql -h localhost -U admin -d cricket_auction -c "\dt"` | List tables |
| | ![List Users](https://img.shields.io/badge/-USERS-blue) | `PGPASSWORD=admin psql -h localhost -U admin -d cricket_auction -c "\du"` | List users |

### 🎯 Quick Shortcuts

#### **Start Everything**
```bash
sudo systemctl start postgresql@12-main && \
cd ~/Documents/R\&D/Cricket\ Auctions/cricket-auction-platform/backend && \
source venv/bin/activate && \
uvicorn app.main:app --reload
```

#### **Stop Everything**
```bash
kill -9 $(lsof -ti:8000) 2>/dev/null && \
deactivate 2>/dev/null && \
echo "✅ FastAPI stopped, venv deactivated"
```

#### **Restart Everything**
```bash
kill -9 $(lsof -ti:8000) 2>/dev/null && \
sudo systemctl restart postgresql@12-main && \
cd ~/Documents/R\&D/Cricket\ Auctions/cricket-auction-platform/backend && \
source venv/bin/activate && \
uvicorn app.main:app --reload
```

---

<div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); padding: 20px; border-radius: 10px; color: white;">

## ⚔️ Kill Commands Guide

</div>

### 🎯 Safe Kill Commands

| Target | Kill Command | Description | Risk Level |
|--------|--------------|-------------|:----------:|
| **FastAPI (Port 8000)** | `kill -9 $(lsof -ti:8000)` | Force kill server on port 8000 | ![Safe](https://img.shields.io/badge/-SAFE-success) |
| **FastAPI (Graceful)** | `kill $(lsof -ti:8000)` | Graceful shutdown (SIGTERM) | ![Safe](https://img.shields.io/badge/-SAFE-success) |
| **DBeaver** | `pkill -f dbeaver` | Close DBeaver application | ![Safe](https://img.shields.io/badge/-SAFE-success) |
| **Specific PID** | `kill -9 12345` | Kill specific process ID | ![Safe](https://img.shields.io/badge/-SAFE-success) |
| **All Uvicorn** | `pkill -f uvicorn` | Kill all uvicorn processes | ![Caution](https://img.shields.io/badge/-CAUTION-yellow) |
| **All Python** | `pkill python` | Kill ALL Python processes | ![Dangerous](https://img.shields.io/badge/-DANGEROUS-red) |
| **PostgreSQL (Wrong!)** | ❌ `pkill postgres` | **NEVER DO THIS!** | ![Critical](https://img.shields.io/badge/-CRITICAL-critical) |
| **PostgreSQL (Correct)** | `sudo systemctl stop postgresql@12-main` | Safe PostgreSQL stop | ![Safe](https://img.shields.io/badge/-SAFE-success) |

### 💣 Kill Signals Explained

| Signal | Command | Behavior | When to Use |
|--------|---------|----------|-------------|
| **SIGTERM (15)** | `kill <PID>` | Graceful shutdown with cleanup | ![Recommended](https://img.shields.io/badge/-RECOMMENDED-success) |
| **SIGKILL (9)** | `kill -9 <PID>` | Force kill (immediate, no cleanup) | ![Last Resort](https://img.shields.io/badge/-LAST_RESORT-orange) |
| **SIGINT (2)** | `Ctrl + C` | Interrupt (in terminal) | ![Normal](https://img.shields.io/badge/-NORMAL-blue) |
| **SIGHUP (1)** | `kill -1 <PID>` | Reload config | ![Config](https://img.shields.io/badge/-CONFIG-yellow) |

**Recommended Kill Order:**
```bash
# 1. Try graceful first
kill <PID>

# 2. Wait 5 seconds
sleep 5

# 3. If still running, force kill
kill -9 <PID>
```

### 🔥 Common Kill Scenarios

#### **Scenario 1: Port 8000 Already in Use**
```bash
# Check what's running
lsof -i:8000

# Kill it
kill -9 $(lsof -ti:8000)

# Verify freed
lsof -i:8000  # Should show nothing

# Start server
uvicorn app.main:app --reload
```

#### **Scenario 2: FastAPI Hang ho Gaya**
```bash
# Method 1: Port-based kill
kill -9 $(lsof -ti:8000)

# Method 2: Process name based
pkill -9 -f "uvicorn app.main:app"

# Verify killed
lsof -i:8000
```

#### **Scenario 3: Multiple Servers Running**
```bash
# Find all Python processes on ports 8000-8010
for port in {8000..8010}; do
    lsof -ti:$port && echo "Port $port in use"
done

# Kill all
for port in {8000..8010}; do
    kill -9 $(lsof -ti:$port) 2>/dev/null
done
```

#### **Scenario 4: Complete Cleanup**
```bash
# Kill FastAPI
kill -9 $(lsof -ti:8000) 2>/dev/null

# Kill all uvicorn
pkill -9 -f uvicorn

# Kill DBeaver
pkill -9 -f dbeaver

# Restart PostgreSQL
sudo systemctl restart postgresql@12-main

# Verify all
echo "FastAPI:" && (lsof -i:8000 || echo "Not running ✅")
echo "DBeaver:" && (pgrep -f dbeaver || echo "Not running ✅")
echo "PostgreSQL:" && pg_lsclusters
```

### 🚨 DANGER ZONE - Never Run These!

<div style="background-color: #ff6b6b; padding: 10px; border-radius: 5px; color: white; font-weight: bold;">

⚠️ **CRITICAL WARNING - NEVER RUN THESE COMMANDS!**

</div>

| ❌ DANGEROUS COMMAND | Why Dangerous | ✅ Correct Alternative |
|---------------------|---------------|----------------------|
| `pkill postgres` | Database corruption/data loss | `sudo systemctl stop postgresql@12-main` |
| `kill -9 $(pidof postgres)` | PostgreSQL crash | Use systemctl |
| `killall python` | Kills ALL Python apps | `kill -9 $(lsof -ti:8000)` |
| `rm -rf /var/lib/postgresql` | **PERMANENT DATA LOSS** | **NEVER DO THIS!** |
| `sudo reboot` (as solution) | Unnecessary system restart | Restart individual services |

### 🔬 Process Debugging Commands

```bash
# Find what's on port 8000
lsof -i:8000

# Get only PID
lsof -ti:8000

# Find by process name
pgrep -f uvicorn

# Full process details
ps aux | grep uvicorn

# Check if process alive
kill -0 <PID> && echo "Alive ✅" || echo "Dead ❌"

# Process tree
pstree -p <PID>
```

---

<div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 20px; border-radius: 10px; color: #333;">

## ✅ Required Services Setup

</div>

### 🎯 Services Priority Table

| Priority | Service | Required For | Auto-Start | Can Skip? |
|:--------:|---------|--------------|:----------:|:---------:|
| 🔴 **CRITICAL** | PostgreSQL Service | Database operations | ✅ Recommended | ❌ NO |
| 🔴 **CRITICAL** | PostgreSQL Auto-Start | Auto-start on boot | ✅ Recommended | ⚠️ Manual start needed |
| 🔴 **CRITICAL** | Virtual Environment | Python packages | ❌ Manual | ❌ NO |
| 🔴 **CRITICAL** | FastAPI Server | API endpoints | ❌ Manual | ❌ NO |
| 🟢 **OPTIONAL** | DBeaver | GUI database access | ❌ Manual | ✅ YES |

### ⚙️ One-Time Setup (Enable Auto-Start)

```bash
# Enable PostgreSQL to auto-start on system boot
sudo systemctl enable postgresql@12-main

# Verify enabled
sudo systemctl is-enabled postgresql@12-main
# Output: enabled ✅

# Start PostgreSQL now
sudo systemctl start postgresql@12-main

# Verify running
pg_lsclusters
# Output: Status: online ✅
```

### 📊 Service Dependency Chain

```mermaid
graph TD
    A[System Boot] --> B[PostgreSQL Auto-Starts]
    B --> C[User Login]
    C --> D[Navigate to Project]
    D --> E[Activate Virtual Environment]
    E --> F[Start FastAPI Server]
    F --> G[✅ Code Running!]
```

**Text Version:**
```
System Boot
    ↓
PostgreSQL Auto-Starts ✅ (if enabled)
    ↓
User Login
    ↓
Navigate to Project Folder
    ↓
Activate Virtual Environment ✅
    ↓
Start FastAPI Server ✅
    ↓
✅ CODE RUNNING!
```

### 🔍 Verify All Services

```bash
#!/bin/bash
echo "🏏 Cricket Auction Platform - Service Check"
echo "=========================================="

# PostgreSQL Service
if pg_lsclusters | grep -q "online"; then
    echo "✅ PostgreSQL: RUNNING"
else
    echo "❌ PostgreSQL: NOT RUNNING"
fi

# PostgreSQL Auto-Start
if sudo systemctl is-enabled postgresql@12-main 2>/dev/null | grep -q "enabled"; then
    echo "✅ PostgreSQL Auto-Start: ENABLED"
else
    echo "⚠️ PostgreSQL Auto-Start: DISABLED"
fi

# Database Connection
if PGPASSWORD=admin psql -h localhost -U admin -d cricket_auction -c "SELECT 1" > /dev/null 2>&1; then
    echo "✅ Database: ACCESSIBLE"
else
    echo "❌ Database: NOT ACCESSIBLE"
fi

# Virtual Environment
if [ -n "$VIRTUAL_ENV" ]; then
    echo "✅ Virtual Env: ACTIVATED"
else
    echo "⚠️ Virtual Env: NOT ACTIVATED"
fi

# FastAPI Server
if lsof -i:8000 > /dev/null 2>&1; then
    PID=$(lsof -ti:8000)
    echo "✅ FastAPI: RUNNING (PID: $PID)"
else
    echo "⚠️ FastAPI: NOT RUNNING"
fi

echo "=========================================="
```

**Save as:** `check_services.sh` and run: `bash check_services.sh`

---

<div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 20px; border-radius: 10px; color: #333;">

## 🔄 Daily Workflow

</div>

### 🌅 Morning - Start Work

```bash
# ✅ Step 1: Check PostgreSQL (should auto-run if enabled)
pg_lsclusters

# ✅ Step 2: Navigate to project + Activate venv
cd ~/Documents/R\&D/Cricket\ Auctions/cricket-auction-platform/backend
source venv/bin/activate

# ✅ Step 3: Start FastAPI Server
uvicorn app.main:app --reload

# ✅ Step 4: Verify running
curl http://localhost:8000
```

**One-Command Version:**
```bash
cd ~/Documents/R\&D/Cricket\ Auctions/cricket-auction-platform/backend && source venv/bin/activate && uvicorn app.main:app --reload
```

### 🌆 Evening - End Work

```bash
# Step 1: Stop FastAPI (Ctrl+C in terminal, or:)
kill -9 $(lsof -ti:8000)

# Step 2: Deactivate venv
deactivate

# Step 3: PostgreSQL (optional - can leave running)
# sudo systemctl stop postgresql@12-main
```

### 📋 Daily Checklist

```
☐ PostgreSQL running: pg_lsclusters
☐ Navigate to backend folder
☐ Activate venv: source venv/bin/activate
☐ Start server: uvicorn app.main:app --reload
☐ Test API: curl http://localhost:8000
☐ Open Swagger: http://localhost:8000/docs
```

---

<div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 20px; border-radius: 10px; color: #333;">

## 🔥 Troubleshooting

</div>

### ❌ Problem 1: Port 8000 Already in Use

**Error:**
```
ERROR: [Errno 98] Address already in use
```

**Solution:**
```bash
# Find what's using port 8000
lsof -i:8000

# Kill it
kill -9 $(lsof -ti:8000)

# Verify port is free
lsof -i:8000  # Should return nothing

# Restart server
uvicorn app.main:app --reload
```

### ❌ Problem 2: PostgreSQL Not Running

**Error:**
```
psql: error: connection to server at "localhost" (::1), port 5432 failed
```

**Solution:**
```bash
# Check status
pg_lsclusters

# If shows "down", start it
sudo systemctl start postgresql@12-main

# Verify
pg_lsclusters
# Should show: Status: online ✅
```

### ❌ Problem 3: Virtual Environment Not Found

**Error:**
```
bash: venv/bin/activate: No such file or directory
```

**Solution:**
```bash
# Navigate to backend
cd ~/Documents/R\&D/Cricket\ Auctions/cricket-auction-platform/backend

# Check if venv exists
ls -la venv

# If not, create it
python3 -m venv venv

# Activate
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### ❌ Problem 4: ModuleNotFoundError

**Error:**
```
ModuleNotFoundError: No module named 'fastapi'
```

**Solution:**
```bash
# Make sure venv is activated
source venv/bin/activate

# Verify active
echo $VIRTUAL_ENV  # Should show path

# Reinstall dependencies
pip install -r requirements.txt

# Or install specific package
pip install fastapi uvicorn
```

### ❌ Problem 5: Database Connection Failed

**Error:**
```
psql: error: fe_sendauth: no password supplied
```

**Solution:**
```bash
# Use PGPASSWORD environment variable
PGPASSWORD=admin psql -h localhost -U admin -d cricket_auction

# Or check PostgreSQL is running
pg_lsclusters

# Check user permissions
PGPASSWORD=admin psql -h localhost -U admin -d cricket_auction -c "\du"
```

### ❌ Problem 6: Permission Denied for systemctl

**Error:**
```
Failed to start postgresql@12-main.service: Access denied
```

**Solution:**
```bash
# Use sudo for systemctl commands
sudo systemctl start postgresql@12-main
sudo systemctl status postgresql@12-main
```

### 🆘 Emergency Full Reset

```bash
# Kill all related processes
kill -9 $(lsof -ti:8000) 2>/dev/null
pkill -f uvicorn 2>/dev/null
pkill -f dbeaver 2>/dev/null

# Restart PostgreSQL
sudo systemctl restart postgresql@12-main

# Deactivate venv
deactivate 2>/dev/null

# Navigate to project
cd ~/Documents/R\&D/Cricket\ Auctions/cricket-auction-platform/backend

# Activate venv
source venv/bin/activate

# Start server
uvicorn app.main:app --reload
```

---

<div style="background: linear-gradient(135deg, #d299c2 0%, #fef9d7 100%); padding: 20px; border-radius: 10px; color: #333;">

## 🌐 Important URLs

</div>

| Service | URL | Description | Status |
|---------|-----|-------------|:------:|
| 🏠 **API Base** | http://localhost:8000 | Main API endpoint | ![Active](https://img.shields.io/badge/-ACTIVE-success) |
| 📚 **Swagger Docs** | http://localhost:8000/docs | Interactive API documentation | ![Active](https://img.shields.io/badge/-ACTIVE-success) |
| 📖 **ReDoc** | http://localhost:8000/redoc | Alternative API docs | ![Active](https://img.shields.io/badge/-ACTIVE-success) |
| 🗄️ **PostgreSQL** | localhost:5432 | Database server | ![Active](https://img.shields.io/badge/-ACTIVE-success) |

### 🧪 Quick API Tests

```bash
# Root endpoint
curl http://localhost:8000
# Response: {"message":"Cricket Auction Platform API","status":"running"}

# Health check
curl http://localhost:8000/health
# Response: {"status":"healthy"}
```

---

<div style="background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%); padding: 20px; border-radius: 10px; color: #333;">

## 📂 Project Structure

</div>

```
🏏 cricket-auction-platform/
├── 📁 backend/
│   ├── 📁 app/
│   │   ├── 📁 api/v1/routes/
│   │   │   ├── 🔐 auth/            # Authentication (Login, Register, Token)
│   │   │   ├── 🏏 players/         # Player CRUD, Search, Stats, Auction
│   │   │   ├── 👥 teams/           # Team CRUD, Players, Budget
│   │   │   └── 🎯 auctions/        # Auction CRUD, Bidding, Results, Rules
│   │   ├── ⚙️ core/                # Config, Security, Dependencies
│   │   ├── 🗄️ db/                  # Database Base, Session, Init
│   │   ├── 📋 models/              # SQLAlchemy Models
│   │   ├── ✅ schemas/             # Pydantic Validation Schemas
│   │   ├── 💼 services/            # Business Logic Layer
│   │   ├── ⚡ websockets/          # Real-time Bidding WebSockets
│   │   ├── 🛠️ utils/               # Helpers, Validators, Constants
│   │   └── 🚀 main.py              # FastAPI Application Entry Point
│   ├── 🧪 tests/                   # Unit & Integration Tests
│   ├── 🔄 alembic/                 # Database Migrations
│   ├── 🐍 venv/                    # Python Virtual Environment
│   ├── 🔑 .env                     # Environment Variables
│   ├── 📦 requirements.txt         # Python Dependencies
│   └── 🐳 Dockerfile               # Docker Configuration
├── 📁 frontend/                    # (Future) React/Vue Frontend
├── 🐳 docker-compose.yml          # Multi-container Setup
└── 📖 README.md                    # Project Documentation
```

---

<div style="background: linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%); padding: 20px; border-radius: 10px; color: #333;">

## 💡 Pro Tips

</div>

### 🚀 Create Bash Alias for Quick Access

**Add to `~/.bashrc`:**
```bash
# Cricket Auction Platform Alias
alias cricket='cd ~/Documents/R\&D/Cricket\ Auctions/cricket-auction-platform/backend && source venv/bin/activate && echo "🏏 Cricket Auction Environment Ready!"'
alias cricket-start='cricket && uvicorn app.main:app --reload'
alias cricket-stop='kill -9 $(lsof -ti:8000) 2>/dev/null && deactivate'
alias cricket-status='pg_lsclusters && echo "" && (lsof -i:8000 || echo "FastAPI: Not running") && echo "" && echo "Venv: $VIRTUAL_ENV"'
```

**Reload bashrc:**
```bash
source ~/.bashrc
```

**Usage:**
```bash
cricket         # Navigate + Activate venv
cricket-start   # Start everything
cricket-stop    # Stop FastAPI + Deactivate venv
cricket-status  # Check all services
```

### 🎯 Terminal Tabs Setup

1. **Tab 1:** FastAPI server running (don't close!)
2. **Tab 2:** Database commands (`psql`, DBeaver)
3. **Tab 3:** Git, testing, general commands

### 📝 Keep DBeaver Connection Ready

- Don't kill/restart DBeaver repeatedly
- Keep it minimized in background
- Connection details already saved

### ⚡ Enable PostgreSQL Auto-Start (One-Time)

```bash
sudo systemctl enable postgresql@12-main
```
- PostgreSQL will auto-start on boot
- No need to manually start daily

### 🔍 Monitor Logs in Real-Time

```bash
# PostgreSQL logs
sudo journalctl -u postgresql@12-main -f

# In separate terminal, watch FastAPI output
# (The terminal where uvicorn is running)
```

### 💾 Database Backup (Recommended)

```bash
# Create backup
PGPASSWORD=admin pg_dump -h localhost -U admin cricket_auction > backup_$(date +%Y%m%d).sql

# Restore backup
PGPASSWORD=admin psql -h localhost -U admin cricket_auction < backup_20260221.sql
```

---

<div style="background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); padding: 20px; border-radius: 10px; color: white;">

## 🔗 Connection Strings & Configuration

</div>

### 📝 PostgreSQL Connection String

```
postgresql://admin:admin@localhost:5432/cricket_auction
```

### 🔑 .env File Template

```env
# Database Configuration
DATABASE_URL=postgresql://admin:admin@localhost:5432/cricket_auction
DB_HOST=localhost
DB_PORT=5432
DB_NAME=cricket_auction
DB_USER=admin
DB_PASSWORD=admin

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=true

# Security (Change in production!)
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 🗄️ DBeaver Connection Details

| Field | Value |
|-------|-------|
| 🏷️ **Connection Name** | Cricket Auction |
| 🖥️ **Host** | localhost |
| 🔌 **Port** | 5432 |
| 🗃️ **Database** | cricket_auction |
| 👤 **Username** | admin |
| 🔑 **Password** | admin |
| 🔐 **Save Password** | ✅ Yes |

---

<div style="background: linear-gradient(135deg, #ee9ca7 0%, #ffdde1 100%); padding: 20px; border-radius: 10px; color: #333;">

## 📊 Development Commands

</div>

### 📦 Python Package Management

```bash
# Install new package
pip install <package-name>

# Install specific version
pip install fastapi==0.115.0

# Update requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt

# Upgrade package
pip install --upgrade <package-name>

# List installed packages
pip list

# Show package info
pip show fastapi
```

### 🔄 Database Migrations (Alembic)

```bash
# Create new migration
alembic revision --autogenerate -m "Add users table"

# Apply migrations
alembic upgrade head

# Rollback last migration
alembic downgrade -1

# View migration history
alembic history

# Current migration version
alembic current
```

### 🧪 Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_players.py

# Run with coverage
pytest --cov=app tests/

# Run with verbose output
pytest -v

# Run and stop on first failure
pytest -x
```

### 📝 Code Quality

```bash
# Format code with black
black app/

# Lint with flake8
flake8 app/

# Type checking with mypy
mypy app/

# Sort imports
isort app/
```

---

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; color: white;">

## 🎯 Quick Reference Cheatsheet

</div>

### ⚡ Most Used Commands (Print & Keep!)

| Task | Command |
|------|---------|
| 🚀 **Start Dev Environment** | `cd ~/Documents/R\&D/Cricket\ Auctions/cricket-auction-platform/backend && source venv/bin/activate && uvicorn app.main:app --reload` |
| ❌ **Stop FastAPI** | `kill -9 $(lsof -ti:8000)` |
| 📊 **Check Status** | `pg_lsclusters && lsof -i:8000` |
| 🔄 **Restart PostgreSQL** | `sudo systemctl restart postgresql@12-main` |
| 🧪 **Test API** | `curl http://localhost:8000` |
| 🗄️ **Connect to DB** | `PGPASSWORD=admin psql -h localhost -U admin -d cricket_auction` |
| 🐍 **Activate venv** | `source venv/bin/activate` |
| 📦 **Install Package** | `pip install <package>` |
| 🔄 **Run Migration** | `alembic upgrade head` |
| 🧪 **Run Tests** | `pytest` |

---

<div style="background: #2c3e50; padding: 20px; border-radius: 10px; color: white;">

## 📞 Support & Documentation

</div>

### 📚 Related Documentation Files

- ✅ **CRICKET_AUCTION_COMPLETE_GUIDE.md** ← You are here!
- 📖 **Backend.md** - Initial setup guide
- 🗺️ **ROADMAP.md** - Project roadmap
- 📝 **cricket-auction-setup-guide.md** - Original setup

### 🆘 Getting Help

**PostgreSQL Issues:**
```bash
# Check logs
sudo journalctl -u postgresql@12-main -n 100

# Log file location
/var/log/postgresql/postgresql-12-main.log
```

**FastAPI Issues:**
- Check terminal output where `uvicorn` is running
- Check API logs in FastAPI stdout
- Enable debug mode: `uvicorn app.main:app --reload --log-level debug`

**Python Issues:**
```bash
# Verify venv active
echo $VIRTUAL_ENV

# Check installed packages
pip list

# Reinstall dependencies
pip install -r requirements.txt
```

---

<div align="center" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 10px; color: white;">

## 🏁 Summary

### ✅ System Status
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-ONLINE-success?style=flat-square)
![Database](https://img.shields.io/badge/Database-READY-success?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-RUNNING-success?style=flat-square)
![Status](https://img.shields.io/badge/Status-READY_TO_CODE-success?style=flat-square)

### 🚀 Quick Start
```bash
cd ~/Documents/R\&D/Cricket\ Auctions/cricket-auction-platform/backend
source venv/bin/activate
uvicorn app.main:app --reload
```

### 🌐 Access
- 🏠 API: http://localhost:8000
- 📚 Docs: http://localhost:8000/docs
- 🗄️ DB: localhost:5432

---

**🏏 Built with ❤️ using FastAPI + PostgreSQL**

**Last Updated:** 2026-02-21 | **Version:** 1.0.0

</div>

