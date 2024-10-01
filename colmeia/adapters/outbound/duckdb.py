import duckdb
from typing import List, Optional, Callable
from functools import wraps

from ...core.models.bee import Bee
from ...core.models.worker import Worker
from ...core.models.queen import Queen
from ...core.models.drone import Drone


def with_connection(func: Callable):
    """Decorator to open and close a DuckDB connection around the execution of a function."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        connection = duckdb.connect(self.path)
        try:
            self.connection = connection
            result = func(self, *args, **kwargs)
        finally:
            connection.close()
        return result
    return wrapper

class DuckDBBeeAdapter:
    def __init__(self, path: str) -> None:
        self.path = path
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> None:
        connection = duckdb.connect(self.path)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS bees (
                id INTEGER PRIMARY KEY,
                type STRING,
                health INTEGER
            )
        """)
        connection.close()

    @with_connection
    def save(self, bee: Bee) -> None:
        self.connection.execute(
            "INSERT OR REPLACE INTO bees (id, type, health) VALUES (?, ?, ?)",
            (bee.id, bee.type, bee.health)
        )

    @with_connection
    def load_by_id(self, id: int) -> Optional[Bee]:
        result = self.connection.execute("SELECT id, type, health FROM bees WHERE id = ?", (id,)).fetchone()
        if result:
            return self._instantiate_bee(id=result[0], type=result[1], health=result[2])
        return None

    @with_connection
    def load_by_type(self, type: str) -> List[Bee]:
        results = self.connection.execute("SELECT id, type, health FROM bees WHERE type = ?", (type,)).fetchall()
        return [self._instantiate_bee(id=row[0], type=row[1], health=row[2]) for row in results]

    @with_connection
    def delete(self, id: int) -> None:
        self.connection.execute("DELETE FROM bees WHERE id = ?", (id,))

    def _instantiate_bee(self, id: int, type: str, health: int) -> Bee:
        if type == "worker":
            return Worker(id=id, health=health)
        if type == "queen":
            return Queen(id=id, health=health)
        if type == "drone":
            return Drone(id=id, health=health)
        raise ValueError(f"Unknown bee type: {type}")