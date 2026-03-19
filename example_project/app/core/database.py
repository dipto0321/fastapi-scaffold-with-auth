from typing import Generator

from app.core.config import settings
from sqlmodel import Session, SQLModel, create_engine

# Create engine with appropriate parameters for different databases
engine = create_engine(
    settings.database_url,
    connect_args=(
        {"check_same_thread": False}
        if settings.database_url.startswith("sqlite")
        else {}
    ),
    echo=settings.debug,
    pool_pre_ping=not settings.database_url.startswith("sqlite"),  # For network DBs
)


def get_session() -> Generator[Session, None, None]:
    """Dependency to get database session."""
    with Session(engine) as session:
        yield session


def create_db_tables() -> None:
    """Create all database tables from models."""
    SQLModel.metadata.create_all(engine)
