# Publishing to GitHub & PyPI

## Step 1: Update Configuration Files

### 1.1 Update `pyproject.toml`

Replace all instances of `yourusername` with your actual GitHub username:

```bash
# Find and replace in pyproject.toml
sed -i 's/yourusername/dipto0321/g' pyproject.toml
```

Update the author information:

```toml
authors = [
    {name = "Dipto Karmakar", email = "diptokmk47@gmail.com"},
]
```

### 1.2 Update `fastapi_scaffold_with_auth/__init__.py`

```python
__author__ = "Dipto Karmakar"
__email__ = "diptokmk47@gmail.com"
```

## Step 2: Create GitHub Repository

1. Go to <https://github.com/new>
2. Create repository: `fastapi-scaffold-with-auth`
3. Initialize with README (uncheck - we already have one)

```bash
git init
git add .
git commit -m "Initial commit: FastAPI scaffold with auth"
git branch -M main
git remote add origin https://github.com/dipto0321/fastapi-scaffold-with-auth.git
git push -u origin main
```

## Step 3: Configure GitHub Settings

### 3.1 Enable Repository Features

1. Go to Settings → General
2. Enable "Discussions"
3. Enable "Sponsorships" (optional)

### 3.2 Configure Branch Protection (optional)

1. Settings → Branches
2. Add rule for `main` branch
3. Require PR reviews
4. Require status checks to pass

### 3.3 Configure GitHub Actions

1. Settings → Actions → General
2. Allow all actions
3. Workflows already in `.github/workflows/`

## Step 4: Setup PyPI Publishing with Trusted Publishers

### 4.1 Create PyPI Account

1. Go to <https://pypi.org/account/register/>
2. Create account
3. Enable 2FA (required for trusted publishers)

### 4.2 Add Trusted Publisher in PyPI

1. Go to <https://pypi.org/manage/account/publishing/>
2. Click "Add a new pending publisher"
3. Fill in:
   - PyPI Project Name: `fastapi-scaffold-with-auth`
   - Owner: `dipto0321`
   - Repository name: `fastapi-scaffold-with-auth`
   - Workflow name: `publish.yml`
   - Environment name: (leave blank)
4. Click "Add"

## Step 5: Create Initial Release

### 5.1 Tag Release

```bash
git tag -a v0.1.0 -m "Initial release: FastAPI scaffold with auth"
git push origin v0.1.0
```

### 5.2 Create GitHub Release

1. Go to <https://github.com/YOUR_USERNAME/fastapi-scaffold-with-auth/releases/new>
2. Release tag: `v0.1.0`
3. Release title: `v0.1.0 - Initial Release`
4. Description:

   ```
   Initial release of FastAPI Scaffold with Auth
   
   Features:
   - JWT authentication with refresh tokens
   - User management module
   - Alembic database migrations
   - Rate limiting
   - Structured logging
   - Multi-database support
   
   Ready for production use!
   ```

5. Click "Publish release"

GitHub Actions will automatically:

1. Build the package
2. Publish to PyPI
3. Create release artifacts

## Step 6: Verify Publication

### 6.1 Check PyPI

Visit: <https://pypi.org/project/fastapi-scaffold-with-auth/>

### 6.2 Install from PyPI

```bash
pip install fastapi-scaffold-with-auth
```

## Step 7: Make It a Template Repository (Optional)

If you want users to use "Use this template" button:

1. Settings → General
2. Check "Template repository"
3. Add repository description
4. Users can now click "Use this template"

## 🎉 You're Done

Your package is now:

- ✅ On GitHub
- ✅ On PyPI
- ✅ Available as a GitHub template
- ✅ Has CI/CD workflows running

## Future Releases

To publish future versions:

1. Update version in `pyproject.toml`
2. Commit changes
3. Create new tag: `git tag -a v0.2.0 -m "Release message"`
4. Push tag: `git push origin v0.2.0`
5. Create GitHub release with same tag
6. PyPI auto-publishes!

## Troubleshooting

### CI/CD Fails

- Check `.github/workflows/publish.yml`
- Verify PyPI trusted publisher is configured correctly
- View logs in GitHub Actions

### Package Not Found on PyPI

- Give PyPI 5-10 minutes to index
- Check: `pip search fastapi-scaffold-with-auth`

### Installation Issues

- Update index: `pip install --upgrade pip`
- Try: `pip install fastapi-scaffold-with-auth --no-cache-dir`

---

See [CONTRIBUTING.md](../CONTRIBUTING.md) for development guidelines.
