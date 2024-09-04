class Bee:
    def __init__(self, id: int, health: int = 100):
        self.id = id
        self.health = health

    @property
    def type(self):
        return self.__class__.__name__.lower()

    def __repr__(self):
        return f"{self.type.capitalize()}(ID={self.id}, Health={self.health})"
