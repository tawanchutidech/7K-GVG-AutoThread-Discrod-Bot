import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
GVG_CHANNEL_IDS = {
    int(channel_id)
    for channel_id in os.environ.get("GVG_CHANNEL_IDS", "").split(",")
    if channel_id.strip()
}
THREAD_AUTO_ARCHIVE_MINUTES = int(os.environ.get("THREAD_AUTO_ARCHIVE_MINUTES", "1440"))
THREAD_NAME_MAX_LENGTH = 100

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("gvg-autothread")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


def build_thread_name(message: discord.Message) -> str:
    name = message.content.strip().splitlines()[0] if message.content.strip() else f"GVG - {message.author.display_name}"
    return name[:THREAD_NAME_MAX_LENGTH]


@bot.event
async def on_ready():
    logger.info("Logged in as %s (id=%s)", bot.user, bot.user.id if bot.user else "?")
    logger.info("Watching channels: %s", GVG_CHANNEL_IDS or "(none configured)")


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.channel.id in GVG_CHANNEL_IDS and isinstance(message.channel, discord.TextChannel):
        try:
            await message.create_thread(
                name=build_thread_name(message),
                auto_archive_duration=THREAD_AUTO_ARCHIVE_MINUTES,
            )
        except discord.HTTPException:
            logger.exception("Failed to create thread for message %s", message.id)

    await bot.process_commands(message)


if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
