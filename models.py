from pydantic import BaseModel, Field


class User(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="John Doe")
    phone_no: str = Field(..., example="1234567890")
    address: str = Field(..., example="123 Main St")


class UserCreate(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="John Doe")
    phone_no: str = Field(..., example="1234567890")
    address: str = Field(..., example="123 Main St")


class UserUpdate(BaseModel):
    name: str = Field(..., example="John Updated")
    phone_no: str = Field(..., example="9876543210")
    address: str = Field(..., example="456 Updated St")

