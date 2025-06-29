from fastapi.testclient import TestClient
from create_api.sales_api import app

client = TestClient(app)

# Test เพิ่มข้อมูล (POST /sales)
def test_add_sale():
    response = client.post("/sales",json={
        "product_id":1,
        "product_name":"Shirt",
        "quantity":2,
        "price":299.0
    })
    assert response.status_code == 200
    assert response.json() == {"message":"Sale data added successfully"}

# Test ดูข้อมูลทั้งหมด (GET /sales)
def test_get_all_sales():
    response = client.get("/sales")
    assert response.status_code == 200
    assert isinstance(response.json(),list)

# Test ดูข้อมูลตาม ID (GET /sales/{product_id})
def test_get_sale_by_id():
    response = client.get("/sales/1")
    assert response.status_code == 200
    assert response.json()["product_name"] == "Shirt"

# Test แก้ไขข้อมูล (PUT /sales/{product_id})
def test_update_sale():
    response = client.put("/sales/1", json={
        "product_id": 1,
        "product_name": "Updated Shirt",
        "quantity": 5,
        "price": 399.0
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Sale data updated successfully"

# Test ลบข้อมูล (DELETE /sales/{product_id})
def test_delete_sale():
    response = client.delete("/sales/1")
    assert response.status_code == 200
    assert "deleted" in response.json()["message"]