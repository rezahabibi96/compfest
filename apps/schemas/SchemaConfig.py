from typing import List, Dict
from pydantic import BaseModel


class Postgres(BaseModel):
    host: str =''
    port: int = None
    username: str =''
    password: str =''
    db: str =''
    optn: str =''


class Salt(BaseModel):
    salt: str = ''


class ConfigApps(BaseModel):
    ENVIRONMENT: str = ''
    INFORMATION: Dict = {}
    ALLOWED_HOSTS: List[str] = []
    ALLOWED_METHODS: List[str]  = []
    DATABASE: Postgres
    TOKEN: List[str]  = []
    SALT: Salt