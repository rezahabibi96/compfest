import json
from fastapi import APIRouter, Body, Response
from apps.controllers.BalanceController import ControllerBalance as balance


router = APIRouter()

example_input = json.dumps({
    "amount": "10000",
}, indent=2)


@router.post("/balances/withdraw")
async def withdraw_balance(response: Response, input_data=Body(..., example=example_input)):
    result = balance.withdraw_balance(input_data=input_data)
    response.status_code = result.status
    return result

@router.post("/balances/add")
async def add_balance(response: Response, input_data=Body(..., example=example_input)):
    result = balance.add_balance(input_data=input_data)
    response.status_code = result.status
    return result