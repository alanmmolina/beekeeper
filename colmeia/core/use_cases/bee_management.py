from loguru import logger
from typing import List, Optional

from ...ports.inbound import InboundPort
from ...ports.outbound import OutboundPort
from ...core.models.bee import Bee
from ...core.models.queen import Queen
from ...core.models.drone import Drone
from ...core.models.worker import Worker

class BeeManagement(InboundPort):
    def __init__(self, port: OutboundPort) -> None:
        self.port = port
        logger.add("logs/hive.log", rotation="1 MB")  

    def birth_bee(self, type: str, id: int, health: int = 100):
        bee: Optional[Bee] = None
        if type == "worker":
            bee = Worker(id=id, health=health)
        elif type == "queen":
            bee = Queen(id=id, health=health)
        elif type == "drone":
            bee = Drone(id=id, health=health)
        else:
            logger.error(f"Oops! Tried to birth an unknown bee species: {type}. Buzz off!")
            raise ValueError(f"Unknown bee type: {type}")

        self.port.save(bee)
        logger.success(f"A new baby {type.capitalize()} bee (ID {id}) has been born with {health}% health. Welcome to the hive!")
        print(bee)

    def find_bee_by_id(self, id: int) -> Optional[Bee]:
        bee = self.port.load_by_id(id)
        if bee:
            logger.info(f"Bee ID {id} found! It's a {bee.type}. Buzzing strong!")
        else:
            logger.error(f"No bee with ID {id} in the hive. Someone's gone missing!")
        return bee

    def find_bees_by_type(self, type: str) -> List[Bee]:
        bees = self.port.load_by_type(type)
        if bees:
            logger.info(f"{len(bees)} {type.capitalize()} bees found in the hive. Busy bees!")
        else:
            logger.error(f"No bees of type {type.capitalize()} found. Maybe they're out pollinating?")
        return bees

    def update_bee_health(self, id: int, health: int) -> None:
        bee = self.port.load_by_id(id)
        if bee:
            bee.health = health
            self.port.save(bee)
            logger.info(f"Bee ID {id} has been healed up to {health}% health. Ready to buzz again!")
            print(bee)
        else:
            logger.error(f"Bee with ID {id} not found! Can't fix what doesn't exist!")

    def kill_bee(self, id: int) -> None:
        self.port.delete(id)
        logger.info(f"Bee ID {id} has been removed from the hive. Rest in peace, little one.")