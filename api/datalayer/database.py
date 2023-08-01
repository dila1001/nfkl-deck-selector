from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

load_dotenv()
__SQL_DB_PATH = os.environ.get("SQL_DB_PATH", None)

SQLALCHEMY_DATABASE_URL = "sqlite:///" + __SQL_DB_PATH

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def delete(db: Session, data: object):
    db.delete(data)
    db.commit()

def save(db: Session, data: object):
    db.add(data)
    db.commit()
    db.refresh(data)
    return data
