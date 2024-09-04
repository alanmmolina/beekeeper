# core/use_cases/manage_bee.py

import logging
from ...ports.inbound import InboundPort
from ...ports.outbound import OutboundPort
from ...core.models.bee import Bee
from typing import List, Optional

class BeeManagement(InboundPort):
    def __init__(self, bee_gateway: OutboundPort) -> None:
        self.bee_gateway = bee_gateway
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def create_bee(self, bee: Bee) -> None:
        self.bee_gateway.save_bee(bee)
        self.logger.info(f"Bee created: {bee.id} of type {bee.type}.")

    def read_bee_by_id(self, bee_id: int) -> Optional[Bee]:
        bee = self.bee_gateway.get_bee_by_id(bee_id)
        if bee:
            self.logger.info(f"Bee retrieved: {bee.id} of type {bee.type}.")
        else:
            self.logger.warning(f"Bee with ID {bee_id} not found.")
        return bee

    def read_bees_by_type(self, bee_type: str) -> List[Bee]:
        bees = self.bee_gateway.get_bees_by_type(bee_type)
        self.logger.info(f"{len(bees)} bees of type {bee_type} retrieved.")
        return bees

    def update_bee_health(self, bee_id: int, new_health: int) -> None:
        bee = self.bee_gateway.get_bee_by_id(bee_id)
        if bee:
            bee.health = new_health
            self.bee_gateway.save_bee(bee)
            self.logger.info(f"Bee ID {bee_id} health updated to {new_health}.")
        else:
            self.logger.warning(f"Bee with ID {bee_id} not found.")

    def delete_bee(self, bee_id: int) -> None:
        self.bee_gateway.delete_bee(bee_id)
        self.logger.info(f"Bee ID {bee_id} deleted.")