from app.auth import get_password_hash

def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "testpass"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_login_user(client):
    # Primero registramos un usuario
    client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "testpass"}
    )
    # Luego intentamos login
    response = client.post(
        "/auth/token",
        data={"username": "test@example.com", "password": "testpass"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"