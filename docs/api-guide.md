# API Guide

## Authentication

### Register User

```bash
POST /api/v1/auth/register

{
  "email": "user@example.com",
  "password": "securepass123"
}

Response (201):
{
  "access_token": "eyJhbGc...",
  "refresh_token": "eyJhbGc...",
  "token_type": "bearer"
}
```

### Login

```bash
POST /api/v1/auth/login

{
  "email": "user@example.com",
  "password": "securepass123"
}

Response (200):
{
  "access_token": "eyJhbGc...",
  "refresh_token": "eyJhbGc...",
  "token_type": "bearer"
}
```

## Protected Endpoints

### Get Current User

Requires `Authorization: Bearer {access_token}` header

```bash
GET /api/v1/users/me

Response (200):
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "email": "user@example.com",
  "is_active": true
}
```

## Error Responses

```json
{
  "detail": "Error message describing what went wrong"
}
```

Common status codes:
- **200**: Success
- **201**: Created
- **400**: Bad request (validation error)
- **401**: Unauthorized (missing/invalid token)
- **403**: Forbidden (insufficient permissions)
- **409**: Conflict (email already exists)
- **422**: Unprocessable entity (validation error)
- **500**: Server error

## Rate Limiting

Endpoints are rate-limited by IP address:

```
GET /api/v1/auth/login: 5 requests per minute
POST /api/v1/auth/register: 3 requests per minute
```

When rate limit is exceeded:

```json
{
  "detail": "429 Too Many Requests"
}
```

## Health Checks

### Liveness Probe

```bash
GET /health
Response: {"status": "healthy"}
```

### Readiness Probe

```bash
GET /ready
Response: {"status": "ready"}
```

## Interactive Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI Schema**: `http://localhost:8000/openapi.json`
