# app/models/generic_pagination.py
from enum import Enum
from typing import Generic, List, TypeVar
from pydantic import BaseModel, Field

T = TypeVar("T")


class MatchType(str, Enum):
    """Enumeration for different types of string matching."""

    PARTIAL = "partial"
    EXACT = "exact"
    STARTS_WITH = "starts_with"


class FilterLogic(str, Enum):
    """Enumeration for filter logic operators."""

    OR = "or"
    AND = "and"


class PaginationParams(BaseModel):
    """Model for pagination parameters."""

    limit: int = Field(10, ge=1, le=100)
    page: int = Field(1, ge=1)  # Page is 1-indexed

    @classmethod
    def offset(cls) -> int:
        """Calculate the offset based on the current page and limit."""
        return (cls.page - 1) * cls.limit


class PaginationMeta(BaseModel):
    """Model for pagination metadata."""

    total_records: int
    limit: int
    current_page: int
    total_pages: int


class PaginatedResponse(BaseModel, Generic[T]):
    """Generic paginated response model."""

    records: List[T]
    pagination: PaginationMeta
