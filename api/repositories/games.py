from datalayer.database import get_db
from sqlalchemy.orm import Session
import datalayer.game_db
from model.game import GameList

async def get_all_games(season: str):
    db: Session = next(get_db())
    games = datalayer.game_db.get_games_by_season(db, season=season)
    return GameList(games=games)

async def get_game(game_id: str):
    db: Session = next(get_db())
    game = datalayer.game_db.get_game(db, game_id=game_id)
    return GameList(game=game, games=None)