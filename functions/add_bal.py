import disnake
from disnake.ext import commands

from database.db import SQLighter


class AddBal(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="addbal", description="Гив юзер балансе")
    @commands.has_any_role("admin")
    async def addbalance(ctx, user: disnake.Member):
        db =  SQLighter("discord.db")
        db.add_bal(user.id)
        await ctx.response.send_message("Успех!", ephemeral=True)


def setup(bot):
    bot.add_cog(AddBal(bot))
