"""Auth schemas."""

from pydantic import BaseModel, Field

from modules.users.schema import UserCreate, UserLogin


class RegisterSchema(UserCreate):
    """User registration schema."""

    password: str = Field(min_length=8, description="Password must be at least 8 characters")


class LoginSchema(UserLogin):
    """User login schema."""

    pass


class TokenResponse(BaseModel):
    """Token response schema."""

    access_token: str
    refresh_token: str
    token_type: str = "bearer"
