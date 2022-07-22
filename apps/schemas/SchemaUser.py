from pydantic import BaseModel


class User(BaseModel):
    id: str = None
    email: str = None
    password: str = None