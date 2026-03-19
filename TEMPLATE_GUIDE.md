# FastAPI Scaffold with Auth - Comprehensive Guide

A production-ready FastAPI template featuring:

- ✅ JWT authentication with refresh tokens
- ✅ User management module
- ✅ Alembic database migrations
- ✅ Rate limiting middleware
- ✅ Structured logging (JSON format)
- ✅ Health check endpoints
- ✅ Multi-database support (SQLite, PostgreSQL, MySQL)
- ✅ Complete test suite
- ✅ Docker & Docker Compose ready
- ✅ CI/CD workflows (GitHub Actions)
- ✅ PyPI package ready

## 📁 Project Structure

```
fastapi-scaffold-with-auth/
├── fastapi_scaffold_with_auth/    # Core package (for pip)
├── example_project/                # Full working example
│   ├── app/
│   │   ├── main.py
│   │   ├── api/v1/
│   │   ├── core/
│   │   └── middleware/
│   ├── modules/
│   │   ├── auth/
│   │   └── users/
│   └── alembic/
├── .github/workflows/              # CI/CD pipelines
├── docs/                          # Documentation
├── tests/                         # Test suite
├── pyproject.toml
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

## 🚀 Quick Start

### Via GitHub Template

1. Click **"Use this template"** on GitHub
2. Clone your new repo
3. Update author info in `fastapi_scaffold_with_auth/__init__.py`
4. Update URLs in `pyproject.toml`

### Via pip

```bash
pip install fastapi-scaffold-with-auth
```

## 📚 Documentation

- [Getting Started](docs/getting-started.md) - Installation and setup
- [API Guide](docs/api-guide.md) - Endpoint documentation
- [Architecture](docs/architecture.md) - Technical design
- [Contributing](CONTRIBUTING.md) - Development guide

## 🛠️ Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest --cov

# Format code
make format

# Run the app
fastapi dev example_project/app/main.py
```

## 🐳 Docker

```bash
cd example_project
docker-compose up
```

Visit `http://localhost:8000/docs`

## 🔑 Features Breakdown

### 1. Authentication (JWT)

- User registration with email validation
- Secure password hashing (Argon2)
- Access & refresh token generation
- Token validation middleware

### 2. User Management

- User model with email uniqueness
- User repository for data access
- Protected endpoints require valid tokens
- Get current user endpoint

### 3. Database Migrations

- Alembic for schema versioning
- Automatic model-based migrations
- Support for SQLite, PostgreSQL, MySQL

### 4. Rate Limiting

- Per-IP request rate limits
- Configurable limits per endpoint
- 429 responses for exceeded limits

### 5. Logging

- JSON structured logging
- Multiple log levels
- Request tracking

### 6. Health Checks

- `/health` - Liveness probe
- `/ready` - Readiness probe

## 📦 Publishing to PyPI

### Prerequisites

- GitHub account with this repo
- PyPI account

### Steps

1. **Update package version** in `pyproject.toml`

2. **Create GitHub release**
   - Tag: `v0.1.0`
   - Release name: `v0.1.0`

3. **GitHub Actions will automatically publish to PyPI**

   The `.github/workflows/publish.yml` workflow:
   - Triggers on GitHub releases
   - Builds the package
   - Publishes to PyPI using trusted publishers

Users can then install:

```bash
pip install fastapi-scaffold-with-auth
```

## 🔄 GitHub Template Usage

Users cloning via "Use this template":

1. Repository is created with your files
2. Git history is reset (clean start)
3. They can customize:
   - Author info
   - Package metadata
   - Remove/modify example project
   - Add their own modules

## 📝 License

MIT License - See [LICENSE](LICENSE) file

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for:

- Development setup
- Code standards
- PR guidelines
- Issue templates

## ⭐ Support

- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions
- **Docs**: See `/docs` folder

---

**Made with ❤️ for the FastAPI community**
