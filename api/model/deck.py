from pydantic import BaseModel

class Deck(BaseModel):
    user_id: str
    deck_id: str
    deck_name: str | None
    house_1: str | None
    house_2: str | None
    house_3: str | None
    expansion: str | None
    enabled: bool | None = False

    class Config:
        from_attributes = True

class SeasonDeck(BaseModel):
    season: str
    lineup: int
    user_id: str
    deck: Deck

    class Config:
        from_attributes = True

class DeckList(BaseModel):
    seasonDeck:list[SeasonDeck] | None = None
    decks:list[Deck] | None = None

    class Config:
        from_attributes = True