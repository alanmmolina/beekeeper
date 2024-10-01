from ...core.use_cases.bee_management import BeeManagement

class NotebookAdapter:
    def __init__(self, use_case: BeeManagement) -> None:
        self.use_case = use_case

    def birth_bee(self, type: str, id: int, health: int = 100):
        self.use_case.birth_bee(type=type, id=id, health=health)

    def find_bee_by_id(self, id: int):
        return self.use_case.find_bee_by_id(id)

    def find_bees_by_type(self, type: str):
        return self.use_case.find_bees_by_type(type)

    def update_bee_health(self, id: int, health: int):
        self.use_case.update_bee_health(id, health)

    def kill_bee(self, id: int):
        self.use_case.kill_bee(id)
