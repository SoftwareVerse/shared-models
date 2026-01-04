import pytest
from pydantic import BaseModel, ValidationError

from generic_models.app_error import AppErrorResponseModel, DetailModel
from generic_models.generic_pagination import (
    FilterLogic,
    MatchType,
    PaginatedResponse,
    PaginationMeta,
    PaginationParams,
)
from generic_models.generic_response import GenericResponseModel


class Item(BaseModel):
    """Simple record type for pagination tests."""

    id: int


class TestAppErrorModels:
    """Tests for application error models."""

    def test_detail_model_roundtrip(self):
        """DetailModel should preserve message and error fields."""
        detail = DetailModel(message="Not found", error="missing_resource")
        response = AppErrorResponseModel(detail=detail)
        assert response.detail.message == "Not found"
        assert response.detail.error == "missing_resource"

    def test_missing_detail_raises_validation_error(self):
        """AppErrorResponseModel should require detail."""
        with pytest.raises(ValidationError):
            AppErrorResponseModel()


class TestGenericResponseModel:
    """Tests for GenericResponseModel."""

    def test_generic_response_with_data(self):
        """GenericResponseModel should accept typed data."""
        response = GenericResponseModel[str](message="ok", data="value")
        assert response.message == "ok"
        assert response.data == "value"

    def test_generic_response_allows_none_data(self):
        """GenericResponseModel should allow data to be None."""
        response = GenericResponseModel[Item](message="ok", data=None)
        assert response.data is None

    def test_generic_response_requires_data_field(self):
        """GenericResponseModel should require the data field even if optional."""
        with pytest.raises(ValidationError):
            GenericResponseModel[str](message="ok")


class TestPaginationEnums:
    """Tests for pagination enums."""

    def test_match_type_values(self):
        """MatchType should expose expected string values."""
        assert MatchType.PARTIAL.value == "partial"
        assert MatchType.EXACT.value == "exact"
        assert MatchType.STARTS_WITH.value == "starts_with"

    def test_filter_logic_values(self):
        """FilterLogic should expose expected string values."""
        assert FilterLogic.OR.value == "or"
        assert FilterLogic.AND.value == "and"


class TestPaginationParams:
    """Tests for PaginationParams."""

    def test_defaults(self):
        """Default pagination values should be limit 10, page 1."""
        params = PaginationParams()
        assert params.limit == 10
        assert params.page == 1
        assert params.offset() == 0

    def test_offset_calculation(self):
        """Offset should match (page - 1) * limit."""
        params = PaginationParams(limit=25, page=3)
        assert params.offset() == 50

    @pytest.mark.parametrize("limit", [0, 101])
    def test_limit_out_of_bounds_raises(self, limit):
        """Limit outside [1, 100] should raise ValidationError."""
        with pytest.raises(ValidationError):
            PaginationParams(limit=limit)

    @pytest.mark.parametrize("page", [0, -1])
    def test_page_out_of_bounds_raises(self, page):
        """Page less than 1 should raise ValidationError."""
        with pytest.raises(ValidationError):
            PaginationParams(page=page)


class TestPaginatedResponse:
    """Tests for PaginatedResponse and PaginationMeta."""

    def test_paginated_response_structure(self):
        """PaginatedResponse should accept records and pagination metadata."""
        meta = PaginationMeta(
            total_records=2,
            limit=10,
            current_page=1,
            total_pages=1,
        )
        response = PaginatedResponse[Item](
            records=[Item(id=1), Item(id=2)],
            pagination=meta,
        )
        assert len(response.records) == 2
        assert response.records[0].id == 1
        assert response.pagination.total_records == 2
