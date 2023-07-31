from datalayer.database import get_db
from sqlalchemy.orm import Session
import datalayer.deck_db
from model.deck import DeckList

async def get_decks(season: str, user_id: str):
    db: Session = next(get_db())
    if season == None:
        decks = datalayer.deck_db.get_decks(db, user_id=user_id)
        return DeckList(decks=decks)

    seasonDecks = datalayer.deck_db.get_decks_by_season(db, user_id=user_id, season=season)
    return DeckList(seasonDeck=seasonDecks)

async def get_all_decks(season: str):
    db: Session = next(get_db())

    if season is None:
        decks = datalayer.deck_db.get_all_decks(db)
        return DeckList(decks=decks)

    seasonDecks = datalayer.deck_db.get_all_decks_by_season(db, season=season)
    return DeckList(seasonDeck=seasonDecks)
