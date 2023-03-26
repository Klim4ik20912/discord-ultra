from functions import *
from config import *
import disnake
from disnake.ext import commands



bot = commands.Bot(command_prefix='?', intents=disnake.Intents.all())
client = disnake.Client()


bot.load_extension("functions.member_join")
bot.load_extension("functions.auth")
bot.load_extension("functions.ban")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}.")


@bot.event
async def on_error(event: str, *args, **kwargs):
    pass
    


bot.run(token)