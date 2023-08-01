from datalayer.database import get_db
import datalayer.database
from sqlalchemy.orm import Session
import datalayer.season_db
import datalayer.schema.seasons
from model.season import SeasonList, Season
from fastapi import HTTPException, status

async def get_all_seasons():
    db: Session = next(get_db())
    seasons = datalayer.season_db.get_all_seasons(db)
    return SeasonList(seasons=seasons)

async def set_season_active_status(active: bool, season: str):
    db: Session = next(get_db())
    db_season = datalayer.season_db.get_season(db,season=season)

    setattr(db_season, "is_active", active)
    db_season = datalayer.database.save(db, data=db_season)
    return Season.model_validate(db_season)

async def create_season(season: Season):
    db: Session = next(get_db())
    if __season_exist(season.season):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Season name must be unique')

    if not __valid_round_type_order(season.round_type_order):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Round_type_order is not valid. Must end with `end` and can only contain `ban`,`safe` or `game`')

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

    season = datalayer.database.save(db, data=season_db)

    return Season.model_validate(season)

def __season_exist(season: str):
    db: Session = next(get_db())
    season = datalayer.season_db.get_season(db, season=season)
    return season is not None

__valid_round_type = ['ban','safe','game']
def __valid_round_type_order(round_type_order: str):
    end_is_last = False
    for round_type in round_type_order.split(','):
        if end_is_last: return False

        if round_type.lower() in __valid_round_type: continue
        if round_type.lower() == 'end':
            end_is_last = True
            continue
        return False
    return end_is_last
