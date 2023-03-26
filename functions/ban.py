from disnake import Member, errors
from disnake.ext import commands

from database.db import SQLighter


class BanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="ban", description="бан юзер бай админс")
    @commands.has_any_role("admin")
    async def ban(self, ctx, member: Member, *, reason=None):
        try:
            db = SQLighter("disnake.db")
            db.ban(member.id, ctx.author.id, reason=reason)
            await member.ban(reason=reason)
            await ctx.response.send_message(f'{member.display_name} был забанен.')
            await member.send(f"Ты был забанен {ctx.author.mention}. Если бан был выдан по ошибке обратись к администраторам")
        except errors.Forbidden:
            await ctx.response.send_message('У меня нет разрешения на бан пользователей.')
        except errors.HTTPException:
            await ctx.response.send_message('Не удалось забанить пользователя.')
            

def setup(bot):
    bot.add_cog(BanCog(bot))