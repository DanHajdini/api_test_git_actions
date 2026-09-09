from pydantic import BaseModel, Field

class UserLoginRequestDto(BaseModel):
    username: str = Field(min_length=2)
    password: str = Field()