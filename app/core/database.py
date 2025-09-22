import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DATABASE_URL")


if not db_url:
    raise ValueError("❌ DATABASE_URL not found. Check your .env file!")

engine = create_engine(db_url, future=True,echo=True)
session = sessionmaker(autoflush=True,bind=engine)

base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

