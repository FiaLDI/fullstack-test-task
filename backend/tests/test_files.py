from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


async def test_create_file():
    response = client.post(
        "/files/",
        data={"title": "Test"},
        files={"file": ("test.txt", b"hello", "text/plain")},
    )

    assert response.status_code == 201, response.text

    data = response.json()
    assert data["title"] == "Test"
    assert data["original_name"] == "test.txt"


async def test_list_files():
    response = client.get("/files/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    