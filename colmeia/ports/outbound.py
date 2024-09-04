from abc import ABC, abstractmethod
from ..core.models.bee import Bee
from typing import List, Optional

class OutboundPort(ABC):
    @abstractmethod
    def save_bee(self, bee: Bee) -> None:
        pass

    @abstractmethod
    def get_bee_by_id(self, id: int) -> Optional[Bee]:
        pass

    @abstractmethod
    def get_bees_by_type(self, type: str) -> List[Bee]:
        pass

    @abstractmethod
    def delete_bee(self, id: int) -> None:
        pass