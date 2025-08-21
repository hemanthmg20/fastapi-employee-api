# 🧑‍💼 Employee Management API with FastAPI

This project is a **FastAPI-based Employee Management System**. It allows you to perform CRUD operations (Create, Read, Update, Delete) and **authenticate employees** securely with hashed passwords.

Built with:
- ✅ FastAPI
- ✅ SQLAlchemy ORM
- ✅ SQLite (default DB)
- ✅ Pydantic for data validation
- ✅ Passlib for secure password hashing

---

## 📌 Features

- 🚀 Create new employee records
- 🔍 Retrieve single or multiple employee records
- ✏️ Update employee information
- ❌ Delete employee entries
- 🔐 Authenticate employee using hashed password verification
- 📄 OpenAPI (Swagger) documentation auto-generated

---

## 📁 Project Structure

your-project-folder/

├── main.py # Main FastAPI application with route definitions    
├── models.py # SQLAlchemy model for Employee    
├── schemas.py # Pydantic schemas for request/response validation                                                                                                             
├── auth.py # Password hashing and verification functions                                                                                                                     
├── database.py # Database configuration and setup                                                                                                                            
├── db.db # SQLite database file (auto-created after first run)  
└── README.md # Project documentation (this file)                                                                                                                             

---

## 💻 Installation

### 1️⃣ Clone the Repository

- git clone https://github.com/hemanthmg20/fastapi-employee-api.git

### 2️⃣ Create a Virtual Environment

- python -m venv env

- On Mac: source env/bin/activate

- On Windows: env\Scripts\activate

### 3️⃣ Install Dependencies

- pip install fastapi uvicorn sqlalchemy passlib[bcrypt]

---

## 🚀 Running the Application

uvicorn main:app --reload

After starting, navigate to:

- 🔍 Swagger UI: http://127.0.0.1:8000/docs

- 📘 ReDoc: http://127.0.0.1:8000/redoc

---

## 🔗 API Endpoints

| Method | Endpoint      | Description                 | Request Body                                  |
| ------ | ------------- | --------------------------- | --------------------------------------------- |
| POST   | `/emp`        | Create a new employee       | `emp_id`, `name`, `dept`, `email`, `password` |
| GET    | `/emp`        | Retrieve all employees      | *None*                                        |
| GET    | `/emp/{id}`   | Retrieve employee by ID     | *None*                                        |
| PUT    | `/emp/{id}`   | Update an existing employee | `emp_id`, `name`, `dept`, `email`, `password` |
| DELETE | `/emp/{id}`   | Delete an employee by ID    | *None*                                        |
| POST   | `/emp/verify` | Verify employee credentials | `emp_id`, `name`, `dept`, `email`, `password` |

---

## 🧠 Password Handling

- Passwords are hashed using bcrypt via passlib.

- No plaintext passwords are stored.

- During login, the hashed password is verified using verify_password().

---

## 🧪 Testing the API

You can use tools like:

- 🔧 Postman

- 🧪 curl

- 🧰 Swagger UI: http://127.0.0.1:8000/docs

---

## ⚙️ Technology Stack

| Technology | Purpose                         |
| ---------- | ------------------------------- |
| FastAPI    | Web framework                   |
| SQLAlchemy | ORM (Object Relational Mapper)  |
| SQLite     | Lightweight DB (local)          |
| Pydantic   | Data validation & serialization |
| Passlib    | Password hashing                |
| Uvicorn    | ASGI server                     |

---

## 🙋‍♂️ Author

Developed by Hemanth M G

- 📧 Email: hmnthmg20@gmail.com

- 🌐 GitHub: https://github.com/hemanthmg20/


