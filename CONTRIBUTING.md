# Contributing to FastAPI Scaffold with Auth

Thank you for your interest in contributing! We welcome PRs, bug reports, and feature suggestions.

## Development Setup

1. **Fork & Clone**
   ```bash
   git clone https://github.com/yourusername/fastapi-scaffold-with-auth.git
   cd fastapi-scaffold-with-auth
   ```

2. **Create Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dev Dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Run Tests Locally**
   ```bash
   pytest
   black . && ruff check . --fix
   mypy example_project
   ```

## Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `test:` Add/improve tests
- `refactor:` Code refactoring without behavior change
- `perf:` Performance improvement
- `chore:` Build, dependencies, etc.

Example:
```bash
git commit -m "feat: add refresh token endpoint"
git commit -m "fix: handle expired tokens gracefully"
```

## PR Guidelines

1. **Branch naming**: `feature/description` or `fix/description`
2. **Small, focused PRs** - easier to review and merge
3. **Write tests** for new features
4. **Update docs** if behavior changes
5. **Check CI passes** - all tests, linting, type checking

## Code Style

- **Python**: Black (line length 100)
- **Linting**: Ruff
- **Type hints**: MyPy strict mode
- **Testing**: pytest with >80% coverage

## Questions?

- Open an issue for discussion
- Check existing issues/discussions first
- Be respectful and constructive

---

Happy coding! 🚀
