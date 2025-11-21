FastAPI CRUD & Search Application

This project is a FastAPI-based web application demonstrating:

- Basic routing
- CRUD operations using Pydantic models
- Nested routing and dynamic URL parameters
- Search & filtering with query parameters
- Error handling using FastAPI's `HTTPException`

The project contains three modules:

1. `main.py` - Basic routes and nested route example  
2. `pmodel.py` - CRUD operations using Pydantic  
3. `search.py` - Product search with optional filters  

 How to Run the Project

1️⃣ Create a virtual environment (recommended)

python -m venv venv

- Windows:
venv\Scripts\activate

- Linux/macOS:
source venv/bin/activate

2️⃣ Install dependencies
pip install fastapi uvicorn pydantic

3️⃣ Run any module using Uvicorn

Run `main.py`:
uvicorn main:app --reload

Run `pmodel.py`:
uvicorn pmodel:app --reload

Run `search.py`:
uvicorn search:app --reload

## 🌐 API Endpoints

🔹 main.py
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/` | Welcome message |
| GET | `/sub` | Internal page |
| GET | `/user/{user_id}/order/{order_id}` | Fetch specific order of a user |

---

🔹 pmodel.py (CRUD using Pydantic)
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/create` | Create a new user |
| GET | `/users` | Get all users |
| GET | `/user/{user_id}` | Get a single user |
| PUT | `/user/{user_id}` | Update user |
| DELETE | `/user/{user_id}` | Delete user |

---

🔹 search.py (Search API)
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/products` | Search products by category and/or max price |

---

## 🧪 Example Requests

Create User (POST)
json
{
  "name": "swathi",
  "phone": 987654,
  "email": "swathi@example.com"
}

Search Products
/products?category=Stationery&max_price=40


Features Implemented

FastAPI routing
Pydantic model validation
Exception handling
Search with multiple optional filters
REST API best practices

