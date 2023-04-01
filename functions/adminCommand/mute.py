import disnake
from disnake.ext import commands
from disnake import Member, errors, Embed, utils
from disnake.ext import commands
from database.db import SQLighter
import asyncio

class TempMuteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="mute")
    async def mute(ctx, user: disnake.Member, duration: int, reason: str):
        db = SQLighter("discord.db")
        tmute_role = utils.get(user.guild.roles, name="muted")
        await user.add_roles(tmute_role)
        db.mute(user_id=user.id, duration=duration, reason=reason)
        await ctx.response.send_message(f"ты замутил {user.display_name}#{user.discriminator} (тут красивый эмбед)")

        embed=disnake.Embed(title="Вам был выдан мут", description=f"{user.mention}, Вы получили мут на **{duration}м** по причине: **{reason}** от модератора {ctx.author.mention}", color=0xff0000)
        embed.set_thumbnail(url=str(user.display_avatar.url))
        await user.send(embed=embed)

    @commands.slash_command(name="unmute")
    async def unmute(ctx, user: disnake.Member):
        db = SQLighter("discord.db")
        tmute_role = utils.get(user.guild.roles, name="muted")
        await user.remove_roles(tmute_role)

        await ctx.response.send_message(f"ты размутил {user.display_name}#{user.discriminator} (тут красивый эмбед)")
        db.unmute(user.id)
        embed=disnake.Embed(title="С вас был снят мут", description=f"{user.mention}, Вы можете продолжить общаться, вас размутил модератор **{ctx.author.mention}**", color=0xff0000)
        embed.set_thumbnail(url=str(user.display_avatar.url))
        await user.send(embed=embed)

def setup(bot):
    bot.add_cog(TempMuteCog(bot))
