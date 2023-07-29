from datalayer.database import get_db
from sqlalchemy.orm import Session
import datalayer.deck_db
from model.deck import DeckList
from model.user import User

async def get_decks(season: str, user: User):
    db: Session = next(get_db())
    decks = datalayer.deck_db.get_decks(db, user=user, season=season)
    return DeckList(seasonDeck=decks)
