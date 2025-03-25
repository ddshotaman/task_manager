# 🚀 Task Manager API – Django + DRF + SQLite3

A **Task Management API** built using **Django Rest Framework (DRF)** and **SQLite3**, deployed on **Render** for backend and **Netlify** for frontend.

---

## 📌 Features
✅ Create a Task  
✅ Assign Tasks to Multiple Users  
✅ Fetch Tasks Assigned to a User  
✅ Uses Django Admin for Management  
✅ Deployed on Render (Backend) & Netlify (Frontend)  

---

## 📌 Setup & Installation Instructions

### 1️⃣ Clone the Repository
git clone https://github.com/yourusername/task-manager-api.git
cd task-manager-api

###2️⃣ Create a Virtual Environment & Activate It
python -m venv venv
# Activate virtual env
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ create database 
python manage.py migrate

3️⃣ create superuser
python manage.py createsuperuser
python manage.py runserver

📌 API Endpoints & Testing
Method	Endpoint	Description
POST	/api/tasks/create/	Create a new task
POST	/api/tasks/assign/<task_id>/	Assign task to users
GET	/api/tasks/user/<user_id>/	Get tasks for a specific user

