from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import redis

engine = create_engine('sqlite:///mydb.sqlite', echo=True)
SessionLocal = sessionmaker(bind=engine)

def get_sql_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_redis():

    return redis.Redis(
        host='localhost',
        port=6379,
        db=9,
    )
