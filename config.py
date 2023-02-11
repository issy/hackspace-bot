from typing import Optional

from environs import Env

env = Env()
env.read_env()

DISCORD_TOKEN: Optional[str] = env("DISCORD_TOKEN")
DEBUG: bool = env.bool("DEBUG", False)
POSTGRES_URI: Optional[str] = env("POSTGRES_URI")
