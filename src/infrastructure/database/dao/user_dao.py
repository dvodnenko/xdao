import uuid, redis
from sqlalchemy.orm import Session
from redis.commands.search.query import Query
from redis.commands.json.path import Path

from domain.user.interfaces import UserDAO
from domain.user.models import User
from infrastructure.database.models.user_model import UserORM


class SQLAlchemyUserDAO(UserDAO):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id: uuid.UUID) -> User | None:
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


class RedisUserDAO(UserDAO):

    def __init__(self, redis: redis.Redis):
        self.redis = redis

    def get_by_id(self, user_id: uuid.UUID):
        obj = self.redis.json().get(f'user:{user_id}')
        if not obj:
            return None
        return User(id=obj.get('id'), name=obj.get('name'), email=obj.get('email'))

    def save(self, user: User):

        user_json = {
            'id': str(user.id),
            'name': user.name,
            'email': user.email
        }
        with self.redis.pipeline(True) as pipe:
            pipe.json().set(f'user:{user.id}', Path.root_path(), user_json)
            pipe.execute(True)

    def exists_by_email(self, email: str) -> bool:
        query = Query(f'@email:"{email}"')
        result = self.redis.ft('user_idx').search(query)

        print(result)

        return result.total > 0
