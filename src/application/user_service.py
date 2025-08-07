import uuid

from domain.user.entity import User
from domain.user.interfaces import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def register_user(self, user: User) -> User:
        if self.dao.exists_by_email(user.email):
            raise ValueError('Email already registered')

        new_user = User(name=user.name, email=user.email)
        self.dao.save(new_user)
        return new_user

    def get_profile(self, user_id: uuid.UUID) -> User:
        user = self.dao.get_by_id(user_id)
        if not user:
            raise ValueError('User not found')
        return user
