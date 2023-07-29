from datalayer.database import get_db
from sqlalchemy.orm import Session
import datalayer.season_db
from model.season import SeasonList

async def get_all_seasons():
    db: Session = next(get_db())
    seasons = datalayer.season_db.get_all_seasons(db)
    return SeasonList(seasons=seasons)