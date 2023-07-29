from sqlalchemy import Boolean, Column, String, Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship, Mapped
from datalayer.database import Base

class Deck(Base):
    __tablename__ = "deck"

    user_id = Column(String, index=True)
    deck_id = Column(String, unique=False, index=True)
    deck_name = Column(String, unique=False, index=False, nullable=True)
    house_1 = Column(String, unique=False, index=False, nullable=True)
    house_2 = Column(String, unique=False, index=False, nullable=True)
    house_3 = Column(String, unique=False, index=False, nullable=True)
    expansion = Column(String, unique=False, index=False, nullable=True)
    enabled = Column(Boolean, unique=False, index=False, nullable=True, default=False)

    __table_args__ = (
        PrimaryKeyConstraint(deck_id, user_id),
        {}
    )

# CREATE TABLE "deck" (
#   user_id TEXT NOT NULL,
#   deck_id TEXT,
#   deck_name TEXT,
#   house_1 TEXT,
#   house_2 TEXT,
#   house_3 TEXT,
#   expansion TEXT,
#   [enabled] BIT,
#   UNIQUE(user_id, deck_id) ON CONFLICT REPLACE
# );

class SeasonDeck(Base):
    __tablename__ = "deckSeason"

    season = Column(String)
    deck_id = Column(String, ForeignKey("deck.deck_id"))
    lineup = Column(Integer)
    user_id = Column(String)
    deck: Mapped["Deck"] = relationship()
    __table_args__ = (
        PrimaryKeyConstraint(season, deck_id, user_id),
        {}
    )


# CREATE TABLE "deckSeason" (
#   season TEXT,
#   deck_id TEXT,
#   lineup int,
#   user_id TEXT,
#   UNIQUE(season, deck_id, lineup, user_id) ON CONFLICT REPLACE
# );