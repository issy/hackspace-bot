from typing import Optional

import disnake
from disnake.ext import commands, tasks

from services.db import DatabaseService
from utils import error_message, success_message


class MyCog(commands.Cog):
    database: Optional[DatabaseService]

    def __init__(self):
        self.database = None
        self.init_dependencies.start()

    @tasks.loop()
    async def init_dependencies(self):
        self.database = await DatabaseService.init()
        self.init_dependencies.stop()

    @commands.slash_command(dm_permission=False)
    async def hackspace(self, inter: disnake.ApplicationCommandInteraction, hackspace_code: str):
        """
        Join a hackspace channel using the unique 5 character code for that hackspace
        """
        role_id = await self.database.get_role_id(hackspace_code)
        if role_id is None:
            return await error_message(inter, "Invalid code")

        role = inter.guild.get_role(role_id)
        if role is None:
            return await error_message(inter, "Role does not exist")

        try:
            await inter.user.add_roles(role, reason="From hackspace command")
            await success_message(inter, title="Added role", message=f"Added the {role.mention} role")
        except disnake.Forbidden:
            await error_message(inter, "The bot is missing the relevant permissions to add this role")
        except disnake.HTTPException:
            await error_message(inter, f"HTTP exception occurred when trying to add the {role.mention} role")


def setup(bot: commands.Bot):
    bot.add_cog(MyCog())
