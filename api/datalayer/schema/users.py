from __future__ import annotations
from typing import List
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, PrimaryKeyConstraint
from sqlalchemy.orm import relationship, Mapped

from datalayer.database import Base

user_role_table = Table(
    "userrole",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("role_id", ForeignKey("role.role_id"), primary_key=True),
)

# CREATE TABLE userrole (
#   user_id TEXT NOT NULL,
#   role_id INT NOT NULL,
#   UNIQUE(user_id, role_id) ON CONFLICT IGNORE
# );

class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=False, index=False)
    discord = Column(String, unique=False, index=False, nullable=True)
    tco = Column(String, unique=False, index=False, nullable=True)
    email = Column(String, unique=True, index=True)
    profile_pic = Column(String, unique=False, index=False)
    approved_user = Column(Boolean, unique=False, index=True, default=False)
    roles:Mapped[List[Role]] = relationship(secondary=user_role_table)

# CREATE TABLE user (
#   id TEXT PRIMARY KEY,
#   name TEXT NOT NULL,
#   discord TEXT NULL,
#   tco TEXT NULL,
#   email TEXT UNIQUE NOT NULL,
#   profile_pic TEXT NOT NULL,
#   approved_user bit not null
# );


class Role(Base):
    __tablename__ = "role"

    role_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=False, nullable=True)

# CREATE TABLE role (
#   role_id INT PRIMARY KEY,
#   name TEXT NOT NULL,
#   UNIQUE(role_id, name) ON CONFLICT IGNORE
# );

class ArchivedUser(Base):
    __tablename__ = "archiveduser"

    user_id = Column(String, ForeignKey("user.id"))
    season = Column(String)
    user: Mapped["User"] = relationship()
    __table_args__ = (
        PrimaryKeyConstraint(season, user_id),
        {}
    )

# CREATE TABLE archiveduser (
#   user_id TEXT NOT null,
#   season TEXT NOT null,
#   UNIQUE(season, user_id) ON CONFLICT IGNORE
# );
