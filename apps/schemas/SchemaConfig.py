from typing import List, Dict
from pydantic import BaseModel


class S3(BaseModel):
    key: str =''
    secret: str =''
    bucket: str=''

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
    STORAGE: S3