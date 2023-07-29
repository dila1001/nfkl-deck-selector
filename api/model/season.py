from pydantic import BaseModel

class SeasonType(BaseModel):
    season_type: str
#    season_type_id: int

    class Config:
        from_attributes = True

class Season(BaseModel):
    season: str
    # season_type_id: int
    season_type: SeasonType
    round_type_order: str
    decks_required: int
    is_active: bool
    lineups: int
    start_date: int | None
    end_date: int | None

    class Config:
        from_attributes = True

class SeasonList(BaseModel):
    seasons: list[Season] | None

    class Config:
        from_attributes = True
