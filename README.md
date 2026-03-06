# FastAPI + Neon PostgreSQL Patient Management API

A RESTful API built with **FastAPI** and **PostgreSQL (Neon)** for managing patient records.
This project demonstrates modern backend development practices including **async database operations, SQLAlchemy ORM, Pydantic validation, and REST API design**.

---

## 🚀 Features

* FastAPI-based REST API
* Async database operations using **SQLAlchemy + AsyncPG**
* Cloud PostgreSQL database using **Neon**
* Pydantic models for request/response validation
* CRUD operations for patient management
* Dynamic sorting of patient records
* Automatic BMI calculation
* Clean project structure

---

## 🛠 Tech Stack

* **FastAPI**
* **Python**
* **SQLAlchemy (Async ORM)**
* **PostgreSQL (Neon Cloud Database)**
* **AsyncPG**
* **Pydantic**
* **Uvicorn**

---

## 📂 Project Structure

```
FASTAPINEON
│
├── database.py        # Database connection and session management
├── main.py            # FastAPI application and API routes
├── models.py          # SQLAlchemy database models
├── schemas.py         # Pydantic request/response schemas
├── requirements.txt   # Project dependencies
├── README.md
└── .env               # Environment variables (not committed)
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/fastapi-neon.git
cd fastapi-neon
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv .venv
```

Activate the environment:

**Windows**

```
.venv\Scripts\activate
```

**Linux / Mac**

```
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
DATABASE_URL=postgresql+asyncpg://username:password@host/database
```

Example for **Neon PostgreSQL**:

```
DATABASE_URL=postgresql+asyncpg://user:password@ep-xxx.region.aws.neon.tech/dbname?sslmode=require
```

---

## ▶️ Run the Server

Start the FastAPI development server:

```
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically generates API docs.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## 📌 API Endpoints

### Create Patient

```
POST /create
```

Request Body:

```json
{
  "name": "John",
  "city": "Hyderabad",
  "age": 30,
  "gender": "male",
  "height": 1.75,
  "weight": 70
}
```

---

### View All Patients

```
GET /view
```

Returns a list of all patients.

---

### View Patient by ID

```
GET /patient/{patient_id}
```

---

### Sort Patients

```
GET /sort?sort_by=height&order=asc
```

Supported fields:

* height
* weight
* bmi

---

### Update Patient

```
PATCH /edit/{patient_id}
```

Allows partial updates of patient data.

---

### Delete Patient

```
DELETE /delete/{patient_id}
```

---

## 📊 Example Response

```json
{
  "patients": [
    {
      "id": 1,
      "name": "John",
      "city": "Hyderabad",
      "age": 30,
      "gender": "male",
      "height": 1.75,
      "weight": 70,
      "bmi": 22.86,
      "verdict": "normal"
    }
  ]
}
```

---

## 🧠 Concepts Demonstrated

* Async database connections
* SQLAlchemy ORM models
* Pydantic schema validation
* Dependency injection with FastAPI
* RESTful API design
* Dynamic query building
* Secure environment configuration

---

## 📌 Future Improvements

* Add authentication (JWT)
* Add pagination
* Add API rate limiting
* Add Docker support
* Implement database migrations using Alembic

---

## 👨‍💻 Author

**Harsha Kalluri**

* GitHub: https://github.com/harsha3733
---

## 📜 License

This project is open source 
