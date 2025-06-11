from pydantic import BaseModel, model_validator

from database.hash import pwd_context


class CreateUserRequest(BaseModel):
    email: str
    name: str
    password: str

    #
    # @model_validator(mode="after")
    # def hash_password(self) -> "CreateUserRequest":
    #     if not self.password.startswith("$2b$"):
    #         self.password = pwd_context.hash(self.password)
    #     return self
