from sqlalchemy.orm import Session
from datalayer.schema.games import Game

def get_games_by_season(db: Session, season:str):
    games = db.query(Game).filter(Game.season==season).all()
    return games

def get_game(db: Session, game_id:str):
    game = db.query(Game).filter(Game.game_id==game_id).first()
    return game
