from pydantic import BaseModel
from model.user import User

class Game(BaseModel):
    game_id: str
    game_name: str
    season: str
    player1_id: str
    player1: User
    player2_id: str | None
    player2: User | None
    game_created: int
    game_updated: int | None
    game_finished: int | None

    class Config:
        from_attributes = True

class GameList(BaseModel):
    games: list[Game]

    class Config:
        from_attributes = True
