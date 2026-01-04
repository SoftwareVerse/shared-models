from pydantic import BaseModel, EmailStr


class PasswordResetRequest(BaseModel):
    """Model for requesting a password reset via email."""

    email: EmailStr


class OTPValidationRequest(BaseModel):
    """Model for validating OTP during password reset."""

    otp: str
