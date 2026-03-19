# Documentation

## Quick Links

- [README](../README.md) - Quick start and features
- [CONTRIBUTING](../CONTRIBUTING.md) - Development guide
- [Architecture](./architecture.md) - Project structure explanation
- [API Guide](./api-guide.md) - API endpoints and authentication

## Quick Start

### Installation

```bash
# From GitHub Template
git clone https://github.com/yourusername/fastapi-scaffold-with-auth
cd fastapi-scaffold-with-auth
pip install -e ".[postgres]"

# Or from PyPI
pip install fastapi-scaffold-with-auth
```

### Configuration

Create `.env` from `.env.example`:

```bash
cp .env.example .env
# Edit .env with your settings
```

### Running the Application

```bash
# Apply migrations
alembic upgrade head

# Start dev server
fastapi dev example_project/app/main.py

# Visit http://localhost:8000/docs for API documentation
```

## Directory Structure

```
fastapi-scaffold-with-auth/
├── fastapi_scaffold_with_auth/   # Core reusable package
├── example_project/               # Full working example
│   ├── app/                      # FastAPI application
│   ├── modules/                  # Business logic modules
│   ├── alembic/                  # Database migrations
│   └── pyproject.toml
├── docs/                         # Documentation
├── tests/                        # Test suite
├── .github/workflows/            # CI/CD pipelines
└── README.md
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `SECRET_KEY` | (required) | JWT signing secret (min 32 chars) |
| `ALGORITHM` | HS256 | JWT algorithm |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | 30 | Access token lifetime |
| `REFRESH_TOKEN_EXPIRE_DAYS` | 7 | Refresh token lifetime |
| `DATABASE_URL` | sqlite:///./app.db | Database connection string |
| `API_V1_STR` | /api/v1 | API base path |
| `DEBUG` | False | Enable debug mode |
| `LOG_LEVEL` | INFO | Logging level |
| `LOG_FORMAT` | json | Log format (json or text) |

## Database Support

### SQLite (Development)
```
DATABASE_URL=sqlite:///./app.db
```

### PostgreSQL
```
pip install "fastapi-scaffold-with-auth[postgres]"
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

### MySQL
```
pip install "fastapi-scaffold-with-auth[mysql]"
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/dbname
```

## Testing

```bash
# Run all tests
pytest

# With coverage
pytest --cov=example_project

# Watch mode
pytest-watch -- --tb=short
```

## Deployment

See [DEPLOYMENT](./deployment.md) for guides on:
- Docker containerization
- Azure deployment
- Heroku deployment
- GitHub Pages
