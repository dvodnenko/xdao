import uuid
from abc import ABC, abstractmethod

from domain.user.entity import User


class UserDAO(ABC):

    @abstractmethod
    def get_by_id(self, user_id: uuid.UUID) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    def save(self, user: User) -> None:
        raise NotImplementedError()

    @abstractmethod
    def exists_by_email(self, email: str) -> bool:
        raise NotImplementedError()
