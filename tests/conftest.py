"""Test configuration and fixtures."""
import pytest
from example_project.app.core.database import get_session
from example_project.app.main import app
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine


@pytest.fixture(name="session")
def session_fixture():
    """Create an in-memory SQLite database for testing."""
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    """Create a TestClient with the in-memory database."""
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


@pytest.fixture(name="test_user")
def test_user_fixture(client: TestClient):
    """Create a test user."""
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "password": "testpass123",
        },
    )
    return response.json()


@pytest.fixture(name="test_user_token")
def test_user_token_fixture(test_user: dict) -> str:
    """Extract access token from test user."""
    return test_user["access_token"]
