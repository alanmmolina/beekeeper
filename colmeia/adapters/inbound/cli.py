import argparse
from ...core.models.bee import Bee
from ...core.models.worker import Worker
from ...core.models.queen import Queen
from ...core.models.drone import Drone
from ...core.use_cases.bee_management import ManageBeeUseCase
from typing import Optional

class CLIAdapter:
    def __init__(self, use_case: ManageBeeUseCase) -> None:
        self.use_case = use_case

    def run(self) -> None:
        parser = argparse.ArgumentParser(description="Beehive Manager CLI")
        parser.add_argument('--create', type=str, help='Create a new bee: worker, queen, or drone')
        parser.add_argument('--id', type=int, help='Bee ID for operations like read, update, delete')
        parser.add_argument('--type', type=str, help='Bee type: worker, queen, drone')
        parser.add_argument('--health', type=int, help='Update health of the bee')
        parser.add_argument('--delete', action='store_true', help='Delete a bee')

        args = parser.parse_args()

        if args.create:
            bee: Optional[Bee] = None
            if args.create == 'worker':
                bee = Worker(id=args.id)
            elif args.create == 'queen':
                bee = Queen(id=args.id)
            elif args.create == 'drone':
                bee = Drone(id=args.id)
            if bee:
                self.use_case.create_bee(bee)

        if args.id and args.health:
            self.use_case.update_bee_health(bee_id=args.id, new_health=args.health)

        if args.id and args.delete:
            self.use_case.delete_bee(bee_id=args.id)

        if args.id and not args.delete and not args.health:
            bee = self.use_case.read_bee_by_id(bee_id=args.id)
            print(bee)

        if args.type and not args.id:
            bees = self.use_case.read_bees_by_type(bee_type=args.type)
            for bee in bees:
                print(bee)