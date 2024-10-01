import typer
from ...core.use_cases.bee_management import BeeManagement

class CLIAdapter:
    def __init__(self, use_case: BeeManagement) -> None:
        self.use_case = use_case
        self.app = typer.Typer()

        # Register CLI commands with Typer
        self.app.command()(self.birth_bee)
        self.app.command()(self.update_bee_health)
        self.app.command()(self.kill_bee)
        self.app.command()(self.find_bee_by_id)
        self.app.command()(self.find_bees_by_type)

    def birth_bee(self, type: str, id: int):
        """
        Birth a new bee into the hive.
        
        Parameters:
        - type: The type of bee (worker, queen, or drone).
        - id: The unique ID for the new bee.

        Usage:
        birth_bee --type worker --id 1
        
        A healthy new bee joins the hive!
        """
        self.use_case.birth_bee(type=type, id=id)

    def update_bee_health(self, id: int, health: int):
        """
        Nurse a bee back to full health.
        
        Parameters:
        - id: The ID of the bee to heal.
        - health: The new health value for the bee.

        Usage:
        update_bee_health --id 1 --health 80
        
        This command restores a bee's health to the desired value. Let's get that buzz back!
        """
        self.use_case.update_bee_health(id, health)

    def kill_bee(self, id: int):
        """
        Remove a bee from the hive.
        
        Parameters:
        - id: The ID of the bee to be... removed. 

        Usage:
        kill_bee --id 1
        
        Sadly, all bees must return to the earth eventually. This command handles it.
        """
        self.use_case.kill_bee(id)

    def find_bee_by_id(self, id: int):
        """
        Locate a bee by its ID.
        
        Parameters:
        - id: The ID of the bee to find.

        Usage:
        find_bee_by_id --id 1
        
        This command helps you find a specific bee in the hive based on its unique ID. Busy bee, where are you?
        """
        return self.use_case.find_bee_by_id(id)

    def find_bees_by_type(self, type: str):
        """
        Get a list of all bees of a certain type.
        
        Parameters:
        - type: The type of bee (worker, queen, or drone) to search for.

        Usage:
        find-bees-by-type worker
        
        Whether you're looking for workers, queens, or drones, this command finds all the buzzing bees of that type.
        """
        return self.use_case.find_bees_by_type(type)

    def run(self):
        """
        Run the CLI application.
        
        This method starts the Typer CLI app, enabling all the commands defined above.
        Use this to interact with the bee hive from the command line.
        """
        self.app()