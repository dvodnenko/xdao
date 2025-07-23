from domain.user.interfaces import UserDAO
from domain.user.models import User

from infrastructure.database.models.user_model import UserORM


class SQLAlchemyUserDAO(UserDAO):
    def __init__(self, session):
        self.session = session

    def get_by_id(self, user_id: int) -> User | None:
        obj = self.session.query(UserORM).get(user_id)
        if not obj:
            return None
        return User(id=obj.id, name=obj.name, email=obj.email)

    def save(self, user: User) -> None:
        orm_obj = UserORM(id=user.id, name=user.name, email=user.email)
        self.session.merge(orm_obj)
        self.session.commit()

    def exists_by_email(self, email: str) -> bool:
        return self.session.query(UserORM).filter_by(email=email).first() is not None
