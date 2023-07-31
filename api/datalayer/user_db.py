from sqlalchemy.orm import Session
from datalayer.schema.users import User, ArchivedUser

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    users = db.query(User).offset(skip).limit(limit).all()
    count = db.query(User).count()
    return (users, count)

def get_archived_users(db: Session, season: str, skip: int = 0, limit: int = 100):
    archived_users = db.query(ArchivedUser).filter(ArchivedUser.season == season).offset(skip).limit(limit).all()
    count = db.query(ArchivedUser).filter(ArchivedUser.season == season).count()
    return (archived_users, count)

def save_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
