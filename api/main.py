from typing import Union, Annotated
from fastapi import FastAPI, Depends
from model.user import User
from model.token import Token
from security.auth import get_current_user, login_user

app = FastAPI()

@app.get("/users/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return current_user

@app.get("/login", response_model=Token)
async def login():
    access_token = login_user('test')
    return { "access_token": access_token, "token_type": "bearer" }