import disnake
from disnake.ext import commands

from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

class Sheduler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def check_kakoy_nibud():
        print("яйца")
    
    scheduler.add_job(check_kakoy_nibud, "interval", seconds=5)
    


def setup(bot):
    bot.add_cog(Sheduler(bot))

