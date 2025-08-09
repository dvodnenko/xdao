import uuid
from abc import ABC, abstractmethod

from domain.cart.entity import Cart


class CartDAO(ABC):

    @abstractmethod
    def get_by_id(self, cart_id: uuid.UUID) -> Cart | None:
        raise NotImplementedError()
    
    @abstractmethod
    def save(self, cart: Cart) -> None:
        raise NotImplementedError()
