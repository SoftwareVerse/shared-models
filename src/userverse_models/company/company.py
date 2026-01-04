from typing import Optional

from pydantic import BaseModel, EmailStr, field_validator, Field

from generic_models.generic_pagination import PaginationParams

from .address import CompanyAddressModel
from ..validators.phone_number import validate_phone_number_format


class CompanyReadModel(BaseModel):
    """Model representing a company."""

    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    industry: Optional[str] = None
    phone_number: Optional[str] = Field(
        None, json_schema_extra={"example": "1236547899"}
    )
    email: EmailStr
    address: Optional[CompanyAddressModel] = None


class CompanyUpdateModel(BaseModel):
    """Model for updating company details."""

    name: Optional[str] = None
    description: Optional[str] = None
    industry: Optional[str] = None
    phone_number: Optional[str] = Field(
        None, json_schema_extra={"example": "1236547899"}
    )
    address: Optional[CompanyAddressModel] = None

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, v: Optional[str]) -> Optional[str]:
        """Validate phone number format."""
        return validate_phone_number_format(v)


class CompanyCreateModel(BaseModel):
    """Model for creating a new company."""

    name: Optional[str] = None
    description: Optional[str] = None
    industry: Optional[str] = None
    phone_number: Optional[str] = Field(
        None, json_schema_extra={"example": "1236547899"}
    )
    email: EmailStr
    address: Optional[CompanyAddressModel] = None

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, v: Optional[str]) -> Optional[str]:
        """Validate phone number format."""
        return validate_phone_number_format(v)


class CompanyQueryParamsModel(PaginationParams):
    """Model for querying companies with optional filters."""

    role_name: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    industry: Optional[str] = None
    email: Optional[str] = None
