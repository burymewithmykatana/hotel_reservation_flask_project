# Smart Hotel Reservation API

Final Project — Flask + MongoDB + JWT Authentication

## Project Features

### Authentication & Roles

- JWT login system  
- Signup endpoint  
- Role-based access control (RBAC)  
- Three roles: manager, staff, guest  
- Automatic role population + default manager account

### User Management

- Manager-only access to user list  
- Pagination  
- WTForms validation  
- Secure endpoints protected by JWT

### Room Management

- CRUD operations  
- staff/manager permissions  
- Image upload capability  
- Pagination  

### Reservation Management

- Date validation  
- Auto price calculation  
- Role-based visibility  
- CRUD operations  

## Installation

### Clone Repository

```bash
git clone <repo-url>
cd <project-folder>
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start MongoDB

Ensure it's running at:

```code
mongodb://localhost:27017/
```

### Run Server

```bash
python hotel_api.py
```

API URL:

```code
http://127.0.0.1:5000
```

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /signup | Create new guest user |
| POST | /login | Login & get JWT token |

### Users (Manager Only)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /users | List users (paginated) |

### Rooms

| Method | Endpoint | Role | Description |
|--------|----------|-------|-------------|
| GET | /rooms | public | List rooms |
| POST | /rooms | staff/manager | Create room |
| PUT | /rooms/<id> | staff/manager | Update room |
| DELETE | /rooms/<id> | manager | Delete room |

### Reservations

| Method | Endpoint | Role | Description |
|--------|----------|-------|-------------|
| POST | /reservations | authenticated | Create reservation |
| GET | /reservations | guest/staff/manager | List reservations |
| PUT | /reservations/<id> | staff/manager | Update reservation |
| DELETE | /reservations/<id> | manager | Delete reservation |

## Business Logic Summary

### Reservation Calculation

```code
nights = end_date - start_date
total_price = nights × price_per_night
```

## Postman Testing Guide

### Signup

```code
POST /signup
```

### Login

```code
POST /login
```

Set:

```code
Authorization: Bearer <token>
```

## Project Structure

```code
project/
│── hotel_api.py
│── README.md
│── public/
│── venv/
└── requirements.txt
```

## Final Checklist

- Signup & Login  
- JWT included  
- Role-based access  
- User list + pagination  
- Room CRUD + file upload  
- Reservation system  
- Postman collection  
- Clean README  
