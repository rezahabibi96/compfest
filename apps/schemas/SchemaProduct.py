from pydantic import BaseModel
from typing import Optional, List


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
    timestamp: str = None


class ListProduct(BaseModel):
    list_product: List[ResponseProduct] = []