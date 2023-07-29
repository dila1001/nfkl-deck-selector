from datalayer.database import get_db
from sqlalchemy.orm import Session
import datalayer.deck_db
from model.deck import DeckList
from model.user import User

async def get_decks_by_season(season: str, user: User):
    if season == None:
        return await get_decks(user)

    db: Session = next(get_db())
    seasonDecks = datalayer.deck_db.get_decks_by_season(db, user=user, season=season)
    return DeckList(seasonDeck=seasonDecks)

async def get_decks(user: User):
    db: Session = next(get_db())
    decks = datalayer.deck_db.get_decks(db, user=user)
    return DeckList(decks=decks)

async def get_all_decks():
    db: Session = next(get_db())
    decks = datalayer.deck_db.get_all_decks(db)
    return DeckList(decks=decks)
