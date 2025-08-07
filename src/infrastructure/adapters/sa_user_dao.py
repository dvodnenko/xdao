import uuid
from sqlalchemy.orm import Session
from sqlalchemy import select

from domain import *


class SQLAlchemyUserDAO(UserDAO):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id: uuid.UUID) -> User | None:
        obj: User | None = self.session.get(User, user_id)
        if not obj:
            return None
        return User(id=obj.id, name=obj.name, email=obj.email)

    def save(self, user: User) -> None:
        orm_obj = User(id=user.id, name=user.name, email=user.email)
        self.session.add(orm_obj)
        self.session.commit()

    def exists_by_email(self, email: str) -> bool:
        query = select(User).where(User.email==email)
        result = self.session.execute(query)

        obj = result.first()
        print(f'\n\n{obj}\n\n')

        return obj is not None
