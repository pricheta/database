from pydantic import BaseModel, field_validator

from database.hash import pwd_context


class CreateUserRequest(BaseModel):
    email: str
    name: str
    password: str


    @classmethod
    @field_validator("password")
    def hash_password(cls, v: str) -> str:
        return pwd_context.hash(v)
