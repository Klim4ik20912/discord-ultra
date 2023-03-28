import disnake
from disnake.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database.db import SQLighter
from config import guild_id

class Sheduler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.scheduler = AsyncIOScheduler()
        self.db = SQLighter("discord.db")

    @commands.Cog.listener()
    async def check_kakoy_nibud(self):
        need_unmute = self.db.get_mutes()
        print(need_unmute)
        for i in need_unmute:
            user_id = i
            user = self.bot.get_guild(guild_id).get_member(user_id)
            role = disnake.utils.get(user.guild.roles, name="text mute")
            await user.remove_roles(role)
            await user.send("ты был автоматически размучен. (тут типо красивый эмбед)")

    
    @commands.Cog.listener()
    async def on_ready(self):
        self.scheduler.add_job(self.check_kakoy_nibud, "interval", seconds=5)
        self.scheduler.start()

def setup(bot):
    bot.add_cog(Sheduler(bot))