import uuid

from dataclasses import dataclass


@dataclass(eq=False, kw_only=True)
class User:

    id: uuid.UUID
    name: str
    email: str

    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id
