from datalayer.database import get_db
from sqlalchemy.orm import Session
import datalayer.season_db
import datalayer.schema.seasons
from model.season import SeasonList, Season

async def get_all_seasons():
    db: Session = next(get_db())
    seasons = datalayer.season_db.get_all_seasons(db)
    return SeasonList(seasons=seasons)

async def create_season(season: Season):
    db: Session = next(get_db())
    if __season_exist(season.season): return None

    season_db = datalayer.schema.seasons.Season(
        season=season.season,
        season_type_id=season.season_type.season_type_id,
        round_type_order=season.round_type_order,
        decks_required=season.decks_required,
        is_active=season.is_active,
        lineups=season.lineups,
        start_date=season.start_date,
        end_date=0
    )

    season = datalayer.season_db.save_season(db, season=season_db)

    return Season.model_validate(season)

def __season_exist(season: str):
    db: Session = next(get_db())
    season = datalayer.season_db.get_season(db, season=season)
    return season is not None