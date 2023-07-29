from datalayer.database import get_db
from sqlalchemy.orm import Session
import datalayer.group_db
from model.group import GroupList

async def groups():
    db: Session = next(get_db())
    groups = datalayer.group_db.get_all_groups(db)
    return GroupList(groups=groups)

async def get_group_user(season: str):
    db: Session = next(get_db())
    group_user = datalayer.group_db.get_groups_with_users(db, season=season)
    return GroupList(group_users=group_user)
