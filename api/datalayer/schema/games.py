from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from datalayer.database import Base

class Game(Base):
    __tablename__ = "game"

    game_id = Column(String, primary_key=True)
    game_name = Column(String)
    season = Column(String)
    player1_id = Column(String, ForeignKey("user.id"))
    player1 = relationship("User", primaryjoin="Game.player1_id==User.id")
    player2_id = Column(String, ForeignKey("user.id"), nullable=True)
    player2 = relationship("User", primaryjoin="Game.player2_id==User.id")
    game_created = Column(Integer)
    game_updated = Column(Integer, nullable=True)
    game_finished = Column(Integer, nullable=True)

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

    game_id = Column(String)
    round_id = Column(Integer)
    round_type = Column(String)
    user_id = Column(String)
    deck_id = Column(Integer)
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

    game_id = Column(String)
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

class GameDeck(Base):
    __tablename__ = "gameDeck"

    game_id = Column(String)
    user_id = Column(String)
    deck_id = Column(String)

    __table_args__ = (
        PrimaryKeyConstraint(game_id, deck_id, user_id),
        {}
    )

# CREATE TABLE gameDeck(
#   game_id TEXT NOT NULL,
#   user_id TEXT NOT NULL,
#   deck_id TEXT NOT NULL,
#   UNIQUE(game_id, deck_id, user_id) ON CONFLICT IGNORE
# );
