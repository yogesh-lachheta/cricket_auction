# 🔀 Git Multiple Account Management Guide

![Git](https://img.shields.io/badge/Git-Multiple_Accounts-orange?style=for-the-badge&logo=git)
![GitHub](https://img.shields.io/badge/GitHub-2_Accounts-black?style=for-the-badge&logo=github)

**Office Account + Personal Account - Simple Switching**

**📌 Pre-configured for Yogesh Lachheta:**
- **Office:** yogesh.lachheta@47billion.com
- **Personal:** yogesh.lachheta111@gmail.com

All commands in this guide are already filled with your actual details!

---

## 📋 Table of Contents

1. [📊 Process Diagrams & Flowcharts](#-process-diagrams--flowcharts) ⭐ **NEW!**
2. [🔍 Current Configuration Check](#-current-configuration-check)
3. [⚡ One-Command Account Switch (RECOMMENDED)](#-one-command-account-switch-recommended)
4. [📂 Project-Specific Setup](#-project-specific-setup)
5. [🔐 SSH Key Setup (Recommended)](#-ssh-key-setup-recommended)
6. [🔑 Password/Token Management (HTTPS Method)](#-passwordtoken-management-https-method)
7. [🚀 Common Workflows](#-common-workflows)
8. [💡 Quick Reference](#-quick-reference)

---

## 📊 Visual Flow Diagrams (ASCII Format)

> **Note:** Ye diagrams directly markdown mein visible hain - code nahi, actual visual diagrams!

---

### 🗺️ Flow Diagram 1: Complete Setup Process (Start to Finish)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    🚀 GIT MULTI-ACCOUNT SETUP FLOW                          │
└─────────────────────────────────────────────────────────────────────────────┘

                              ┌──────────────┐
                              │   START ⚡   │
                              └──────┬───────┘
                                     │
                    ┌────────────────▼────────────────┐
                    │  PHASE 1: Initial Setup 📦      │
                    ├─────────────────────────────────┤
                    │  1. Install Git                 │
                    │     $ sudo apt install git      │
                    │                                 │
                    │  2. Setup ~/.bashrc Aliases     │
                    │     (git-office, git-personal)  │
                    │                                 │
                    │  3. Reload Bashrc               │
                    │     $ source ~/.bashrc          │
                    │                                 │
                    │  4. Set Global Default          │
                    │     $ git-office                │
                    └────────────────┬────────────────┘
                                     │
                    ┌────────────────▼────────────────┐
                    │  PHASE 2: SSH Key Setup 🔐      │
                    ├─────────────────────────────────┤
                    │  5. Create .ssh folder          │
                    │     $ mkdir -p ~/.ssh           │
                    │                                 │
                    │  6. Generate Personal Key       │
                    │     ssh-keygen ... personal     │
                    │                                 │
                    │  7. Generate Office Key         │
                    │     ssh-keygen ... office       │
                    │                                 │
                    │  8. Create SSH Config           │
                    │     ~/.ssh/config               │
                    │                                 │
                    │  9. Set Permissions             │
                    │     chmod 600/644               │
                    └────────────────┬────────────────┘
                                     │
                    ┌────────────────▼────────────────┐
                    │  PHASE 3: GitHub Config ☁️      │
                    ├─────────────────────────────────┤
                    │  10. Upload Personal Public Key │
                    │      → Personal GitHub          │
                    │                                 │
                    │  11. Upload Office Public Key   │
                    │      → Office GitHub            │
                    │                                 │
                    │  12. Test Personal SSH          │
                    │      $ ssh -T git@github-       │
                    │        personal                 │
                    │                                 │
                    │  13. Test Office SSH            │
                    │      $ ssh -T git@github-office │
                    └────────────────┬────────────────┘
                                     │
                    ┌────────────────▼────────────────┐
                    │  PHASE 4: Ready ✅              │
                    ├─────────────────────────────────┤
                    │  • Create/Clone Projects        │
                    │  • Switch Accounts as Needed    │
                    │  • Commit & Push                │
                    │  • Verify Before Each Commit    │
                    └────────────────┬────────────────┘
                                     │
                              ┌──────▼───────┐
                              │ COMPLETE! 🎉 │
                              └──────────────┘
```

---

### 🔷 Flow Diagram 2: Account Switching Process

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      🔄 ACCOUNT SWITCHING WORKFLOW                          │
└─────────────────────────────────────────────────────────────────────────────┘

                        ┌──────────────────────┐
                        │ Need to Switch? 🤔   │
                        └──────────┬───────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │   Which Scope?              │
                    │                             │
                    │   [1] Global (All Projects) │
                    │   [2] Local (This Project)  │
                    │   [3] Just Check Status     │
                    └──┬──────────┬───────────┬───┘
                       │          │           │
        ┌──────────────▼──┐  ┌───▼────┐  ┌──▼──────────────┐
        │ GLOBAL SWITCH   │  │ LOCAL  │  │ CHECK STATUS    │
        │ 🌍              │  │ SWITCH │  │ ℹ️               │
        │                 │  │ 📁     │  │                 │
        │ For Office:     │  │        │  │ Run:            │
        │ $ git-office    │  │ Office:│  │ $ git-whoami    │
        │                 │  │ $ git- │  │                 │
        │ Output:         │  │ office-│  │ Shows:          │
        │ ✅ Switched to  │  │ here   │  │ Global + Local  │
        │ OFFICE (Global) │  │        │  │ Config          │
        │                 │  │ Person:│  │                 │
        │ For Personal:   │  │ $ git- │  │ OR              │
        │ $ git-personal  │  │ person-│  │                 │
        │                 │  │ al-here│  │ $ git-identity  │
        │ Output:         │  │        │  │                 │
        │ ✅ Switched to  │  │ Output:│  │ Shows:          │
        │ PERSONAL (...)  │  │ ✅ Cur │  │ What will be    │
        └─────────┬───────┘  │ rent   │  │ used for commit │
                  │          │ proj → │  └─────────┬───────┘
                  │          │ OFFICE │            │
                  │          └───┬────┘            │
                  │              │                 │
                  └──────────────┼─────────────────┘
                                 │
                        ┌────────▼─────────┐
                        │ VERIFY! 🔍       │
                        │                  │
                        │ $ git-identity   │
                        │                  │
                        │ Check output:    │
                        │ Yogesh Lachheta  │
                        │ email@domain.com │
                        └────────┬─────────┘
                                 │
                        ┌────────▼─────────┐
                        │ Correct? ✅      │
                        │                  │
                        │ [YES] → Ready!   │
                        │ [NO]  → Try Again│
                        └──────────────────┘
```

---

### 🔷 Flow Diagram 3: New Project Setup

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       📁 NEW PROJECT SETUP FLOW                             │
└─────────────────────────────────────────────────────────────────────────────┘

                        ┌────────────────┐
                        │ New Project 📁 │
                        └────────┬───────┘
                                 │
                        ┌────────▼────────┐
                        │ Which Account?  │
                        └────┬───────┬────┘
                             │       │
              ┌──────────────▼┐     ┌▼─────────────┐
              │ OFFICE 🏢     │     │ PERSONAL 👤  │
              └───────┬───────┘     └──────┬───────┘
                      │                    │
    ┌─────────────────▼──────────┐  ┌──────▼────────────────┐
    │ OFFICE PROJECT STEPS       │  │ PERSONAL PROJECT STEPS│
    ├────────────────────────────┤  ├───────────────────────┤
    │                            │  │                       │
    │ 1️⃣ cd ~/office-project     │  │ 1️⃣ cd ~/my-app        │
    │                            │  │                       │
    │ 2️⃣ git init                │  │ 2️⃣ git init           │
    │                            │  │                       │
    │ 3️⃣ git-office-here         │  │ 3️⃣ git-personal-here  │
    │    Output:                 │  │    Output:            │
    │    ✅ Current project →    │  │    ✅ Current project│
    │    OFFICE                  │  │    → PERSONAL         │
    │                            │  │                       │
    │ 4️⃣ git-identity            │  │ 4️⃣ git-identity       │
    │    Verify:                 │  │    Verify:            │
    │    yogesh.lachheta@        │  │    yogesh.lachheta111 │
    │    47billion.com ✅        │  │    @gmail.com ✅      │
    │                            │  │                       │
    │ 5️⃣ git remote add origin   │  │ 5️⃣ git remote add     │
    │    git@github-office:      │  │    origin             │
    │    yogesh47/repo.git       │  │    git@github-        │
    │                            │  │    personal:yogesh-   │
    │                            │  │    lachheta/repo.git  │
    │ 6️⃣ git add .               │  │                       │
    │    git commit -m "..."     │  │ 6️⃣ git add .          │
    │                            │  │    git commit -m "..." │
    │ 7️⃣ git push -u origin main │  │                       │
    │                            │  │ 7️⃣ git push -u origin │
    │ 8️⃣ Verify on GitHub ✅     │  │    main               │
    │                            │  │                       │
    └────────────┬───────────────┘  │ 8️⃣ Verify on GitHub ✅│
                 │                  │                       │
                 │                  └───────────┬───────────┘
                 │                              │
                 └──────────────┬───────────────┘
                                │
                       ┌────────▼────────┐
                       │ SUCCESS! 🎉     │
                       │                 │
                       │ Project Ready   │
                       │ for Development │
                       └─────────────────┘
```

---

### 🔷 Flow Diagram 4: Daily Commit Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    💻 DAILY COMMIT PROCESS FLOW                             │
└─────────────────────────────────────────────────────────────────────────────┘

                    ┌──────────────────────┐
                    │ Ready to Commit? 💾  │
                    └──────────┬───────────┘
                               │
                ┌──────────────▼──────────────┐
                │ ⚠️ MANDATORY PRE-CHECK      │
                │                             │
                │ $ git-identity              │
                │                             │
                │ Output:                     │
                │ Yogesh Lachheta             │
                │ email@domain.com            │
                └──────────┬──────────────────┘
                           │
                  ┌────────▼────────┐
                  │ Correct Account?│
                  └────┬───────┬────┘
                       │       │
              ┌────────▼──┐  ┌▼────────────┐
              │ YES ✅    │  │ NO ❌       │
              └────┬──────┘  └──┬──────────┘
                   │            │
                   │         ┌──▼───────────────┐
                   │         │ FIX IT NOW! 🔧   │
                   │         │                  │
                   │         │ For Office:      │
                   │         │ $ git-office-here│
                   │         │                  │
                   │         │ For Personal:    │
                   │         │ $ git-personal-  │
                   │         │   here           │
                   │         └──┬───────────────┘
                   │            │
                   │        ┌───▼──────────┐
                   │        │ Verify Again │
                   │        │ git-identity │
                   │        └───┬──────────┘
                   │            │
                   └────────────┘
                   │
        ┌──────────▼─────────┐
        │ STAGE CHANGES 📋  │
        │                    │
        │ $ git status       │
        │ $ git add .        │
        │ $ git status       │
        └──────────┬─────────┘
                   │
        ┌──────────▼─────────┐
        │ COMMIT 💾          │
        │                    │
        │ $ git commit -m    │
        │   "description"    │
        │                    │
        │ Commit created:    │
        │ ✅ Author: Yogesh  │
        │ ✅ Email: verified │
        └──────────┬─────────┘
                   │
        ┌──────────▼─────────┐
        │ PUSH TO GITHUB 📤  │
        │                    │
        │ $ git push origin  │
        │   main             │
        │                    │
        │ SSH authenticates  │
        │ automatically 🔐   │
        └──────────┬─────────┘
                   │
            ┌──────▼──────┐
            │ Success? ✅ │
            └──┬───────┬──┘
               │       │
        ┌──────▼──┐  ┌▼────────────┐
        │ YES 🎉 │  │ NO - Error ❌│
        └────┬───┘  └──┬───────────┘
             │         │
             │      ┌──▼───────────────┐
             │      │ TROUBLESHOOT 🚨  │
             │      │                  │
             │      │ Read error       │
             │      │ Check SSH keys   │
             │      │ Check network    │
             │      │ Try again        │
             │      └──────────────────┘
             │
    ┌────────▼────────┐
    │ VERIFY 🔍       │
    │                 │
    │ • Open GitHub   │
    │ • Check commit  │
    │ • Verify author │
    └────────┬────────┘
             │
      ┌──────▼──────┐
      │ COMPLETE! ✅│
      └─────────────┘
```

---

### 🔷 Flow Diagram 5: Troubleshooting Common Errors

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    🚨 ERROR TROUBLESHOOTING FLOW                            │
└─────────────────────────────────────────────────────────────────────────────┘

                        ┌────────────────┐
                        │ Error Occurred │
                        │      ⚠️         │
                        └────────┬───────┘
                                 │
                    ┌────────────▼────────────┐
                    │   What's the Error?     │
                    │                         │
                    │ [1] command not found   │
                    │ [2] Permission denied   │
                    │ [3] Wrong commit author │
                    │ [4] Push rejected       │
                    └┬──┬──────────┬──────┬───┘
                     │  │          │      │
    ┌────────────────▼┐ │          │      │
    │ ERROR 1:        │ │          │      │
    │ command not     │ │          │      │
    │ found           │ │          │      │
    ├─────────────────┤ │          │      │
    │                 │ │          │      │
    │ Try:            │ │          │      │
    │ $ source        │ │          │      │
    │   ~/.bashrc     │ │          │      │
    │                 │ │          │      │
    │ If still fails: │ │          │      │
    │ • Check aliases │ │          │      │
    │   in .bashrc    │ │          │      │
    │ • Open new      │ │          │      │
    │   terminal      │ │          │      │
    │                 │ │          │      │
    │ ✅ Fixed!       │ │          │      │
    └─────────────────┘ │          │      │
                        │          │      │
         ┌──────────────▼┐         │      │
         │ ERROR 2:      │         │      │
         │ Permission    │         │      │
         │ denied        │         │      │
         ├───────────────┤         │      │
         │               │         │      │
         │ Check keys:   │         │      │
         │ $ ssh-add -l  │         │      │
         │               │         │      │
         │ If empty:     │         │      │
         │ $ eval ssh-   │         │      │
         │   agent -s    │         │      │
         │ $ ssh-add ... │         │      │
         │               │         │      │
         │ Test:         │         │      │
         │ $ ssh -T git@ │         │      │
         │   github-*    │         │      │
         │               │         │      │
         │ ✅ Fixed!     │         │      │
         └───────────────┘         │      │
                                   │      │
                  ┌────────────────▼┐     │
                  │ ERROR 3:        │     │
                  │ Wrong author    │     │
                  ├─────────────────┤     │
                  │                 │     │
                  │ Already pushed? │     │
                  │                 │     │
                  │ NO:             │     │
                  │ 1. Switch account│    │
                  │    git-office-  │     │
                  │    here         │     │
                  │ 2. Amend commit │     │
                  │    git commit   │     │
                  │    --amend ...  │     │
                  │                 │     │
                  │ YES:            │     │
                  │ ⚠️ Can't fix    │     │
                  │ Be careful next │     │
                  │ time!           │     │
                  │                 │     │
                  │ ✅ Fixed/Learned│     │
                  └─────────────────┘     │
                                          │
                           ┌──────────────▼┐
                           │ ERROR 4:      │
                           │ Push rejected │
                           ├───────────────┤
                           │               │
                           │ Reason:       │
                           │ Remote has    │
                           │ changes       │
                           │               │
                           │ Fix:          │
                           │ $ git pull    │
                           │   --rebase    │
                           │               │
                           │ Resolve       │
                           │ conflicts     │
                           │               │
                           │ $ git push    │
                           │               │
                           │ ✅ Fixed!     │
                           └───────────────┘
                                  │
                         ┌────────▼────────┐
                         │ RESOLVED! 🎉    │
                         │                 │
                         │ Continue working│
                         └─────────────────┘
```

---

### 🔷 Flow Diagram 6: System Format Recovery

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    💾 SYSTEM FORMAT RECOVERY FLOW                           │
└─────────────────────────────────────────────────────────────────────────────┘

                       ┌───────────────────┐
                       │ System Formatted  │
                       │       💥          │
                       └────────┬──────────┘
                                │
                       ┌────────▼─────────┐
                       │ Had Backup? 🔍   │
                       └────┬──────────┬──┘
                            │          │
              ┌─────────────▼┐      ┌─▼────────────┐
              │ YES ✅       │      │ NO ❌        │
              │ Backup exists│      │ No backup    │
              └──────┬───────┘      └──┬───────────┘
                     │                 │
    ┌────────────────▼──────────┐      │
    │ RESTORE FROM BACKUP ♻️    │      │
    ├───────────────────────────┤      │
    │                           │      │
    │ 1. Locate backup          │      │
    │    (USB/Cloud)            │      │
    │                           │      │
    │ 2. Copy .ssh folder       │      │
    │    $ cp -r backup/.ssh ~/ │      │
    │                           │      │
    │ 3. Copy .gitconfig        │      │
    │    $ cp backup/.gitconfig │      │
    │       ~/                  │      │
    │                           │      │
    │ 4. Copy .bashrc aliases   │      │
    │                           │      │
    │ 5. Set permissions        │      │
    │    $ chmod 700 ~/.ssh     │      │
    │    $ chmod 600 ...        │      │
    │                           │      │
    │ 6. Start SSH agent        │      │
    │    $ eval ssh-agent -s    │      │
    │    $ ssh-add ~/.ssh/id_*  │      │
    │                           │      │
    │ 7. Test SSH               │      │
    │    $ ssh -T git@github-*  │      │
    │                           │      │
    │ ✅ RESTORED!              │      │
    │ Same keys working!        │      │
    └───────────┬───────────────┘      │
                │                      │
                │    ┌─────────────────▼────────────┐
                │    │ FRESH SETUP REQUIRED 🆕     │
                │    ├────────────────────────────  │
                │    │                              │
                │    │ 1. Install Git               │
                │    │    $ sudo apt install git    │
                │    │                              │
                │    │ 2. Setup .bashrc aliases     │
                │    │                              │
                │    │ 3. Reload bashrc             │
                │    │    $ source ~/.bashrc        │
                │    │                              │
                │    │ 4. Generate NEW SSH keys     │
                │    │    (Different from old!)     │
                │    │    ssh-keygen ...personal    │
                │    │    ssh-keygen ...office      │
                │    │                              │
                │    │ 5. Create SSH config         │
                │    │    ~/.ssh/config             │
                │    │                              │
                │    │ 6. Set permissions           │
                │    │                              │
                │    │ 7. Upload NEW public keys    │
                │    │    to GitHub                 │
                │    │                              │
                │    │ 8. Delete OLD keys from      │
                │    │    GitHub (Settings)         │
                │    │                              │
                │    │ 9. Test new SSH              │
                │    │    $ ssh -T git@github-*     │
                │    │                              │
                │    │ 10. BACKUP immediately! 💾   │
                │    │     (Don't repeat mistake)   │
                │    │                              │
                │    │ ✅ FRESH SETUP COMPLETE!     │
                │    └──────────────┬───────────────┘
                │                   │
                └───────────────────┘
                            │
                ┌───────────▼──────────┐
                │ POST-RECOVERY TASKS  │
                ├──────────────────────┤
                │                      │
                │ 1. Set global        │
                │    account           │
                │    $ git-office      │
                │                      │
                │ 2. Clone/Navigate    │
                │    to projects       │
                │                      │
                │ 3. Set local         │
                │    accounts          │
                │    $ git-office-here │
                │                      │
                │ 4. Verify            │
                │    $ git-whoami      │
                │    $ git-identity    │
                │                      │
                │ 5. CREATE BACKUP!    │
                │    IMMEDIATELY! 💾   │
                └───────────┬──────────┘
                            │
                     ┌──────▼──────┐
                     │ RECOVERED! 🎉│
                     │             │
                     │ Ready for   │
                     │ development │
                     └─────────────┘
```

---

## 📊 Process Diagrams & Flowcharts

```mermaid
flowchart TD
    Start([🚀 Start: Multi-Account Git Setup]) --> CheckGit{Git Installed?}

    CheckGit -->|No| InstallGit[📦 Install Git<br/>sudo apt install git -y]
    CheckGit -->|Yes| SetupBashrc
    InstallGit --> SetupBashrc

    SetupBashrc[📝 Setup .bashrc Aliases<br/>git-office, git-personal, etc.]
    SetupBashrc --> ReloadBashrc[🔄 Reload Bashrc<br/>source ~/.bashrc]

    ReloadBashrc --> TestAliases{Test Aliases?<br/>git-office}
    TestAliases -->|command not found| SetupBashrc
    TestAliases -->|✅ Works| SetGlobal

    SetGlobal[🌍 Set Global Default<br/>git-office]
    SetGlobal --> VerifyGlobal[🔍 Verify<br/>git-whoami]

    VerifyGlobal --> SSHorHTTPS{Choose Method}

    SSHorHTTPS -->|🔐 SSH<br/>Recommended| SSHSetup
    SSHorHTTPS -->|🔑 HTTPS| HTTPSSetup

    %% SSH Path
    SSHSetup[🔑 Generate SSH Keys<br/>Personal + Office]
    SSHSetup --> CreateConfig[📝 Create SSH Config<br/>~/.ssh/config]
    CreateConfig --> SetPermissions[🔒 Set Permissions<br/>chmod 600/644]
    SetPermissions --> StartAgent[🔧 Start SSH Agent<br/>ssh-add keys]
    StartAgent --> UploadKeys[📤 Upload Public Keys<br/>to GitHub]
    UploadKeys --> TestSSH{Test SSH<br/>ssh -T git@github-*}
    TestSSH -->|❌ Failed| CheckKeys[🔍 Check Keys Loaded<br/>ssh-add -l]
    CheckKeys --> StartAgent
    TestSSH -->|✅ Success| Ready

    %% HTTPS Path
    HTTPSSetup[🔑 Generate Personal Access Tokens<br/>GitHub Settings]
    HTTPSSetup --> ConfigCred[⚙️ Configure Credential Helper<br/>cache/store/manager]
    ConfigCred --> FirstPush[🚀 First Push<br/>Enter token]
    FirstPush --> Ready

    Ready([✅ Setup Complete!<br/>Ready to Use])

    style Start fill:#4CAF50,stroke:#2E7D32,color:#fff
    style Ready fill:#4CAF50,stroke:#2E7D32,color:#fff
    style SSHSetup fill:#2196F3,stroke:#1565C0,color:#fff
    style HTTPSSetup fill:#FF9800,stroke:#E65100,color:#fff
```

---

### 🔄 Daily Usage Workflow

```mermaid
flowchart LR
    Start([Start Working]) --> CheckProject{New or<br/>Existing Project?}

    CheckProject -->|New| InitGit[git init]
    CheckProject -->|Existing| CloneRepo[git clone]

    InitGit --> SetAccount
    CloneRepo --> SetAccount

    SetAccount{Which Account?}
    SetAccount -->|Office| SetOffice[git-office-here]
    SetAccount -->|Personal| SetPersonal[git-personal-here]

    SetOffice --> Verify
    SetPersonal --> Verify

    Verify[🔍 VERIFY!<br/>git-identity]
    Verify --> CheckCorrect{Correct<br/>Account?}

    CheckCorrect -->|❌ No| SetAccount
    CheckCorrect -->|✅ Yes| AddRemote

    AddRemote{Remote<br/>Exists?}
    AddRemote -->|No| AddRemoteCmd
    AddRemote -->|Yes| Work

    AddRemoteCmd[Add Remote<br/>git@github-office: OR<br/>git@github-personal:]
    AddRemoteCmd --> Work

    Work([💻 Work on Code])
    Work --> Commit[git add .<br/>git commit -m '...']
    Commit --> Push[git push]
    Push --> Done([✅ Done!])

    style Start fill:#4CAF50,stroke:#2E7D32,color:#fff
    style Verify fill:#FF5722,stroke:#D84315,color:#fff
    style Done fill:#4CAF50,stroke:#2E7D32,color:#fff
```

---

### 🌳 New Project Setup - Decision Tree

```mermaid
flowchart TD
    Start([📁 New Project]) --> ProjectType{Project Type?}

    ProjectType -->|🏢 Office Work| OfficeFlow
    ProjectType -->|👤 Personal| PersonalFlow
    ProjectType -->|🤔 Not Sure| CheckOrg

    CheckOrg[Check:<br/>Company project?<br/>Work hours?<br/>Office repo?]
    CheckOrg -->|Yes| OfficeFlow
    CheckOrg -->|No| PersonalFlow

    %% Office Flow
    OfficeFlow[Office Project]
    OfficeFlow --> OfficeSteps[1️⃣ cd project-folder<br/>2️⃣ git init<br/>3️⃣ git-office-here<br/>4️⃣ git-identity ✅]
    OfficeSteps --> OfficeRemote[5️⃣ git remote add origin<br/>git@github-office:yogesh47/repo.git]
    OfficeRemote --> OfficeCommit[6️⃣ git add .<br/>7️⃣ git commit -m 'msg'<br/>8️⃣ git push -u origin main]
    OfficeCommit --> OfficeDone([✅ Office Project Ready])

    %% Personal Flow
    PersonalFlow[Personal Project]
    PersonalFlow --> PersonalSteps[1️⃣ cd project-folder<br/>2️⃣ git init<br/>3️⃣ git-personal-here<br/>4️⃣ git-identity ✅]
    PersonalSteps --> PersonalRemote[5️⃣ git remote add origin<br/>git@github-personal:yogesh-lachheta/repo.git]
    PersonalRemote --> PersonalCommit[6️⃣ git add .<br/>7️⃣ git commit -m 'msg'<br/>8️⃣ git push -u origin main]
    PersonalCommit --> PersonalDone([✅ Personal Project Ready])

    style Start fill:#2196F3,stroke:#1565C0,color:#fff
    style OfficeFlow fill:#FF9800,stroke:#E65100,color:#fff
    style PersonalFlow fill:#9C27B0,stroke:#6A1B9A,color:#fff
    style OfficeDone fill:#4CAF50,stroke:#2E7D32,color:#fff
    style PersonalDone fill:#4CAF50,stroke:#2E7D32,color:#fff
```

---

### ⚡ Account Switching Process

```mermaid
flowchart TD
    Start([Need to Switch Account]) --> SwitchType{Switch Scope?}

    SwitchType -->|🌍 All Projects<br/>Global| GlobalSwitch
    SwitchType -->|📁 This Project Only<br/>Local| LocalSwitch
    SwitchType -->|🔍 Just Check| CheckOnly

    %% Global Switch
    GlobalSwitch{Switch To?}
    GlobalSwitch -->|Office| CmdGlobalOffice[Run: git-office]
    GlobalSwitch -->|Personal| CmdGlobalPersonal[Run: git-personal]

    CmdGlobalOffice --> OutputGlobalOffice[Output:<br/>✅ Switched to OFFICE Global]
    CmdGlobalPersonal --> OutputGlobalPersonal[Output:<br/>✅ Switched to PERSONAL Global]

    OutputGlobalOffice --> VerifyGlobal
    OutputGlobalPersonal --> VerifyGlobal

    %% Local Switch
    LocalSwitch{Switch To?}
    LocalSwitch -->|Office| CmdLocalOffice[Run: git-office-here]
    LocalSwitch -->|Personal| CmdLocalPersonal[Run: git-personal-here]

    CmdLocalOffice --> OutputLocalOffice[Output:<br/>✅ Current project → OFFICE]
    CmdLocalPersonal --> OutputLocalPersonal[Output:<br/>✅ Current project → PERSONAL]

    OutputLocalOffice --> VerifyLocal
    OutputLocalPersonal --> VerifyLocal

    %% Verification
    VerifyGlobal[Verify: git-whoami]
    VerifyLocal[Verify: git-identity]
    CheckOnly[Run: git-whoami<br/>or git-identity]

    VerifyGlobal --> CheckResult
    VerifyLocal --> CheckResult
    CheckOnly --> CheckResult

    CheckResult{Correct<br/>Account?}
    CheckResult -->|✅ Yes| Done([✅ Switch Complete!])
    CheckResult -->|❌ No| SwitchType

    style Start fill:#2196F3,stroke:#1565C0,color:#fff
    style Done fill:#4CAF50,stroke:#2E7D32,color:#fff
    style CmdGlobalOffice fill:#FF9800,stroke:#E65100,color:#fff
    style CmdGlobalPersonal fill:#9C27B0,stroke:#6A1B9A,color:#fff
```

---

### 🚨 Troubleshooting Flowchart

```mermaid
flowchart TD
    Start([⚠️ Problem Occurred]) --> ProblemType{What's the Issue?}

    ProblemType -->|git-office not found| AliasIssue
    ProblemType -->|SSH asks password| SSHIssue
    ProblemType -->|Wrong account in commit| CommitIssue
    ProblemType -->|Permission denied| PermissionIssue

    %% Alias Issue
    AliasIssue[git-office: command not found]
    AliasIssue --> ReloadBash[Try: source ~/.bashrc]
    ReloadBash --> TestAlias{Works Now?}
    TestAlias -->|✅ Yes| Fixed1
    TestAlias -->|❌ No| CheckBashrc[Check: tail -20 ~/.bashrc]
    CheckBashrc --> AliasExists{Aliases<br/>Exist?}
    AliasExists -->|No| AddAlias[Add Aliases to .bashrc<br/>See Setup Section]
    AliasExists -->|Yes| NewTerminal[Open New Terminal]
    AddAlias --> ReloadBash
    NewTerminal --> Fixed1

    %% SSH Issue
    SSHIssue[SSH asks for password]
    SSHIssue --> CheckKeys[Run: ssh-add -l]
    CheckKeys --> KeysLoaded{Keys Listed?}
    KeysLoaded -->|No| AddKeys[Run: eval ssh-agent -s<br/>ssh-add ~/.ssh/id_ed25519_*]
    KeysLoaded -->|Yes| TestConnection[Run: ssh -T git@github-*]
    AddKeys --> TestConnection
    TestConnection --> SSHWorks{Connected?}
    SSHWorks -->|✅ Yes| Fixed2
    SSHWorks -->|❌ No| CheckGitHub[Check: Public key<br/>uploaded to GitHub?]
    CheckGitHub --> UploadKey[Upload public key<br/>to GitHub Settings]
    UploadKey --> TestConnection

    %% Commit Issue
    CommitIssue[Wrong account in commit]
    CommitIssue --> Pushed{Already<br/>Pushed?}
    Pushed -->|No ✅| FixCommit[1. git-office-here<br/>2. git commit --amend<br/>--reset-author --no-edit]
    Pushed -->|Yes ⚠️| CantFix[Can't fix easily<br/>Be careful next time]
    FixCommit --> Fixed3
    CantFix --> LearnLesson[Lesson: Always run<br/>git-identity before commit]
    LearnLesson --> Done

    %% Permission Issue
    PermissionIssue[Permission denied publickey]
    PermissionIssue --> CheckSSHKeys[Check SSH keys exist:<br/>ls ~/.ssh/]
    CheckSSHKeys --> KeysExist{Keys Exist?}
    KeysExist -->|No| GenerateKeys[Generate new keys<br/>See SSH Setup Section]
    KeysExist -->|Yes| CheckAgent[Check SSH agent:<br/>ssh-add -l]
    GenerateKeys --> CheckAgent
    CheckAgent --> AgentRunning{Agent has keys?}
    AgentRunning -->|No| StartAgentFix[eval ssh-agent -s<br/>ssh-add keys]
    AgentRunning -->|Yes| CheckRemote[Check remote URL:<br/>git remote -v]
    StartAgentFix --> CheckRemote
    CheckRemote --> CorrectHost{Using correct<br/>github-office/<br/>github-personal?}
    CorrectHost -->|No| FixRemote[git remote set-url origin<br/>git@github-CORRECT:user/repo]
    CorrectHost -->|Yes| CheckPermissions[Check permissions:<br/>ls -l ~/.ssh/]
    FixRemote --> Fixed4
    CheckPermissions --> FixPerms[chmod 600 ~/.ssh/id_*<br/>chmod 644 ~/.ssh/*.pub]
    FixPerms --> Fixed4

    Fixed1([✅ Fixed: Aliases Working])
    Fixed2([✅ Fixed: SSH Working])
    Fixed3([✅ Fixed: Commit Corrected])
    Fixed4([✅ Fixed: Permission OK])

    Fixed1 --> Done
    Fixed2 --> Done
    Fixed3 --> Done
    Fixed4 --> Done

    Done([✅ Problem Resolved!])

    style Start fill:#FF5722,stroke:#D84315,color:#fff
    style Fixed1 fill:#4CAF50,stroke:#2E7D32,color:#fff
    style Fixed2 fill:#4CAF50,stroke:#2E7D32,color:#fff
    style Fixed3 fill:#4CAF50,stroke:#2E7D32,color:#fff
    style Fixed4 fill:#4CAF50,stroke:#2E7D32,color:#fff
    style Done fill:#4CAF50,stroke:#2E7D32,color:#fff
```

---

### 🏗️ System Architecture Diagram

```mermaid
flowchart TB
    subgraph Local["💻 Your Computer /home/billion/"]
        direction TB

        subgraph Bashrc["📝 ~/.bashrc"]
            Aliases["Git Aliases:<br/>• git-personal<br/>• git-office<br/>• git-whoami<br/>• git-identity"]
        end

        subgraph SSHFolder["🔐 ~/.ssh/"]
            PrivatePersonal["🔑 id_ed25519_personal<br/>Private Key SECRET"]
            PublicPersonal["🔓 id_ed25519_personal.pub<br/>Public Key"]
            PrivateOffice["🔑 id_ed25519_office<br/>Private Key SECRET"]
            PublicOffice["🔓 id_ed25519_office.pub<br/>Public Key"]
            SSHConfig["⚙️ config<br/>Host mappings"]
        end

        subgraph GitConfig["⚙️ Git Configuration"]
            GlobalConfig["🌍 ~/.gitconfig<br/>Global Settings"]
            LocalConfig["📁 .git/config<br/>Project Settings"]
        end

        subgraph Projects["📂 Projects"]
            OfficeProj["🏢 Office Projects<br/>~/Documents/R&D/"]
            PersonalProj["👤 Personal Projects<br/>~/projects/"]
        end
    end

    subgraph GitHub["☁️ GitHub Servers"]
        direction TB

        subgraph PersonalGH["👤 Personal Account<br/>yogesh-lachheta"]
            PersonalRepos["📚 Repositories"]
            PersonalKeys["🔓 SSH Keys<br/>id_ed25519_personal.pub"]
        end

        subgraph OfficeGH["🏢 Office Account<br/>yogesh47 47billion"]
            OfficeRepos["📚 Repositories"]
            OfficeKeys["🔓 SSH Keys<br/>id_ed25519_office.pub"]
        end
    end

    %% Connections
    Aliases -.->|Controls| GlobalConfig
    Aliases -.->|Controls| LocalConfig

    SSHConfig -->|Maps| PrivatePersonal
    SSHConfig -->|Maps| PrivateOffice

    PrivatePersonal -->|Authenticates with| PersonalKeys
    PrivateOffice -->|Authenticates with| OfficeKeys

    PersonalProj -->|Uses| PrivatePersonal
    PersonalProj -->|Pushes to| PersonalRepos

    OfficeProj -->|Uses| PrivateOffice
    OfficeProj -->|Pushes to| OfficeRepos

    PublicPersonal -.->|Uploaded to| PersonalKeys
    PublicOffice -.->|Uploaded to| OfficeKeys

    style Local fill:#E3F2FD,stroke:#1976D2
    style GitHub fill:#FFF3E0,stroke:#F57C00
    style Bashrc fill:#C8E6C9,stroke:#388E3C
    style SSHFolder fill:#FFCDD2,stroke:#C62828
    style GitConfig fill:#F8BBD0,stroke:#C2185B
    style PersonalGH fill:#E1BEE7,stroke:#7B1FA2
    style OfficeGH fill:#FFE0B2,stroke:#E65100
```

---

### 🔄 SSH Authentication Flow

```mermaid
sequenceDiagram
    participant You as 💻 You
    participant Git as 🔧 Git
    participant SSH as 🔐 SSH Client
    participant Agent as 🔑 SSH Agent
    participant GitHub as ☁️ GitHub

    Note over You,GitHub: Office Project Push Scenario

    You->>Git: git push origin main
    Git->>SSH: Connect to git@github-office:yogesh47/repo

    SSH->>SSH: Check ~/.ssh/config
    Note over SSH: Host github-office<br/>IdentityFile id_ed25519_office

    SSH->>Agent: Get private key: id_ed25519_office
    Agent-->>SSH: Here's the key 🔑

    SSH->>GitHub: Connect with signed request
    Note over SSH,GitHub: Using id_ed25519_office

    GitHub->>GitHub: Verify signature with<br/>stored public key

    alt ✅ Key Matches
        GitHub-->>SSH: Authentication successful
        SSH-->>Git: Connection established
        Git-->>You: Push successful! ✅
    else ❌ Key Doesn't Match
        GitHub-->>SSH: Permission denied
        SSH-->>Git: Authentication failed
        Git-->>You: Error: Permission denied (publickey) ❌
    end

    Note over You,GitHub: No password needed! 🎉
```

---

### 📊 Before Commit - Verification Process

```mermaid
flowchart TD
    Start([Ready to Commit]) --> BeforeCommit[⚠️ STOP!<br/>Verify First]

    BeforeCommit --> RunIdentity[Run: git-identity]
    RunIdentity --> ShowsAccount[Shows:<br/>Yogesh Lachheta<br/>email@domain.com]

    ShowsAccount --> CheckEmail{Is this the<br/>CORRECT account<br/>for this project?}

    CheckEmail -->|✅ Yes, Correct| SafeCommit[Proceed Safely]
    CheckEmail -->|❌ No, Wrong!| FixNow[🚨 FIX NOW!]
    CheckEmail -->|🤔 Not Sure| CheckProject

    CheckProject[Ask Yourself:<br/>• Is this office work?<br/>• Personal project?<br/>• Which GitHub account?]
    CheckProject --> Decide{Decide}
    Decide -->|Office| NeedOffice
    Decide -->|Personal| NeedPersonal

    FixNow --> WhichNeeded{Which Account<br/>Needed?}
    WhichNeeded -->|Office| NeedOffice
    WhichNeeded -->|Personal| NeedPersonal

    NeedOffice[Run: git-office-here]
    NeedPersonal[Run: git-personal-here]

    NeedOffice --> Verify[Verify Again:<br/>git-identity]
    NeedPersonal --> Verify

    Verify --> VerifyResult{Correct Now?}
    VerifyResult -->|✅ Yes| SafeCommit
    VerifyResult -->|❌ Still No| FixNow

    SafeCommit --> Commit[git add .<br/>git commit -m 'message']
    Commit --> Push[git push]
    Push --> Success([✅ Committed with<br/>Correct Account!])

    style Start fill:#2196F3,stroke:#1565C0,color:#fff
    style BeforeCommit fill:#FF5722,stroke:#D84315,color:#fff
    style FixNow fill:#FF9800,stroke:#E65100,color:#fff
    style Success fill:#4CAF50,stroke:#2E7D32,color:#fff
```

---

### 🎯 Quick Reference - Command Decision Tree

```mermaid
flowchart TD
    Start([What do you want to do?]) --> Action{Choose Action}

    Action -->|🔄 Switch Account| Switch
    Action -->|🔍 Check Status| Check
    Action -->|📁 New Project| NewProj
    Action -->|🔧 Fix Problem| Fix

    %% Switch Path
    Switch{Switch Where?}
    Switch -->|🌍 All Projects| GlobalSwitch[Use: git-office<br/>or git-personal]
    Switch -->|📁 This Project| LocalSwitch[Use: git-office-here<br/>or git-personal-here]
    GlobalSwitch --> Done1
    LocalSwitch --> Done1

    %% Check Path
    Check{What to Check?}
    Check -->|📊 See All Config| UseWhoami[Use: git-whoami]
    Check -->|✅ Before Commit| UseIdentity[Use: git-identity]
    UseWhoami --> Done2
    UseIdentity --> Done2

    %% New Project Path
    NewProj{Project Type?}
    NewProj -->|🏢 Office| OfficeSetup[1. cd project<br/>2. git init<br/>3. git-office-here<br/>4. git-identity]
    NewProj -->|👤 Personal| PersonalSetup[1. cd project<br/>2. git init<br/>3. git-personal-here<br/>4. git-identity]
    OfficeSetup --> Done3
    PersonalSetup --> Done3

    %% Fix Path
    Fix{What's Broken?}
    Fix -->|Aliases not working| FixAlias[source ~/.bashrc]
    Fix -->|SSH not working| FixSSH[ssh-add -l<br/>ssh-add ~/.ssh/id_*]
    Fix -->|Wrong account| FixAccount[git-office-here<br/>or git-personal-here]
    FixAlias --> Done4
    FixSSH --> Done4
    FixAccount --> Done4

    Done1([✅ Account Switched])
    Done2([✅ Status Checked])
    Done3([✅ Project Ready])
    Done4([✅ Problem Fixed])

    style Start fill:#2196F3,stroke:#1565C0,color:#fff
    style Done1 fill:#4CAF50,stroke:#2E7D32,color:#fff
    style Done2 fill:#4CAF50,stroke:#2E7D32,color:#fff
    style Done3 fill:#4CAF50,stroke:#2E7D32,color:#fff
    style Done4 fill:#4CAF50,stroke:#2E7D32,color:#fff
```

---

## 📐 Detailed Flow Diagrams

### 🔷 Flow Diagram 1: Overall Git Multi-Account Setup & Usage

```mermaid
flowchart TB
    Start([🚀 START: Git Multi-Account Setup]) --> Phase1

    subgraph Phase1["📦 Phase 1: Initial Setup"]
        direction TB
        S1[Install Git<br/>sudo apt install git]
        S2[Setup ~/.bashrc Aliases<br/>git-office, git-personal, etc.]
        S3[Reload Bashrc<br/>source ~/.bashrc]
        S4[Set Global Default<br/>git-office]

        S1 --> S2 --> S3 --> S4
    end

    Phase1 --> Phase2

    subgraph Phase2["🔐 Phase 2: SSH Key Setup"]
        direction TB
        S5[Create .ssh Folder<br/>mkdir -p ~/.ssh]
        S6[Generate Personal Key<br/>ssh-keygen ... personal]
        S7[Generate Office Key<br/>ssh-keygen ... office]
        S8[Create SSH Config<br/>~/.ssh/config]
        S9[Set Permissions<br/>chmod 600/644]

        S5 --> S6 --> S7 --> S8 --> S9
    end

    Phase2 --> Phase3

    subgraph Phase3["☁️ Phase 3: GitHub Configuration"]
        direction TB
        S10[Upload Personal Public Key<br/>to Personal GitHub]
        S11[Upload Office Public Key<br/>to Office GitHub]
        S12[Test Personal SSH<br/>ssh -T git@github-personal]
        S13[Test Office SSH<br/>ssh -T git@github-office]

        S10 --> S11 --> S12 --> S13
    end

    Phase3 --> Ready

    subgraph Ready["✅ Phase 4: Ready for Daily Use"]
        direction TB
        D1[Create/Clone Projects]
        D2[Switch Accounts as Needed]
        D3[Commit & Push]
        D4[Verify Before Each Commit]

        D1 --> D2 --> D3 --> D4
    end

    Ready --> Loop([🔄 Daily Development Cycle])

    style Start fill:#4CAF50,stroke:#2E7D32,color:#fff,stroke-width:3px
    style Loop fill:#2196F3,stroke:#1565C0,color:#fff,stroke-width:3px
    style Phase1 fill:#E3F2FD,stroke:#1976D2
    style Phase2 fill:#FFF3E0,stroke:#F57C00
    style Phase3 fill:#F3E5F5,stroke:#7B1FA2
    style Ready fill:#E8F5E9,stroke:#388E3C
```

---

### 🔷 Flow Diagram 2: SSH Key Generation & Configuration Flow

```mermaid
flowchart LR
    Start([Start SSH Setup]) --> Step1

    subgraph Setup["SSH Key Generation"]
        direction TB
        Step1[📁 Create Folder<br/>mkdir -p ~/.ssh<br/>chmod 700 ~/.ssh]

        Step2[🔑 Generate Personal Key<br/>ssh-keygen -t ed25519<br/>-C 'yogesh.lachheta111@gmail.com'<br/>-f ~/.ssh/id_ed25519_personal]

        Step3[🔑 Generate Office Key<br/>ssh-keygen -t ed25519<br/>-C 'yogesh.lachheta@47billion.com'<br/>-f ~/.ssh/id_ed25519_office]

        Step1 --> Step2 --> Step3
    end

    Step3 --> Step4

    subgraph Config["SSH Configuration"]
        direction TB
        Step4[⚙️ Create Config File<br/>~/.ssh/config<br/><br/>Host github-personal<br/>IdentityFile id_ed25519_personal<br/><br/>Host github-office<br/>IdentityFile id_ed25519_office]

        Step5[🔒 Set Permissions<br/><br/>chmod 600 config<br/>chmod 600 id_ed25519_*<br/>chmod 644 *.pub]

        Step4 --> Step5
    end

    Step5 --> Step6

    subgraph Agent["SSH Agent Setup"]
        direction TB
        Step6[🔧 Start SSH Agent<br/>eval ssh-agent -s]

        Step7[➕ Add Personal Key<br/>ssh-add ~/.ssh/id_ed25519_personal]

        Step8[➕ Add Office Key<br/>ssh-add ~/.ssh/id_ed25519_office]

        Step9[✅ Verify Keys Loaded<br/>ssh-add -l]

        Step6 --> Step7 --> Step8 --> Step9
    end

    Step9 --> Step10

    subgraph Upload["Upload to GitHub"]
        direction TB
        Step10[📤 Copy Personal Public Key<br/>cat ~/.ssh/id_ed25519_personal.pub]

        Step11[📤 Copy Office Public Key<br/>cat ~/.ssh/id_ed25519_office.pub]

        Step12[☁️ Upload to Personal GitHub<br/>Settings → SSH Keys → Add]

        Step13[☁️ Upload to Office GitHub<br/>Settings → SSH Keys → Add]

        Step10 --> Step12
        Step11 --> Step13
    end

    Step12 --> Test
    Step13 --> Test

    subgraph Test["Testing"]
        direction TB
        Test1[🧪 Test Personal<br/>ssh -T git@github-personal]
        Test2[🧪 Test Office<br/>ssh -T git@github-office]

        Test1 --> Test2
    end

    Test --> Complete([✅ SSH Setup Complete!])

    style Start fill:#4CAF50,stroke:#2E7D32,color:#fff
    style Complete fill:#4CAF50,stroke:#2E7D32,color:#fff
    style Setup fill:#E3F2FD,stroke:#1976D2
    style Config fill:#FFF3E0,stroke:#F57C00
    style Agent fill:#F3E5F5,stroke:#7B1FA2
    style Upload fill:#FCE4EC,stroke:#C2185B
    style Test fill:#E8F5E9,stroke:#388E3C
```

---

### 🔷 Flow Diagram 3: Complete Project Workflow (New Project)

```mermaid
flowchart TB
    Start([📁 New Project Created]) --> Identify

    Identify{🤔 Which Account?}
    Identify -->|🏢 Office Project| OfficeFlow
    Identify -->|👤 Personal Project| PersonalFlow

    subgraph OfficeFlow["🏢 Office Project Workflow"]
        direction TB

        O1[📂 Navigate to Project<br/>cd ~/Documents/office-project]

        O2[🎬 Initialize Git<br/>git init]

        O3[⚙️ Set Account Locally<br/>git-office-here<br/><br/>Output: ✅ Current project → OFFICE]

        O4[🔍 Verify Identity<br/>git-identity<br/><br/>Expected:<br/>yogesh.lachheta@47billion.com]

        O5{✅ Correct?}

        O6[🔗 Add Remote<br/>git remote add origin<br/>git@github-office:yogesh47/repo.git]

        O7[📝 First Commit<br/>git add .<br/>git commit -m 'Initial commit']

        O8[📤 Push to GitHub<br/>git push -u origin main]

        O9[🔍 Verify on GitHub<br/>Check commit author]

        O1 --> O2 --> O3 --> O4 --> O5
        O5 -->|Yes| O6
        O5 -->|No| O3
        O6 --> O7 --> O8 --> O9
    end

    subgraph PersonalFlow["👤 Personal Project Workflow"]
        direction TB

        P1[📂 Navigate to Project<br/>cd ~/projects/my-app]

        P2[🎬 Initialize Git<br/>git init]

        P3[⚙️ Set Account Locally<br/>git-personal-here<br/><br/>Output: ✅ Current project → PERSONAL]

        P4[🔍 Verify Identity<br/>git-identity<br/><br/>Expected:<br/>yogesh.lachheta111@gmail.com]

        P5{✅ Correct?}

        P6[🔗 Add Remote<br/>git remote add origin<br/>git@github-personal:yogesh-lachheta/repo.git]

        P7[📝 First Commit<br/>git add .<br/>git commit -m 'Initial commit']

        P8[📤 Push to GitHub<br/>git push -u origin main]

        P9[🔍 Verify on GitHub<br/>Check commit author]

        P1 --> P2 --> P3 --> P4 --> P5
        P5 -->|Yes| P6
        P5 -->|No| P3
        P6 --> P7 --> P8 --> P9
    end

    O9 --> Success
    P9 --> Success

    Success([✅ Project Setup Complete!<br/>Ready for Development])

    style Start fill:#2196F3,stroke:#1565C0,color:#fff
    style Success fill:#4CAF50,stroke:#2E7D32,color:#fff
    style OfficeFlow fill:#FFE0B2,stroke:#E65100
    style PersonalFlow fill:#E1BEE7,stroke:#7B1FA2
```

---

### 🔷 Flow Diagram 4: Daily Commit Process Flow

```mermaid
flowchart TD
    Start([💻 Ready to Commit Changes]) --> PreCheck

    subgraph PreCheck["⚠️ Pre-Commit Verification MANDATORY"]
        direction TB
        C1[🔍 Check Identity<br/>git-identity]

        C2[📊 Output Shows:<br/>Yogesh Lachheta<br/>email@domain.com]

        C3{🎯 Is this the<br/>CORRECT account?}

        C1 --> C2 --> C3
    end

    C3 -->|❌ NO - Wrong Account!| FixAccount
    C3 -->|✅ YES - Correct!| Stage

    subgraph FixAccount["🔧 Fix Account Before Committing"]
        direction TB
        F1{Which Account<br/>Do You Need?}

        F2[🏢 Switch to Office<br/>git-office-here]

        F3[👤 Switch to Personal<br/>git-personal-here]

        F4[🔍 Verify Again<br/>git-identity]

        F1 -->|Office| F2 --> F4
        F1 -->|Personal| F3 --> F4
    end

    F4 --> C3

    subgraph Stage["📋 Stage Changes"]
        direction TB
        S1[📝 Check Status<br/>git status]

        S2[➕ Stage All Changes<br/>git add .]

        S3[Or Stage Specific Files<br/>git add file1.txt file2.py]

        S4[📊 Review Staged<br/>git status]

        S1 --> S2
        S1 --> S3
        S2 --> S4
        S3 --> S4
    end

    Stage --> Commit

    subgraph Commit["💾 Create Commit"]
        direction TB
        CM1[✍️ Write Commit Message<br/>git commit -m 'description']

        CM2[📜 Commit Created with:<br/>Author: Yogesh Lachheta<br/>Email: verified-email@domain.com<br/>Timestamp: current time]

        CM3[🔍 Verify Commit<br/>git log -1 --format='%an %ae']

        CM1 --> CM2 --> CM3
    end

    Commit --> Push

    subgraph Push["📤 Push to GitHub"]
        direction TB
        P1[🚀 Push Changes<br/>git push origin main]

        P2[🔐 SSH Authenticates<br/>Using correct key automatically]

        P3{✅ Push<br/>Successful?}

        P4[🎉 Success!<br/>Changes on GitHub]

        P5[❌ Error Occurred]

        P1 --> P2 --> P3
        P3 -->|Yes| P4
        P3 -->|No| P5
    end

    P4 --> Verify
    P5 --> Troubleshoot

    subgraph Verify["✅ Final Verification"]
        direction TB
        V1[🌐 Open GitHub in Browser]
        V2[📊 Check Commit Author]
        V3[✅ Verify Email is Correct]

        V1 --> V2 --> V3
    end

    Verify --> Complete

    subgraph Troubleshoot["🚨 Troubleshoot Push Error"]
        direction TB
        T1[📋 Read Error Message]
        T2{Error Type?}
        T3[🔐 Permission Denied<br/>Check SSH keys<br/>ssh -T git@github-*]
        T4[🔄 Rejected/Conflict<br/>Pull first<br/>git pull origin main]
        T5[🌐 Network Error<br/>Check internet connection]

        T1 --> T2
        T2 -->|Permission| T3
        T2 -->|Rejected| T4
        T2 -->|Network| T5
    end

    T3 --> Push
    T4 --> Push
    T5 --> Push

    Complete([✅ Commit Process Complete!])

    style Start fill:#2196F3,stroke:#1565C0,color:#fff
    style Complete fill:#4CAF50,stroke:#2E7D32,color:#fff
    style PreCheck fill:#FFEBEE,stroke:#C62828
    style FixAccount fill:#FFF3E0,stroke:#E65100
    style Stage fill:#E3F2FD,stroke:#1976D2
    style Commit fill:#F3E5F5,stroke:#7B1FA2
    style Push fill:#E8F5E9,stroke:#388E3C
    style Verify fill:#E0F2F1,stroke:#00695C
    style Troubleshoot fill:#FCE4EC,stroke:#C2185B
```

---

### 🔷 Flow Diagram 5: Account Switching Decision Flow

```mermaid
flowchart TB
    Start([🔄 Need to Switch Account]) --> Why

    Why{📋 Why Switching?}
    Why -->|Starting New Project| NewProj
    Why -->|Working on Existing Project| ExistingProj
    Why -->|Changed Mind About Account| Change
    Why -->|Fixing Wrong Account| Fix

    subgraph NewProj["📁 New Project Account Setup"]
        direction TB
        N1{Project Type?}
        N2[🏢 Office Project<br/>Use: git-office-here]
        N3[👤 Personal Project<br/>Use: git-personal-here]
        N4[🔍 Verify<br/>git-identity]

        N1 -->|Office| N2 --> N4
        N1 -->|Personal| N3 --> N4
    end

    subgraph ExistingProj["📂 Existing Project Switch"]
        direction TB
        E1[📍 Navigate to Project<br/>cd /path/to/project]
        E2{Switch Scope?}
        E3[📁 This Project Only<br/>git-office-here<br/>or<br/>git-personal-here]
        E4[🌍 Change Global Default<br/>git-office<br/>or<br/>git-personal]
        E5[🔍 Verify<br/>git-whoami<br/>git-identity]

        E1 --> E2
        E2 -->|Local Only| E3 --> E5
        E2 -->|All Projects| E4 --> E5
    end

    subgraph Change["🔄 Change Global Strategy"]
        direction TB
        CH1{New Strategy?}
        CH2[Set Office as Default<br/>git-office<br/><br/>Reason: Most work is office]
        CH3[Set Personal as Default<br/>git-personal<br/><br/>Reason: Most work is personal]
        CH4[Apply to All Future Projects]
        CH5[Override Individual Projects<br/>as needed with<br/>git-office-here or<br/>git-personal-here]

        CH1 -->|Office Default| CH2
        CH1 -->|Personal Default| CH3
        CH2 --> CH4 --> CH5
        CH3 --> CH4 --> CH5
    end

    subgraph Fix["🔧 Fix Wrong Account"]
        direction TB
        F1[⚠️ Discovered Wrong Account<br/>Before Commit ✅ GOOD]
        F2[❌ After Commit Not Pushed<br/>Can Fix with --amend]
        F3[❌ After Pushed<br/>⚠️ Cannot Easily Fix]

        F4[Switch to Correct Account<br/>git-office-here or<br/>git-personal-here]

        F5[Amend Last Commit<br/>git commit --amend<br/>--reset-author --no-edit]

        F6[⚠️ Lesson Learned<br/>Always verify BEFORE commit!]

        F1 --> F4
        F2 --> F4 --> F5
        F3 --> F6
    end

    NewProj --> Verify
    ExistingProj --> Verify
    Change --> Verify
    Fix --> Verify

    subgraph Verify["✅ Verification Steps"]
        direction TB
        V1[Run: git-identity]
        V2[Check Output:<br/>Yogesh Lachheta<br/>email@domain.com]
        V3{Matches<br/>Expected?}
        V4[✅ Perfect!<br/>Ready to commit]
        V5[❌ Still Wrong<br/>Try again]

        V1 --> V2 --> V3
        V3 -->|Yes| V4
        V3 -->|No| V5
    end

    V5 --> Why
    V4 --> Complete

    Complete([✅ Account Switch Complete!<br/>Safe to Continue Working])

    style Start fill:#2196F3,stroke:#1565C0,color:#fff
    style Complete fill:#4CAF50,stroke:#2E7D32,color:#fff
    style NewProj fill:#E3F2FD,stroke:#1976D2
    style ExistingProj fill:#FFF3E0,stroke:#F57C00
    style Change fill:#F3E5F5,stroke:#7B1FA2
    style Fix fill:#FFEBEE,stroke:#C62828
    style Verify fill:#E8F5E9,stroke:#388E3C
```

---

### 🔷 Flow Diagram 6: Error Recovery & Troubleshooting Flow

```mermaid
flowchart TB
    Start([⚠️ Error Occurred]) --> Identify

    Identify{🔍 What's the Error?}

    Identify -->|command not found| AliasError
    Identify -->|Permission denied| SSHError
    Identify -->|Wrong commit author| AuthorError
    Identify -->|Push rejected| PushError
    Identify -->|Other| OtherError

    subgraph AliasError["🔧 Fix: command not found"]
        direction TB
        A1[Error:<br/>git-office: command not found]
        A2[Try: source ~/.bashrc]
        A3{Works Now?}
        A4[✅ Fixed!<br/>Aliases loaded]
        A5[Check aliases exist:<br/>tail -20 ~/.bashrc]
        A6{Aliases<br/>Present?}
        A7[Add aliases to .bashrc<br/>See setup section]
        A8[Open new terminal]

        A1 --> A2 --> A3
        A3 -->|Yes| A4
        A3 -->|No| A5 --> A6
        A6 -->|No| A7 --> A2
        A6 -->|Yes| A8 --> A4
    end

    subgraph SSHError["🔐 Fix: Permission denied"]
        direction TB
        S1[Error:<br/>Permission denied publickey]
        S2[Check keys loaded:<br/>ssh-add -l]
        S3{Keys Listed?}
        S4[Start agent & add keys:<br/>eval ssh-agent -s<br/>ssh-add ~/.ssh/id_ed25519_*]
        S5[Test connection:<br/>ssh -T git@github-personal<br/>ssh -T git@github-office]
        S6{Connected?}
        S7[✅ Fixed!<br/>SSH working]
        S8[Check GitHub:<br/>Public key uploaded?]
        S9[Upload public key<br/>to GitHub Settings]

        S1 --> S2 --> S3
        S3 -->|No| S4 --> S5
        S3 -->|Yes| S5
        S5 --> S6
        S6 -->|Yes| S7
        S6 -->|No| S8 --> S9 --> S5
    end

    subgraph AuthorError["👤 Fix: Wrong Author"]
        direction TB
        AU1[Error:<br/>Commit has wrong author]
        AU2{Already<br/>Pushed?}
        AU3[❌ Cannot easily fix<br/>Next time verify first!]
        AU4[✅ Not pushed yet<br/>Can fix now]
        AU5[Switch account:<br/>git-office-here or<br/>git-personal-here]
        AU6[Amend commit:<br/>git commit --amend<br/>--reset-author --no-edit]
        AU7[Verify fix:<br/>git log -1 --format='%an %ae']
        AU8[✅ Fixed!<br/>Author corrected]

        AU1 --> AU2
        AU2 -->|Yes| AU3
        AU2 -->|No| AU4 --> AU5 --> AU6 --> AU7 --> AU8
    end

    subgraph PushError["📤 Fix: Push Rejected"]
        direction TB
        PR1[Error:<br/>Push rejected]
        PR2{Error Type?}
        PR3[Non-fast-forward<br/>Remote has changes]
        PR4[Pull first:<br/>git pull origin main<br/>--rebase]
        PR5[Resolve conflicts if any]
        PR6[Try push again:<br/>git push origin main]
        PR7[Branch protection<br/>Need pull request]
        PR8[Create PR instead:<br/>gh pr create]
        PR9[Large file detected]
        PR10[Use Git LFS or<br/>remove large file]
        PR11[✅ Fixed!<br/>Push successful]

        PR1 --> PR2
        PR2 -->|Non-fast-forward| PR3 --> PR4 --> PR5 --> PR6 --> PR11
        PR2 -->|Protection| PR7 --> PR8 --> PR11
        PR2 -->|Large file| PR9 --> PR10 --> PR6
    end

    subgraph OtherError["🔍 Fix: Other Issues"]
        direction TB
        O1[Read error message carefully]
        O2[Google the exact error]
        O3[Check Git documentation]
        O4[Check GitHub status]
        O5[Try basic troubleshooting:<br/>- Check internet<br/>- Restart terminal<br/>- Re-clone repo]

        O1 --> O2 --> O3 --> O4 --> O5
    end

    AliasError --> Success
    SSHError --> Success
    AuthorError --> Success
    PushError --> Success
    OtherError --> Success

    Success([✅ Error Resolved!<br/>Continue Working])

    style Start fill:#FF5722,stroke:#D84315,color:#fff
    style Success fill:#4CAF50,stroke:#2E7D32,color:#fff
    style AliasError fill:#E3F2FD,stroke:#1976D2
    style SSHError fill:#FFF3E0,stroke:#F57C00
    style AuthorError fill:#F3E5F5,stroke:#7B1FA2
    style PushError fill:#FCE4EC,stroke:#C2185B
    style OtherError fill:#E0F2F1,stroke:#00695C
```

---

### 🔷 Flow Diagram 7: System Format Recovery Flow

```mermaid
flowchart TB
    Start([💾 System Formatted]) --> Check

    Check{🔍 Had Backup?}
    Check -->|✅ Yes, Backup Exists| RestoreFlow
    Check -->|❌ No Backup| FreshFlow

    subgraph RestoreFlow["♻️ Restore from Backup"]
        direction TB
        R1[📁 Locate Backup<br/>External drive / Cloud]
        R2[📂 Copy .ssh folder<br/>cp -r backup/.ssh ~/]
        R3[📂 Copy .gitconfig<br/>cp backup/.gitconfig ~/]
        R4[📂 Copy .bashrc section<br/>Git aliases]
        R5[🔒 Set Permissions<br/>chmod 700 ~/.ssh<br/>chmod 600 ~/.ssh/id_*<br/>chmod 644 ~/.ssh/*.pub]
        R6[🔧 Start SSH Agent<br/>eval ssh-agent -s<br/>ssh-add ~/.ssh/id_ed25519_*]
        R7[🧪 Test SSH<br/>ssh -T git@github-personal<br/>ssh -T git@github-office]
        R8[✅ Restored!<br/>Same keys working]

        R1 --> R2 --> R3 --> R4 --> R5 --> R6 --> R7 --> R8
    end

    subgraph FreshFlow["🆕 Fresh Setup Required"]
        direction TB

        F1[📦 Install Git<br/>sudo apt install git]

        F2[📝 Setup .bashrc<br/>Add Git aliases]

        F3[🔄 Reload bashrc<br/>source ~/.bashrc]

        F4[🔑 Generate NEW SSH Keys<br/>Personal + Office<br/>Different from old keys]

        F5[⚙️ Create SSH Config<br/>~/.ssh/config]

        F6[🔒 Set Permissions<br/>chmod 600/644]

        F7[📤 Upload NEW Public Keys<br/>to GitHub]

        F8[🗑️ Delete Old Keys from GitHub<br/>Settings → SSH Keys → Delete old]

        F9[🧪 Test New SSH<br/>ssh -T git@github-*]

        F10[✅ Fresh Setup Complete!<br/>New keys active]

        F11[💾 BACKUP Now!<br/>Don't make same mistake]

        F1 --> F2 --> F3 --> F4 --> F5 --> F6 --> F7 --> F8 --> F9 --> F10 --> F11
    end

    RestoreFlow --> Complete
    FreshFlow --> Complete

    subgraph Complete["✅ Post-Recovery Tasks"]
        direction TB
        C1[🌍 Set Global Account<br/>git-office or git-personal]
        C2[📂 Clone Repositories<br/>or navigate to existing projects]
        C3[⚙️ Set Local Accounts<br/>git-office-here or<br/>git-personal-here]
        C4[🔍 Verify Everything<br/>git-whoami<br/>git-identity]
        C5[💾 Create New Backup<br/>IMMEDIATELY!]

        C1 --> C2 --> C3 --> C4 --> C5
    end

    Complete --> Ready([🎉 Fully Recovered!<br/>Ready for Development])

    style Start fill:#FF5722,stroke:#D84315,color:#fff
    style Ready fill:#4CAF50,stroke:#2E7D32,color:#fff
    style RestoreFlow fill:#E8F5E9,stroke:#388E3C
    style FreshFlow fill:#FFF3E0,stroke:#F57C00
    style Complete fill:#E3F2FD,stroke:#1976D2
```

---

### 📊 Flow Diagram Summary Table

| # | Diagram Name | Type | Purpose | Complexity |
|---|-------------|------|---------|:----------:|
| 1 | Overall Multi-Account Setup | Phase Flow | Complete setup process | Medium |
| 2 | SSH Key Generation | Sequential Flow | SSH setup steps | High |
| 3 | Project Workflow | Parallel Flow | New project setup | Medium |
| 4 | Daily Commit Process | Detailed Flow | Commit workflow | High |
| 5 | Account Switching | Decision Flow | Switch scenarios | Medium |
| 6 | Error Recovery | Troubleshooting Flow | Fix common errors | High |
| 7 | System Format Recovery | Recovery Flow | After system format | Medium |

**Total Flow Diagrams:** 7 comprehensive workflows covering all scenarios! 🎯

---

## 🔍 Current Configuration Check

### Check What's Currently Configured

```bash
# Install Git first (if not installed)
sudo apt install git -y

# Check global configuration
git config --global user.name
git config --global user.email

# Check local (current project) configuration
git config --local user.name
git config --local user.email

# See all configuration (with file locations)
git config --list --show-origin
```

---

### ✅ Your Current Setup (Yogesh Lachheta)

**Global Configuration (Office Account):**

```bash
# Check current global config
git config --global user.name
# Should show: Yogesh Lachheta

git config --global user.email
# Should show: yogesh.lachheta@47billion.com
```

**Accounts:**

| Account Type | Name | Email | Usage |
|-------------|------|-------|-------|
| **Office (47billion)** | Yogesh Lachheta | yogesh.lachheta@47billion.com | Global (default) ✅ |
| **Personal** | Yogesh Lachheta | yogesh.lachheta111@gmail.com | Local override (when needed) |

**Strategy:**
- ✅ Office = Global → Most projects automatically use office account
- ✅ Personal projects → Use `git-personal-here` to override locally

---

## 🚀 Quick Setup - Set Global to Office (If Not Already Set)

**Run these commands to confirm/set your global config to office account:**

```bash
# Set global to office account (47billion)
git config --global user.name "Yogesh Lachheta"
git config --global user.email "yogesh.lachheta@47billion.com"

# Verify
git config --global user.name
# Output: Yogesh Lachheta ✅

git config --global user.email
# Output: yogesh.lachheta@47billion.com ✅
```

**✅ Done! Now office account is your global default.**

---

## ⚡ One-Command Account Switch (RECOMMENDED)

### Setup: Add to ~/.bashrc (Step-by-Step)

#### Step 1: Open .bashrc File

```bash
nano ~/.bashrc
```

**File Location:** `/home/billion/.bashrc`

---

#### Step 2: Scroll to End of File

**In Nano Editor:**
- Press `Ctrl+End` (jump to end)
- OR use arrow keys to scroll down

**You'll see existing content like:**
```bash
# pnpm
export PNPM_HOME="/home/billion/.local/share/pnpm"
...
# pnpm end
```

---

#### Step 3: Paste Git Aliases at the End

**Copy-paste ye lines AFTER the last line (Your actual details already filled):**

```bash

# ========================================
# Git Account Switchers - Yogesh Lachheta
# ========================================

# Switch to PERSONAL account (Global)
alias git-personal='git config --global user.name "Yogesh Lachheta" && git config --global user.email "yogesh.lachheta111@gmail.com" && echo "✅ Switched to PERSONAL (Global)"'

# Switch to OFFICE account (Global) - 47billion
alias git-office='git config --global user.name "Yogesh Lachheta" && git config --global user.email "yogesh.lachheta@47billion.com" && echo "✅ Switched to OFFICE (Global)"'

# Set PERSONAL for CURRENT PROJECT only
alias git-personal-here='git config --local user.name "Yogesh Lachheta" && git config --local user.email "yogesh.lachheta111@gmail.com" && echo "✅ Current project → PERSONAL"'

# Set OFFICE for CURRENT PROJECT only - 47billion
alias git-office-here='git config --local user.name "Yogesh Lachheta" && git config --local user.email "yogesh.lachheta@47billion.com" && echo "✅ Current project → OFFICE"'

# Check who am I?
alias git-whoami='echo "=== GLOBAL CONFIG ===" && git config --global user.name && git config --global user.email && echo "" && echo "=== LOCAL CONFIG (current project) ===" && git config --local user.name 2>/dev/null && git config --local user.email 2>/dev/null || echo "(No local config set)"'

# Show current identity (what will be used for commits)
alias git-identity='echo "Commits will use:" && git config user.name && git config user.email'
```

**After Adding, File Will Look Like:**

```bash
...
# pnpm end

# ========================================  ← START from here (line 131)
# Git Account Switchers - Yogesh Lachheta
# ========================================

alias git-personal='...'
alias git-office='...'
...
alias git-identity='...'                   ← END here (line 151)
```

---

#### Step 4: Save File

**In Nano Editor:**

1. Press `Ctrl+X` (exit nano)
2. Prompt: `Save modified buffer?`
3. Press `Y` (yes, save changes)
4. Press `Enter` (confirm filename `/home/billion/.bashrc`)

**Output:**
```
[File saved successfully]
```

---

#### Step 5: Reload Bashrc (Activate Aliases)

```bash
source ~/.bashrc
```

**Expected Output:** (No output = success!)

---

#### Step 6: Test Git Aliases

**Test 1: Check if aliases are loaded**

```bash
git-whoami
```

**Expected Output (if Git not configured yet):**
```
=== GLOBAL CONFIG ===


=== LOCAL CONFIG (current project) ===
(No local config set)
```

---

**Test 2: Set global to office**

```bash
git-office
```

**Expected Output:**
```
✅ Switched to OFFICE (Global)
```

---

**Test 3: Verify configuration**

```bash
git-whoami
```

**Expected Output:**
```
=== GLOBAL CONFIG ===
Yogesh Lachheta
yogesh.lachheta@47billion.com

=== LOCAL CONFIG (current project) ===
(No local config set)
```

**✅ Setup Complete!**

---

#### Step 7: Check Identity Before Commits

```bash
git-identity
```

**Expected Output:**
```
Commits will use:
Yogesh Lachheta
yogesh.lachheta@47billion.com
```

---

### ✅ Verification Checklist

| Step | Command | Expected Result | Status |
|------|---------|----------------|:------:|
| 1 | `nano ~/.bashrc` | File opens | ⬜ |
| 2 | Scroll to end | See `# pnpm end` | ⬜ |
| 3 | Paste aliases | Code added after line 129 | ⬜ |
| 4 | `Ctrl+X, Y, Enter` | File saved | ⬜ |
| 5 | `source ~/.bashrc` | No errors | ⬜ |
| 6 | `git-office` | `✅ Switched to OFFICE` | ⬜ |
| 7 | `git-whoami` | Shows office email | ⬜ |
| 8 | `git-identity` | Shows office email | ⬜ |

**All ✅? You're ready to use Git with auto-switching!**

---

### 📋 Quick Copy-Paste (All Commands)

```bash
# Open bashrc
nano ~/.bashrc

# (Scroll to end, paste the aliases, save with Ctrl+X, Y, Enter)

# Reload bashrc
source ~/.bashrc

# Set global to office
git-office

# Verify
git-whoami
```

---

### ⚡ Usage: One-Command Switching

**Switch Global Account (affects all future projects):**

```bash
# Switch to personal account globally
git-personal
# Output: ✅ Switched to PERSONAL (Global)

# Switch to office account globally
git-office
# Output: ✅ Switched to OFFICE (Global)
```

**Switch Current Project Only:**

```bash
# Navigate to your project first
cd /path/to/your/project

# Set THIS project to office account
git-office-here
# Output: ✅ Current project → OFFICE

# Set THIS project to personal account
git-personal-here
# Output: ✅ Current project → PERSONAL
```

**Check Current Identity:**

```bash
# See what's configured globally and locally
git-whoami

# See what will actually be used for commits
git-identity
```

---

## 🔄 How to Switch Accounts - Complete Guide

### 🎯 **Quick Switch Commands**

| Command | Scope | What It Does | Example |
|---------|:-----:|-------------|---------|
| `git-office` | 🌍 **Global** | Switch **all projects** to Office | `git-office` ✅ |
| `git-personal` | 🌍 **Global** | Switch **all projects** to Personal | `git-personal` ✅ |
| `git-office-here` | 📁 **Local** | Switch **only current project** to Office | `git-office-here` ✅ |
| `git-personal-here` | 📁 **Local** | Switch **only current project** to Personal | `git-personal-here` ✅ |
| `git-whoami` | ℹ️ **Info** | Show global + local config | Shows both configs |
| `git-identity` | ℹ️ **Info** | Show what will be used for **next commit** | Shows active account |

---

### 📖 **Step-by-Step Examples**

#### ✅ **Example 1: Switch Globally to Office**

```bash
# Terminal mein type karo
git-office
```

**Output:**
```
✅ Switched to OFFICE (Global)
```

**Kya hua:**
- ✅ **All new projects** automatically office account use karenge
- ✅ **Existing projects** (without local config) office account use karenge
- ✅ Git config global level par update ho gayi

**Verify karo:**
```bash
git-whoami
```

**Expected Output:**
```
=== GLOBAL CONFIG ===
Yogesh Lachheta
yogesh.lachheta@47billion.com  ← Office account ✅

=== LOCAL CONFIG (current project) ===
(No local config set)
```

---

#### ✅ **Example 2: Switch Globally to Personal**

```bash
git-personal
```

**Output:**
```
✅ Switched to PERSONAL (Global)
```

**Verify:**
```bash
git-whoami
```

**Expected:**
```
=== GLOBAL CONFIG ===
Yogesh Lachheta
yogesh.lachheta111@gmail.com  ← Personal account ✅

=== LOCAL CONFIG (current project) ===
(No local config set)
```

---

#### ✅ **Example 3: Override Current Project to Office**

```bash
# Navigate to project first
cd ~/Documents/R\&D/Cricket\ Auctions/cricket-auction-platform/backend

# Set THIS project to office
git-office-here
```

**Output:**
```
✅ Current project → OFFICE
```

**Verify:**
```bash
git-identity
```

**Expected:**
```
Commits will use:
Yogesh Lachheta
yogesh.lachheta@47billion.com  ← Office account ✅
```

**What Happened:**
- ✅ **Only this folder** will use office account
- ✅ Other folders will still use **global setting**
- ✅ Local config created for this project

---

#### ✅ **Example 4: Override Current Project to Personal**

```bash
cd ~/projects/my-personal-app

# Set THIS project to personal
git-personal-here
```

**Output:**
```
✅ Current project → PERSONAL
```

**Verify:**
```bash
git-identity
```

**Expected:**
```
Commits will use:
Yogesh Lachheta
yogesh.lachheta111@gmail.com  ← Personal account ✅
```

---

### 🔍 **Check Commands - Always Verify Before Commit!**

#### Command 1: `git-whoami` (Complete View)

**Shows:** Global + Local config (both)

```bash
git-whoami
```

**Sample Output:**
```
=== GLOBAL CONFIG ===
Yogesh Lachheta
yogesh.lachheta@47billion.com  ← Default for all projects

=== LOCAL CONFIG (current project) ===
Yogesh Lachheta
yogesh.lachheta111@gmail.com  ← Override for THIS project
```

**Interpretation:**
- 🌍 **Global** = Office account (default)
- 📁 **Local** = Personal account (override)
- ✅ **Next commit** will use **Local** (personal)

---

#### Command 2: `git-identity` (What Will Be Used)

**Shows:** Exactly what will be used for **next commit**

```bash
git-identity
```

**Sample Output:**
```
Commits will use:
Yogesh Lachheta
yogesh.lachheta@47billion.com  ← This account will be in commit
```

**Use this:** Right before `git commit` to verify!

---

### 🎬 **Live Demo Session**

```bash
# Check current status
$ git-whoami
=== GLOBAL CONFIG ===
Yogesh Lachheta
yogesh.lachheta@47billion.com

=== LOCAL CONFIG (current project) ===
(No local config set)

# Switch globally to personal
$ git-personal
✅ Switched to PERSONAL (Global)

# Verify change
$ git-whoami
=== GLOBAL CONFIG ===
Yogesh Lachheta
yogesh.lachheta111@gmail.com  ← Changed! ✅

# Navigate to office project
$ cd ~/Documents/R\&D/Cricket\ Auctions/cricket-auction-platform/backend

# Override locally to office
$ git-office-here
✅ Current project → OFFICE

# Check what will be used for commits
$ git-identity
Commits will use:
Yogesh Lachheta
yogesh.lachheta@47billion.com  ← Office account (local override) ✅

# Perfect! Office project uses office account, global is personal
```

---

### ⚠️ **IMPORTANT: Always Check Before Commit!**

```bash
# BEFORE every commit in new project, run this:
git-identity
```

**If wrong account shown:**
```bash
# Fix it immediately
git-office-here   # OR git-personal-here

# Verify again
git-identity

# Now commit
git commit -m "Your message"
```

---

### 💡 **Best Practices**

#### ✅ **DO:**

- ✅ **Always run** `git-identity` before first commit in new project
- ✅ **Set global** to your most common account (office or personal)
- ✅ **Override locally** for exceptions
- ✅ **Verify** after switching: `git-whoami` or `git-identity`
- ✅ **Use descriptive** commit messages
- ✅ **Check** git remote URL matches account (github-office or github-personal)

#### ❌ **DON'T:**

- ❌ **Don't** commit without checking identity first
- ❌ **Don't** assume global setting is correct for every project
- ❌ **Don't** mix HTTPS and SSH URLs
- ❌ **Don't** use wrong remote host (use `git@github-office:` for office repos)
- ❌ **Don't** forget to reload bashrc (`source ~/.bashrc`) after editing

---

### 🔁 **Common Workflows**

#### **Workflow 1: New Office Project Setup**

```bash
# 1. Navigate to project
cd ~/Documents/office-project

# 2. Initialize git
git init

# 3. Set to office (local override)
git-office-here

# 4. VERIFY (IMPORTANT!)
git-identity
# Should show: yogesh.lachheta@47billion.com ✅

# 5. Add remote (use office SSH host)
git remote add origin git@github-office:yogesh47/office-project.git

# 6. First commit
git add .
git commit -m "Initial commit"

# 7. Push (no password!)
git push -u origin main
```

---

#### **Workflow 2: New Personal Project Setup**

```bash
# 1. Navigate
cd ~/projects/my-app

# 2. Initialize
git init

# 3. Set to personal
git-personal-here

# 4. VERIFY
git-identity
# Should show: yogesh.lachheta111@gmail.com ✅

# 5. Add remote (use personal SSH host)
git remote add origin git@github-personal:yogesh-lachheta/my-app.git

# 6. Commit & push
git add .
git commit -m "Initial commit"
git push -u origin main
```

---

#### **Workflow 3: Clone Existing Office Repo**

```bash
# 1. Clone using office SSH host
git clone git@github-office:yogesh47/existing-project.git

# 2. Navigate
cd existing-project

# 3. Set to office
git-office-here

# 4. Verify
git-identity
# Should show: yogesh.lachheta@47billion.com ✅

# 5. Start working
git checkout -b feature/my-feature
```

---

#### **Workflow 4: Clone Existing Personal Repo**

```bash
# 1. Clone using personal SSH host
git clone git@github-personal:yogesh-lachheta/my-project.git

# 2. Navigate
cd my-project

# 3. Verify (might use global by default)
git-identity

# 4. If needed, override to personal
git-personal-here

# 5. Start working
git checkout -b feature/new-feature
```

---

### 📊 **Decision Matrix: Which Command to Use?**

| Scenario | Command | Why |
|----------|---------|-----|
| Most projects are **office**, few are personal | `git-office` (global) | Office as default, override personal projects |
| Most projects are **personal**, few are office | `git-personal` (global) | Personal as default, override office projects |
| 50-50 mix of both | `git-office` (global) | Set one as default, always override others |
| Starting **new office** project | `git-office-here` | Set project-specific config |
| Starting **new personal** project | `git-personal-here` | Set project-specific config |
| Not sure which account is active | `git-whoami` | Check both global + local |
| About to commit | `git-identity` | Verify what will be used |
| Wrong account in last commit (not pushed) | `git commit --amend --reset-author` | Fix author before push |

---

### 🚨 **Troubleshooting Switches**

#### Problem: `git-office: command not found`

**Solution:**
```bash
# Reload bashrc
source ~/.bashrc

# Test
git-office
```

**If still not working:** See full troubleshooting section below.

---

#### Problem: Switched but identity not changing

**Check:**
```bash
# See what's configured
git-whoami

# Local config might be overriding global
cd /path/to/project
git config --local --list
```

**Solution:**
```bash
# Remove local config if unwanted
git config --local --unset user.name
git config --local --unset user.email

# Or set new local config
git-office-here   # OR git-personal-here
```

---

#### Problem: Committed with wrong account

**If NOT pushed yet:**
```bash
# Fix identity first
git-office-here  # or git-personal-here

# Amend commit
git commit --amend --reset-author --no-edit

# Verify
git log -1 --format='%an %ae'
```

**If PUSHED already:**
- ⚠️ Can't easily fix
- Best practice: Always check before pushing!

---

## 📂 Project-Specific Setup

### Your Current Strategy: Global = Office (47billion), Project Override = Personal

**✅ Current Setup:**
- **Global Config** = Office account (yogesh.lachheta@47billion.com)
- **Office Projects** = Use global (no local config needed)
- **Personal Projects** = Override with local config (git-personal-here)

**Why This Works:**
- ✅ Office projects (majority) automatically use office account
- ✅ Personal projects explicitly set to personal account
- ✅ Safe: Won't accidentally commit to personal repo with office account

---

### Example 1: Cricket Auction (Office Project - Uses Global)

```bash
# Step 1: Navigate to office project
cd ~/Documents/R\&D/Cricket\ Auctions/cricket-auction-platform

# Step 2: Verify what will be used (should use global = office)
git-identity
# Output:
# Commits will use:
# Yogesh Lachheta
# yogesh.lachheta@47billion.com  ✅ (from global config)

# Step 3: No local config needed! Global office account will be used
# Just commit normally:
git add .
git commit -m "Your changes"
# ✅ Commits with office account automatically!
```

---

### Example 2: Personal Side Project (Needs Local Override)

```bash
# Step 1: Navigate to personal project
cd ~/projects/my-personal-app

# Step 2: Set THIS project to personal account (override global)
git-personal-here
# Output: ✅ Current project → PERSONAL

# Step 3: Verify
git-identity
# Output:
# Commits will use:
# Yogesh Lachheta
# yogesh.lachheta111@gmail.com  ✅ (from local config)

# Step 4: Now commit - will use personal account
git add .
git commit -m "My personal project changes"
# ✅ Commits with personal account!
```

---

## 🔀 Git SSH vs HTTPS - Complete Comparison

### 🤔 SSH aur HTTPS Mein Kya Fark Hai?

Git repositories ko access karne ke **2 tarike** hain:

| Method | URL Format | Example |
|--------|-----------|---------|
| **HTTPS** | `https://github.com/user/repo.git` | `https://github.com/johndoe/my-app.git` |
| **SSH** | `git@github.com:user/repo.git` | `git@github.com:johndoe/my-app.git` |

---

### 📊 Detailed Comparison Table

| Feature | HTTPS | SSH |
|---------|-------|-----|
| **🔐 Authentication** | Username + Personal Access Token (PAT) | SSH Key Pair (Public + Private) |
| **🔑 Password/Token** | ❌ Token needed every time (unless cached) | ✅ No token needed |
| **⏰ Expiration** | ❌ Tokens expire (30/60/90 days) | ✅ Keys never expire |
| **👥 Multi-Account** | ⚠️ Difficult (same host = github.com) | ✅ Easy (different SSH keys) |
| **🛡️ Security** | ⭐⭐⭐ Good (if token stored securely) | ⭐⭐⭐⭐ Better (keys never transmitted) |
| **🔥 Firewall** | ✅ Works everywhere (port 443/HTTPS) | ⚠️ May be blocked (port 22/SSH) |
| **🚀 Speed** | ⭐⭐⭐ Normal | ⭐⭐⭐⭐ Slightly faster |
| **📝 Setup** | ⭐⭐⭐⭐ Easy (just clone) | ⭐⭐⭐ Moderate (key generation needed) |
| **💻 Credentials** | Stored in cache/store/manager | SSH keys in `~/.ssh/` |
| **🔄 Token Renewal** | ❌ Manual (when expired) | ✅ Not needed |
| **👤 Multiple Accounts** | ⚠️ Last token overwrites previous | ✅ Different keys → auto switch |
| **🌐 Corporate Network** | ✅ Usually allowed | ⚠️ Often blocked |
| **📱 Simplicity** | ⭐⭐⭐⭐ Simple for beginners | ⭐⭐⭐ Requires SSH knowledge |

---

### 🎯 When to Use What?

#### Use HTTPS When:
- ✅ You're behind corporate firewall (port 22 blocked)
- ✅ You're a beginner (simpler to understand)
- ✅ You only have one GitHub account
- ✅ You're using GitHub occasionally
- ✅ You're on shared/temporary computer

#### Use SSH When:
- ✅ You have multiple GitHub accounts (office + personal)
- ✅ You push/pull frequently (no token entry)
- ✅ You want maximum security
- ✅ You're on your own computer
- ✅ Port 22 is not blocked on your network
- ✅ **RECOMMENDED for development work**

---

### 🔍 How Authentication Works

#### HTTPS Authentication Flow:

```
You                    GitHub
 │                       │
 │── git push ──────────>│
 │                       │
 │<─ "Username?" ────────│
 │── "johndoe" ─────────>│
 │                       │
 │<─ "Password?" ────────│
 │── "ghp_token..." ────>│ (Personal Access Token)
 │                       │
 │<─ ✅ Access Granted ──│
 │                       │
```

**Kya Hota Hai:**
1. Git asks for username
2. Git asks for password (actually **token**, not real password)
3. Token verified by GitHub
4. Access granted if valid

**Problems:**
- ❌ Token expire hone par phir se enter karna padega
- ❌ Multiple accounts ke liye token confuse ho jata hai
- ❌ Token store karna risky (if plain text)

---

#### SSH Authentication Flow:

```
You                                 GitHub
 │                                    │
 │── git push ─────────────────────> │
 │    (signed with private key)      │
 │                                    │
 │                                    │─┐
 │                                    │ │ Verifies signature
 │                                    │ │ using your public key
 │                                    │<┘ (uploaded to GitHub)
 │                                    │
 │<─ ✅ Access Granted ───────────────│
 │    (no password asked!)            │
```

**Kya Hota Hai:**
1. Git push karte time, request **private key** se sign hoti hai
2. GitHub tumhara **public key** use karke verify karta hai
3. Match hua? Access granted, no password asked!

**Benefits:**
- ✅ Password/token kuch nahi chahiye
- ✅ Private key kabhi transmit nahi hoti (super secure)
- ✅ Multiple keys = multiple accounts easily

---

### 🔑 SSH Key Pair - Kya Hai?

SSH mein **2 keys** hoti hain:

| Key Type | File | Location | Purpose | Share? |
|----------|------|----------|---------|--------|
| **Private Key** | `id_ed25519` | `~/.ssh/id_ed25519` | Apne paas (password jaise) | ❌ NEVER! |
| **Public Key** | `id_ed25519.pub` | `~/.ssh/id_ed25519.pub` | GitHub pe upload karo | ✅ Yes |

**Analogy:**
- **Private Key** = Your house key 🔑 (apne paas rakho)
- **Public Key** = Your house lock 🔒 (darwaze pe laga do)

**Kaise Kaam Karta Hai:**
1. You create **key pair** (private + public)
2. **Private key** apne computer pe (secret!)
3. **Public key** GitHub pe upload karo
4. Jab push karo → Private key se "sign" karo
5. GitHub public key se verify kare
6. Match? ✅ Access granted!

---

### 📋 Real-World Example Comparison

#### Scenario: Pushing Code to GitHub

**Using HTTPS:**

```bash
# Clone repository
git clone https://github.com/johndoe/my-app.git
cd my-app

# Make changes
echo "Hello" > file.txt
git add .
git commit -m "Add file"

# Push
git push

# ⚠️ Git asks:
# Username: johndoe
# Password: ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# ✅ Pushed!

# ❌ Problem: Token expire hoga 90 days baad
# ❌ Problem: Har baar enter karna padega (unless cached)
```

**Using SSH:**

```bash
# Clone repository (SSH URL)
git clone git@github.com:johndoe/my-app.git
cd my-app

# Make changes
echo "Hello" > file.txt
git add .
git commit -m "Add file"

# Push
git push

# ✅ Pushed! (No password asked!)

# ✅ Benefit: Kabhi password nahi puchega
# ✅ Benefit: Token expire ka tension nahi
```

---

### 🎯 Recommendation for Your Use Case

**You have 2 accounts (Office + Personal):**

| Method | Rating | Reason |
|--------|--------|--------|
| **SSH** | ⭐⭐⭐⭐⭐ **RECOMMENDED** | Easy multi-account management |
| **HTTPS** | ⭐⭐⭐ Okay | Token confusion with 2 accounts |

**Why SSH is Better for You:**

```bash
# With SSH - Easy!
# Personal project
git remote add origin git@github-personal:johndoe/my-app.git
git push  # Uses personal key automatically ✅

# Office project
git remote add origin git@github-office:company/project.git
git push  # Uses office key automatically ✅

# With HTTPS - Confusing!
# Personal project
git remote add origin https://github.com/johndoe/my-app.git
git push  # Asks for token - which one? 😕

# Office project
git remote add origin https://github.com/company/project.git
git push  # Asks for token again - overwrites previous? 😕
```

---

## 🔐 SSH Key Setup (Recommended)

### Why SSH Keys?
- ✅ No password/token needed each push
- ✅ More secure (keys never transmitted over network)
- ✅ Different keys for different accounts = automatic switching
- ✅ Never expires (unlike tokens)
- ✅ Faster authentication

---

### 📁 SSH Keys Kahan Store Hongi?

**Important:** SSH keys generate karne se pehle ye samajh lo ki kahan store hongi.

**Storage Location:** `/home/billion/.ssh/` folder mein

```
/home/billion/.ssh/
├── id_ed25519_personal          ← Private key (PERSONAL) - SECRET
├── id_ed25519_personal.pub      ← Public key (PERSONAL) - GitHub par upload
├── id_ed25519_office            ← Private key (OFFICE) - SECRET
├── id_ed25519_office.pub        ← Public key (OFFICE) - GitHub par upload
└── config                       ← SSH configuration file
```

**Key Points:**
- **Private keys** (`id_ed25519_*`) → Apne computer par rahti hain (NEVER SHARE!)
- **Public keys** (`id_ed25519_*.pub`) → GitHub par upload karte ho
- **Config file** → SSH ko batati hai ki kaun si key kab use karni hai

---

### 🚀 Complete Terminal Commands - Step by Step

**Neeche diye gaye commands ko ek-ek karke run karo:**

---

#### Step 1: .ssh folder create karo aur permissions set karo

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
cd ~/.ssh
```

**Kya hoga:**
- `~/.ssh` folder ban jayega (agar nahi hai to)
- Folder ki permissions set ho jayengi (700 = only you can access)
- Terminal `.ssh` folder mein chala jayega

---

#### Step 2: PERSONAL account ke liye SSH key generate karo

```bash
ssh-keygen -t ed25519 -C "yogesh.lachheta111@gmail.com" -f ~/.ssh/id_ed25519_personal -N ""
```

**Command Breakdown:**
- `-t ed25519` → Modern encryption algorithm use karo
- `-C "email"` → Comment (identification ke liye)
- `-f filename` → Kis naam se file save karni hai
- `-N ""` → No passphrase (khali password)

**Output:**
```
Generating public/private ed25519 key pair.
Your identification has been saved in /home/billion/.ssh/id_ed25519_personal
Your public key has been saved in /home/billion/.ssh/id_ed25519_personal.pub
The key fingerprint is:
SHA256:xxxxx... yogesh.lachheta111@gmail.com
```

**✅ Personal key ban gayi!**

---

#### Step 3: OFFICE account ke liye SSH key generate karo

```bash
ssh-keygen -t ed25519 -C "yogesh.lachheta@47billion.com" -f ~/.ssh/id_ed25519_office -N ""
```

**Output:**
```
Generating public/private ed25519 key pair.
Your identification has been saved in /home/billion/.ssh/id_ed25519_office
Your public key has been saved in /home/billion/.ssh/id_ed25519_office.pub
The key fingerprint is:
SHA256:yyyyy... yogesh.lachheta@47billion.com
```

**✅ Office key ban gayi!**

---

#### Step 4: SSH agent start karo aur keys add karo

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_personal
ssh-add ~/.ssh/id_ed25519_office
```

**Output:**
```
Agent pid 12345
Identity added: /home/billion/.ssh/id_ed25519_personal (yogesh.lachheta111@gmail.com)
Identity added: /home/billion/.ssh/id_ed25519_office (yogesh.lachheta@47billion.com)
```

**Kya hua:**
- SSH agent background mein start ho gaya
- Dono keys agent mein load ho gayi

---

#### Step 5: SSH config file create karo

```bash
cat > ~/.ssh/config << 'EOF'
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
EOF
```

**Kya hua:**
- Config file ban gayi jo SSH ko batati hai ki kaun si key kab use karni hai
- `github-personal` → personal key use karega
- `github-office` → office key use karega

---

#### Step 6: Permissions set karo

```bash
chmod 600 ~/.ssh/config
chmod 600 ~/.ssh/id_ed25519_personal
chmod 600 ~/.ssh/id_ed25519_office
chmod 644 ~/.ssh/id_ed25519_personal.pub
chmod 644 ~/.ssh/id_ed25519_office.pub
```

**Why:**
- `600` (private keys & config) → Only you can read/write (security!)
- `644` (public keys) → Anyone can read (public keys share hoti hain)

---

#### Step 7: Verify karo ki sab kuch ban gaya

```bash
ls -la ~/.ssh/
```

**Expected Output:**
```
-rw------- 1 billion billion  411 Feb 21 12:30 id_ed25519_personal
-rw-r--r-- 1 billion billion  103 Feb 21 12:30 id_ed25519_personal.pub
-rw------- 1 billion billion  411 Feb 21 12:30 id_ed25519_office
-rw-r--r-- 1 billion billion  103 Feb 21 12:30 id_ed25519_office.pub
-rw------- 1 billion billion  268 Feb 21 12:31 config
```

**✅ Sab files ban gayi!**

---

### 📋 Quick Copy-Paste Summary

**Terminal mein ye sab ek saath copy-paste kar do:**

```bash
# Step 1: Folder create + permissions
mkdir -p ~/.ssh && chmod 700 ~/.ssh && cd ~/.ssh

# Step 2: Personal key generate
ssh-keygen -t ed25519 -C "yogesh.lachheta111@gmail.com" -f ~/.ssh/id_ed25519_personal -N ""

# Step 3: Office key generate
ssh-keygen -t ed25519 -C "yogesh.lachheta@47billion.com" -f ~/.ssh/id_ed25519_office -N ""

# Step 4: SSH agent start + keys add
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_personal
ssh-add ~/.ssh/id_ed25519_office

# Step 5: Config file create
cat > ~/.ssh/config << 'EOF'
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
EOF

# Step 6: Permissions set
chmod 600 ~/.ssh/config
chmod 600 ~/.ssh/id_ed25519_personal
chmod 600 ~/.ssh/id_ed25519_office
chmod 644 ~/.ssh/id_ed25519_personal.pub
chmod 644 ~/.ssh/id_ed25519_office.pub

# Step 7: Verify
ls -la ~/.ssh/
```

**✅ Copy-paste karo, Enter dabao, SSH keys ready!**

---

### 📤 Next Step: GitHub Par Public Keys Upload Karo

**IMPORTANT:** Keys generate hone ke baad, public keys ko GitHub par upload karna zaroori hai!

#### Personal Account ke liye:

```bash
# Public key copy karo
cat ~/.ssh/id_ed25519_personal.pub

# Output copy karo (puri line):
# ssh-ed25519 AAAAC3Nz... yogesh.lachheta111@gmail.com
```

**GitHub par upload karo:**
1. Personal GitHub account mein login karo
2. Settings → SSH and GPG keys → New SSH key
3. Title: `Personal Computer - Ubuntu`
4. Key: Paste copied public key
5. Add SSH key

---

#### Office Account ke liye:

```bash
# Public key copy karo
cat ~/.ssh/id_ed25519_office.pub

# Output copy karo (puri line):
# ssh-ed25519 AAAAC3Nz... yogesh.lachheta@47billion.com
```

**GitHub par upload karo:**
1. Office GitHub account mein login karo
2. Settings → SSH and GPG keys → New SSH key
3. Title: `Office Computer - Ubuntu`
4. Key: Paste copied public key
5. Add SSH key

---

### ✅ Test Karo - SSH Working Hai Ya Nahi

**Personal account test karo:**

```bash
ssh -T git@github-personal
```

**Expected Output:**
```
Hi YourPersonalUsername! You've successfully authenticated, but GitHub does not provide shell access.
```

**✅ Working!**

---

**Office account test karo:**

```bash
ssh -T git@github-office
```

**Expected Output:**
```
Hi YourOfficeUsername! You've successfully authenticated, but GitHub does not provide shell access.
```

**✅ Working!**

---

### 🎉 SSH Setup Complete! Ab Kya Kar Sakte Ho?

**Personal project:**

```bash
cd ~/projects/my-personal-app
git init
git remote add origin git@github-personal:your-username/my-app.git
git push -u origin main
# ✅ No password! Automatic authentication!
```

**Office project:**

```bash
cd ~/Documents/office-project
git init
git remote add origin git@github-office:company-org/office-project.git
git push -u origin main
# ✅ No password! Automatic authentication!
```

---

### 📝 Complete SSH Setup - Detailed Step by Step

**Neeche detailed explanation hai agar samajhna ho step-by-step:**

---

### 🔑 Understanding SSH Key Filenames

**Default SSH key files ka naam hota hai:**
- `id_ed25519` (private key - secret!)
- `id_ed25519.pub` (public key - GitHub pe upload)

**Problem:** Agar dono accounts ke liye same naam use karoge, overwrite ho jayega!

**Solution:** Different filenames use karo:

| Account | Private Key File | Public Key File |
|---------|-----------------|-----------------|
| **Personal** | `id_ed25519_personal` | `id_ed25519_personal.pub` |
| **Office** | `id_ed25519_office` | `id_ed25519_office.pub` |

**Filename Breakdown:**

```
id_ed25519_personal
│  │       │
│  │       └─ Account identifier (personal/office)
│  └───────── Encryption algorithm (ed25519)
└──────────── ID key (standard prefix)
```

**Location:** All keys stored in `~/.ssh/` folder

```
~/.ssh/
├── id_ed25519_personal         # Personal account - Private key
├── id_ed25519_personal.pub     # Personal account - Public key
├── id_ed25519_office           # Office account - Private key
├── id_ed25519_office.pub       # Office account - Public key
└── config                      # SSH configuration file
```

---

### 📋 Step 0: Prerequisites (Check First)

```bash
# Check if .ssh folder exists
ls -la ~/.ssh

# If doesn't exist, create it
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# Verify creation
ls -la ~/.ssh
```

---

### Step 1: Generate Personal Account SSH Key

**Open terminal and run:**

```bash
# Generate personal SSH key (Yogesh's personal account)
ssh-keygen -t ed25519 -C "yogesh.lachheta111@gmail.com" -f ~/.ssh/id_ed25519_personal
```

**Command Breakdown:**

| Part | Meaning | Value |
|------|---------|-------|
| `ssh-keygen` | SSH key generation tool | Command |
| `-t ed25519` | Type of encryption | ed25519 algorithm (modern, secure) |
| `-C "email"` | Comment (for identification) | yogesh.lachheta111@gmail.com |
| `-f filepath` | Filename | `~/.ssh/id_ed25519_personal` |

**What Will Happen:**

```
Generating public/private ed25519 key pair.
Enter passphrase (empty for no passphrase):
```

**⚠️ Passphrase Choice:**

| Option | Security | Convenience | Recommendation |
|--------|----------|-------------|----------------|
| **No passphrase** (Press Enter) | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ For personal computer |
| **Set passphrase** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ✅ For shared computer |

**Press Enter (no passphrase)**

```
Enter same passphrase again:
```

**Press Enter again**

**Complete Output:**

```
Your identification has been saved in /home/billion/.ssh/id_ed25519_personal
Your public key has been saved in /home/billion/.ssh/id_ed25519_personal.pub
The key fingerprint is:
SHA256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx yogesh.lachheta111@gmail.com
The key's randomart image is:
+--[ED25519 256]--+
|        .o+      |
|       . + .     |
|      . . o      |
+----[SHA256]-----+
```

**✅ Personal key created!**

**Verify files created:**

```bash
ls -la ~/.ssh/id_ed25519_personal*

# Output:
# -rw------- 1 billion billion 419 Feb 21 14:00 id_ed25519_personal       (Private)
# -rw-r--r-- 1 billion billion 105 Feb 21 14:00 id_ed25519_personal.pub   (Public)
```

---

### Step 2: Generate Office Account SSH Key

```bash
# Generate office SSH key (Yogesh's 47billion account)
ssh-keygen -t ed25519 -C "yogesh.lachheta@47billion.com" -f ~/.ssh/id_ed25519_office
```

**Same process:**

```
Generating public/private ed25519 key pair.
Enter passphrase (empty for no passphrase):
```

**Press Enter (no passphrase)**

```
Enter same passphrase again:
```

**Press Enter again**

**Complete Output:**

```
Your identification has been saved in /home/billion/.ssh/id_ed25519_office
Your public key has been saved in /home/billion/.ssh/id_ed25519_office.pub
The key fingerprint is:
SHA256:yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy yogesh.lachheta@47billion.com
The key's randomart image is:
+--[ED25519 256]--+
|      E+o        |
|     . oo        |
|      +.o        |
+----[SHA256]-----+
```

**✅ Office key created!**

**Verify:**

```bash
ls -la ~/.ssh/id_ed25519_office*

# Output:
# -rw------- 1 billion billion 419 Feb 21 14:01 id_ed25519_office         (Private)
# -rw-r--r-- 1 billion billion 105 Feb 21 14:01 id_ed25519_office.pub     (Public)
```

---

### Step 2.5: Verify Both Keys Created

**Now you have 4 files:**

```bash
ls -la ~/.ssh/

# Output:
# id_ed25519_personal       ← Personal private key (DON'T SHARE!)
# id_ed25519_personal.pub   ← Personal public key (upload to GitHub)
# id_ed25519_office         ← Office private key (DON'T SHARE!)
# id_ed25519_office.pub     ← Office public key (upload to GitHub)
```

---

### Step 3: Add Keys to SSH Agent

**Kya Hai SSH Agent?**
- Background process jo keys ko manage karta hai
- Passphrase ek baar enter karo, phir yaad rakhta hai
- Automatically sahi key use karta hai

**Start SSH Agent:**

```bash
# Start SSH agent (if not running)
eval "$(ssh-agent -s)"

# Output:
# Agent pid 12345
```

**Add Personal Key:**

```bash
ssh-add ~/.ssh/id_ed25519_personal

# Output:
# Identity added: /home/billion/.ssh/id_ed25519_personal (your-personal@gmail.com)
```

**Add Office Key:**

```bash
ssh-add ~/.ssh/id_ed25519_office

# Output:
# Identity added: /home/billion/.ssh/id_ed25519_office (your-office@company.com)
```

**Verify keys loaded:**

```bash
ssh-add -l

# Output:
# 256 SHA256:xxxxx yogesh.lachheta111@gmail.com (ED25519)
# 256 SHA256:yyyyy yogesh.lachheta@47billion.com (ED25519)
```

**✅ Dono keys SSH agent mein loaded!**

---

### Step 4: Copy Public Keys

**Personal Public Key:**

```bash
cat ~/.ssh/id_ed25519_personal.pub

# Output:
# ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx yogesh.lachheta111@gmail.com
```

**⚠️ Copy this entire line!** (from `ssh-ed25519` to `@gmail.com`)

**Office Public Key:**

```bash
cat ~/.ssh/id_ed25519_office.pub

# Output:
# ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy yogesh.lachheta@47billion.com
```

**⚠️ Copy this entire line!**

---

### Step 5: Upload Public Keys to GitHub

#### For Personal GitHub Account:

1. **Login** to Personal GitHub (https://github.com)
2. Click **profile picture** (top right) → **Settings**
3. Left sidebar → **SSH and GPG keys**
4. Click **New SSH key** (green button)
5. **Title:** `Personal Computer - Ubuntu` (koi bhi identifying name)
6. **Key type:** `Authentication Key`
7. **Key:** Paste copied public key (`id_ed25519_personal.pub` contents)
   ```
   ssh-ed25519 AAAAC3Nz... your-personal@gmail.com
   ```
8. Click **Add SSH key**
9. **Confirm** with GitHub password

**✅ Personal key uploaded!**

---

#### For Office GitHub Account:

1. **Login** to Office GitHub
2. Same steps as above
3. **Title:** `Office Computer - Ubuntu`
4. **Key:** Paste office public key (`id_ed25519_office.pub`)
   ```
   ssh-ed25519 AAAAC3Nz... your-office@company.com
   ```
5. Click **Add SSH key**

**✅ Office key uploaded!**

---

### Step 6: Configure SSH Config File

**Kya Hai SSH Config?**
- Tells SSH which key to use for which account
- Maps `github-personal` → personal key
- Maps `github-office` → office key

**Create/Edit config file:**

```bash
nano ~/.ssh/config
```

**Add this content:**

```
# Personal GitHub Account
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes

# Office GitHub Account
Host github-office
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_office
    IdentitiesOnly yes
```

**Config Breakdown:**

| Line | Meaning | Example Value |
|------|---------|---------------|
| `Host github-personal` | Alias name (you define this) | `github-personal` (can be anything) |
| `HostName github.com` | Actual server | `github.com` |
| `User git` | SSH username (always `git` for GitHub) | `git` |
| `IdentityFile ~/.ssh/id_ed25519_personal` | Which key to use | Path to personal private key |
| `IdentitiesOnly yes` | Use ONLY this key | `yes` (prevents trying other keys) |

**Save file:** `Ctrl+X` → `Y` → `Enter`

**Set permissions:**

```bash
chmod 600 ~/.ssh/config
```

**✅ SSH config created!**

---

### Step 7: Test SSH Connections

**Test Personal Account:**

```bash
ssh -T git@github-personal

# Output:
# Hi your-personal-username! You've successfully authenticated, but GitHub does not provide shell access.
```

**✅ Personal account working!**

**Test Office Account:**

```bash
ssh -T git@github-office

# Output:
# Hi your-office-username! You've successfully authenticated, but GitHub does not provide shell access.
```

**✅ Office account working!**

**❌ If you get "Permission denied":**

```bash
# Check SSH agent has keys
ssh-add -l

# If empty, add keys again
ssh-add ~/.ssh/id_ed25519_personal
ssh-add ~/.ssh/id_ed25519_office

# Test again
ssh -T git@github-personal
```

---

### Step 8: Use SSH URLs in Projects

**Personal Project:**

```bash
cd ~/projects/my-personal-app

# Initialize git
git init

# Add remote using PERSONAL SSH host
git remote add origin git@github-personal:your-username/my-personal-app.git
#                          ^^^^^^^^^^^^^ Uses personal key automatically!

# Push
git push -u origin main
# ✅ No password asked! Uses personal key!
```

**Office Project:**

```bash
cd ~/Documents/office-project

# Initialize git
git init

# Add remote using OFFICE SSH host
git remote add origin git@github-office:company-org/office-project.git
#                          ^^^^^^^^^^^^^ Uses office key automatically!

# Push
git push -u origin main
# ✅ No password asked! Uses office key!
```

---

### 📋 SSH URL Format Explained

**General Format:**

```
git@HOST:username/repository.git
│   │    │        │
│   │    │        └─ Repository name
│   │    └────────── GitHub username or organization
│   └─────────────── Host from SSH config
└─────────────────── Always 'git@' for GitHub
```

**Examples:**

| Account | Host (from config) | URL Format | Example |
|---------|-------------------|------------|---------|
| **Personal** | `github-personal` | `git@github-personal:user/repo.git` | `git@github-personal:johndoe/my-app.git` |
| **Office** | `github-office` | `git@github-office:org/repo.git` | `git@github-office:company/project.git` |

**How It Works:**

```
git@github-personal:johndoe/my-app.git
     │
     └─ SSH sees "github-personal"
        Checks ~/.ssh/config
        Finds:
            Host github-personal
                HostName github.com
                IdentityFile ~/.ssh/id_ed25519_personal
        Uses personal key automatically!
```

---

```bash
# Generate office SSH key
ssh-keygen -t ed25519 -C "office@company.com" -f ~/.ssh/id_ed25519_office

# Press Enter for passphrase (or set one)

# Add to SSH agent
ssh-add ~/.ssh/id_ed25519_office

# Copy public key
cat ~/.ssh/id_ed25519_office.pub
# Copy output → Go to Office GitHub → Settings → SSH Keys → Add New
```

---

### Configure SSH Config File

```bash
# Create/edit SSH config
nano ~/.ssh/config
```

**Add this content:**

```
# Personal GitHub
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes

# Office GitHub
Host github-office
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_office
    IdentitiesOnly yes
```

**Save and set permissions:**

```bash
chmod 600 ~/.ssh/config
```

---

### Use Different Hosts for Different Projects

**Personal Project:**

```bash
cd ~/projects/my-app

# Use personal SSH host
git remote add origin git@github-personal:yourusername/my-app.git

# Push (automatically uses personal key)
git push -u origin main
```

**Office Project:**

```bash
cd ~/Documents/R\&D/Cricket\ Auctions/cricket-auction-platform

# Use office SSH host
git remote add origin git@github-office:company-org/cricket-auction.git

# Push (automatically uses office key)
git push -u origin main
```

---

### Step 9: Set File Permissions (Security)

**Important: Set correct permissions for all SSH files**

```bash
# Set permissions for SSH config
chmod 600 ~/.ssh/config

# Set permissions for private keys (strict - only you can read)
chmod 600 ~/.ssh/id_ed25519_personal
chmod 600 ~/.ssh/id_ed25519_office

# Set permissions for public keys (readable by others)
chmod 644 ~/.ssh/id_ed25519_personal.pub
chmod 644 ~/.ssh/id_ed25519_office.pub
```

**Why These Permissions?**

| File | Permission | Meaning | Why |
|------|-----------|---------|-----|
| Private keys | `600` | Only you can read/write | Security - private keys must be secret |
| Public keys | `644` | You: read/write, Others: read | Public keys are meant to be shared |
| Config file | `600` | Only you can read/write | Contains sensitive paths |

**Verify permissions:**

```bash
ls -la ~/.ssh/

# Expected output:
# -rw------- (600) id_ed25519_personal       ✅
# -rw-r--r-- (644) id_ed25519_personal.pub   ✅
# -rw------- (600) id_ed25519_office         ✅
# -rw-r--r-- (644) id_ed25519_office.pub     ✅
# -rw------- (600) config                    ✅
```

**✅ Permissions set correctly!**

---

### Step 10: Final Testing & Verification

**Test 1: Check SSH agent has keys**

```bash
ssh-add -l

# Expected output:
# 256 SHA256:xxxxx yogesh.lachheta111@gmail.com (ED25519)
# 256 SHA256:yyyyy yogesh.lachheta@47billion.com (ED25519)
```

**✅ If you see both keys, you're good!**

**❌ If "Could not open a connection to your authentication agent":**

```bash
# Start SSH agent
eval "$(ssh-agent -s)"

# Add keys again
ssh-add ~/.ssh/id_ed25519_personal
ssh-add ~/.ssh/id_ed25519_office

# Check again
ssh-add -l
```

---

**Test 2: Test GitHub connections**

```bash
# Test personal account
ssh -T git@github-personal

# Expected output:
# Hi YourPersonalUsername! You've successfully authenticated, but GitHub does not provide shell access.
```

**✅ Personal account working!**

```bash
# Test office account
ssh -T git@github-office

# Expected output:
# Hi YourOfficeUsername! You've successfully authenticated, but GitHub does not provide shell access.
```

**✅ Office account working!**

---

**Test 3: Verify SSH config is working**

```bash
# Check config file exists and is readable
cat ~/.ssh/config

# Should show:
# Host github-personal
#     HostName github.com
#     User git
#     IdentityFile ~/.ssh/id_ed25519_personal
#     IdentitiesOnly yes
#
# Host github-office
#     HostName github.com
#     User git
#     IdentityFile ~/.ssh/id_ed25519_office
#     IdentitiesOnly yes
```

**✅ Config correct!**

---

### Step 11: Quick Command Summary (Copy All at Once)

**For easy setup, copy and run all these commands at once:**

```bash
# ============================================
# Complete SSH Setup - All Commands
# ============================================

# Step 0: Create .ssh folder (if doesn't exist)
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# Step 1: Generate personal SSH key
ssh-keygen -t ed25519 -C "yogesh.lachheta111@gmail.com" -f ~/.ssh/id_ed25519_personal
# Press Enter twice (no passphrase)

# Step 2: Generate office SSH key
ssh-keygen -t ed25519 -C "yogesh.lachheta@47billion.com" -f ~/.ssh/id_ed25519_office
# Press Enter twice (no passphrase)

# Step 3: Start SSH agent & add keys
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_personal
ssh-add ~/.ssh/id_ed25519_office

# Step 4: Verify keys loaded
ssh-add -l

# Step 5: Display public keys (copy these to GitHub)
echo "========================================="
echo "PERSONAL PUBLIC KEY (copy to Personal GitHub):"
echo "========================================="
cat ~/.ssh/id_ed25519_personal.pub
echo ""
echo "========================================="
echo "OFFICE PUBLIC KEY (copy to Office GitHub):"
echo "========================================="
cat ~/.ssh/id_ed25519_office.pub
echo ""

# Step 6: Create SSH config file
cat > ~/.ssh/config << 'EOF'
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
EOF

# Step 9: Set correct permissions
chmod 600 ~/.ssh/config
chmod 600 ~/.ssh/id_ed25519_personal
chmod 600 ~/.ssh/id_ed25519_office
chmod 644 ~/.ssh/id_ed25519_personal.pub
chmod 644 ~/.ssh/id_ed25519_office.pub

# Step 10: Verify permissions
ls -la ~/.ssh/

# Step 11: Test connections
echo ""
echo "Testing Personal GitHub connection..."
ssh -T git@github-personal

echo ""
echo "Testing Office GitHub connection..."
ssh -T git@github-office

echo ""
echo "✅ Setup complete!"
```

**⚠️ Note:** After running the ssh-keygen commands, you'll need to:
1. Copy the public keys (displayed by the script)
2. Upload to respective GitHub accounts (Settings → SSH Keys)
3. Then run the test commands again

---

### 🎉 SSH Setup Complete!

**What You Can Do Now:**

```bash
# Personal project
cd ~/projects/my-personal-app
git init
git remote add origin git@github-personal:your-username/my-app.git
git push -u origin main
# ✅ No password! Automatic!

# Office project
cd ~/Documents/office-project
git init
git remote add origin git@github-office:47billion/office-project.git
git push -u origin main
# ✅ No password! Automatic!
```

**Benefits You Got:**
- ✅ No password entry needed (forever!)
- ✅ Automatic account switching (different keys for different projects)
- ✅ Secure (keys never transmitted over network)
- ✅ Keys never expire
- ✅ Easy multi-account management

---

## 🔑 Password/Token Management (HTTPS Method)

### ⚠️ Important: GitHub Password Authentication Discontinued

**GitHub no longer accepts passwords for Git operations!**

You must use **Personal Access Tokens (PAT)** instead.

---

### 📝 Step 1: Generate Personal Access Tokens

#### For Personal GitHub Account

**1. Login to Personal GitHub**
   - Go to: https://github.com
   - Login with your personal account

**2. Navigate to Settings → Developer Settings**
   - Click your profile picture (top right) → **Settings**
   - Scroll down → Click **Developer settings** (bottom left)
   - Click **Personal access tokens** → **Tokens (classic)**

**3. Generate New Token**
   - Click **Generate new token** → **Generate new token (classic)**
   - **Note:** `Git Access - Personal Projects` (koi bhi naam)
   - **Expiration:** 90 days (ya No expiration - but risky)
   - **Select scopes:**
     - ✅ `repo` (Full control of private repositories)
     - ✅ `workflow` (Update GitHub Action workflows)
     - ✅ `read:org` (Read org and team membership)
   - Click **Generate token**

**4. Copy Token IMMEDIATELY**
   ```
   ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
   **⚠️ Save this somewhere safe! You won't see it again!**

---

#### For Office GitHub Account

**Repeat same steps on Office GitHub account:**
   - Login to Office GitHub
   - Settings → Developer settings → Personal access tokens
   - Generate new token
   - Note: `Git Access - Office Projects`
   - Select same scopes
   - Copy token: `ghp_yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy`

---

### 🔐 Step 2: Store Credentials in Git

#### Option A: Git Credential Cache (15 min timeout)

**What it does:** Stores credentials in memory for 15 minutes

```bash
# Enable credential cache (stores for 15 minutes)
git config --global credential.helper cache

# Set cache timeout to 1 hour (3600 seconds)
git config --global credential.helper 'cache --timeout=3600'

# Set cache timeout to 24 hours (86400 seconds)
git config --global credential.helper 'cache --timeout=86400'
```

**Pros:**
- ✅ Secure (stored in memory, not disk)
- ✅ Auto-expires after timeout

**Cons:**
- ❌ Need to re-enter after timeout
- ❌ Lost on system reboot

---

#### Option B: Git Credential Store (Permanent, Plain Text)

**What it does:** Stores credentials in plain text file `~/.git-credentials`

```bash
# Enable credential store (permanent storage)
git config --global credential.helper store
```

**⚠️ Security Warning:**
- Credentials stored in **plain text** in `~/.git-credentials`
- Anyone with file access can read your tokens!
- Use only on trusted machines

**File location:**
```bash
cat ~/.git-credentials
# Format:
# https://username:token@github.com
```

---

#### Option C: Git Credential Manager (RECOMMENDED)

**What it does:** Stores credentials securely in system keychain

```bash
# Install Git Credential Manager
sudo apt update
sudo apt install git-credential-manager -y

# Configure to use it
git config --global credential.helper manager

# Or on Ubuntu/Debian, use libsecret
sudo apt install libsecret-1-0 libsecret-1-dev -y
cd /usr/share/doc/git/contrib/credential/libsecret
sudo make
git config --global credential.helper /usr/share/doc/git/contrib/credential/libsecret/git-credential-libsecret
```

**Pros:**
- ✅ Secure (uses system keychain)
- ✅ Encrypted storage
- ✅ Permanent (until you remove)

---

### 💻 Step 3: Use Token for First Time

#### Example 1: Clone Personal Repository

```bash
# Clone using HTTPS
git clone https://github.com/yourusername/my-personal-project.git

# Git will prompt:
# Username for 'https://github.com': yourusername
# Password for 'https://yourusername@github.com':

# Paste your PERSONAL token here (not password!)
# ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Credential saved! (based on helper configured)
```

---

#### Example 2: Clone Office Repository

```bash
# Clone using HTTPS
git clone https://github.com/company-org/office-project.git

# Git will prompt:
# Username for 'https://github.com': your-office-username
# Password for 'https://your-office-username@github.com':

# Paste your OFFICE token here
# ghp_yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy

# Credential saved!
```

---

#### Example 3: Push to Existing Repository

```bash
# Navigate to project
cd /path/to/your/project

# Add remote (if not exists)
git remote add origin https://github.com/username/repo.git

# Push
git push -u origin main

# If first time, Git will ask:
# Username: yourusername
# Password: ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Next time, it uses saved credentials automatically!
```

---

### 🔄 Step 4: Update/Change Stored Credentials

#### Method 1: Using Git Credential Fill (RECOMMENDED)

**Update Personal Account Token:**

```bash
# Fill/update credential for personal account
git credential fill <<EOF
protocol=https
host=github.com
username=your-personal-username
password=ghp_NEW_PERSONAL_TOKEN_HERE
EOF

# Approve (save) the credential
git credential approve <<EOF
protocol=https
host=github.com
username=your-personal-username
password=ghp_NEW_PERSONAL_TOKEN_HERE
EOF
```

**Update Office Account Token:**

```bash
# Fill/update credential for office account
git credential approve <<EOF
protocol=https
host=github.com
username=your-office-username
password=ghp_NEW_OFFICE_TOKEN_HERE
EOF
```

---

#### Method 2: Clear All Credentials & Re-enter

```bash
# Remove all stored credentials
git credential reject <<EOF
protocol=https
host=github.com
EOF

# Or if using credential store, delete file
rm ~/.git-credentials

# Next push/pull will ask for credentials again
git push
# Enter username and new token
```

---

#### Method 3: Edit Credentials File (if using store)

```bash
# Edit credentials file
nano ~/.git-credentials

# File format:
# https://username1:token1@github.com
# https://username2:token2@github.com

# Update tokens manually
# Save: Ctrl+X → Y → Enter
```

---

### 🎯 Step 5: Using Different Tokens for Different Projects

#### Strategy: Store Multiple Credentials

**Problem:** Git credential store saves one credential per `host` (github.com)

**Solution 1: Use Different Hosts (HTTPS Doesn't Support This Well)**

❌ HTTPS limitation: Can't easily use different tokens for same host

**Solution 2: Use SSH Keys (RECOMMENDED - See SSH Section Above)**

✅ SSH allows different keys for different accounts easily

---

#### Workaround for HTTPS: Manual Token Per Project

**Personal Project:**

```bash
cd ~/projects/personal-app

# Remove saved credential (if any)
git credential reject <<EOF
protocol=https
host=github.com
EOF

# Push (will ask for credentials)
git push
# Username: personal-username
# Password: ghp_PERSONAL_TOKEN

# Credential cached for this session
```

**Office Project:**

```bash
cd ~/Documents/office-project

# Remove saved credential
git credential reject <<EOF
protocol=https
host=github.com
EOF

# Push (will ask for credentials)
git push
# Username: office-username
# Password: ghp_OFFICE_TOKEN
```

**⚠️ Limitation:** Last entered credential overwrites previous one for same host.

**💡 Better Solution:** Use SSH keys (different keys for different accounts) - See SSH section above!

---

### 📋 Examples: Complete Workflows with Tokens

#### Example 1: First Time Setup - Personal Project

```bash
# Step 1: Configure Git identity
git-personal

# Step 2: Enable credential storage (choose one)
git config --global credential.helper cache  # or 'store' or 'manager'

# Step 3: Create new project
cd ~/projects
mkdir my-app
cd my-app
git init

# Step 4: Create some files
echo "# My App" > README.md
git add .
git commit -m "Initial commit"

# Step 5: Create repo on GitHub (Personal account)
# Go to github.com → New repository → my-app

# Step 6: Add remote
git remote add origin https://github.com/your-personal-username/my-app.git

# Step 7: Push (will ask for token FIRST TIME)
git push -u origin main

# Prompt:
# Username: your-personal-username
# Password: ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx (paste personal token)

# ✅ Done! Next time no password needed
```

---

#### Example 2: First Time Setup - Office Project

```bash
# Step 1: Configure Git identity for this project
cd ~/Documents/office-project
git-office-here

# Step 2: Verify identity
git-identity
# Should show office email

# Step 3: Add remote
git remote add origin https://github.com/company-org/office-project.git

# Step 4: Push
git push -u origin main

# Prompt:
# Username: your-office-username
# Password: ghp_yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy (paste office token)

# ✅ Done!
```

---

#### Example 3: Clone Existing Repo with Token

```bash
# Method 1: Clone, then Git asks for credentials
git clone https://github.com/username/repo.git
# Username: username
# Password: ghp_token_here

# Method 2: Embed token in URL (NOT RECOMMENDED - visible in history)
git clone https://username:ghp_token_here@github.com/username/repo.git
# ❌ Insecure: Token visible in shell history and git config!
```

---

#### Example 4: Update Expired Token

**Scenario:** Token expired after 90 days

```bash
# Step 1: Generate new token on GitHub
# (Follow Step 1 above)

# Step 2: Update stored credential
git credential approve <<EOF
protocol=https
host=github.com
username=your-username
password=ghp_NEW_TOKEN_HERE
EOF

# Step 3: Test
git push
# ✅ Should work with new token!
```

---

### 🔍 Check Current Stored Credentials

#### Using Credential Fill

```bash
# Check what credential Git will use
git credential fill <<EOF
protocol=https
host=github.com
EOF

# Output shows stored username (password hidden)
# protocol=https
# host=github.com
# username=saved-username
# password=ghp_***
```

#### If Using Credential Store

```bash
# View all stored credentials
cat ~/.git-credentials

# Output:
# https://username1:ghp_token1@github.com
# https://username2:ghp_token2@github.com
```

---

### 🗑️ Remove/Clear Credentials

#### Clear All GitHub Credentials

```bash
# Method 1: Reject credential for github.com
git credential reject <<EOF
protocol=https
host=github.com
EOF

# Method 2: Delete credentials file (if using store)
rm ~/.git-credentials

# Method 3: Unset credential helper
git config --global --unset credential.helper
```

#### Clear Specific Account Credential

```bash
# Reject specific username
git credential reject <<EOF
protocol=https
host=github.com
username=specific-username
EOF
```

---

### 💡 Best Practices for Token Management

| Practice | Why |
|----------|-----|
| ✅ Use SSH keys instead of HTTPS | More secure, easier multi-account management |
| ✅ Use `credential.helper cache` for temporary work | Credentials auto-expire |
| ✅ Use `credential.helper manager` for permanent | Secure, encrypted storage |
| ✅ Set token expiration (90 days) | Limits risk if token leaked |
| ✅ Use descriptive token names | Easy to identify and revoke |
| ✅ Store tokens in password manager | Safe backup if you forget |
| ❌ Don't use `credential.helper store` on shared machines | Plain text = insecure |
| ❌ Don't embed tokens in URLs | Visible in history and logs |
| ❌ Don't commit tokens to git | Public exposure risk |
| ❌ Don't share tokens | Each person should have own |

---

### 🆚 HTTPS vs SSH Comparison

| Feature | HTTPS (with Token) | SSH (with Keys) |
|---------|-------------------|-----------------|
| **Setup Difficulty** | ⭐⭐ Easy | ⭐⭐⭐ Moderate |
| **Multi-Account** | ⭐⭐ Harder | ⭐⭐⭐⭐ Easy |
| **Security** | ⭐⭐⭐ Good (if cached) | ⭐⭐⭐⭐ Better |
| **Expiration** | ❌ Tokens expire | ✅ Keys don't expire |
| **Password Needed** | ❌ No (use token) | ✅ Optional passphrase |
| **Behind Firewall** | ✅ Works (port 443) | ⚠️ May be blocked (port 22) |
| **Recommendation** | Use if SSH blocked | **RECOMMENDED** |

---

### 🎯 Quick Commands Reference

#### Setup Credential Helper

```bash
# Cache (15 min default)
git config --global credential.helper cache

# Cache (1 hour)
git config --global credential.helper 'cache --timeout=3600'

# Store (permanent, plain text)
git config --global credential.helper store

# Manager (permanent, encrypted)
git config --global credential.helper manager
```

#### Update Token

```bash
# Update stored credential
git credential approve <<EOF
protocol=https
host=github.com
username=your-username
password=ghp_NEW_TOKEN
EOF
```

#### Clear Credentials

```bash
# Clear all for github.com
git credential reject <<EOF
protocol=https
host=github.com
EOF
```

#### Check Credentials

```bash
# View saved credential (if using store)
cat ~/.git-credentials

# Test what Git will use
git credential fill <<EOF
protocol=https
host=github.com
EOF
```

---

## 🔄 System Format / Recovery Scenarios

### ❓ System Format Hone Par Kya Hoga?

**Important Question:** Agar system format ho jaye to SSH keys ka kya hoga?

---

### 🚨 Kya Kho Jayega (After Format):

```
Local Computer (Format ho gaya)
├── ~/.ssh/ folder                    ← DELETED ❌
├── id_ed25519_personal               ← DELETED ❌
├── id_ed25519_personal.pub           ← DELETED ❌
├── id_ed25519_office                 ← DELETED ❌
├── id_ed25519_office.pub             ← DELETED ❌
└── config                            ← DELETED ❌
```

**Result:** SSH keys delete ho jayengi!

---

### ✅ Kya Safe Rahega:

```
GitHub Servers (Cloud - Safe)
├── Personal Account
│   └── Public Keys (uploaded)        ← SAFE ✅
└── Office Account
    └── Public Keys (uploaded)        ← SAFE ✅
```

**But:** GitHub par old public keys hain, lekin tumhare paas corresponding private keys nahi!

---

### 🔑 Problem:

```
You: git push
      ↓
SSH tries to authenticate
      ↓
No private key found! ❌
      ↓
Error: Permission denied (publickey)
```

**Reason:** Private key (local) aur Public key (GitHub) match nahi kar rahe.

---

## 💡 Recovery Solutions - 3 Options

### **Option 1: Backup Rakhna (BEFORE Format) - RECOMMENDED** ⭐

**Format karne se PEHLE backup lo:**

#### Backup Commands:

```bash
# Method 1: Simple copy
cp -r ~/.ssh ~/Documents/ssh_backup/

# Method 2: Compressed archive
tar -czf ssh_backup_$(date +%Y%m%d).tar.gz ~/.ssh/

# Method 3: Copy to external drive
cp -r ~/.ssh /media/usb/ssh_backup/
```

**Backup Store Kahan Karein:**
- ✅ External USB drive (encrypted)
- ✅ Google Drive / Dropbox (in encrypted zip)
- ✅ Password Manager (1Password, Bitwarden)
- ❌ Public cloud without encryption

---

#### After Format - Restore Backup:

```bash
# Method 1: Restore from folder
cp -r ~/Documents/ssh_backup/ ~/.ssh/

# Method 2: Extract from archive
tar -xzf ssh_backup_20260221.tar.gz -C ~/

# Method 3: Copy from USB
cp -r /media/usb/ssh_backup/ ~/.ssh/

# Set correct permissions (IMPORTANT!)
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519_*
chmod 644 ~/.ssh/id_ed25519_*.pub
chmod 600 ~/.ssh/config

# Restart SSH agent and add keys
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_personal
ssh-add ~/.ssh/id_ed25519_office

# Test connections
ssh -T git@github-personal
ssh -T git@github-office
```

**✅ Benefit:** Same keys restore ho gayi, GitHub par kuch change nahi karna pada!

---

### **Option 2: New Keys Generate Karna (AFTER Format) - Common**

**Agar backup nahi hai to fresh start:**

```bash
# Complete setup from scratch
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# Generate new keys
ssh-keygen -t ed25519 -C "yogesh.lachheta111@gmail.com" -f ~/.ssh/id_ed25519_personal -N ""
ssh-keygen -t ed25519 -C "yogesh.lachheta@47billion.com" -f ~/.ssh/id_ed25519_office -N ""

# Create config
cat > ~/.ssh/config << 'EOF'
# Personal GitHub Account
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes

# Office GitHub Account
Host github-office
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_office
    IdentitiesOnly yes
EOF

# Set permissions
chmod 600 ~/.ssh/config
chmod 600 ~/.ssh/id_ed25519_personal
chmod 600 ~/.ssh/id_ed25519_office
chmod 644 ~/.ssh/id_ed25519_personal.pub
chmod 644 ~/.ssh/id_ed25519_office.pub

# Add to SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_personal
ssh-add ~/.ssh/id_ed25519_office

# Display new public keys
cat ~/.ssh/id_ed25519_personal.pub
cat ~/.ssh/id_ed25519_office.pub
```

**GitHub Par Update Karo:**

1. **Personal GitHub** → Settings → SSH Keys
   - Delete old key (optional)
   - Add new key → Paste new `id_ed25519_personal.pub`

2. **Office GitHub** → Settings → SSH Keys
   - Delete old key (optional)
   - Add new key → Paste new `id_ed25519_office.pub`

**✅ Done! New keys se kaam chalega.**

---

### **Option 3: Multiple Devices - Multiple Keys**

**Best Practice for Multiple Computers:**

```
GitHub Personal Account
├── Key 1: "Home Laptop Ubuntu 2026" (old)
├── Key 2: "Office Desktop Windows" (new after format)
└── Key 3: "Personal MacBook" (another device)

GitHub Office Account
├── Key 1: "Home Laptop Ubuntu 2026" (old)
├── Key 2: "Office Desktop Windows" (new)
└── Key 3: "Work MacBook" (another)
```

**Benefit:**
- ✅ Ek device format hone se dusre devices ki keys kaam karegi
- ✅ Multiple devices par simultaneously work kar sakte ho
- ✅ Har device ka alag key = better security tracking

**How to Add Multiple Keys on GitHub:**

1. Go to Settings → SSH and GPG keys
2. Each device ke liye alag key add karo:
   - "Home Laptop - Ubuntu 2026" → key1.pub
   - "Office Desktop - Windows" → key2.pub
   - "Personal MacBook - Mac" → key3.pub

**All keys valid rahegi simultaneously!**

---

## 💾 Backup Strategies (Best Practices)

### 🔐 Secure Backup Methods

#### Method 1: Encrypted Archive (Recommended)

```bash
# Create password-protected encrypted backup
tar -czf - ~/.ssh | openssl enc -aes-256-cbc -salt -out ssh_backup.tar.gz.enc

# Restore encrypted backup
openssl enc -aes-256-cbc -d -in ssh_backup.tar.gz.enc | tar -xzf - -C ~/
```

**Where to Store:**
- ✅ External USB drive
- ✅ Cloud storage (encrypted)
- ✅ Password manager

---

#### Method 2: Cloud Backup (With Encryption)

```bash
# Create encrypted zip
zip -er ssh_backup.zip ~/.ssh/*

# Upload to:
# - Google Drive (personal)
# - Dropbox
# - OneDrive
```

**⚠️ Security:** Always encrypt before uploading to cloud!

---

#### Method 3: Password Manager Storage

**Store in password managers:**
- 1Password (Secure Notes)
- Bitwarden (Secure Notes)
- LastPass (Secure Notes)

**Store:**
- Private key content (copy file content)
- Public key content
- SSH config content

---

### 📋 Backup Checklist

| Item | What to Backup | Why |
|------|---------------|-----|
| **Private Keys** | `~/.ssh/id_ed25519_*` | Secret authentication keys |
| **Public Keys** | `~/.ssh/id_ed25519_*.pub` | Reference (can regenerate) |
| **Config File** | `~/.ssh/config` | SSH configuration |
| **Git Config** | `~/.gitconfig` | Git global settings |
| **Bashrc Aliases** | `~/.bashrc` | Git account switchers |

**Backup Command (All in One):**

```bash
# Create comprehensive backup
mkdir -p ~/git_config_backup
cp -r ~/.ssh ~/git_config_backup/
cp ~/.gitconfig ~/git_config_backup/
cp ~/.bashrc ~/git_config_backup/

# Create archive
tar -czf git_config_backup_$(date +%Y%m%d).tar.gz ~/git_config_backup/

# Encrypt (optional but recommended)
openssl enc -aes-256-cbc -salt -in git_config_backup_*.tar.gz -out git_config_backup_encrypted.tar.gz.enc
```

---

## 🔄 Complete Recovery Workflow (Step-by-Step)

### Scenario: System format ho gaya, backup nahi hai

```bash
# ============================================
# Fresh Ubuntu Install - Complete Git Setup
# ============================================

# 1. Update system
sudo apt update && sudo apt upgrade -y

# 2. Install Git
sudo apt install git -y

# 3. Verify Git installed
git --version

# 4. Setup Git aliases (.bashrc)
nano ~/.bashrc
# Add these lines at the end:

# ========================================
# Git Account Switchers - Yogesh Lachheta
# ========================================

# Switch to PERSONAL account (Global)
alias git-personal='git config --global user.name "Yogesh Lachheta" && git config --global user.email "yogesh.lachheta111@gmail.com" && echo "✅ Switched to PERSONAL (Global)"'

# Switch to OFFICE account (Global) - 47billion
alias git-office='git config --global user.name "Yogesh Lachheta" && git config --global user.email "yogesh.lachheta@47billion.com" && echo "✅ Switched to OFFICE (Global)"'

# Set PERSONAL for CURRENT PROJECT only
alias git-personal-here='git config --local user.name "Yogesh Lachheta" && git config --local user.email "yogesh.lachheta111@gmail.com" && echo "✅ Current project → PERSONAL"'

# Set OFFICE for CURRENT PROJECT only - 47billion
alias git-office-here='git config --local user.name "Yogesh Lachheta" && git config --local user.email "yogesh.lachheta@47billion.com" && echo "✅ Current project → OFFICE"'

# Check who am I?
alias git-whoami='echo "=== GLOBAL CONFIG ===" && git config --global user.name && git config --global user.email && echo "" && echo "=== LOCAL CONFIG (current project) ===" && git config --local user.name 2>/dev/null && git config --local user.email 2>/dev/null || echo "(No local config set)"'

# Show current identity (what will be used for commits)
alias git-identity='echo "Commits will use:" && git config user.name && git config user.email'

# Save: Ctrl+X → Y → Enter

# 5. Reload bashrc
source ~/.bashrc

# 6. Set global to office
git-office

# 7. Verify
git-whoami

# 8. Generate NEW SSH keys
mkdir -p ~/.ssh && chmod 700 ~/.ssh
ssh-keygen -t ed25519 -C "yogesh.lachheta111@gmail.com" -f ~/.ssh/id_ed25519_personal -N ""
ssh-keygen -t ed25519 -C "yogesh.lachheta@47billion.com" -f ~/.ssh/id_ed25519_office -N ""

# 9. Create SSH config
cat > ~/.ssh/config << 'EOF'
# Personal GitHub Account
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes

# Office GitHub Account
Host github-office
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_office
    IdentitiesOnly yes
EOF

# 10. Set permissions
chmod 600 ~/.ssh/config
chmod 600 ~/.ssh/id_ed25519_personal
chmod 600 ~/.ssh/id_ed25519_office
chmod 644 ~/.ssh/id_ed25519_personal.pub
chmod 644 ~/.ssh/id_ed25519_office.pub

# 11. Start SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_personal
ssh-add ~/.ssh/id_ed25519_office

# 12. Display public keys
echo "========================================="
echo "PERSONAL PUBLIC KEY:"
cat ~/.ssh/id_ed25519_personal.pub
echo ""
echo "OFFICE PUBLIC KEY:"
cat ~/.ssh/id_ed25519_office.pub
echo "========================================="

# 13. Upload keys to GitHub (manual - browser mein)
# Personal GitHub → Settings → SSH Keys → Add new key
# Office GitHub → Settings → SSH Keys → Add new key

# 14. Test connections
ssh -T git@github-personal
ssh -T git@github-office

# 15. Expected output:
# Hi yogesh-lachheta! You've successfully authenticated...
# Hi yogesh47! You've successfully authenticated...

# ✅ Recovery Complete!
```

---

## 🛡️ Security Best Practices

### Before System Format:

- [ ] Backup `~/.ssh/` folder (encrypted)
- [ ] Backup `~/.gitconfig` file
- [ ] Backup `~/.bashrc` (Git aliases section)
- [ ] Document which keys are on GitHub
- [ ] Store backup in secure location (external drive/cloud encrypted)

---

### After System Format:

- [ ] Delete old keys from GitHub (if generating new ones)
- [ ] Generate new keys with descriptive names
- [ ] Upload new public keys to GitHub
- [ ] Test SSH connections
- [ ] Create new backup immediately
- [ ] Document new setup

---

### Multiple Devices:

- [ ] Each device has unique SSH key pair
- [ ] Each key has descriptive title on GitHub
- [ ] Keep track of which key is on which device
- [ ] Remove unused/old keys from GitHub
- [ ] Backup keys from each device separately

---

## 📊 Recovery Scenarios Summary

| Scenario | Action Required | GitHub Changes | Time Required |
|----------|----------------|----------------|---------------|
| **Backup available** | Restore `~/.ssh/` folder | None | 5 minutes |
| **No backup** | Generate new keys | Upload new keys, delete old | 15 minutes |
| **Multiple devices** | Each device has own keys | Add all device keys | 10 min per device |
| **Lost private key** | Generate new key pair | Replace public key | 10 minutes |
| **Compromised key** | Delete + generate new ASAP | Replace immediately | 10 minutes |

---

## ⚠️ Important Security Notes

### 1. Private Keys Kabhi Recover Nahi Ho Sakti (Without Backup)

```
Private Key Lost = Must Generate New Key Pair
```

### 2. Public Keys Multiple Hone Mein Koi Dikkat Nahi

```
Laptop 1 → key1_personal.pub   ✅
Laptop 2 → key2_personal.pub   ✅  All valid simultaneously!
Desktop  → key3_personal.pub   ✅
```

### 3. Old Keys Security Risk (Agar Device Lost/Format)

```
Old public key on GitHub + Private key deleted = Limited risk
(Private key nahi hai to authenticate nahi kar sakte)

Best Practice: Delete unused keys from GitHub
```

---

## 🚀 Common Workflows

### Workflow 1: New Office Project

```bash
# 1. Set global to personal (default)
git-personal

# 2. Navigate to office project
cd /path/to/office/project

# 3. Initialize git
git init

# 4. Set THIS project to office
git-office-here

# 5. Verify
git-identity
# Should show office@company.com

# 6. Add remote (office SSH host)
git remote add origin git@github-office:company/project.git

# 7. First commit
git add .
git commit -m "Initial commit"
git push -u origin main
```

---

### Workflow 2: New Personal Project

```bash
# 1. Ensure global is personal
git-personal

# 2. Navigate to personal project
cd ~/projects/my-app

# 3. Initialize git
git init

# 4. Verify (should use personal from global)
git-identity
# Should show personal@gmail.com

# 5. Add remote (personal SSH host)
git remote add origin git@github-personal:username/my-app.git

# 6. First commit
git add .
git commit -m "Initial commit"
git push -u origin main
```

---

### Workflow 3: Clone & Setup Office Repo

```bash
# 1. Clone using office SSH host
git clone git@github-office:company/existing-project.git

# 2. Navigate to project
cd existing-project

# 3. Set to office account
git-office-here

# 4. Verify
git-identity
# Should show office@company.com

# 5. Start working
git checkout -b feature/my-feature
```

---

### Workflow 4: Clone & Setup Personal Repo

```bash
# 1. Clone using personal SSH host
git clone git@github-personal:username/existing-project.git

# 2. Navigate to project
cd existing-project

# 3. Verify (should use global personal)
git-identity
# Should show personal@gmail.com

# 4. Start working
git checkout -b feature/my-feature
```

---

## 💡 Quick Reference

### One-Command Switches

| Command | What It Does | Scope |
|---------|-------------|-------|
| `git-personal` | Switch to personal account | Global (all projects) |
| `git-office` | Switch to office account | Global (all projects) |
| `git-personal-here` | Set current project to personal | Local (this project only) |
| `git-office-here` | Set current project to office | Local (this project only) |
| `git-whoami` | Show global & local config | Info only |
| `git-identity` | Show what will be used for commits | Info only |

---

### Before Every Commit - CHECK!

```bash
# Always verify before first commit in new project
git-identity

# If wrong, fix it:
git-office-here   # or git-personal-here
```

---

### SSH Remote URLs

| Account | Remote URL Format | Example |
|---------|------------------|---------|
| **Personal** | `git@github-personal:username/repo.git` | `git@github-personal:johndoe/my-app.git` |
| **Office** | `git@github-office:org/repo.git` | `git@github-office:company/cricket-auction.git` |

---

## 🎯 Recommended Setup

**1. Set Personal as Global Default**

```bash
git-personal
```

**2. For Each Office Project**

```bash
cd /path/to/office/project
git-office-here
```

**3. Before Any Commit**

```bash
git-identity   # Verify!
```

---

## 🛠️ Troubleshooting

### Problem: Git asks for password even with SSH

**Solution:**

```bash
# Check SSH keys loaded
ssh-add -l

# If empty, add keys
ssh-add ~/.ssh/id_ed25519_personal
ssh-add ~/.ssh/id_ed25519_office

# Test connections
ssh -T git@github-personal
ssh -T git@github-office
```

---

### Problem: Committed with wrong account

**If NOT pushed yet:**

```bash
# Fix identity
git-office-here  # or git-personal-here

# Amend last commit
git commit --amend --reset-author --no-edit
```

**If PUSHED already:**
- Can't easily fix - better to be careful before pushing!

---

### Problem: git-office: command not found

**Reason:** Bashrc aliases load nahi hui hain.

**Solution 1: Reload Bashrc (Quick Fix)**

```bash
# Reload bashrc
source ~/.bashrc

# Test
git-office
# Expected: ✅ Switched to OFFICE (Global)
```

**✅ Fixed!**

---

**Solution 2: Check Aliases Exist in Bashrc**

```bash
# Check last 20 lines of bashrc
tail -20 ~/.bashrc

# Should show:
# alias git-personal='...'
# alias git-office='...'
# alias git-whoami='...'
# etc.
```

**Agar aliases nahi dikhe to dobara add karo:**

```bash
# Open bashrc
nano ~/.bashrc

# Scroll to end (Ctrl+End)

# Paste Git aliases section:
# ========================================
# Git Account Switchers - Yogesh Lachheta
# ========================================

# Switch to PERSONAL account (Global)
alias git-personal='git config --global user.name "Yogesh Lachheta" && git config --global user.email "yogesh.lachheta111@gmail.com" && echo "✅ Switched to PERSONAL (Global)"'

# Switch to OFFICE account (Global) - 47billion
alias git-office='git config --global user.name "Yogesh Lachheta" && git config --global user.email "yogesh.lachheta@47billion.com" && echo "✅ Switched to OFFICE (Global)"'

# Set PERSONAL for CURRENT PROJECT only
alias git-personal-here='git config --local user.name "Yogesh Lachheta" && git config --local user.email "yogesh.lachheta111@gmail.com" && echo "✅ Current project → PERSONAL"'

# Set OFFICE for CURRENT PROJECT only - 47billion
alias git-office-here='git config --local user.name "Yogesh Lachheta" && git config --local user.email "yogesh.lachheta@47billion.com" && echo "✅ Current project → OFFICE"'

# Check who am I?
alias git-whoami='echo "=== GLOBAL CONFIG ===" && git config --global user.name && git config --global user.email && echo "" && echo "=== LOCAL CONFIG (current project) ===" && git config --local user.name 2>/dev/null && git config --local user.email 2>/dev/null || echo "(No local config set)"'

# Show current identity (what will be used for commits)
alias git-identity='echo "Commits will use:" && git config user.name && git config user.email'

# Save: Ctrl+X → Y → Enter

# Reload bashrc
source ~/.bashrc

# Test all aliases
git-office
git-personal
git-whoami
```

**✅ Fixed!**

---

**Solution 3: New Terminal Mein Automatic Load**

**Important:** `source ~/.bashrc` sirf current terminal session mein kaam karta hai.

**New terminal kholo:**
- Aliases automatically load ho jayengi
- `git-office` direct kaam karega

**Ya restart terminal:**
```bash
# Close current terminal (Ctrl+D)
# Open new terminal (Ctrl+Alt+T)

# Test
git-office
```

---

### Problem: Aliases Work, But Forget After Reboot

**Reason:** Aliases `.bashrc` mein properly save nahi hui.

**Solution:**

```bash
# Check bashrc saved hai ya nahi
cat ~/.bashrc | grep "git-office"

# Agar output nahi aaya to aliases missing hain
# Dobara add karo (Solution 2 dekho uper)
```

**Verify Permanent Save:**

```bash
# Open new terminal
# Test
git-office

# Agar kaam kiya = permanently saved ✅
```

---

## ✅ Setup Checklist

- [ ] Git installed (`sudo apt install git`)
- [ ] Aliases added to `~/.bashrc`
- [ ] Bashrc reloaded (`source ~/.bashrc`)
- [ ] Test `git-personal` command
- [ ] Test `git-office` command
- [ ] Test `git-whoami` command
- [ ] SSH keys generated for both accounts
- [ ] SSH config file created (`~/.ssh/config`)
- [ ] Public keys added to GitHub accounts
- [ ] Test SSH: `ssh -T git@github-personal`
- [ ] Test SSH: `ssh -T git@github-office`

---

<div align="center">

## 🎉 You're All Set!

**Switch accounts with one command:**

```bash
git-personal      # Personal account (global)
git-office        # Office account (global)
git-office-here   # Office for this project
git-whoami        # Check current setup
```

**Last Updated:** 2026-02-21

</div>
