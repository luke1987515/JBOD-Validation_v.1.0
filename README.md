# JBOD Validation Platform

A web-based **JBOD (Just a Bunch Of Disks) Validation Platform** built with **Django** for enterprise storage validation management.

The platform centralizes **asset management, firmware management, validation planning, automated execution, and report generation** into a modern web interface designed for Product Validation Engineers.

---

# Features

## Dashboard

- Validation Overview
- Running Jobs
- Recent Firmware Releases
- Validation Statistics
- Quick Navigation

---

## Asset Management

### JBOD Models

- Create / Edit / Delete Models
- Vendor Management
- Platform Management
- Firmware Association
- Status Management

### Firmware Management

Support multiple firmware types:

- BIOS
- BMC
- CPLD
- Expander
- PSU

Features:

- Version Management
- Release Date
- Build Number
- Vendor
- Status Tracking

---

## Validation Management

### Validation Center

Manage validation projects.

Features:

- Create Validation
- Edit Validation
- Validation Status
- Assigned Test Plan
- Assigned Firmware

### Test Case

Manage validation scripts.

Support:

- Function Test
- Hardware Test
- Firmware Test
- Performance Test
- Stress Test

Each Test Case contains:

- Command / Script
- Timeout
- Description
- Status

### Test Plan

Create reusable validation plans.

Each Test Plan contains:

- JBOD Model
- Firmware
- Multiple Test Cases
- Description

---

## Validation Executor *(In Development)*

Execute validation tasks with:

- Progress Monitoring
- Real-time Status
- Execution Logs
- PASS / FAIL Result
- Live Console Output

---

## Report System *(Planned)*

Generate validation reports including:

- Validation Summary
- Firmware Information
- Test Results
- Execution Logs
- PDF Export
- HTML Report

---

# Enterprise UI

Current UI includes:

- Bootstrap 5 Dashboard
- Responsive Sidebar
- Reusable UI Components
- Card Layout
- Search Component
- Status Badge
- Empty State
- Responsive Tables

---

# Technology Stack

## Backend

- Python 3.14
- Django 6

## Frontend

- Bootstrap 5
- HTML5
- CSS3
- JavaScript
- Font Awesome

## Database

Development

- SQLite

Production (Planned)

- PostgreSQL

---

# Project Structure

```text
JBOD-Validation/
│
├── dashboard/
├── models_app/
├── firmware/
├── validation/
├── testcase/
├── testplan/
├── executor/
├── report/
│
├── templates/
│   ├── dashboard/
│   ├── model/
│   ├── firmware/
│   ├── validation/
│   ├── testcase/
│   ├── testplan/
│   ├── components/
│   └── includes/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── docs/
│
├── jbod_validation/
│
├── manage.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/<your-account>/JBOD-Validation.git

cd JBOD-Validation
```

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Database Migration

```bash
python manage.py makemigrations

python manage.py migrate
```

## Create Superuser

```bash
python manage.py createsuperuser
```

## Run Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

# Development Roadmap

## Phase 1 ✅

- [x] Dashboard
- [x] Models
- [x] Firmware
- [x] Validation Center
- [x] Reusable UI Components
- [x] Enterprise Sidebar

## Phase 2 🚧

- [ ] Test Case CRUD
- [ ] Test Plan CRUD
- [ ] Executor
- [ ] Progress Monitor

## Phase 3

- [ ] Validation Report
- [ ] PDF Export
- [ ] Charts
- [ ] Dashboard Analytics

## Phase 4

- [ ] REST API
- [ ] WebSocket
- [ ] Celery
- [ ] PostgreSQL
- [ ] Docker

---

# Screenshots

Coming Soon

---

# License

This project is licensed under the **MIT License**.

See the LICENSE file for details.

---

# Author

**Travis**

Product Validation Engineer

Python Developer

Django Developer

Storage Validation Automation

---

⭐ If you like this project, please consider giving it a star.