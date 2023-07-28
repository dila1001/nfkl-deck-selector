from datalayer.database import get_db
from sqlalchemy.orm import Session
import datalayer.user_db
from model.user import UserList

async def users(page_number: int=0, page_size: int=100):
    db: Session = next(get_db())
    skip = page_number * page_size
    (users, count) = datalayer.user_db.get_users(db, skip=skip, limit=page_size)
    return UserList(users=users, total=count)
