import uuid
from dataclasses import dataclass, field


@dataclass(eq=False, kw_only=True)
class User:

    id: uuid.UUID
    email: str
    name: str
    phone: str
    password_hash: str
    is_active: bool = field(default=True)
    is_admin: bool = field(default=False)

    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id
