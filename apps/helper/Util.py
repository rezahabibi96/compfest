from fastapi import HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
from apps.helper import Config


PARAMS = Config.PARAMS

API_TOKEN_SECURE = "X-Api-Token"
API_TOKEN_HEADER = APIKeyHeader(name=API_TOKEN_SECURE, auto_error=False)

async def verify_token(api_token_header: str = Security(API_TOKEN_HEADER)):
    if api_token_header not in PARAMS.TOKEN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="could not validate credentials")