import uuid
from dataclasses import dataclass, field
from datetime import datetime

from domain.product.enums import CategoryEnum, EnumSizesClothes, EnumSizesShoes


@dataclass(eq=False, kw_only=True)
class Product:
    title: str
    brand: str
    description: str
    category: CategoryEnum
    type: str
    size: EnumSizesClothes | EnumSizesShoes
    color: str
    material: str
    photo_url: str
    price: float
    quantity_store: int
    state: bool
    is_available: bool
    slug: str
    parsed_from: str
    created_at: datetime
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __eq__(self, other):
        return isinstance(other, Product) and self.id == other.id
