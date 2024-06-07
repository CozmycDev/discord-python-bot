import discord

from cogwatch import Watcher

import config_util

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    watcher = Watcher(bot, path='cogs', preload=True, debug=False)

    await watcher.start()  # Watches cogs for file changes and reloads them
    await bot.sync_commands()  # Syncs this bots slash commands with Discord

    print("--------------------------------------")
    print(f"Logged in as {bot.user} (v{config_util.GLOBAL_CONFIG.get('main.version')})")
    print("--------------------------------------")


config_util.load()  # Loads variables from .env and bot_config.json
bot.run(config_util.GLOBAL_CONFIG.get('DISCORD_TOKEN'))  # Logs the bot into Discord
