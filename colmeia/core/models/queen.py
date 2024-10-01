from .bee import Bee

class Queen(Bee):
    def __init__(self, id: str, health: int = 100):
        super().__init__(id, health)