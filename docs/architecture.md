# Project Architecture

## High-Level Overview

```
FastAPI App
├── API Routers (v1)
│   ├── Auth (register, login)
│   └── Users (me, profile)
├── Core (Security, Database, Config)
├── Middleware (Rate limiting)
└── Modules (Business logic)
    ├── Auth (services, schemas)
    └── Users (model, repository)
```

## Directory Structure

### `/app/`

FastAPI application core:

- **main.py** - FastAPI instance and startup events
- **core/** - Configuration, database, security, logging
- **api/** - Route definitions
- **middleware/** - Custom middleware (rate limiting)

### `/modules/`

Domain-driven modules with business logic:

- **auth/** - Authentication logic
  - router.py - Endpoints
  - service.py - Business logic
  - schema.py - Request/response models
- **users/** - User management
  - model.py - Database model
  - repo.py - Data access layer
  - router.py - Endpoints
  - schema.py - Schemas

### `/alembic/`

Database migration scripts:

- **env.py** - Migration environment configuration
- **versions/** - Migration scripts
- **script.py.mako** - Migration template

### `/example_project/`

Complete working example that can be forked or copied.

## Architecture Patterns

### Clean Architecture

```
Routes (API Contracts)
    ↓
Schemas (Data Validation)
    ↓
Services (Business Logic)
    ↓
Repository (Data Access)
    ↓
Models (Database Layer)
```

### Dependency Injection

```python
@app.get("/endpoint")
async def my_endpoint(session: Session = Depends(get_session)):
    # Session automatically injected
    return service.do_something(session)
```

### Configuration Management

```python
# Settings loaded from environment variables
from app.core.config import settings

SECRET_KEY = settings.secret_key  # From .env
DATABASE_URL = settings.database_url
```

### Database Sessions

```python
# FastAPI automatically manages session lifecycle
def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session  # Request gets session
        # Cleanup happens automatically
```

## Data Flow

### Authentication Flow

```
1. User -> POST /auth/register
2. Router -> Service.register_user()
3. Service -> Repo.create_user()
4. Repo -> Model.User (DB insert)
5. Service -> Security.create_tokens()
6. Router -> Response {access_token, refresh_token}
```

### Protected Request Flow

```
1. Client -> GET /users/me + Authorization header
2. Middleware -> Rate limiter checks IP
3. Router -> Get current user dependency
4. Dependency -> Security.decode_token()
5. Dependency -> Repo.get_user_by_email()
6. Dependency returns User object
7. Router -> Response {id, email, is_active}
```

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Web Framework | FastAPI | HTTP APIs |
| ORM | SQLModel | Database abstraction |
| Async | Uvicorn | ASGI server |
| Auth | PyJWT | Token generation |
| Password Hashing | Argon2 | Secure hashing |
| Migrations | Alembic | Version control for DB schema |
| Rate Limiting | SlowAPI | API protection |
| Logging | Python logging | Structured logging |
