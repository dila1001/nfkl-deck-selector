from datalayer.database import get_db
from sqlalchemy.orm import Session
import datalayer.user_db
from model.user import UserList, User
import datalayer.schema.users

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

async def get_user(user_id: str):
    db: Session = next(get_db())
    user = datalayer.user_db.get_user(db, user_id=user_id)
    return None if user is None else User.model_validate(user)

async def create_user(user: User):
    db: Session = next(get_db())
    db_user = datalayer.schema.users.User(
            id=user.id,
            name=user.name,
            email=user.email,
            profile_pic=user.profile_pic,
            approved_user=user.approved_user,
            discord=user.discord,
            tco=user.tco,
        )
    new_user = datalayer.user_db.create_user(db, user=db_user)
    return User.model_validate(new_user)
