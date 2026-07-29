# JBOD Validation Platform

Enterprise Validation Management System based on Django.

## Features

- Dashboard
- Model Management
- Firmware Management
- Test Case Management
- Test Plan Management
- Validation Center
- Report Management
- Executor

---

## Environment

- Python 3.14
- Django 6
- SQLite

---

## Installation

```bash
git clone <repository>

cd JBOD-Validation

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

---

## Project Structure

```
dashboard/
firmware/
models_app/
testcase/
testplan/
validation/
executor/
report/
```