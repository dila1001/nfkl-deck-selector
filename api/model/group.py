from pydantic import BaseModel
from model.user import User

class Group(BaseModel):
    name: str
    rank: int

    class Config:
        from_attributes = True

class GroupUser(BaseModel):
    group: Group
    season: str
    user: User

    class Config:
        from_attributes = True

class GroupList(BaseModel):
    group_users: list[GroupUser] | None = None
    groups: list[Group] | None = None

    class Config:
        from_attributes = True
