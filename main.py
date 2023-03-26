from functions import *
from config import *
import disnake
from disnake.ext import commands



bot = commands.Bot(command_prefix='?', intents=disnake.Intents.all())
client = disnake.Client()

bot.load_extension("functions.member_join")
bot.load_extension("functions.auth")


bot.run(token)