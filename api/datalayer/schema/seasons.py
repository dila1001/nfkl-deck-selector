from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, relationship
from datalayer.database import Base

class SeasonType(Base):
    __tablename__ = "seasonType"

    season_type_id = Column(Integer, primary_key=True)
    season_type = Column(String)

# CREATE TABLE seasonType (
#   season_type_id INT NOT null,
#   season_type TEXT NOT null,
#   UNIQUE(season_type) ON CONFLICT IGNORE
# );

class Season(Base):
    __tablename__ = "season"

    season = Column(String, primary_key=True)
    season_type_id = Column(Integer, ForeignKey("seasonType.season_type_id"))
    season_type: Mapped["SeasonType"] = relationship()
    round_type_order = Column(String)
    decks_required = Column(Integer)
    is_active = Column(Boolean)
    lineups = Column(Integer)
    start_date = Column(Integer)
    end_date = Column(Integer)


# CREATE TABLE "season" (
#   season TEXT NOT null,
#   season_type_id INT NOT null,
#   round_type_order TEXT NOT null,
#   decks_required INT NOT null,
#   is_active INT NOT null,
#   lineups INT,
#   [start_date] INT,
#   [end_date] INT,
#   UNIQUE(season) ON CONFLICT IGNORE
# );