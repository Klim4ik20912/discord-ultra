import disnake
from disnake.ext import commands


from database.db import SQLighter

class Unban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="unban", description="Разбанить челика")
    @commands.has_any_role("admin", "?")
    async def unban(self, ctx,
                 user: disnake.Member = commands.Param(description="Кого разбанить?")):
        
        db = SQLighter("discord.py")
        if db.check_user(user.id):
            db.unban(user.id)

            embed=disnake.Embed(title="Ты был разбанен", description=f"{user.mention}, Вас разбанил модератор {ctx.author.mention}")
            embed.set_thumbnail(url=str(user.display_avatar.url))

            user.send(embed=embed)

            await ctx.response.send_message(f'{user.display_name} был разбанен.')
            

def setup(bot):
    bot.add_cog(Unban(bot))
