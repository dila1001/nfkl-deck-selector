from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    discord: str
    tco: str
    email: str
    profile_pic: str
    approved_user: bool

    class Config:
        from_attributes = True