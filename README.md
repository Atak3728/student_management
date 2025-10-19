# Student Management API

A simple backend API built with Django and Django REST Framework to manage students, courses, and attendance.

This project is part of the BE Capstone. It runs locally and demonstrates CRUD operations, Django ORM usage, filtering, and admin data management.

---

## Features

- Manage Students, Courses, and Attendance records  
- Create, Read, Update, Delete (CRUD) for all models  
- Filter Attendance by Course title or Date  
- Admin panel for manual management  
- SQLite local database  
- Clean RESTful API structure

---

## API Endpoints

| Function | Endpoint | Method |
|-----------|-----------|--------|
| List or Create Students | `/api/students/` | GET, POST |
| Single Student | `/api/students/{id}/` | GET, PUT, PATCH, DELETE |
| List or Create Courses | `/api/courses/` | GET, POST |
| Single Course | `/api/courses/{id}/` | GET, PUT, PATCH, DELETE |
| List or Create Attendance | `/api/attendance/` | GET, POST |
| Single Attendance | `/api/attendance/{id}/` | GET, PUT, PATCH, DELETE |

---

## Filtering Examples

Filter attendance by course title:
http://127.0.0.1:8000/api/attendance/?search=Python
Filter attendance by date:
http://127.0.0.1:8000/api/attendance/?search=2025-10-06
Order by date:
http://127.0.0.1:8000/api/attendance/?ordering=date
---

## Admin Panel

Access the admin panel to manage data manually:
http://127.0.0.1:8000/admin/

---

## Setup Instructions

1. **Clone the repository**
   ``` 
   git clone https://github.com/atak2891/student_management.git
   cd student_management
   ```
   
2. **Create and activate a virtual environment**
	``` 
	python -m venv venv
	venv\Scripts\activate    
	```

3. **Install dependencies**
	``` 
	pip install django djangorestframework
	```	
	
4. **Run migrations**
	```
	python manage.py migrate
	```

6. **Start the server**
	```
	python manage.py runserver
	```

8. **Open your browser and visit:**
	```
	http://127.0.0.1:8000/api/
	```	


## Tech Stack

- **Python 3**
- **Django**
- **Django REST Framework**
- **SQLite** (local database)


## Author

Ataklti Abraham
ALX Backend Engineering Project
