from sqlalchemy.orm import Session
from datalayer.schema.games import Game

def get_games_by_season(db: Session, season=str):
    games = db.query(Game).filter(Game.season==season).all()
    return games