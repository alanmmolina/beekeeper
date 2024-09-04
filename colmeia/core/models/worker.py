from bee import Bee

class Worker(Bee):
    def __init__(self, id: str, health: int):
        super().__init__(id, health)