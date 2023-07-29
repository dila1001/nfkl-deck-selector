from datalayer.database import get_db
from sqlalchemy.orm import Session
import datalayer.user_db
from model.user import UserList
from datalayer.schema.users import ArchivedUser

async def users(page_number: int=0, page_size: int=100):
    db: Session = next(get_db())
    skip = page_number * page_size
    (users, count) = datalayer.user_db.get_users(db, skip=skip, limit=page_size)
    return UserList(users=users, total=count)

async def get_archived_users(season: str, page_number: int=0, page_size: int=100):
    db: Session = next(get_db())
    skip = page_number * page_size
    (archived_users, count) = datalayer.user_db.get_archived_users(db, season=season, skip=skip, limit=page_size)
    get_users = lambda archived_users: (au.user for au in archived_users)
    return UserList(users=get_users(archived_users), total=count)
