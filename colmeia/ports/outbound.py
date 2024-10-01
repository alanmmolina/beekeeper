from abc import ABC, abstractmethod
from ..core.models.bee import Bee
from typing import List, Optional

class OutboundPort(ABC):
    @abstractmethod
    def save(self, bee: Bee) -> None:
        pass

    @abstractmethod
    def load_by_id(self, id: int) -> Optional[Bee]:
        pass

    @abstractmethod
    def load_by_type(self, type: str) -> List[Bee]:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass