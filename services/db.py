import random
import string
from typing import Optional

import asyncpg

import config


class DatabaseService:
    _connection: asyncpg.Connection

    def __init__(self, connection: asyncpg.Connection):
        self._connection = connection

    @classmethod
    async def init(cls):
        return cls(await asyncpg.connect(config.POSTGRES_URI))

    @staticmethod
    def generate_code(*, length: int = 5) -> str:
        return "".join(random.choice(string.ascii_uppercase) * length)

    async def add_role_mapping(self, role_id: int) -> str:
        code_exists = True
        async with self._connection.transaction():
            while code_exists:
                code = self.generate_code()
                code_exists = await self._connection.fetchval("SELECT 1 FROM hackspace_role WHERE code = $1", code)

            await self._connection.execute("INSERT INTO hackspace_role (code, role_id) VALUES($1, $2)", code, str(role_id))

        return code

    async def get_role_id(self, code: str) -> Optional[int]:
        role_id: Optional[str] = await self._connection.fetchval("SELECT role_id FROM hackspace_role WHERE code = $1", code)
        if role_id is not None:
            return int(role_id)
