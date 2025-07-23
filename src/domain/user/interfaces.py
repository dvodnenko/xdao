from abc import ABC, abstractmethod
from domain.user.models import User


class UserDAO(ABC):

    @abstractmethod
    def get_by_id(self, user_id: int) -> User | None: ...

    @abstractmethod
    def save(self, user: User) -> None: ...

    @abstractmethod
    def exists_by_email(self, email: str) -> bool: ...
