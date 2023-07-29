from sqlalchemy import and_
from sqlalchemy.orm import Session
from datalayer.schema.decks import SeasonDeck
from model.user import User

def get_decks(db: Session, user: User, season=str):
    decks = db.query(SeasonDeck).filter(and_(SeasonDeck.user_id==user.id, SeasonDeck.season==season)).all()
    return decks
