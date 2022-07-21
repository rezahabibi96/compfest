import json
from fastapi import APIRouter, Body, Response, Form
from fastapi import File, UploadFile
from apps.controllers.ProductController import ControllerBalance as product


router = APIRouter()

example_input = json.dumps({
    "amount": "10000",
}, indent=2)


@router.get("/products")
async def get_products(response: Response):
    result = product.get_products()
    response.status_code = result.status
    return result

@router.get("/products/{product_id}")
async def get_products(response: Response, product_id: int):
    result = product.get_product(product_id=product_id)
    response.status_code = result.status
    return result

@router.get("/products/checkout/{product_id}")
async def checkout(response: Response, product_id: int):
    result = product.checkout(product_id=product_id)
    response.status_code = result.status
    return result

@router.post("/products")
async def create_product(response:Response, name: str=Form(..., example='name'), 
                         price: int=Form(..., example=1000), desc: str=Form(..., example='desc'),
                         file:UploadFile=File(...)):
    result = product.create_product(name=name, price=price, desc=desc, file=file)
    response.status_code = result.status
    return result