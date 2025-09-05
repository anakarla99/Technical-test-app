def test_create_task(client):
    # Registro y login
    client.post("/auth/register", json={"email": "test@example.com", "password": "testpass"})
    token_response = client.post("/auth/token", data={"username": "test@example.com", "password": "testpass"})
    token = token_response.json()["access_token"]

    # Crear tarea
    response = client.post(
        "/tasks",
        json={"title": "Test Task", "description": "Test Description"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"
    assert data["status"] == "pendiente"