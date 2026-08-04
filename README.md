JBOD Validation Platform

<div align="center">



Enterprise-level JBOD Validation Management Platform

企業級 JBOD 驗證管理平台

</div>

📖 Introduction / 專案介紹

JBOD Validation Platform is an enterprise-level web application built with Django for validating and managing JBOD (Just a Bunch Of Disks) storage systems.

JBOD Validation Platform 是一套以 Django 開發的企業級 JBOD（Just a Bunch Of Disks）驗證管理平台，提供完整的驗證流程管理、測試規劃、執行追蹤與報告管理。

✨ Features / 功能特色

Dashboard / 儀表板

Model Management / Model 管理

Firmware Management / Firmware 管理

Test Case Management / Test Case 管理

Test Plan Management / Test Plan 管理

Validation Center / Validation 管理

Execute Validation Workflow / 驗證執行流程

Report Center (Planned) / 報告中心（規劃中）

🏗 System Architecture / 系統架構

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

📊 Development Progress / 開發進度

Module

Progress

Dashboard

✅

Models

✅

Firmware

✅

Test Case

✅

Test Plan

✅

Validation

🟡

Execute

🟢

Report

🚧

Logs

🚧

🛠 Tech Stack / 技術架構

Category

Technology

Backend

Django 6.x

Frontend

Bootstrap 5

Database

SQLite3

Language

Python 3.14

IDE

Visual Studio Code

Version Control

Git

Repository

GitHub

📁 Project Structure / 專案架構

JBOD-Validation/
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
├── static/
├── templates/
├── manage.py
└── README.md

⚙ Installation / 安裝方式

git clone https://github.com/shingyu0205/JBOD-Validation.git
cd JBOD-Validation
python -m venv .venv

Windows:

.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
python manage.py runserver

Open:

http://127.0.0.1:8000/

🏷 Version Naming Convention / 版本命名規範

This project follows Semantic Versioning (SemVer).

Version

Description

Major

Breaking Changes

Minor

New Features

Patch

Bug Fixes

📜 Release History / 版本歷程

v1.1.0

Execute Validation

Execute Detail

Pending / Running / Stop / Retry

Dashboard Improvements

v1.0.2

Login Page

v1.0.1

Traditional Chinese / English UI

v1.0.0

Initial Release

🗺 Roadmap / 開發規劃

v1.2.0 Mock Validation Engine

v1.3.0 Execute Logs

v1.4.0 Report Center

v2.0.0 Hardware Integration (SSH/IPMI/Smartctl/StorCLI/Iometer)

👨‍💻 Author

Shing-Yu Chou

GitHub: https://github.com/shingyu0205

📄 License

MIT License