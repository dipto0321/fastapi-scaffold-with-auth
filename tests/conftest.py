"""Test configuration and fixtures."""


import pytest
from app.core.database import get_session
from app.main import app
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine


@pytest.fixture(name="db_engine")
def db_engine_fixture():
    engine = create_engine(
        "sqlite:///file::memory:?cache=shared",
        connect_args={"check_same_thread": False},
    )
    yield engine


@pytest.fixture(scope="function", autouse=True)
def reset_db(db_engine):
    SQLModel.metadata.drop_all(db_engine)
    SQLModel.metadata.create_all(db_engine)
    yield


@pytest.fixture(name="session")
def session_fixture(db_engine):
    """Create a session with the in-memory database."""
    with Session(db_engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(db_engine):
    SQLModel.metadata.create_all(db_engine)

    def get_session_override():
        with Session(db_engine) as session:
            yield session

    # IMPORTANT: override the correct dependency
    app.dependency_overrides[get_session] = get_session_override

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()



@pytest.fixture(name="test_user")
def test_user_fixture(client: TestClient):
    email = "test@example.com"
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": email,
            "password": "testpass123",
        },
    )

    return {
        "email": email,
        "password": "testpass123",
    }


@pytest.fixture(name="test_user_token")
def test_user_token_fixture(client: TestClient, test_user: dict) -> str:
    response = client.post(
        "/api/v1/auth/login",
        json=test_user,
    )
    return response.json()["access_token"]














