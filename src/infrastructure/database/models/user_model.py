from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class UserORM(Base):
    __tablename__ = 'users'
    id = Column(UUID, primary_key=True)
    name = Column(String)
    email = Column(String)
