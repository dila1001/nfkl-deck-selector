from datalayer.database import get_db
from sqlalchemy.orm import Session
import datalayer.database
import datalayer.deck_db
import datalayer.schema.decks
from model.deck import DeckList, Deck
import re
import apiclients.keyforge_api

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

async def disable_deck(deck_id: str, user_id: str):
    db: Session = next(get_db())
    db_deck = datalayer.deck_db.get_deck(db, user_id=user_id, deck_id=deck_id)
    setattr(db_deck, "enabled", False)
    updated_deck = datalayer.database.save(db, data=db_deck)
    return Deck.model_validate(updated_deck)

async def enable_deck(deck_id: str, user_id: str):
    db: Session = next(get_db())
    db_deck = datalayer.deck_db.get_deck(db, user_id=user_id, deck_id=deck_id)
    setattr(db_deck, "enabled", True)
    updated_deck = datalayer.database.save(db, data=db_deck)
    return Deck.model_validate(updated_deck)

async def register_decks(links: list[str], user_id: str):
    db: Session = next(get_db())

    decks:list[Deck] = []
    for link in links:
        uuid = __get_uuid(link)
        if uuid is None: continue
        if await __deck_exists(deck_id=uuid, user_id=user_id):
            deck = await enable_deck(deck_id=uuid, user_id=user_id)
            decks.append(deck)
            continue

        keyForgeDeck: apiclients.keyforge_api.KeyForgeDeck = await apiclients.keyforge_api.crawl_deck(uuid=uuid)
        db_deck = datalayer.schema.decks.Deck(
            user_id=user_id,
            deck_id=keyForgeDeck.id,
            deck_name=keyForgeDeck.name,
            house_1=keyForgeDeck.houses[0],
            house_2=keyForgeDeck.houses[1],
            house_3=keyForgeDeck.houses[2],
            expansion=keyForgeDeck.expansion,
            enabled=True
        )
        deck = datalayer.database.save(db, data=db_deck)
        decks.append(deck)

    return DeckList(decks=decks)

async def __deck_exists(deck_id:str, user_id:str):
    db: Session = next(get_db())
    db_deck = datalayer.data.get_deck(db, user_id=user_id, deck_id=deck_id)
    return db_deck is not None

def __get_uuid(text:str ):
    pattern = re.compile(
        (
            '[a-f0-9]{8}-' +
            '[a-f0-9]{4}-' +
            '[1-5][a-f0-9]{3}-' +
            '[89ab][a-f0-9]{3}-' +
            '[a-f0-9]{12}$'
        ),
        re.IGNORECASE
    )

    match = pattern.search(text)
    if match is None:
        return match
    else:
        return match.group(0)