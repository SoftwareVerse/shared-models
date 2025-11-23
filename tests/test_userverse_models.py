import pytest
from pydantic import ValidationError

from userverse.generic_pagination import PaginationParams
from userverse.validators.phone_number import validate_phone_number_format
from userverse.user.user import (
    TokenResponseModel,
    UserCreateModel,
    UserQueryParams,
)
from userverse.company.roles import CompanyDefaultRoles, RoleDeleteModel
from userverse.company.user import CompanyUserAddModel
from userverse.company.company import CompanyCreateModel


class TestPhoneNumberValidation:
    def test_accepts_none(self):
        assert validate_phone_number_format(None) is None

    def test_valid_number_returns_e164(self):
        assert validate_phone_number_format("+12025550123") == "+12025550123"

    def test_invalid_number_raises_value_error(self):
        with pytest.raises(ValueError):
            validate_phone_number_format("123")


class TestPaginationParams:
    def test_offset_calculation_defaults(self):
        params = PaginationParams()
        assert params.offset == 0

    def test_offset_calculation_non_default(self):
        params = PaginationParams(limit=25, page=3)
        assert params.offset == 50


class TestUserModels:
    def test_user_create_validates_and_formats_phone_number(self):
        user = UserCreateModel(phone_number="+441234567890")
        assert user.phone_number == "+441234567890"

    def test_user_query_params_inherit_pagination(self):
        params = UserQueryParams(page=2)
        assert params.limit == 10
        assert params.offset == 10

    def test_token_response_default_token_type(self):
        token = TokenResponseModel(
            access_token="access",
            access_token_expiration="2025-01-01 00:00:00",
            refresh_token="refresh",
            refresh_token_expiration="2025-01-02 00:00:00",
        )
        assert token.token_type == "bearer"


class TestCompanyModels:
    def test_company_create_validates_phone_number(self):
        company = CompanyCreateModel(
            phone_number="+12025550123",
            email="info@example.com",
        )
        assert company.phone_number == "+12025550123"


class TestCompanyRoles:
    def test_default_role_properties(self):
        assert CompanyDefaultRoles.ADMINISTRATOR.name_value == "Administrator"
        assert CompanyDefaultRoles.ADMINISTRATOR.description == "Full access to manage users and data"

    def test_role_delete_rejects_default_role(self):
        with pytest.raises(ValidationError):
            RoleDeleteModel(
                replacement_role_name="Manager",
                role_name_to_delete=CompanyDefaultRoles.ADMINISTRATOR.name_value,
            )


class TestCompanyUser:
    def test_company_user_add_default_role(self):
        company_user = CompanyUserAddModel(email="user@example.com")
        assert company_user.role == CompanyDefaultRoles.VIEWER.name_value
