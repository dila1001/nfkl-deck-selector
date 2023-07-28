from pydantic import BaseModel

class Role(BaseModel):
    name: str
    class Config:
        from_attributes = True

class User(BaseModel):
    id: int
    name: str
    discord: str | None
    tco: str | None
    email: str
    profile_pic: str
    approved_user: bool
    roles: list[Role] = []

    class Config:
        from_attributes = True

class UserList(BaseModel):
    users: list[User]
    total: int

    class Config:
        from_attributes = True