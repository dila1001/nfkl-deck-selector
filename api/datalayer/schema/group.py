from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from datalayer.database import Base

class Group(Base):
    __tablename__ = "group"

    group_id = Column(String, primary_key=True)
    name = Column(String)
    rank = Column(Integer)

# CREATE TABLE "group" (
#   group_id TEXT NOT null,
#   [name] TEXT not null,
#   rank INT not null,
#   UNIQUE(group_id, [name]) ON CONFLICT IGNORE
# );

class GroupUser(Base):
    __tablename__ = "groupUser"

    group_id = Column(String, ForeignKey("group.group_id"))
    group = relationship("Group", primaryjoin="GroupUser.group_id==Group.group_id")
    season = Column(String)
    user_id = Column(String, ForeignKey("user.id"))
    user = relationship("User", primaryjoin="GroupUser.user_id==User.id")
    __table_args__ = (
        PrimaryKeyConstraint(season, user_id),
        {}
    )

# CREATE TABLE groupuser (
#   group_id TEXT NOT null,
#   season TEXT NOT null,
#   user_id TEXT NOT null,
#   UNIQUE(season, user_id) ON CONFLICT IGNORE
# );
