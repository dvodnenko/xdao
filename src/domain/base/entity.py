import uuid

from dataclasses import dataclass, field


@dataclass(eq=False, kw_only=True)
class Entity:

    id: uuid.UUID = field(init=False, default_factory=uuid.uuid4)

    def __eq__(self, other):
        return isinstance(other, Entity) and self.id == other.id
