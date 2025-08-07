from abc import ABC, abstractmethod


class PasswordHasher(ABC):
    
    @abstractmethod
    def hash(self, raw_password: str) -> str: ...

    @abstractmethod
    def verify_password(self, raw_password: str, hashed_password: str) -> bool: ...
