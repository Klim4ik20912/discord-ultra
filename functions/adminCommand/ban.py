from disnake import Member, errors, Embed, utils
from disnake.ext import commands
from config import *
from database.db import SQLighter


class BanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
            
    @commands.slash_command(name="unban", description="unban")
    @commands.has_any_role("admin")       
    async def unban(ctx, member: Member):
        db = SQLighter("discord.db")
        if db.check_ban(member.id) == False:
            if db.check_user(member.id):
                role = utils.get(member.guild.roles, name=ban_role)
                await member.remove_roles(role)
                db.unban(user=member.id)
                embed=Embed(title="С вас был снят бан", description=f"{member.mention}, Вы можете продолжить общаться, вас разбанил модератор **{ctx.author.mention}**")
                embed.set_thumbnail(url=str(member.display_avatar.url))
                await member.send(embed=embed)
                await ctx.response.send_message("вы разбанили челика")
        else:
            await ctx.response.send_message("этот человек не забанен")



    @commands.slash_command(name="ban", description="бан юзер бай админс")
    @commands.has_any_role("admin")
    async def ban(ctx, member: Member=commands.Param(description="Кому выдать бан?"), *,
                    reason=commands.Param(description="Причина бана", default=None, autocomplete=ban_reasons)):
        db = SQLighter("discord.db")
        if db.check_ban(member.id) == True:
            if db.check_user(member.id):
                role = utils.get(member.guild.roles, name=ban_role)
                await member.add_roles(role)
                if reason != None:
                    embed=Embed(title="Вам был выдан бан", description=f"{member.mention}, Вы получили бан **навсегда** по причине \"**{reason}**\" от модератора {ctx.author.mention}")
                    embed.set_thumbnail(url=str(member.display_avatar.url))

                else:
                    embed=Embed(title="Вам был выдан бан", description=f"{member.mention}, Вы получили бан **навсегда** от модератора {ctx.author.mention}")
                    embed.set_thumbnail(url=str(member.display_avatar.url))

                db.ban(member.id, f"{ctx.author.display_name}#{ctx.author.discriminator}", reason=reason)

                await member.move_to(None)
                await member.send(embed=embed)
                await ctx.response.send_message(f'{member.display_name} был забанен.')
        else:
            await ctx.response.send_message(f'{member.display_name} уже забанен.')

def setup(bot):
    bot.add_cog(BanCog(bot))