import json
import os
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Sales API",
    description="A simple API for managing sales data",
    version="1.0.0"
)

DATA_FILE = "sales_data.json"

# Model ของข้อมูลที่จะส่งเข้ามา
class Sale(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    price: float

# ฟังก์ชันช่วย: โหลดและบันทึกไฟล์ JSON
def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)  # ถ้าไม่มีไฟล์ จะสร้างไฟล์ว่าง
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# Route: เพิ่มข้อมูลการขาย (หลายชุด)
@app.post("/sales/bulk")
def add_sales_bulk(sales: List[Sale]):
    data = load_data()
    for sale in sales:
        data.append(sale.dict())
    save_data(data)
    return {"message": f"Added {len(sales)} sales records successfully"}

# Route: เพิ่มข้อมูลการขาย (ทีละชุด)
@app.post("/sales")
def add_sale(sale: Sale):
    data = load_data()
    data.append(sale.dict())
    save_data(data)
    return {"message": "Sale data added successfully"}

# Route: ดูข้อมูลทั้งหมด
@app.get("/sales", response_model=List[Sale])
def get_all_sales():
    return load_data()

# Route: ดูข้อมูลตาม product_id
@app.get("/sales/{product_id}")
def get_sale_by_id(product_id: int):
    data = load_data()
    for item in data:
        if item["product_id"] == product_id:
            return item
    raise HTTPException(status_code=404, detail="Product not found")

# Route: แก้ไขข้อมูลตาม product_id
@app.put("/sales/{product_id}")
def update_sale(product_id: int, sale: Sale):
    data = load_data()
    for index, item in enumerate(data):
        if item["product_id"] == product_id:
            data[index] = sale.dict()
            save_data(data)
            return {"message": "Sale data updated successfully"}
    raise HTTPException(status_code=404, detail="Product not found")

# Route: ลบข้อมูลตาม product_id
@app.delete("/sales/{product_id}")
def delete_sale(product_id: int):
    data = load_data()
    for index, item in enumerate(data):
        if item["product_id"] == product_id:
            deleted_item = data.pop(index)
            save_data(data)
            return {"message": f"Product {product_id} deleted", "data": deleted_item}
    raise HTTPException(status_code=404, detail="Product not found")
