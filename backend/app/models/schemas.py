"""Data models and schemas for the API."""

from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class BaseResponse(BaseModel):
    """Base response model."""
    status: str
    message: Optional[str] = None
    data: Optional[Dict[str, Any]] = None


class User(BaseModel):
    """User model."""
    id: str
    email: str
    name: str
    created_at: datetime


class Community(BaseModel):
    """Community model."""
    id: str
    name: str
    description: Optional[str] = None
    created_at: datetime


class Document(BaseModel):
    """Document model."""
    id: str
    title: str
    content: str
    community_id: str
    created_at: datetime
    updated_at: datetime


class Insight(BaseModel):
    """Insight model."""
    id: str
    title: str
    description: str
    metrics: Dict[str, Any]
    created_at: datetime
