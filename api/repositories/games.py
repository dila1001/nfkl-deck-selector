from datalayer.database import get_db
from sqlalchemy.orm import Session
import datalayer.game_db
from model.game import GameList

async def get_all_decks(season: str):
    db: Session = next(get_db())
    games = datalayer.game_db.get_games_by_season(db, season=season)
    return GameList(games=games)
