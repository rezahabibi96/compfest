import os
from time import time
from datetime import datetime
from uuid import uuid4
from fastapi import File, UploadFile
from apps.helper import Log
from apps.models.ProductModel import Product
from apps.schemas import BaseResponse
from apps.schemas.SchemaProduct import RequestProduct, ResponseProduct, ListProduct


class ControllerBalance(object):
    @classmethod
    def get_products(cls):
        result = BaseResponse()
        result.status = 400

        try:
            data = Product.all()
            result.message = 'success'
            result.status = 200  
            result.data = ListProduct(**{"list_product": data.serialize()})
            Log.info(result.message)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def get_product(cls, product_id=None):
        result = BaseResponse()
        result.status = 400

        try:
            data = Product.where('id', '=', product_id).first()
            if data:
                result.data = ResponseProduct(**data.serialize())
            else:
                result.data = []
            result.message = 'success'
            result.status = 200  
            Log.info(result.message)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def checkout(cls, product_id=None):
        result = BaseResponse()
        result.status = 400

        try:
            data = Product.where('id', '=', product_id).first()
            if data:
                data.delete()
                result.message = 'success'
            else:
                result.message = 'product id not found'
            result.status = 200  
            Log.info(result.message)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    async def create_product(cls, name, price, desc, file:UploadFile):
        result = BaseResponse()
        result.status = 400

        try:
            dirpath = f"{os.getcwd()}/assets/images"
            filename = f"{time()}_{uuid4()}.jpg"
            
            data = Product(name=name, price=price, desc=desc,
                           imagepath=filename, timestamp=str(datetime.now()))
            data.save()

            file.filename = filename
            contents = await file.read()

            with open(f"{dirpath}/{filename}", "wb") as f:
                f.write(contents)

            result.message = 'success'
            result.data = ResponseProduct(**data.serialize())
            result.status = 200
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)
        
        return result