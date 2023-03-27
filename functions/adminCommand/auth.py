import disnake, asyncio
from disnake.ext import commands
from database.db import SQLighter
from config import auth_role, start_role, adm_msg, user_msg


class Verify(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.slash_command(name="v2", description="Вирифай юзер бай админ")
    @commands.has_any_role("admin")
    async def verifyuser(self, ctx, user: disnake.Member = commands.Param(description="кого хочешь авторизовать?") ):
        db =  SQLighter("disnake.db")

        if db.check_user(user.id):
            await ctx.response.send_message("Он уже авторизован")

        elif db.register(user.id, ctx.author.id):
            role = disnake.utils.get(user.guild.roles, name=auth_role)
            role_rem = disnake.utils.get(user.guild.roles, name=start_role)
            await user.add_roles(role)
            await user.remove_roles(role_rem)

            embed=disnake.Embed(title="Ты авторизирован!", description=f"{user_msg}", color=0xff0000)
            embed.set_thumbnail(url=str(user.display_avatar.url))
            embed.set_footer(text=f"авторизовал - {ctx.author.name}")


            embed2=disnake.Embed(title="Готово!", description=f"{adm_msg}", color=0xff0000)
            embed2.add_field(name="+100 social credits", value="Поздравляю!", inline=False)

            await ctx.response.send_message(embed=embed2)
            
            await user.send(embed=embed)
        else:
            await ctx.response.send_message("Прости, но этот чел уже авторизирован")




def setup(bot):
    bot.add_cog(Verify(bot))