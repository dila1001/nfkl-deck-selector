from sqlalchemy import and_
from sqlalchemy.orm import Session
from datalayer.schema.decks import SeasonDeck, Deck
from model.user import User

def get_decks_by_season(db: Session, user: User, season=str):
    decks = db.query(SeasonDeck).filter(and_(SeasonDeck.user_id==user.id, SeasonDeck.season==season)).all()
    return decks

def get_decks(db: Session, user: User):
    decks = db.query(Deck).filter(Deck.user_id==user.id).all()
    return decks
