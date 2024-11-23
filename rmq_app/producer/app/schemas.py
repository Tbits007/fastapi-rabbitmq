from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    email: str
    password: str
    is_active: bool = True
    is_superuser: bool = True
    