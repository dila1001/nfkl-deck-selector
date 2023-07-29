from typing import Union, Annotated
from fastapi import FastAPI, Depends, Request, HTTPException, status
from model.user import UserList, User
from model.deck import DeckList
from model.token import Token
import security.auth
import security.google
import repositories.users
import repositories.decks

app = FastAPI()

@app.get("/decks", response_model=DeckList, response_model_exclude_none=True)
async def decks(
    current_user: Annotated[User, Depends(security.auth.get_current_user)],
    season: str = None
):
    if not current_user.approved_user:
        raise __create_exception(status.HTTP_400_BAD_REQUEST, "User needs to be approved first")

    return await repositories.decks.get_decks_by_season(season, current_user)

@app.get("/users/", response_model=UserList)
async def users(
    current_user: Annotated[User, Depends(security.auth.get_current_user)],
    page_number: int=0, page_size: int=100,
):
    if not security.auth.has_role(current_user, 'Admin'):
        raise __create_exception(status.HTTP_401_UNAUTHORIZED, "Admin only endpoint")
    return await repositories.users.users(page_number=page_number, page_size=page_size)

@app.get("/login/callback", response_model=Token)
async def login_callback(code: str, request: Request):
    access_token = security.google.login_user(code, request.url._url, request.base_url._url)
    return { "access_token": access_token, "token_type": "bearer" }

@app.get("/login")
async def login(request: Request):
    return { "google_auth_url": security.google.get_auth_endpoint(request.base_url._url) }

def __create_exception(status_code: int, message: str):
    return HTTPException(
    status_code,
    detail=message,
)