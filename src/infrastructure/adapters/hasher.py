from domain.user_auth.interfaces import PasswordHasher
from passlib.context import CryptContext


class BcryptPasswordHasher(PasswordHasher):
    def __init__(self, context: CryptContext):
        self._context = context

    def hash(self, raw_password: str) -> str:
        return self._context.hash(raw_password)

    def verify(self, raw_password: str, hashed_password: str) -> bool:
        return self._context.verify(raw_password, hashed_password)
