from typing import List
from pydantic import BaseModel


class BaseResponse(BaseModel):
    status: int = 200
    message: str = None
    data: List = []