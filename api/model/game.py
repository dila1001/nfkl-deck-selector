from pydantic import BaseModel
from model.user import User
from model.deck import Deck

class Game(BaseModel):
    game_id: str
    game_name: str
    season: str
    player1: User
    player2: User | None
    game_created: int
    game_updated: int | None
    game_finished: int | None

    class Config:
        from_attributes = True

class Choice(BaseModel):
    round_id: int
    round_type: str
    user_id: str
    deck: Deck | None

    class Config:
        from_attributes = True

class Score(BaseModel):
    round_id: int
    player1_keys: int
    player2_keys: int

    class Config:
        from_attributes = True

class GameActive(Game):
    # player1_decks: list[Deck] | None
    # player2_decks: list[Deck] | None
    choices: list[Choice] | None
    scores: list[Score] | None
    decks: list[Deck] | None

    class Config:
        from_attributes = True

class GameList(BaseModel):
    games: list[Game] | None = True
    game: GameActive | None = True

    class Config:
        from_attributes = True
