from fastapi.testclient import TestClient
import logging

# Import our app from main.py.
from apitesting import app

# Instantiate the testing client with our app.
client = TestClient(app)

# Write tests using the same syntax as with the requests module.
def test_api_locally_get_root():
    r = client.get("/items/22")
    assert r.status_code == 200
    r = client.get("/items")
    assert r.status_code == 404
    r = client.get("/malformed")
    assert r.status_code == 404
    r = client.get("/items/22?count=2")
    assert r.status_code == 200
