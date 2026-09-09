from pydantic import BaseModel, EmailStr, Field

from enums.user_role import UserRole

class UserRegisterRequestDto(BaseModel):
    username: str = Field(min_length=2)
    password: str = Field()
    email: EmailStr = Field()
    role: UserRole = Field()