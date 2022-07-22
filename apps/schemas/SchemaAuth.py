from pydantic import BaseModel


class RequestAuth(BaseModel):
    email: str = ''
    password: str = ''


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


class UserPayload():
    user_email: str = None
    user_password: str = None


class ResponseAuth(BaseModel):
    access_token: str = ''
    refresh_token: str = ''