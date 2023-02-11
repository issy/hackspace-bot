import config
from disnake.ext import commands
from utils import get_logger


logger = get_logger(__name__)
startup_extensions = ("hackspace_role",)
if config.DEBUG:
    bot = commands.AutoShardedInteractionBot(
        test_guilds=[662107547972534302],
        sync_commands_debug=True,
        reload=True,
    )
else:
    bot = commands.AutoShardedInteractionBot()


def load_cogs():
    for extension in startup_extensions:
        try:
            bot.load_extension(f"cogs.{extension}")
            logger.info(f"loaded: {extension}")
        except Exception as error:
            logger.error(f"failed to load: {extension}", exc_info=error)


if __name__ == "__main__":
    load_cogs()
    bot.run(config.DISCORD_TOKEN)
