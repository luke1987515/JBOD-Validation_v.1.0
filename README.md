# JBOD Validation Platform

A web-based **JBOD (Just a Bunch Of Disks) Validation Platform** built with **Django** for managing validation assets, firmware, test plans, and automated execution workflows.

The platform is designed to streamline the validation process for enterprise storage products by integrating asset management, test execution, progress monitoring, and report generation into a single web interface.

---

## Features

### Dashboard

- Validation overview
- Running jobs
- Recent firmware releases
- Validation statistics

### Model Management

- Create, edit, delete and view JBOD models
- Vendor information
- Platform information
- Firmware association

### Firmware Management

- BIOS
- BMC
- CPLD
- Expander
- PSU Firmware

Support for:

- Version management
- Release date
- Vendor
- Build number
- Status management

### Test Case Management

Manage validation scripts including:

- Function Test
- Hardware Test
- Firmware Test
- Performance Test
- Stress Test

Each test case contains:

- Script / Command
- Timeout
- Description
- Status

### Test Plan Management

Create reusable validation plans.

Each Test Plan contains:

- JBOD Model
- Firmware
- Multiple Test Cases
- Description

### Validation Executor

Execute validation tasks with:

- Progress monitoring
- Real-time status
- Execution logs
- PASS / FAIL result

### Report System (Planned)

Generate validation reports including:

- Test Summary
- Execution Result
- Firmware Information
- Test Log
- PDF Export

---

## Technology Stack

### Backend

- Django 6
- Python 3

### Frontend

- Bootstrap 5
- HTML5
- CSS3
- JavaScript

### Database

- SQLite (Development)
- PostgreSQL (Future)

### Icons

- Font Awesome

---

## Project Structure

```text
JBOD-Validation/
│
├── dashboard/
├── models_app/
├── firmware/
├── testcase/
├── testplan/
├── executor/
├── report/
│
├── templates/
│
├── static/
│
├── jbod_validation/
│
└── manage.py
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourname/JBOD-Validation.git

cd JBOD-Validation
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Database Migration

```bash
python manage.py makemigrations

python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Development Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000
```

---

## Development Roadmap

### Phase 1

- [x] Dashboard
- [x] Model Management
- [x] Firmware Management
- [ ] Test Case Management
- [ ] Test Plan Management

### Phase 2

- [ ] Validation Executor
- [ ] Execution Log
- [ ] Progress Monitor
- [ ] Real-time Status

### Phase 3

- [ ] Report Generation
- [ ] PDF Export
- [ ] Charts
- [ ] Email Notification

### Phase 4

- [ ] REST API
- [ ] WebSocket
- [ ] Docker Deployment
- [ ] PostgreSQL
- [ ] Celery Task Queue

---

## Screenshots

Coming Soon

---

## License

MIT License

---

## Author

**Travis**

Product Validation Engineer

Django Developer

Storage Validation Automation