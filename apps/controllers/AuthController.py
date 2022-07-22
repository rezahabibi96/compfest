from apps.helper import Log
from apps.models.UserModel import User as UserModel
from apps.schemas import BaseResponse
from apps.schemas.SchemaAuth import RequestAuth, ResponseAuth
from apps.schemas.SchemaUser import User as UserSchema
from apps.services.AuthServices import AuthService



class ControllerAuth(object):
    @classmethod
    def signup(cls, input_data=None):
        input_data = RequestAuth(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.email is not None and input_data.password is not None:
                user = UserModel.where('email', '=', input_data.email).first()

                if user:
                    result.message = "user with the given email already exist"
                    result.data = {} 
                else:
                    hashed = AuthService.hash_password(input_data.password)
                    email = input_data.email

                    user = UserModel(email=input_data.email, password=hashed)
                    user.save()

                    data = {
                        "access_token": AuthService.generate_token(email, 'access_token'),
                        "refresh_token": AuthService.generate_token(email, 'refresh_token')
                    }
                    
                    result.message = "success"
                    result.status = 200 
                    result.data = data

                Log.info(result.message)
            else:
                e = "credentials must not be empty!"
                result.message = str(e)
                Log.error(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def login(cls, input_data=None):
        #input_data = RequestAuth(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.username is not None and input_data.password is not None:
                user = UserModel.where('email', '=', input_data.username).first()

                if not user:
                    result.message = "incorrect credentials"
                    result.data = {} 
                else:
                    if not AuthService.verify_password(input_data.password, user.password):
                        result.message = "incorrect credentials"
                        result.data = {}
                    else:
                        data = {
                            "access_token": AuthService.generate_token(user.email, 'access_token'),
                            "refresh_token": AuthService.generate_token(user.email, 'refresh_token')
                        }      
                        result.message = "success"
                        result.status = 200 
                        result.data = data
                Log.info(result.message)
            else:
                e = "credentials must not be empty!"
                result.message = str(e)
                Log.error(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result