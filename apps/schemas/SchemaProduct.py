from typing import List
from datetime import datetime
from pydantic import BaseModel


class RequestProduct(BaseModel):
    name: str = ''
    price: int = 0
    desc: str = ''


class ResponseProduct(BaseModel):
    id: str = None
    name: str = None
    price: str = None
    desc: str = None
    imagepath: str = None
    timestamp: datetime = None


class ListProduct(BaseModel):
    list_product: List[ResponseProduct] = []