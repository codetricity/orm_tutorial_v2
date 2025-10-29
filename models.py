# =========================
# base_assets/models.py
# Minimal models for base_assets - only User model
# =========================
import uuid
from typing import Optional
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    __tablename__ = "users"  # type: ignore

    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(unique=True, index=True, nullable=False)
    hashed_password: str = Field(nullable=False)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    is_staff: bool = Field(default=False)  # New field for staff permissions
    group: Optional[str] = Field(default=None)  # marketing, sales, support, etc.


class Product(SQLModel, table=True):
    __tablename__ = "products"  # type: ignore

    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(unique=True, index=True, nullable=False)
    description: str = Field(nullable=True)
    price: float = Field(nullable=True)


class Attendee(SQLModel, table=True):
    __tablename__ = "attendees"  # type: ignore

    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(unique=True, index=True, nullable=False)
