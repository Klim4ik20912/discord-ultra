import disnake
from disnake.ext import commands

from database.db import SQLighter

class Transfer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="transfer", description="Перевод валют")
    async def trans(ctx, user: disnake.Member = commands.Param(description="Кому хочешь передать климчики?"),
                    value: int =commands.Param(description="Сколько передать климчиков?")):
        try:
            db = SQLighter("discord.db")
            if not db.check_user(ctx.author.id):
                await ctx.response.send_message("Ты не авторизован :(")

            elif value > db.get_bal(ctx.author.id):
                await ctx.response.send_message("Недостатоно средств")
            
            elif value <= 0:
                await ctx.response.send_message("Неверная сумма")

            elif not db.check_user(user.id):
                await ctx.response.send_message("Пользователь не записан в базе")

            elif user.id == ctx.author.id:
                await ctx.response.send_message("Нельзя передавать деньги самому себе♿ ")

            else:
                if db.trans(ctx.author.id, user.id, value):
                    
                    klim4ik = await ctx.guild.fetch_emoji(1089599616917438608)

                    embed=disnake.Embed(title="Вам передали климчики")
                    embed.add_field(name="Кто передал климчики", value=f"{ctx.author.mention} [{ctx.author.display_name}#{ctx.author.discriminator}]", inline=False)
                    embed.add_field(name="Количество климчиков", value=f"{value} {klim4ik}", inline=False)


                    await user.send(embed=embed)

                    embed=disnake.Embed(title="Ты передал климчики")
                    embed.add_field(name="Кому передал климчики", value=f"{user.mention} [{user.display_name}#{user.discriminator}]", inline=False)
                    embed.add_field(name="Сколько передал климчиков", value=f"{value} {klim4ik}", inline=False)
                    await ctx.send(embed=embed)

                else:
                    await ctx.response.send_message("Операция не удалась♿")

        except Exception as e:
            await ctx.response.send_message(e)
    


def setup(bot):
    bot.add_cog(Transfer(bot))