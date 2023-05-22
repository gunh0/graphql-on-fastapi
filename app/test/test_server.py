import os
import pytest
import requests
import sys

root_path = os.path.join(os.path.dirname(__file__), "..")
print(root_path)
sys.path.append(root_path)

from main import app

BASE_URL = "http://localhost:8000"

@pytest.fixture
def client():
    yield requests.Session().request


def test_read_root(client):
    for _ in range(1000):
        print("Testing read_root...")
        response = client("GET", f"{BASE_URL}/")
        print("Response:", response.text)
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}


def test_read_item(client):
    for _ in range(1000):
        print("Testing read_item...")
        response = client("GET", f"{BASE_URL}/items/42", params={"q": "test"})
        print("Response:", response.text)
        assert response.status_code == 200
        assert response.json() == {"item_id": 42, "q": "test"}


def test_update_item(client):
    for _ in range(1000):
        print("Testing update_item...")
        item_data = {"name": "Test Item", "price": 9.99, "is_offer": True}
        response = client("PUT", f"{BASE_URL}/items/42", json=item_data)
        print("Response:", response.text)
        assert response.status_code == 200
        assert response.json() == {"item_name": "Test Item", "item_id": 42}
