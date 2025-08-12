import uuid
from dataclasses import dataclass

from domain.user.entity import User
from domain.user.interfaces import UserDAO
from domain.user_auth.interfaces import PasswordHasher


@dataclass(frozen=True, kw_only=True)
class CreateUserRequest:
    
    name: str
    email: str
    phone: str
    password: str # it arrives not hashed
    is_active: bool
    is_admin: bool


class UserService:
    def __init__(self, dao: UserDAO, hasher: PasswordHasher):
        self.dao = dao
        self.hasher = hasher

    def register_user(self, user: CreateUserRequest) -> User:
        if self.dao.exists_by_email(user.email):
            raise ValueError('Email already registered')
        
        hashed_password = self.hasher.hash(user.password)

        new_user = User(
            email=user.email,
            name=user.name,
            phone=user.phone,
            password_hash=hashed_password,
            is_active=user.is_active,
        )
        self.dao.save(new_user)
        return new_user

    def get_profile(self, user_id: uuid.UUID) -> User:
        user = self.dao.get_by_id(user_id)
        if not user:
            raise ValueError('User not found')
        return user
