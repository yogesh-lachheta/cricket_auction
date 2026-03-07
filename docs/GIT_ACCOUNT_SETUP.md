# 🔧 Git Multi-Account Setup Guide
**For: yogesh47 (Office) & yogesh-lachheta (Personal)**

---

## 🚀 TL;DR - Abhi Kis Account Par Ho? Kaise Switch Karein?

### ✅ Check Karne Ke Liye (Which Account Am I On?):
```bash
# Method 1: Simple check
git config user.email
git remote -v

# Method 2: Complete info (if functions loaded)
bash -c 'source ~/.bashrc && git-status-check'
```

### 🔄 Switch Karne Ke Liye (How to Switch?):

#### **Is Repository Ke Liye (Current Project Only)**:
```bash
# Personal account (yogesh-lachheta)
git config user.name "Yogesh Lachheta"
git config user.email "yogesh.lachheta111@gmail.com"
echo "✅ Switched to PERSONAL"

# Office account (yogesh47)
git config user.name "Yogesh Lachheta"
git config user.email "yogesh.lachheta@47billion.com"
echo "✅ Switched to OFFICE"
```

#### **Global Switch (All Projects)**:
```bash
# Personal account globally
git config --global user.name "Yogesh Lachheta"
git config --global user.email "yogesh.lachheta111@gmail.com"

# Office account globally
git config --global user.name "Yogesh Lachheta"
git config --global user.email "yogesh.lachheta@47billion.com"
```

#### **Using Aliases (If ~/.bashrc is sourced)**:
Open **NEW terminal** or run: `source ~/.bashrc`

```bash
# For this repo only
git-personal-here    # Switch to Personal
git-office-here      # Switch to Office

# For all repos (global)
git-personal         # Switch to Personal globally
git-office           # Switch to Office globally
```

### 📍 Current Status of THIS Repository:
```
✅ Account: PERSONAL (yogesh-lachheta)
📧 Email: yogesh.lachheta111@gmail.com
🔗 Remote: git@github-personal:yogesh-lachheta/cricket_auction.git
```

---

## 🔥 Ek Sath 2 Terminals Me 2 Alag GitHub Accounts Chalana

### ✅ Haan, Bilkul Possible Hai! Yeh Setup Already Ready Hai!

**Setup Kaise Kaam Karta Hai:**
- Alag SSH keys hai dono accounts ke liye
- Alag hosts hai (`github-office` aur `github-personal`)
- Dono terminals ek saath kaam kar sakte hain!

---

### 🎯 Step-by-Step: Dono Accounts Ek Sath Use Karna

#### **Terminal 1 - Office Work (yogesh47)**

```bash
# 1. Office project folder me jao
cd ~/Documents/work/office-project

# 2. Check/Set office account for this repo
git config --local user.name "Yogesh Lachheta"
git config --local user.email "yogesh.lachheta@47billion.com"

# 3. Set office remote (agar nahi hai to)
git remote set-url origin git@github-office:yogesh47/project-name.git

# 4. Verify
git config user.email
git remote -v

# 5. Ab normally kaam karo
git add .
git commit -m "Office work"
git push origin main
```

#### **Terminal 2 - Personal Work (yogesh-lachheta) - SAME TIME!**

```bash
# 1. Personal project folder me jao
cd ~/Documents/R&D/cricket_auction/backend

# 2. Check/Set personal account for this repo
git config --local user.name "Yogesh Lachheta"
git config --local user.email "yogesh.lachheta111@gmail.com"

# 3. Set personal remote (agar nahi hai to)
git remote set-url origin git@github-personal:yogesh-lachheta/cricket_auction.git

# 4. Verify
git config user.email
git remote -v

# 5. Ab normally kaam karo
git add .
git commit -m "Personal work"
git push origin master
```

---

### 🚀 Quick Setup Using Aliases (Fastest Method!)

Pehle ek baar `source ~/.bashrc` kar lo (ya naya terminal kholo)

#### **Terminal 1 - Office Setup:**
```bash
cd ~/Documents/work/office-project
git-office-here
git remote set-url origin git@github-office:yogesh47/project-name.git
```

#### **Terminal 2 - Personal Setup:**
```bash
cd ~/Documents/R&D/cricket_auction/backend
git-personal-here
git remote set-url origin git@github-personal:yogesh-lachheta/cricket_auction.git
```

**Done! Ab dono terminals me alag-alag accounts se kaam kar sakte ho!** ✅

---

### 🔍 Test Karna Hai? Yeh Karo:

**Terminal 1:**
```bash
ssh -T git@github-office
# Expected: Hi yogesh47! You've successfully authenticated...
```

**Terminal 2:**
```bash
ssh -T git@github-personal
# Expected: Hi yogesh-lachheta! You've successfully authenticated...
```

Dono commands ek sath different terminals me run kar sakte ho! 🎊

---

### 📊 Visual Guide: Ek Sath Kaam Karna

```
┌─────────────────────────────────┐    ┌─────────────────────────────────┐
│   Terminal 1 - OFFICE           │    │   Terminal 2 - PERSONAL         │
├─────────────────────────────────┤    ├─────────────────────────────────┤
│ $ cd ~/work/office-project      │    │ $ cd ~/cricket_auction/backend  │
│ $ git-office-here               │    │ $ git-personal-here             │
│ ✅ Switched to OFFICE           │    │ ✅ Switched to PERSONAL         │
│                                 │    │                                 │
│ $ git add .                     │    │ $ git add .                     │
│ $ git commit -m "Office work"   │    │ $ git commit -m "Personal work" │
│ $ git push origin main          │    │ $ git push origin master        │
│ ✅ Pushed to yogesh47           │    │ ✅ Pushed to yogesh-lachheta    │
└─────────────────────────────────┘    └─────────────────────────────────┘
        ↓                                       ↓
   github-office                          github-personal
   (yogesh47 account)                     (yogesh-lachheta account)
```

---

### 💡 Pro Tips for Simultaneous Work:

1. **Har Project Ka Apna Folder**: Office aur Personal projects alag folders me rakho
2. **Local Config Use Karo**: Har repo me `--local` config set karo (not global)
3. **Remote URL Check**: Hamesha `git remote -v` se verify karo
4. **Aliases Ka Use**: `git-office-here` aur `git-personal-here` sabse aasan hai

---

### ⚠️ Important Notes:

- **Global config mat use karo** jab dono accounts simultaneously chalane ho
- **Local config** har repository me set karo
- **Remote URL** sahi host use kare (`github-office` ya `github-personal`)
- **SSH keys already setup hai**, kuch aur karne ki zarurat nahi!

---

## 📌 Quick Reference

### Current SSH Configuration
```bash
# Personal GitHub Account
Host: github-personal
SSH Key: ~/.ssh/id_ed25519_personal

# Office GitHub Account (47billion)
Host: github-office
SSH Key: ~/.ssh/id_ed25519_office
```

---

## 🚀 EASIEST METHOD - Shell Functions (✅ Already Installed!)

Functions are already added to your `~/.bashrc`. Open a **NEW terminal** or run:
```bash
source ~/.bashrc
```

### 🎯 Super Simple Usage

#### Method 1: One Command Switch (Changes Remote + User)

**Switch to OFFICE account:**
```bash
git-switch-office yogesh47/project-name
```
**What it does:**
- Changes remote to: `git@github-office:yogesh47/project-name.git`
- Sets user name: "Yogesh (47billion)"
- Sets email: yogesh@47billion.com

**Switch to PERSONAL account:**
```bash
git-switch-personal yogesh-lachheta/cricket_auction
```
**What it does:**
- Changes remote to: `git@github-personal:yogesh-lachheta/cricket_auction.git`
- Sets user name: "Yogesh Lachheta"
- Sets email: yogesh.lachheta111@gmail.com

#### Method 2: Check Current Status
```bash
git-status-check
```
**Shows:** Current remote URL, user name, and email

#### Method 3: Test SSH Connections
```bash
git-test-ssh
```
**Tests:** Both office and personal SSH authentication

---

## 📝 Real Example Workflow

### Scenario 1: Working on Personal Project
```bash
# 1. Navigate to your project
cd ~/cricket_auction

# 2. Switch to personal account
git-switch-personal yogesh-lachheta/cricket_auction

# 3. Verify the switch
git-status-check

# 4. Make changes and push
git add .
git commit -m "Added new feature"
git push origin master
```

### Scenario 2: Working on Office Project
```bash
# 1. Navigate to office project
cd ~/work/office-project

# 2. Switch to office account
git-switch-office yogesh47/office-project

# 3. Verify the switch
git-status-check

# 4. Make changes and push
git add .
git commit -m "Fixed bug"
git push origin main
```

---

## 🔥 Available Functions & Aliases

### New Functions (Changes Remote + User):
| Command | What it does |
|---------|--------------|
| `git-switch-office yogesh47/repo` | Switch to office (changes remote + user) |
| `git-switch-personal yogesh-lachheta/repo` | Switch to personal (changes remote + user) |
| `git-status-check` | Show current config (remote + user) |
| `git-test-ssh` | Test SSH connections |

### Old Aliases (User Config Only):
| Command | What it does |
|---------|--------------|
| `git-office` | Change user to office (global) |
| `git-personal` | Change user to personal (global) |
| `git-office-here` | Change user to office (current project) |
| `git-personal-here` | Change user to personal (current project) |
| `git-whoami` | Show global & local config |
| `git-identity` | Show what will be used for commits |

---

## 📊 Comparison Table

| Method | Changes Remote URL | Changes User Config | Usage |
|--------|-------------------|---------------------|-------|
| `git-switch-office` | ✅ Yes | ✅ Yes | **Best for switching projects** |
| `git-switch-personal` | ✅ Yes | ✅ Yes | **Best for switching projects** |
| `git-office` | ❌ No | ✅ Yes (Global) | Quick user change only |
| `git-personal` | ❌ No | ✅ Yes (Global) | Quick user change only |
| `git-office-here` | ❌ No | ✅ Yes (Local) | Quick user change only |
| `git-personal-here` | ❌ No | ✅ Yes (Local) | Quick user change only |

---

## 🎬 Quick Demo

```bash
# Check current status
$ git-status-check
📍 Current Git Configuration:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Remote URL: git@github-personal:yogesh-lachheta/cricket_auction.git
User Name:  Yogesh Lachheta
User Email: yogesh.lachheta111@gmail.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Switch to office
$ git-switch-office yogesh47/work-project
✅ Switched to OFFICE account
Remote: git@github-office:yogesh47/work-project.git
User: Yogesh (47billion) <yogesh@47billion.com>

# Test SSH
$ git-test-ssh
🔑 Testing SSH Connections...

Office Account:
Hi yogesh47! You've successfully authenticated, but GitHub does not provide shell access.

Personal Account:
Hi yogesh-lachheta! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## 🏢 Office Project (yogesh47) - Setup & Push

### Step 1: Clone/Create Repository
```bash
# Option A: Clone existing office repo
git clone git@github-office:yogesh47/project-name.git

# Option B: Initialize new office repo
git init
git remote add origin git@github-office:yogesh47/project-name.git
```

### Step 2: Verify Remote URL
```bash
git remote -v
# Should show: git@github-office:yogesh47/project-name.git
```

### Step 3: Add & Commit Files
```bash
git add .
git commit -m "Your commit message"
```

### Step 4: Push to Office Account
```bash
git push origin master
# or
git push origin main
```

---

## 👤 Personal Project (yogesh-lachheta) - Setup & Push

### Step 1: Clone/Create Repository
```bash
# Option A: Clone existing personal repo
git clone git@github-personal:yogesh-lachheta/project-name.git

# Option B: Initialize new personal repo
git init
git remote add origin git@github-personal:yogesh-lachheta/project-name.git
```

### Step 2: Verify Remote URL
```bash
git remote -v
# Should show: git@github-personal:yogesh-lachheta/project-name.git
```

### Step 3: Add & Commit Files
```bash
git add .
git commit -m "Your commit message"
```

### Step 4: Push to Personal Account
```bash
git push origin master
# or
git push origin main
```

---

## 🔄 Switch Existing Repository (Multiple Methods)

### Method 1: Using Shell Functions (Easiest! - See Above)
```bash
# Switch to office
git-office yogesh47/project-name

# Switch to personal
git-personal yogesh-lachheta/project-name
```

### Method 2: Multiple Remotes (Keep Both!)
```bash
# Add both remotes to same repo
git remote add office git@github-office:yogesh47/project-name.git
git remote add personal git@github-personal:yogesh-lachheta/project-name.git

# Push to office account
git push office main

# Push to personal account
git push personal master

# Check all remotes
git remote -v
```

### Method 3: Manual Remote Change
#### Switch to Office Account:
```bash
git remote set-url origin git@github-office:yogesh47/project-name.git
git remote -v  # Verify
```

#### Switch to Personal Account:
```bash
git remote set-url origin git@github-personal:yogesh-lachheta/project-name.git
git remote -v  # Verify
```

---

## 🚨 Common Issues & Solutions

### Issue 1: Permission Denied Error
```
ERROR: Permission to yogesh-lachheta/repo.git denied to yogesh47
```

**Solution:** Wrong SSH host being used
```bash
# Check current remote
git remote -v

# Fix for personal repo
git remote set-url origin git@github-personal:yogesh-lachheta/repo-name.git

# Fix for office repo
git remote set-url origin git@github-office:yogesh47/repo-name.git
```

---

### Issue 2: Check Which Account Git Will Use
```bash
# Test personal account
ssh -T git@github-personal

# Test office account
ssh -T git@github-office
```

**Expected Response:**
```
Hi yogesh-lachheta! You've successfully authenticated...
Hi yogesh47! You've successfully authenticated...
```

---

### Issue 3: Wrong User Name/Email in Commits

#### For Office Projects:
```bash
git config user.name "Yogesh (47billion)"
git config user.email "yogesh@47billion.com"
```

#### For Personal Projects:
```bash
git config user.name "Yogesh Lachheta"
git config user.email "yogesh.lachheta111@gmail.com"
```

#### Check Current Config:
```bash
git config user.name
git config user.email
```

---

## 📋 Quick Checklist

### Before Pushing:
- [ ] Check remote URL: `git remote -v`
- [ ] Verify correct host: `github-office` or `github-personal`
- [ ] Check branch: `git branch`
- [ ] Check status: `git status`
- [ ] Test SSH: `ssh -T git@github-office` or `ssh -T git@github-personal`

---

## 🎯 One-Command Setup

### Office Project Quick Setup:
```bash
git init && \
git remote add origin git@github-office:yogesh47/PROJECT_NAME.git && \
git config user.name "Yogesh (47billion)" && \
git config user.email "yogesh@47billion.com"
```

### Personal Project Quick Setup:
```bash
git init && \
git remote add origin git@github-personal:yogesh-lachheta/PROJECT_NAME.git && \
git config user.name "Yogesh Lachheta" && \
git config user.email "yogesh.lachheta111@gmail.com"
```

---

## 📝 SSH Config File Location
`~/.ssh/config`

```ssh
# Personal GitHub Account
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes

# Office GitHub Account (47billion)
Host github-office
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_office
    IdentitiesOnly yes
```

---

## 💡 Pro Tips

1. **Always verify after switching:**
   ```bash
   git-status-check
   ```

2. **Use tab completion:**
   ```bash
   git-sw<TAB>  # Auto-completes to git-switch-
   ```

3. **Before pushing, double-check:**
   ```bash
   git remote -v
   git config user.email
   ```

4. **Test SSH before working:**
   ```bash
   git-test-ssh
   ```

5. **Use branch names wisely:**
   - Office: Usually `main` or `develop`
   - Personal: Usually `master` or `main`

6. **Check before you wreck:**
   ```bash
   git log --oneline -5  # See last 5 commits
   git diff origin/master  # See what will be pushed
   ```

---

## 🔍 Troubleshooting

### Functions not working?
```bash
# Reload bashrc
source ~/.bashrc

# Or open a NEW terminal window
```

### Wrong account error?
```bash
# Check current setup
git-status-check

# Switch to correct account
git-switch-personal yogesh-lachheta/repo-name
# or
git-switch-office yogesh47/repo-name
```

### Diagnostic Commands
```bash
# 1. Check SSH keys loaded
ssh-add -l

# 2. Test GitHub connection (or use git-test-ssh)
ssh -T git@github-personal
ssh -T git@github-office

# 3. Check Git configuration
git config --list | grep -E "(user|remote)"

# 4. Check all branches (local + remote)
git branch -a

# 5. See remote details
git remote show origin
```

---

## ⚡ Quick Reference Table

| Task | Office (yogesh47) | Personal (yogesh-lachheta) |
|------|-------------------|----------------------------|
| Clone | `git clone git@github-office:yogesh47/repo.git` | `git clone git@github-personal:yogesh-lachheta/repo.git` |
| Remote | `git@github-office:yogesh47/repo.git` | `git@github-personal:yogesh-lachheta/repo.git` |
| Test SSH | `ssh -T git@github-office` | `ssh -T git@github-personal` |
| SSH Key | `~/.ssh/id_ed25519_office` | `~/.ssh/id_ed25519_personal` |

---

## 📞 Need Help?

1. Check this guide first
2. Run diagnostic: `git remote -v && ssh -T git@github-office && ssh -T git@github-personal`
3. Check SSH config: `cat ~/.ssh/config`

---

**Last Updated:** March 7, 2026
**Author:** Claude Code
