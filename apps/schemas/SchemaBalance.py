from pydantic import BaseModel
from typing import Optional, List


class RequestBalance(BaseModel):
    amount: int = 0


class ResponseBalance(BaseModel):
    amount: int = 0