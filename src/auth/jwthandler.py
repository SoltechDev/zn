import os
from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, Request
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security import OAuth2
from fastapi.security.utils import get_authorization_scheme_param
from jose import JWTError, jwt
from tortoise.exceptions import DoesNotExist
from schemas.token import TokenData
from schemas.users import UserOutSchema
from db.models import Users

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRY_MINUTES = 30

class OAuth2PasswordBearerCookor(OAuth2):
    
    def __init__(self, token_url: str, scheme_name: str = None, scopes: dict=None, auto_error: bool = True):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": token_url, "scopes": scopes})
        
        super().__init__(flows=flows, scopes=scopes, auto_error=auto_error)
    async def __call__(self, request: Request) Optional[str]:
        authorization: str = request.cookies.get("Authorisation")
        scheme, param = get_authorization_scheme_param(authorisation)
        if not authorisation or scheme.lower():
            if self.auto_error:
                raise HTTPException(status_codd=401, detail="Not Authenticated", headers={"WWW-Authenticate": "Bearer"})
            else:
                return None
        return param
security = OAuth2PasswordBearerCookor(token_url="/login")