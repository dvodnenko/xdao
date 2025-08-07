import phonenumbers

from pydantic import BaseModel, EmailStr, Field, field_validator


class UserSchema(BaseModel):

    name: str = Field(max_length=32)
    email: EmailStr = Field(max_length=255)
    phone: str
    password: str
    is_active: bool = Field(default=True)

    class Config:
        from_attributes = True

    @field_validator('phone')
    def validate_phone(cls, v):
        try:
            parsed = phonenumbers.parse(v, None)
            if not phonenumbers.is_valid_number(parsed):
                raise ValueError('Invalid phone number')
            return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
        except phonenumbers.NumberParseException:
            raise ValueError('Invalid phone number format')
