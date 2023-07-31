from typing import Union, Annotated
from fastapi import FastAPI, Depends, Request, HTTPException, status
from model.season import SeasonList, Season
from model.user import UserList, User, UserCreate
from model.deck import DeckList
from model.group import GroupList
from model.game import GameList
from model.token import Token
import security.auth, security.google
import repositories.users, repositories.decks, repositories.seasons, repositories.group, repositories.games

app = FastAPI()

@app.get("/games/seasons/{season}", response_model=GameList, response_model_exclude_none=True)
async def games(
    current_user: Annotated[User, Depends(security.auth.get_current_user)],
    season:str
):
    if not current_user.approved_user:
        raise __create_exception(status.HTTP_401_UNAUTHORIZED, "User needs to be approved first")

    return await repositories.games.get_all_games(season=season)

@app.get("/games/{game_id}", response_model=GameList, response_model_exclude_none=True)
async def active_game(
    current_user: Annotated[User, Depends(security.auth.get_current_user)],
    game_id:str
):
    if not current_user.approved_user:
        raise __create_exception(status.HTTP_401_UNAUTHORIZED, "User needs to be approved first")

    return await repositories.games.get_game(game_id=game_id)

@app.get("/groups", response_model=GroupList, response_model_exclude_none=True)
async def groups(
    current_user: Annotated[User, Depends(security.auth.get_current_user)]
):
    if not current_user.approved_user:
        raise __create_exception(status.HTTP_401_UNAUTHORIZED, "User needs to be approved first")

    return await repositories.group.groups()

@app.get("/groups/{season}", response_model=GroupList, response_model_exclude_none=True)
async def groups(
    current_user: Annotated[User, Depends(security.auth.get_current_user)],
    season:str
):
    if not current_user.approved_user:
        raise __create_exception(status.HTTP_401_UNAUTHORIZED, "User needs to be approved first")

    return await repositories.group.get_group_user(season=season)

@app.get("/seasons", response_model=SeasonList)
async def seasons(
    current_user: Annotated[User, Depends(security.auth.get_current_user)]
):
    if not current_user.approved_user:
        raise __create_exception(status.HTTP_401_UNAUTHORIZED, "User needs to be approved first")

    return await repositories.seasons.get_all_seasons()

@app.post("/seasons", response_model=Season)
async def create_season(
    current_user: Annotated[User, Depends(security.auth.get_current_user)],
    season: Season
):
    if not security.auth.has_role(current_user, 'Admin'):
        raise __create_exception(status.HTTP_401_UNAUTHORIZED, "Admin only endpoint")

    return await repositories.seasons.create_season(season=season)

@app.get("/decks", response_model=DeckList, response_model_exclude_none=True)
async def decks(
    current_user: Annotated[User, Depends(security.auth.get_current_user)],
    user_id: str = None,
    season: str = None,
    include_all: bool = False
):
    if not current_user.approved_user:
        raise __create_exception(status.HTTP_401_UNAUTHORIZED, "User needs to be approved first")
    if include_all and not security.auth.has_role(current_user, 'Admin'):
        raise __create_exception(status.HTTP_401_UNAUTHORIZED, "`include_all` is only available for Admin")

    if include_all:
        return await repositories.decks.get_all_decks(season=season)

    user_id = current_user.id if user_id is None else user_id
    return await repositories.decks.get_decks(season=season, user_id=user_id)

@app.post("/decks", response_model=DeckList, response_model_exclude_none=True)
async def register_decks(
    current_user: Annotated[User, Depends(security.auth.get_current_user)],
    links:list[str]
):
    if not current_user.approved_user:
        raise __create_exception(status.HTTP_401_UNAUTHORIZED, "User needs to be approved first")

    return await repositories.decks.register_decks(links, current_user.id)

@app.delete("/decks/{deck_id}")
async def delete_deck(
    current_user: Annotated[User, Depends(security.auth.get_current_user)],
    deck_id: str
):
    await repositories.decks.disable_deck(deck_id=deck_id, user_id=current_user.id)
    return { "Success": True}

@app.get("/users", response_model=UserList)
async def users(
    current_user: Annotated[User, Depends(security.auth.get_current_user)],
    page_number: int=0, page_size: int=100,
):
    if not security.auth.has_role(current_user, 'Admin'):
        raise __create_exception(status.HTTP_401_UNAUTHORIZED, "Admin only endpoint")
    return await repositories.users.users(page_number=page_number, page_size=page_size)

@app.get("/users/archived", response_model=UserList)
async def archived_users(
    current_user: Annotated[User, Depends(security.auth.get_current_user)],
    season: str,
    page_number: int=0, page_size: int=100,
):
    if not security.auth.has_role(current_user, 'Admin'):
        raise __create_exception(status.HTTP_401_UNAUTHORIZED, "Admin only endpoint")
    return await repositories.users.get_archived_users(season=season, page_number=page_number, page_size=page_size)

@app.patch("/users/{user_id}", response_model=User)
async def update_user(
    current_user: Annotated[User, Depends(security.auth.get_current_user)],
    user: UserCreate,
    user_id: str
):
    update_other_user = current_user.id != user_id
    is_admin = security.auth.has_role(current_user, 'Admin')
    if update_other_user and not is_admin:
        raise __create_exception(status.HTTP_401_UNAUTHORIZED, "Only admin can update other users")

    return await repositories.users.update_user(user=user, user_id=user_id)

@app.post("/users/{user_id}/approve", response_model=User)
async def approve_user(
    current_user: Annotated[User, Depends(security.auth.get_current_user)],
    user_id: str
):
    if not security.auth.has_role(current_user, 'Admin'):
        raise __create_exception(status.HTTP_401_UNAUTHORIZED, "Admin only endpoint")

    return await repositories.users.approve_user(user_id=user_id)

@app.get("/login/callback", response_model=Token)
async def login_callback(code: str, request: Request):
    access_token = await security.google.login_user(code, request.url._url, request.base_url._url)
    return { "access_token": access_token, "token_type": "bearer" }

@app.get("/login")
async def login(request: Request):
    return { "google_auth_url": security.google.get_auth_endpoint(request.base_url._url) }

def __create_exception(status_code: int, message: str):
    return HTTPException(
    status_code,
    detail=message,
)