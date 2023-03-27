from disnake import Member, errors, Embed, utils
from disnake.ext import commands
from config import *
from database.db import SQLighter


class BanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="pban", description="перманетный бан юзер бай админс")
    @commands.has_any_role("admin")
    async def ban(self, ctx, member: Member = commands.Param(description="Кому выдать бан?"), *,
                   reason=commands.Param(description="Причина бана", default=None, autocomplete=ban_reasons)):
        db = SQLighter("discord.db")
        if db.check_user(member.id):
            try:
                if reason != None:
                    embed=Embed(title="Вам был выдан бан", description=f"{member.mention}, Вы получили бан **навсегда** по причине \"**{reason}**\" от модератора {ctx.author.mention}")
                    embed.set_thumbnail(url=str(member.display_avatar.url))
                
                else:
                    embed=Embed(title="Вам был выдан бан", description=f"{member.mention}, Вы получили бан **навсегда** от модератора {ctx.author.mention}")
                    embed.set_thumbnail(url=str(member.display_avatar.url))

                await member.send(embed=embed)


                db.ban(member.id, f"{ctx.author.display_name}#{ctx.author.discriminator}", reason=reason)
                await member.ban(reason=reason)
                await ctx.response.send_message(f'{member.display_name} был забанен.')
                
            except errors.Forbidden:
                await ctx.response.send_message('У меня нет разрешения на бан пользователей.')
            except errors.HTTPException:
                await ctx.response.send_message('Не удалось забанить пользователя.')
            
    
    @commands.slash_command(name="tban", description="бан юзер бай админс")
    @commands.has_any_role("admin")
    async def tban(ctx, member: Member=commands.Param(description="Кому выдать бан?"), *,
                    reason=commands.Param(description="Причина бана", default=None, autocomplete=ban_reasons)):
        db = SQLighter("discord.db")
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

def setup(bot):
    bot.add_cog(BanCog(bot))