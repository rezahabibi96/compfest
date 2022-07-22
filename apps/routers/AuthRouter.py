import json
from fastapi import APIRouter, Body, Response
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from apps.controllers.AuthController import ControllerAuth as auth


router = APIRouter()

example_input = json.dumps({
    "email": "email@email.com",
    "password": "mypswd"
}, indent=2)


@router.post("/signup")
async def signup(response: Response, input_data=Body(..., example=example_input)):
    result = auth.signup(input_data=input_data)
    response.status_code = result.status
    return result

@router.post("/login")
async def login(response: Response, input_data: OAuth2PasswordRequestForm= Depends()):
    result = auth.login(input_data=input_data)
    response.status_code = result.status
    return result.data