from datalayer.database import get_db
import datalayer.database
from sqlalchemy.orm import Session
import datalayer.group_db
import datalayer.schema.group
from model.group import GroupList, GroupUser
from fastapi import HTTPException, status

async def groups():
    db: Session = next(get_db())
    groups = datalayer.group_db.get_all_groups(db)
    return GroupList(groups=groups)

async def get_group_user(season: str):
    db: Session = next(get_db())
    group_user = datalayer.group_db.get_groups_with_users(db, season=season)
    return GroupList(group_users=group_user)

async def add_user_to_group(group_name: str, season: str, user_id: str):
    db: Session = next(get_db())
    group:datalayer.schema.group.GroupUser = datalayer.group_db.get_group(db, group_name=group_name)
    if group is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='No group name {} found'.format(group_name))

    # Check if user already has a group for the season
    db_group_user:datalayer.schema.group.GroupUser = datalayer.group_db.get_group_user(db, user_id=user_id, season=season)
    if db_group_user is None:
        db_group_user = datalayer.schema.group.GroupUser(
            group_id=group.group_id,
            season=season,
            user_id=user_id
        )
    else:
        setattr(db_group_user, "season", season)
        setattr(db_group_user, "group_id",group.group_id)

    db_group_user = datalayer.database.save(db, data=db_group_user)
    return GroupUser.model_validate(db_group_user)
