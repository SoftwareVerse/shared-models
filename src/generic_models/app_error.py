from pydantic import BaseModel

class DetailModel(BaseModel):
    """Model representing error details."""
    message: str
    error: str

class AppErrorResponseModel(BaseModel):
    """Model representing an application error response."""
    detail: DetailModel
