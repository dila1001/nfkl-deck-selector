from sqlalchemy import and_
from sqlalchemy.orm import Session
from datalayer.schema.group import Group, GroupUser

def get_all_groups(db: Session):
    groups = db.query(Group).all()
    return groups

def get_groups_with_users(db: Session, season: str):
    groups_with_users = db.query(GroupUser).filter(GroupUser.season==season).all()
    return groups_with_users

def get_group(db: Session, group_name: str):
    group = db.query(Group).filter(Group.name==group_name).first()
    return group

def get_group_user(db: Session, user_id: str, season: str):
    group_user = db.query(GroupUser).filter(and_(GroupUser.user_id==user_id, GroupUser.season==season)).first()
    return group_user
