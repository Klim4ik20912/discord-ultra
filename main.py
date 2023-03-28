from functions import *
from config import *
import disnake
from disnake.ext import commands


bot = commands.Bot(command_prefix='?', intents=disnake.Intents.all())
client = disnake.Client()


bot.load_extensions("functions/adminCommand")
bot.load_extensions("functions/events")
bot.load_extensions("functions/usersCommand")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}.")


bot.run(token)
