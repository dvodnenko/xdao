import uuid
from dataclasses import dataclass, field

from domain.product.entity import Product


@dataclass(eq=False, kw_only=True)
class CartItem:

    product: Product
    quantity: int
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __eq__(self, other):
        return isinstance(other, CartItem) and self.id == other.id
