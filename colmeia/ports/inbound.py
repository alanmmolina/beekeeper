from abc import ABC, abstractmethod
from ..core.models.bee import Bee
from typing import List, Optional

class InboundPort(ABC):
    @abstractmethod
    def birth_bee(self, bee: Bee) -> None:
        pass

    @abstractmethod
    def find_bee_by_id(self, id: int) -> Optional[Bee]:
        pass

    @abstractmethod
    def find_bees_by_type(self, type: str) -> List[Bee]:
        pass

    @abstractmethod
    def update_bee_health(self, id: int, health: int) -> None:
        pass

    @abstractmethod
    def kill_bee(self, id: int) -> None:
        pass