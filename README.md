# 🧑‍💼 Employee Management API with FastAPI + JWT Authentication

This project is a **FastAPI-based Employee Management System**.  
It supports **secure JWT authentication** and full **CRUD operations** on employee data.

Built with:
- ✅ FastAPI (web framework)
- ✅ SQLAlchemy ORM
- ✅ SQLite (default DB)
- ✅ Pydantic (data validation)
- ✅ Passlib (bcrypt password hashing)
- ✅ Python-JOSE (JWT signing & verification)
- ✅ Uvicorn (ASGI server)

---

## 📌 Features

- 🚀 Create new employee records (passwords securely hashed with bcrypt)
- 🔍 Retrieve single or multiple employee records
- ✏️ Update employee information
- ❌ Delete employee entries
- 🔐 JWT-based Authentication:
  - Login with email + password to get a JWT
  - Access protected routes using `Authorization: Bearer <token>`
- 📄 Auto-generated API docs with **Swagger UI** and **ReDoc**

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

- pip install fastapi uvicorn sqlalchemy passlib[bcrypt] "python-jose[cryptography]" python-multipart

---

## 🚀 Running the Application

uvicorn main:app --reload

After starting, navigate to:

- 🔍 Swagger UI: http://127.0.0.1:8000/docs

- 📘 ReDoc: http://127.0.0.1:8000/redoc

---

## 🔗 API Endpoints

| Method | Endpoint    | Description                      | Auth Required |
| ------ | ----------- | -------------------------------- | ------------- |
| POST   | `/emp`      | Create new employee              | ❌             |
| GET    | `/emp`      | Retrieve all employees           | ✅             |
| GET    | `/emp/{id}` | Retrieve employee by ID          | ✅             |
| PUT    | `/emp/{id}` | Update employee by ID            | ✅             |
| DELETE | `/emp/{id}` | Delete employee by ID            | ✅             |
| POST   | `/token`    | Login → returns JWT access token | ❌             |


---

## 🧠 Password Handling

- Passwords are hashed using bcrypt via passlib.

- No plaintext passwords are stored.

- The hashed password is verified using verify_password().

---

## 🔐 Authentication Flow

### Register Employee
Use /emp to create an employee (password is hashed).

### Login & Get Token
Call /token with form data

### Access Protected Routes

---

## 🧠 Security Highlights

- Passwords stored only in hashed form (bcrypt).

- JWT tokens include expiry claim (exp).

- Tokens signed with HS256 using a secret key.

- Unauthorized users cannot access protected endpoints.

---

## 🧪 Testing the API

You can use tools like:

- 🔧 Postman

- 🧪 curl

- 🧰 Swagger UI: http://127.0.0.1:8000/docs

---

## ⚙️ Technology Stack

| Technology     | Purpose                    |
| -------------- | -------------------------- |
| FastAPI        | Web framework              |
| SQLAlchemy ORM | Database ORM               |
| SQLite         | Lightweight DB             |
| Pydantic       | Data validation            |
| Passlib        | Secure password hashing    |
| Python-JOSE    | JWT handling (sign/verify) |
| Uvicorn        | ASGI server                |


---

## 🙋‍♂️ Author

Developed by Hemanth M G

- 📧 Email: hmnthmg20@gmail.com

- 🌐 GitHub: https://github.com/hemanthmg20/


