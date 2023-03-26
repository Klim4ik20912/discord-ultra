import disnake
from disnake.ext import commands

from database.db import SQLighter

class Checkbal(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="balance", description="Проверить свой или чужой баланс")
    async def checkbalance(ctx, member: disnake.Member=None):
        db = SQLighter("discord.db")
        klim4ik = await ctx.guild.fetch_emoji(1089599616917438608)

        if member == None:
            if db.check_user(ctx.author.id):

                embed=disnake.Embed(title="Твой баланс")
                embed.add_field(name=f"> {klim4ik} Климчики:", value=f"```{db.get_bal(ctx.author.id)}```", inline=True)
                #embed.add_field(name="> хуимчики", value="```100```", inline=True)
                embed.set_thumbnail(url=ctx.author.display_avatar.url)

                await ctx.send(embed=embed)
            
            else:
                await ctx.send("Ты не авторизован♿")

        else:
            if db.check_user(member.id):

                embed=disnake.Embed(title="Твой баланс")
                embed.add_field(name=f"> {klim4ik} Климчики:", value=f"```{db.get_bal(member.id)}```", inline=True)
                #embed.add_field(name="> хуимчики", value="```100```", inline=True)
                embed.set_thumbnail(url=member.display_avatar.url)

                await ctx.send(embed=embed)
            else:
                await ctx.send("Пользователь не авторизован♿")
    

def setup(bot):
    bot.add_cog(Checkbal(bot))
