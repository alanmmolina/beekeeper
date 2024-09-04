from abc import ABC, abstractmethod
from ..core.models.bee import Bee
from typing import List, Optional

class InboundPort(ABC):
    @abstractmethod
    def create_bee(self, bee: Bee) -> None:
        pass

    @abstractmethod
    def read_bee_by_id(self, id: int) -> Optional[Bee]:
        pass

    @abstractmethod
    def read_bees_by_type(self, type: str) -> List[Bee]:
        pass

    @abstractmethod
    def update_bee_health(self, id: int, health: int) -> None:
        pass

    @abstractmethod
    def delete_bee(self, id: int) -> None:
        pass