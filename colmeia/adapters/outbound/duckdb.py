import duckdb
from ...core.models.bee import Bee
from typing import List, Optional

class DuckDBBeeAdapter:
    def __init__(self, database_path: str) -> None:
        self.conn = duckdb.connect(database_path)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS bees (
                id INTEGER PRIMARY KEY,
                type STRING,
                health INTEGER
            )
        """)

    def save(self, bee: Bee) -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO bees (id, type, health) VALUES (?, ?, ?)",
            (bee.id, bee.type, bee.health)
        )

    def load_by_id(self, bee_id: int) -> Optional[Bee]:
        result = self.conn.execute("SELECT id, type, health FROM bees WHERE id = ?", (bee_id,)).fetchone()
        if result:
            return Bee(id=result[0], type=result[1], health=result[2])
        return None

    def load_by_type(self, bee_type: str) -> List[Bee]:
        results = self.conn.execute("SELECT id, type, health FROM bees WHERE type = ?", (bee_type,)).fetchall()
        return [Bee(id=row[0], type=row[1], health=row[2]) for row in results]

    def delete(self, bee_id: int) -> None:
        self.conn.execute("DELETE FROM bees WHERE id = ?", (bee_id,))