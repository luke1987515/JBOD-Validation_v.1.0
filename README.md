## JBOD Validation Platform

<div align="center">

Enterprise-level JBOD Validation Management Platform built with Django.

The platform provides a complete validation workflow including:

- Dashboard Monitoring
- Model Management
- Firmware Management
- Test Plan Management
- Validation Execution
- Authentication System
- Report Management

Designed for enterprise JBOD validation and automation.

企業級 JBOD 驗證管理平台

</div>

📖 Introduction / 專案介紹

JBOD Validation Platform is an enterprise-level web application built with Django for validating and managing JBOD (Just a Bunch Of Disks) storage systems.

JBOD Validation Platform 是一套以 Django 開發的企業級 JBOD（Just a Bunch Of Disks）驗證管理平台，提供完整的驗證流程管理、測試規劃、執行追蹤與報告管理。

---

## ✨ Features / 功能特色

- Dashboard / 儀表板
- Model Management / Model 管理
- Firmware Management / Firmware 管理
- Test Case Management / Test Case 管理
- Test Plan Management / Test Plan 管理
- Validation Center / Validation 管理
- Execute Validation Workflow / 驗證執行流程
- Report Center (Planned) / 報告中心（規劃中）

---

## 🏗 System Architecture / 系統架構

Dashboard
    │
    ├── Models
    ├── Firmware
    ├── Test Case
    ├── Test Plan
    ├── Validation
    │       │
    │       ▼
    │   Execute Validation
    │       │
    │       ├── Progress
    │       ├── Logs
    │       └── Reports
    └── User

---

## 📊 Development Progress / 開發進度
| Module            |  Progress  |
| ----------------- | :--------: |
| Dashboard         |   ✅ 100%   |
| User              |   ✅ 100%   |
| Models            |   ✅ 100%   |
| Firmware          |   ✅ 100%   |
| Test Case         |   ✅ 100%   |
| Test Plan         |   ✅ 100%   |
| Validation        |   🟡 90%   |
| Execute           |   🟢 95%   |
| Report            | 🔴 Planned |
| Logs              | 🔴 Planned |
| Automation Engine |  ⚪ Planned |

---

## 🛠 Tech Stack / 技術架構
| Category        | Technology         | 說明    |
| --------------- | ------------------ | ----- |
| Backend         | Django 6.x         | 後端框架  |
| Frontend        | HTML5, Bootstrap 5 | 前端    |
| Language        | Python 3.14        | 程式語言  |
| Database        | SQLite3            | 資料庫   |
| Icons           | Font Awesome       | 圖示    |
| Version Control | Git                | 版本控制  |
| Repository      | GitHub             | 原始碼管理 |
| IDE             | Visual Studio Code | 開發工具  |

---

## 📁 Project Structure / 專案架構

JBOD-Validation/
│
├── dashboard/
├── executor/
├── firmware/
├── logs/
├── models_app/
├── report/
├── testcase/
├── testplan/
├── user/
├── validation/
│
├── static/
├── templates/
├── docs/
│
├── manage.py
├── requirements.txt
└── README.md

---

## ⚙ Installation / 安裝方式

### Clone Repository / 複製專案
> git clone https://github.com/shingyu0205/JBOD-Validation.git

### Enter Project / 進入專案
> cd JBOD-Validation

### Create Virtual Environment / 建立虛擬環境
> Create Virtual Environment / 建立虛擬環境

### Activate Virtual Environment / 啟用虛擬環境
> .\.venv\Scripts\Activate.ps1

### Install Dependencies / 安裝套件
> pip install -r requirements.txt

### Run Server / 啟動伺服器
> python manage.py runserver

### Open Browser / 開啟瀏覽器
> http://127.0.0.1:8000/

---

## 📦 Main Applications / 主要模組
| App        | Description          | 中文            |
| ---------- | -------------------- | ------------- |
| dashboard  | Dashboard            | 儀表板           |
| models_app | Model Management     | Model 管理      |
| firmware   | Firmware Management  | Firmware 管理   |
| testcase   | Test Case Management | Test Case 管理  |
| testplan   | Test Plan Management | Test Plan 管理  |
| validation | Validation Center    | Validation 管理 |
| executor   | Execute Validation   | 執行驗證          |
| report     | Report Center        | 報告中心          |
| logs       | Log Center           | 日誌中心          |
| user       | User Management      | 使用者管理         |

---

## 🏷 Version Naming Convention / 版本命名規範
This project follows Semantic Versioning (SemVer).
本專案採用 Semantic Versioning（SemVer）。

| Version | Description      | 中文            |
| ------- | ---------------- | ------------- |
| Major   | Breaking Changes | 架構重大變更        |
| Minor   | New Features     | 新功能           |
| Patch   | Bug Fixes        | Bug 修正與 UI 優化 |

Example:
> v1.0.0 → v1.1.0 → v1.2.0

---

## 📜 Release History / 版本歷程
### v1.1.1 (2026-08-05)

**New Features**
- Enterprise Login UI
- User Registration
- Auto Login after Registration
- Remember Username
- Password Visibility Toggle

**Improvements**
- Redesigned Login Interface
- Improved Authentication Module
- Updated Project Structure
- Enhanced UI Consistencyb

### v1.1.0 (2026-08-04)
**Added**
- Execute Validation Workflow
- Execute Detail
- Pending / Running / Stop / Retry
- Validation Center

**Improved**
- Dashboard UI
- Execute Dashboard
- Progress Bar

### v1.0.2 (2026-07-31)
**Added**
- Login Page

### v1.0.1 (2026-07-30)
**Added**
- Traditional Chinese / English UI

**Improved**
- User Interface

### v1.0.0 (2026-07-27)
Initial Release

---

## 🗺 Roadmap / 開發規劃

### v1.2.0
- Mock Validation Engine
- Auto Progress Simulation
- Current Running Status
### v1.3.0
- Execute Logs
- Timeline View
### v1.4.0
- Report Center
- PDF Export
- Excel Export
### v2.0.0
- SSH Integration
- IPMI Integration
- Smartctl Integration
- StorCLI Integration
- Iometer Integration

## 👨‍💻 Author

Shing-Yu Chou(Travis)

GitHub: https://github.com/shingyu0205

## 📄 License

MIT License