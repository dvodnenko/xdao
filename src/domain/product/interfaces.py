import uuid
from abc import ABC, abstractmethod

from domain.product.entity import Product


class ProductDAO(ABC):

    @abstractmethod
    def get_by_id(self, product_id: uuid.UUID) -> Product | None:
        raise NotImplementedError()
    
    @abstractmethod
    def save(self, product: Product) -> None:
        raise NotImplementedError()
