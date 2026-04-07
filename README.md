# Finance Backend System

## Overview

This project is a backend system for managing financial records with role-based access control.

It allows users to:

* Manage financial transactions (income & expenses)
* View dashboard analytics
* Access data based on user roles

---

##  Features

### User Management

* Create users with roles:

  * Viewer
  * Analyst
  * Admin

### Financial Records

* Create, view records
* Filter by:

  * Type (income/expense)
  * Category
* Pagination support

### Dashboard Analytics

* Total Income
* Total Expenses
* Net Balance
* Category-wise summary

### Role-Based Access Control

* Viewer → read-only
* Analyst → read + analytics
* Admin → full access

---

## Tech Stack

* Python
* Flask
* SQLite (easily switchable to MySQL)
* REST APIs

---

## Setup Instructions

### 1. Clone repo

```bash
git clone <your-repo-link>
cd finance-backend
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup database

```bash
python setup_db.py
```

### 4. Run server

```bash
python app.py
```

---

## API Endpoints

### Users

* POST /users → Create user

### Records

* POST /records → Create record (Admin)
* GET /records → Get records (All roles)

### Dashboard

* GET /dashboard → Summary (Admin, Analyst)
* GET /dashboard/categories → Category totals

---

## Authentication (Simplified)

Role is passed via headers:

Example:

```
role: admin
```

---

## Design Decisions

* Used SQLite for simplicity and fast setup
* Modular structure (routes, utils, config)
* Decorator-based access control
* Clean separation of logic

---

## Future Improvements

* JWT Authentication
* User login system
* Soft delete
* Advanced analytics
* Frontend integration

---

## Author

Komal
