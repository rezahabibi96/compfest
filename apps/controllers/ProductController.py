import os
from time import time
from datetime import datetime
from uuid import uuid4
from boto3 import client
from fastapi import UploadFile, File
from apps.helper import Log, Config
from apps.models.ProductModel import Product
from apps.schemas import BaseResponse
from apps.schemas.SchemaProduct import ResponseProduct, ListProduct, RequestProduct


storage = Config.PARAMS.STORAGE


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
                result.data = {}
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
    def create_product(cls, name, price, desc, file:UploadFile):
        result = BaseResponse()
        result.status = 400

        try:
            s3 = client('s3', aws_access_key_id=storage.key, aws_secret_access_key=storage.secret)
            
            filename = f"{int(time())}_{uuid4()}.jpg" 
            s3.upload_fileobj(file.file, storage.bucket, filename)

            imagepath = f"https://s3-bucket-compfest.s3.ap-southeast-1.amazonaws.com/{filename}"
            timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")

            data = Product(name=name, price=price, desc=desc,
                           imagepath=imagepath, timestamp=timestamp)
            data.save()

            result.message = 'success'
            result.data = ResponseProduct(**data.serialize())
            result.status = 200
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)
        
        return result

    @classmethod
    async def create_product_local_legacy(cls, name, price, desc, file:UploadFile):
        result = BaseResponse()
        result.status = 400

        try:
            dirpath = f"{os.getcwd()}/assets/images"
            filename = f"{int(datetime.timestamp())}_{uuid4()}.jpg"
            
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