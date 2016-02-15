from flask import Flask
from app import app


def test_app_creation():
    assert isinstance(app, Flask) is True


def test_get_index():
    with app.test_client() as c:
        response = c.get("/")
        assert response.status_code == 200
