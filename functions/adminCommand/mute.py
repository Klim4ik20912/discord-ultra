import disnake
from disnake.ext import commands
from disnake import Member, errors, Embed, utils
from disnake.ext import commands
from database.db import SQLighter
import asyncio

class TempMuteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="tmute")
    async def text_mute(ctx, user: disnake.Member, duration: int, reason: str):
        db = SQLighter("discord.db")
        tmute_role = utils.get(user.guild.roles, name="text mute")
        await user.add_roles(tmute_role)
        db.mute(user_id=user.id, duration=duration, reason=reason)
        await ctx.response.send_message(f"ты замутил {user.display_name}#{user.id.denominator} (тут красивый эмбед)")
        await user.send("ты был замучен (тут типа красивый эмбед)")

    

def setup(bot):
    bot.add_cog(TempMuteCog(bot))
