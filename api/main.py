from typing import Union, Annotated
from fastapi import FastAPI, Depends, Request
from model.user import User
from model.token import Token
import security.auth
import security.google 

app = FastAPI()

@app.get("/users/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(security.auth.get_current_user)]
):
    return current_user

@app.get("/login/callback", response_model=Token)
async def login_callback(code: str, request: Request):
    access_token = security.google.login_user(code, request.url._url, request.base_url._url)
    return { "access_token": access_token, "token_type": "bearer" }

@app.get("/login")
async def login(request: Request):
    return { "google_auth_url": security.google.get_auth_endpoint(request.base_url._url) }
