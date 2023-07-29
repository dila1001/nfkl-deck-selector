from sqlalchemy.orm import Session
from datalayer.schema.seasons import Season

def get_all_seasons(db: Session):
    seasons = db.query(Season).all()
    return seasons
