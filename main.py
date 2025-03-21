import os

import dotenv
from discord.ext import commands

bot = commands.Bot(
    [
        "kouyou#",
        "kouyou♪",
        "kouyouanko#",
        "kouyouanko♪",
        "紅葉#",
        "紅葉♪",
        "紅葉杏狐#",
        "紅葉杏狐♪",
    ],
    description="紅葉杏狐だよ♪よろしくね♪",
)

@bot.event
async def on_ready():
    print(bot.user.email)

@bot.event
async def setup_hook():
    await bot.load_extension("cogs.aichat")


dotenv.load_dotenv()
bot.run(os.getenv("discord"))
