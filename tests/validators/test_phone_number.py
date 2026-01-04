import pytest

from src.validators.phone_number import validate_phone_number_format


class TestValidatePhoneNumberFormat:
    """Tests for phone number validation and formatting."""
    def test_none_returns_none(self):
        """None should pass through unchanged."""
        assert validate_phone_number_format(None) is None

    def test_empty_string_returns_empty(self):
        """Empty values should pass through unchanged."""
        assert validate_phone_number_format("") == ""

    def test_valid_number_formats_to_e164(self):
        """Valid phone numbers should be formatted to E.164."""
        assert validate_phone_number_format("+12025550123") == "+12025550123"

    def test_invalid_number_raises_value_error(self):
        """Invalid phone numbers should raise ValueError."""
        with pytest.raises(ValueError):
            validate_phone_number_format("123")

    def test_invalid_format_raises_value_error(self):
        """Non-numeric strings should raise ValueError."""
        with pytest.raises(ValueError):
            validate_phone_number_format("not-a-number")
