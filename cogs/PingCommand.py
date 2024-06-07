import discord

from discord.commands import slash_command
from discord.ext import commands


class PingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='ping', description='Example slash command.')
    async def ping_command(
        self,
        ctx: discord.ApplicationContext
    ):
        await ctx.defer(ephemeral=True)
        await ctx.followup.send(content=f"Pong!", ephemeral=True)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(PingCommand(bot))
