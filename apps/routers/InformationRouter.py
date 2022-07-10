from fastapi import APIRouter
from apps.helper import Config


PARAMS = Config.PARAMS
INFORMATION = PARAMS.INFORMATION


router = APIRouter()


@router.get("/")
async def home():
    return INFORMATION["title"]


@router.get("/ping")
async def ping():
    return INFORMATION["version"]