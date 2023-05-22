import os
import pytest
import sys

from fastapi.testclient import TestClient

root_path = os.path.join(os.path.dirname(__file__), "..")
print(root_path)
sys.path.append(root_path)

from main import app


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_read_root(client):
    response = client.get("/")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_item(client):
    response = client.get("/items/42", params={"q": "test"})
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "test"}


def test_update_item(client):
    item_data = {"name": "Test Item", "price": 9.99, "is_offer": True}
    response = client.put("/items/42", json=item_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"item_name": "Test Item", "item_id": 42}
