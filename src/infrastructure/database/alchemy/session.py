from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import SQLITE_URI


engine = create_engine(SQLITE_URI, echo=True)
SessionLocal = sessionmaker(bind=engine)


def get_sql_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
