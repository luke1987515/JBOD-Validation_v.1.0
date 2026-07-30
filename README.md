# JBOD Validation Platform

Enterprise-level JBOD Validation Management Platform built with Django.

## 📖 Introduction

JBOD Validation Platform is a web-based management system designed for validating and managing JBOD (Just a Bunch Of Disks) storage systems.

The platform integrates:

- Model Management
- Firmware Management
- Test Case Management
- Validation Execution
- Report Management
- Dashboard Monitoring

This project aims to simplify the validation workflow and improve engineering efficiency.

---

## 🚀 Features

### Dashboard

- System Overview
- Validation Statistics
- Running Jobs
- Recent Firmware
- Recent Test Results

### Model Management

- Add/Delete/Edit JBOD Models
- Product Information
- Vendor Management

### Firmware Management

- Upload Firmware
- Firmware Version Control
- Release Date Management

### Test Case Management

- Create Test Cases
- Test Category
- Test Description
- Expected Result

### Validation Execution

- Execute Validation Jobs
- Running Status
- Progress Monitoring
- Execution History

### Report Management

- Validation Reports
- Export Results
- Historical Records

---

## 🏗 Project Structure

```
JBOD-Validation/
│
├── dashboard/
├── firmware/
├── models_app/
├── testcase/
├── executor/
├── report/
├── validation/
├── user/
│
├── static/
├── templates/
├── docs/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## 💻 Development Environment

| Item | Version |
|------|----------|
| Python | 3.14 |
| Django | 5.x |
| Database | SQLite3 |
| IDE | Visual Studio Code |
| Version Control | Git |
| Repository | GitHub |

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/shingyu0205/JBOD-Validation_v.1.0.git
```

### Enter Project

```bash
cd JBOD-Validation_v.1.0
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Server

```bash
python manage.py runserver
```

Open Browser

```
http://127.0.0.1:8000/
```

---

## 📂 Main Applications

| App | Description |
|------|-------------|
| dashboard | Dashboard Homepage |
| models_app | JBOD Model Management |
| firmware | Firmware Management |
| testcase | Test Case Management |
| executor | Validation Execution |
| report | Report Management |
| validation | Validation Control |
| user | User Management |

---

## 🎯 Future Plans

- User Authentication
- Permission Management
- Report Export (PDF/Excel)
- Email Notification
- Dark Mode
- REST API
- Real-time Dashboard
- Test Automation Integration
- Jenkins CI/CD
- Docker Deployment

---

## 📸 Screenshots

Coming Soon...

---

## 📝 Version

Current Version

```
v1.0.0
```

---

## 👨‍💻 Author

**Shing-Yu Chou**

GitHub

https://github.com/shingyu0205

---

## 📄 License

This project is licensed under the MIT License.