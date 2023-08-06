import pytest


def test_user_registration(client):
    response = client.post(
        "/api/users",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123",
        },
    )
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "User registration successful"
    assert "data" in data


def test_user_login(client, user):
    response = client.post(
        "/api/login", json={"email": "test@example.com", "password": "password123"}
    )
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "User login successful"
    assert "token" in data


def test_user_logout(client, user):
    response = client.post(
        "/api/logout", headers={"Authorization": f"Bearer {user.generate_auth_token()}"}
    )
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "Successfully logged out"


def test_get_user_details(client, user):
    response = client.get(
        "/api/users", headers={"Authorization": f"Bearer {user.generate_auth_token()}"}
    )
    data = response.get_json()
    assert response.status_code == 200
    assert "data" in data
    assert data["data"]["username"] == "testuser"
    assert data["data"]["email"] == "test@example.com"
