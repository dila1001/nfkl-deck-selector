from sqlalchemy import and_
from sqlalchemy.orm import Session
from datalayer.schema.decks import SeasonDeck, Deck

def get_decks_by_season(db: Session, user_id: str, season: str):
    decks = db.query(SeasonDeck).filter(and_(SeasonDeck.user_id==user_id, SeasonDeck.season==season)).all()
    return decks

def get_decks(db: Session, user_id: str):
    decks = db.query(Deck).filter(Deck.user_id==user_id).all()
    return decks

def get_all_decks(db: Session):
    decks = db.query(Deck).all()
    return decks

def get_all_decks_by_season(db: Session, season: str):
    decks = db.query(SeasonDeck).filter(SeasonDeck.season==season).all()
    return decks

def get_deck(db: Session, user_id: str, deck_id: str):
    deck = db.query(Deck).filter(and_(Deck.deck_id==deck_id, Deck.user_id==user_id)).first()
    return deck

def save_deck(db: Session, deck: Deck):
    db.add(deck)
    db.commit()
    db.refresh(deck)
    return deck
