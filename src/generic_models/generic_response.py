from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")

class GenericResponseModel(BaseModel, Generic[T]):
    """Generic response model wrapping a message and optional data."""
    message: str
    data: Optional[T]
