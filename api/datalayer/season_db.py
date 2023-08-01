from sqlalchemy.orm import Session
from datalayer.schema.seasons import Season

def get_all_seasons(db: Session):
    seasons = db.query(Season).all()
    return seasons

def get_season(db: Session, season: str):
    season_data = db.query(Season).filter(Season.season==season).first()
    return season_data
