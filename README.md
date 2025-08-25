# 🧑‍💼 Employee Management API with FastAPI + JWT Authentication

This project is a **FastAPI-based Employee Management System** with secure JWT authentication and full CRUD functionality for employee data.

---

## 🚀 Features

- Create new employee records (passwords securely hashed with bcrypt)
- Retrieve single or multiple employees
- Update employee information
- Delete employee entries
- JWT-based Authentication:
  - Login with email + password to obtain a JWT access token
  - Access protected routes using `Authorization: Bearer <token>`
- Auto-generated interactive API docs with **Swagger UI** and **ReDoc**
- Swagger UI integrates authentication via the **Authorize** button

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

| Method | Endpoint     | Description                 | Auth Required |
| ------ | ------------ | --------------------------- | ------------- |
| POST   | `/emp`       | Create a new employee       | ❌            |
| GET    | `/emp`       | Retrieve all employees      | ✅            |
| GET    | `/emp/{id}`  | Retrieve employee by ID     | ✅            |
| PUT    | `/emp/{id}`  | Update an existing employee | ✅            |
| DELETE | `/emp/{id}`  | Delete an employee by ID    | ✅            |

---

## 🧠 Password Handling

- Passwords are hashed using bcrypt via passlib.

- No plaintext passwords are stored.

- The hashed password is verified using verify_password().

---

## 🔐 Authentication Flow

1. **Register User (Sign Up)**  
   `POST /emp` — create a new employee with hashed password.

2. **Authorize via Swagger UI**  
   Click **Authorize**, enter email + password.  
   Swagger automatically calls `/token` to get a JWT and stores it.  
   Subsequent requests include `Authorization: Bearer <token>`.

3. **Access Protected Routes**  
   Use Swagger or any HTTP client with the token to call:
   - `GET /emp`
   - `GET /emp/{id}`
   - `PUT /emp/{id}`
   - `DELETE /emp/{id}`
  
---

## 🧠 Security Highlights

- Passwords hashed using **bcrypt** (`passlib`)
- JWT tokens signed with **HS256** and include **expiry (`exp`)**
- Expired or invalid tokens are rejected with `401 Unauthorized`
- Swagger UI login flow integrated via **OAuth2 Password Flow**

---

## 🧪 Testing the API

You can use tools like:

- 🔧 Postman
- 🧪 curl
- 🧰 Swagger UI: http://127.0.0.1:8000/docs

---

## ⚙️ Technology Stack

| Technology     | Purpose                         |
| -------------- | ------------------------------- |
| FastAPI        | Web framework                   |
| SQLAlchemy ORM | Database ORM                    |
| SQLite         | Lightweight database            |
| Pydantic       | Data validation & serialization |
| Passlib        | Secure password hashing         |
| Python-JOSE    | JWT signing & verification      |
| Uvicorn        | ASGI server                     |

---

## 🙋‍♂️ Author

Developed by Hemanth M G

- 📧 Email: hmnthmg20@gmail.com

- 🌐 GitHub: https://github.com/hemanthmg20/


