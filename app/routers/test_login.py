import pytest
from fastapi.testclient import TestClient
from app.routers.login import router

client = TestClient(router)

def test_login_user_not_found():
    response = client.post("/login/", json={"username": "nonexistent_user", "password": "password123"})
    assert response.status_code == 200
    assert response.json() == {"message": "User not found"}

def test_login_incorrect_password():
    response = client.post("/login/", json={"username": "existing_user", "password": "wrong_password"})
    assert response.status_code == 200
    assert response.json() == {"message": "Incorrect password"}

def test_login_successful():
    response = client.post("/login/", json={"username": "existing_user", "password": "correct_password"})
    assert response.status_code == 200
    assert response.json() == {"message": "Login successful"}