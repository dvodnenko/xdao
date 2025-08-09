import uuid
from dataclasses import dataclass, field
from typing import List

from domain.cart_item.entity import CartItem


@dataclass(eq=False, kw_only=True)
class Cart:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    user_id: uuid.UUID
    items: List[CartItem] = field(default_factory=list)

    def __eq__(self, other):
        return isinstance(other, Cart) and self.id == other.id

    @property
    def total_price(self) -> float:
        total = .0
        for item in self.items:
            total += item.product.price * item.quantity
        return total
