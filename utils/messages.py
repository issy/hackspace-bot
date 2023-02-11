from typing import Optional

import disnake


async def error_message(
    inter: disnake.Interaction,
    error_message: str,
    *,
    title: str = "Error",
    ephemeral: bool = True
):
    await inter.send(
        ephemeral=ephemeral,
        embed=disnake.Embed(
            colour=disnake.Colour.red(),
            title=title,
            description=error_message
        )
    )


async def success_message(
    inter: disnake.Interaction,
    message: str,
    *,
    title: str = Optional[str],
    ephemeral: bool = True,
    colour: disnake.Colour = disnake.Colour.green()
):
    await inter.send(
        ephemeral=ephemeral,
        embed=disnake.Embed(
            colour=colour,
            title=title or disnake.Embed.Empty,
            description=message
        )
    )
