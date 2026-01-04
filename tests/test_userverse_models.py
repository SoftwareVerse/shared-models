import pytest
from pydantic import ValidationError

from src.generic_models.generic_pagination import PaginationParams
from src.userverse_models.validators.phone_number import validate_phone_number_format
from src.userverse_models.user.user import (
    TokenResponseModel,
    UserCreateModel,
    UserQueryParams,
)
from src.userverse_models.company.roles import CompanyDefaultRoles, RoleDeleteModel
from src.userverse_models.company.user import CompanyUserAddModel
from src.userverse_models.company.company import CompanyCreateModel


class TestPhoneNumberValidation:
    """Tests for phone number validation."""
    def test_accepts_none(self):
        """Test that None is accepted and returns None."""
        assert validate_phone_number_format(None) is None

    def test_valid_number_returns_e164(self):
        """Test that a valid phone number is returned in E.164 format."""
        assert validate_phone_number_format("+12025550123") == "+12025550123"

    def test_invalid_number_raises_value_error(self):
        """Test that an invalid phone number raises a ValueError."""
        with pytest.raises(ValueError):
            validate_phone_number_format("123")


class TestPaginationParams:
    """Tests for PaginationParams model."""    
    def test_offset_calculation_defaults(self):
        """Test that default pagination parameters calculate offset correctly."""
        params = PaginationParams()
        assert params.offset == 0

    def test_offset_calculation_non_default(self):
        """Test that non-default pagination parameters calculate offset correctly."""
        params = PaginationParams(limit=25, page=3)
        assert params.offset == 50


class TestUserModels:
    """Tests for user models."""
    def test_user_create_validates_and_formats_phone_number(self):
        """Test that UserCreateModel validates and formats phone number."""
        user = UserCreateModel(phone_number="+441234567890")
        assert user.phone_number == "+441234567890"

    def test_user_query_params_inherit_pagination(self):
        """Test that UserQueryParams inherits from PaginationParams."""
        params = UserQueryParams(page=2)
        assert params.limit == 10
        assert params.offset == 10

    def test_token_response_default_token_type(self):
        """Test that TokenResponseModel has default token_type 'bearer'."""
        token = TokenResponseModel(
            access_token="access",
            access_token_expiration="2025-01-01 00:00:00",
            refresh_token="refresh",
            refresh_token_expiration="2025-01-02 00:00:00",
        )
        assert token.token_type == "bearer"


class TestCompanyModels:
    """Tests for company models."""
    def test_company_create_validates_phone_number(self):
        """Test that CompanyCreateModel validates phone number."""
        company = CompanyCreateModel(
            phone_number="+12025550123",
            email="info@example.com",
        )
        assert company.phone_number == "+12025550123"


class TestCompanyRoles:
    """Tests for company role models."""
    def test_default_role_properties(self):
        """Test that CompanyDefaultRoles properties return correct values."""
        assert CompanyDefaultRoles.ADMINISTRATOR.name_value == "Administrator"
        assert (
            CompanyDefaultRoles.ADMINISTRATOR.description
            == "Full access to manage users and data"
        )

    def test_role_delete_rejects_default_role(self):
        """Test that RoleDeleteModel raises ValidationError when deleting a default role."""
        with pytest.raises(ValidationError):
            RoleDeleteModel(
                replacement_role_name="Manager",
                role_name_to_delete=CompanyDefaultRoles.ADMINISTRATOR.name_value,
            )


class TestCompanyUser:
    """Tests for company user models."""
    def test_company_user_add_default_role(self):
        """Test that CompanyUserAddModel assigns default role if none provided."""
        company_user = CompanyUserAddModel(email="user@example.com")
        assert company_user.role == CompanyDefaultRoles.VIEWER.name_value
