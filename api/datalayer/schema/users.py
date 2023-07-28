from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from datalayer.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=False, index=False)
    discord = Column(String, unique=False, index=False, nullable=True)
    tco = Column(String, unique=False, index=False, nullable=True)
    email = Column(String, unique=True, index=True)
    profile_pic = Column(String, unique=False, index=False)
    approved_user = Column(Boolean, unique=False, index=True, default=False)

# CREATE TABLE user (
#   id TEXT PRIMARY KEY,
#   name TEXT NOT NULL,
#   discord TEXT NULL,
#   tco TEXT NULL,
#   email TEXT UNIQUE NOT NULL,
#   profile_pic TEXT NOT NULL,
#   approved_user bit not null
# );
