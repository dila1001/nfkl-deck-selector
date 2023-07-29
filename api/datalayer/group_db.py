from sqlalchemy.orm import Session
from datalayer.schema.group import Group, GroupUser

def get_all_groups(db: Session):
    groups = db.query(Group).all()
    return groups

def get_groups_with_users(db: Session, season: str):
    groups_with_users = db.query(GroupUser).filter(GroupUser.season==season).all()
    return groups_with_users
