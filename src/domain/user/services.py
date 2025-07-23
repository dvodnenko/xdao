import uuid

from domain.user.models import User
from domain.user.interfaces import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def register_user(self, name: str, email: str) -> User:
        if self.dao.exists_by_email(email):
            raise ValueError('Email already registered')

        new_user = User(id=uuid.uuid4(), name=name, email=email)
        self.dao.save(new_user)
        return new_user

    def get_profile(self, user_id: uuid.UUID) -> User:
        user = self.dao.get_by_id(user_id)
        if not user:
            raise ValueError('User not found')
        return user
