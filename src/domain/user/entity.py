import uuid
from dataclasses import dataclass

from domain.base.entity import Entity


@dataclass(eq=False, kw_only=True)
class User(Entity):

    name: str
    email: str

    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id
