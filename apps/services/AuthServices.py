from os import environ
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from apps.helper import Log
from apps.models.UserModel import User 
from apps.schemas.SchemaAuth import TokenPayload


ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
JWT_ACCESS_SECRET_KEY = "rnm4v9zWfp5Rv5jVqAsaefv3Ktx3HyEY"
JWT_REFRESH_SECRET_KEY = "dHPWJJWUWbxE2CJfkHk2qtCYRC395bLs"


pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_bearer = OAuth2PasswordBearer(tokenUrl="/login", scheme_name="JWT")


class AuthService(object):
    
    
    @classmethod
    def hash_password(cls, password):
        return pwd_ctx.hash(password)

    @classmethod
    def verify_password(cls, password, hashed):
        return pwd_ctx.verify(password, hashed)

    @classmethod
    def generate_token(cls, subject, type):
        if type == "access_token":
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            keys = JWT_ACCESS_SECRET_KEY
        else:
            expire = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
            keys = JWT_REFRESH_SECRET_KEY
    
        claim = {"exp": expire, "sub": str(subject)}
        token = jwt.encode(claim, keys, "HS256")
        
        return token

    @classmethod
    def verify_token(cls, token=Depends(oauth_bearer)):
        try:
            payload = jwt.decode(token, JWT_ACCESS_SECRET_KEY, "HS256")
            claim = TokenPayload(**payload)

            if datetime.fromtimestamp(claim.exp) < datetime.now():
                raise HTTPException(
                                    status_code = status.HTTP_401_UNAUTHORIZED, 
                                    detail="token expired", 
                                    headers={"WWW-Authenticate": "Bearer"}
                )
        
            user = User.where('email', '=', claim.sub).first()
            if not user:
                raise HTTPException(
                                    status_code=status.HTTP_404_NOT_FOUND,
                                    detail="could not find user"
                )

        except Exception as e:
            Log.error(e)
            raise HTTPException(
                                status_code=status.HTTP_403_FORBIDDEN,
                                detail="could not validate credentials",
                                headers={"WWW-Authenticate": "Bearer"}
            )