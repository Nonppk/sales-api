# Sales API Project

A clean and simple **FastAPI** project that provides a RESTful API for managing sales records.  

---

## Features

-FastAPI CRUD endpoints  
-JSON file-based persistence (`sales_data.json`)  
-Validation with Pydantic models  
-Complete test coverage using Pytest  
-Poetry for dependency management  
-Python 3.9+  

---

## Project Structure

├── src/
│ └── create_api/
│ ├── sales_api.py
│ └── sales_data.json
├── tests/
│ └── test_sales_api.py
├── pyproject.toml
├── poetry.lock
├── pytest.ini
└── README.md


---

## Requirements

- Python >= 3.9
- Poetry

---

## Installation

Clone this repository:

```bash
git clone https://github.com/Nonppk/sales-api.git
cd sales-api

Install dependencies:

poetry install

# Running the API
Start the FastAPI server:

poetry run uvicorn src.create_api.sales_api:app --reload

API will be available at:

http://127.0.0.1:8000

# Running Tests
Execute all test cases:

poetry run pytest

# API Endpoints

# Add a sale
POST /sales

Request body:

{
  "product_id": 1,
  "product_name": "Shirt",
  "quantity": 2,
  "price": 299.0
}

    Response:

    {
    "message": "Sale data added successfully"
    }

➕ Add multiple sales
POST /sales/bulk

Request body (array):

[
  {
    "product_id": 2,
    "product_name": "Pants",
    "quantity": 3,
    "price": 499.0
  },
  {
    "product_id": 3,
    "product_name": "Hat",
    "quantity": 1,
    "price": 199.0
  }
]

# Get all sales
GET /sales

# Get sale by ID
GET /sales/{product_id}

# Update sale
PUT /sales/{product_id}

Request body:

{
  "product_id": 1,
  "product_name": "Updated Shirt",
  "quantity": 5,
  "price": 399.0
}

# Delete sale
DELETE /sales/{product_id}

# Development Notes
The project uses Poetry for dependency management.

Tests cover all endpoints.

Sales data persists to sales_data.json in the same directory.

For production deployment, consider replacing JSON storage with a database (PostgreSQL, MongoDB, etc.).

# Author
Nonppk
ratchanonppk@gmail.com
LinkedIn https://www.linkedin.com/in/ratchanonppk/
GitHub https://github.com/Nonppk/sales-api