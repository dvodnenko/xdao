from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///mydb.sqlite', echo=True)
SessionLocal = sessionmaker(bind=engine)


def get_sql_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
