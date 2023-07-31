from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint, Table
from sqlalchemy.orm import relationship, Mapped
from datalayer.database import Base
from datalayer.schema.decks import Deck

game_deck_table = Table(
    "gameDeck",
    Base.metadata,
    Column("game_id", ForeignKey("game.game_id"), primary_key=True),
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("deck_id", ForeignKey("deck.deck_id"), primary_key=True),
    extend_existing=True,
)

class Game(Base):
    __tablename__ = "game"

    game_id = Column(String, primary_key=True)
    game_name = Column(String)
    season = Column(String)
    player1_id = Column(String, ForeignKey("user.id"))
    player1 = relationship("User", primaryjoin="Game.player1_id==User.id")
    # player1_decks = relationship("Deck", primaryjoin="and_(GameDeck.deck_id==Deck.deck_id, GameDeck.user_id==Game.player1_id)", secondary="GameDeck", secondaryjoin="and_(GameDeck.deck_id==Deck.deck_id, GameDeck.game_id==Game.game_id, GameDeck.user_id==Game.player1_id)")
    player2_id = Column(String, ForeignKey("user.id"), nullable=True)
    player2 = relationship("User", primaryjoin="Game.player2_id==User.id")
    # player2_decks = relationship("Deck", secondary="GameDeck", secondaryjoin="and_(GameDeck.deck_id==Deck.deck_id, GameDeck.game_id==Game.game_id, GameDeck.user_id==Game.player2_id)")
    game_created = Column(Integer)
    game_updated = Column(Integer, nullable=True)
    game_finished = Column(Integer, nullable=True)
    choices: Mapped[list["Choice"]] = relationship("Choice", primaryjoin="Game.game_id==Choice.game_id")
    scores: Mapped[list["Score"]] = relationship("Score", primaryjoin="Game.game_id==Score.game_id")
    decks: Mapped[list[Deck]] = relationship(secondary=game_deck_table)

# CREATE TABLE "game" (
#   game_id TEXT PRIMARY KEY,
#   game_name TEXT NOT NULL,
#   season TEXT,
#   player1_id TEXT NOT NULL,
#   player2_id TEXT,
#   game_created INT,
#   game_updated INT,
#   game_finished INT
# );

class Choice(Base):
    __tablename__ = "choice"

    game_id = Column(String, ForeignKey("game.game_id"))
    round_id = Column(Integer)
    round_type = Column(String)
    user_id = Column(String, ForeignKey("user.id"))
    # No need to resolve user since choice is always presented with Game class
    # user = relationship("User", primaryjoin="Choice.user_id==User.id")
    deck_id = Column(Integer, ForeignKey("deck.deck_id"), nullable=True)
    deck = relationship("Deck", primaryjoin="and_(Choice.deck_id==Deck.deck_id, Choice.user_id==Deck.user_id)")
    __table_args__ = (
        PrimaryKeyConstraint(game_id, round_id,user_id),
        {}
    )

# CREATE TABLE choice (
#   game_id TEXT NOT NULL,
#   round_id INT NOT NULL,
#   round_type TEXT NOT NULL,
#   user_id TEXT NOT NULL,
#   deck_id INT NOT NULL,
#   UNIQUE(game_id, round_id, user_id) ON CONFLICT IGNORE
# );

class Score(Base):
    __tablename__ = "score"

    game_id = Column(String, ForeignKey("game.game_id"))
    round_id = Column(Integer)
    player1_keys = Column(Integer, nullable=True)
    player2_keys = Column(Integer, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint(game_id, round_id),
        {}
    )

# CREATE TABLE score (
#   game_id TEXT NOT null,
#   round_id INT NOT NULL,
#   player1_keys INT,
#   player2_keys INT,
#   UNIQUE(game_id, round_id) ON CONFLICT IGNORE
# );

# class GameDeck(Base):
#     __tablename__ = "gameDeck"

#     game_id = Column(String, ForeignKey("game.game_id"))
#     user_id = Column(String, ForeignKey("user"))
#     deck_id = Column(String, ForeignKey("deck.deck_id"))

#     __table_args__ = (
#         PrimaryKeyConstraint(game_id, deck_id, user_id),
#         {}
#     )

# CREATE TABLE gameDeck(
#   game_id TEXT NOT NULL,
#   user_id TEXT NOT NULL,
#   deck_id TEXT NOT NULL,
#   UNIQUE(game_id, deck_id, user_id) ON CONFLICT IGNORE
# );
