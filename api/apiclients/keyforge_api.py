import requests
from pydantic import BaseModel

class KeyForgeDeck(BaseModel):
    id:str
    name: str
    houses: list[str]
    expansion: int

async def crawl_deck(uuid: str) -> KeyForgeDeck:
    response = requests.get('https://www.keyforgegame.com/api/decks/{}'.format(uuid))
    response.raise_for_status()
    jsonResponse = response.json()
    data = jsonResponse['data']
    return KeyForgeDeck(
      id=data['id'],
      name=data['name'],
      houses=data['_links']['houses'],
      expansion=data['expansion']
    )
