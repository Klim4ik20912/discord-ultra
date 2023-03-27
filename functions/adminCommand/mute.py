import disnake
from disnake.ext import commands
import asyncio

from config import mute_time


class TempMuteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="tmute", description="Временный мут")
    @commands.has_any_role("admin", "?")
    async def tempmute(self, ctx, member: disnake.Member, duration: int,
                       type: str = commands.Param(description="Данные в ...", autocomplete=mute_time),
                        *, reason: str = None):
        
        mute_role = disnake.utils.get(ctx.guild.roles, name="Muted")

        if not mute_role:
            mute_role = await ctx.guild.create_role(name="Muted")

            for channel in ctx.guild.channels:
                await channel.set_permissions(mute_role, speak=False, send_messages=False, add_reactions=False)

        await member.add_roles(mute_role)

        roles = member.roles

        if type == "минуты":
    
            await ctx.response.send_message(f"{member.mention} был замучен на {duration} минут(у) по причине: {reason if reason else 'не указано'}")

            await member.send(f"{member.mention}, ты был замучен на {duration} минут(у) по причине: {reason if reason else 'не указано'}")

            asyncio.create_task(self.unmute(member, mute_role, duration*60, roles))
        
        if type == "часы":
    
            await ctx.response.send_message(f"{member.mention} был замучен на {duration} час(ов) по причине: {reason if reason else 'не указано'}")

            await member.send(f"{member.mention}, ты был замучен на {duration} час(ов) по причине: {reason if reason else 'не указано'}")

            asyncio.create_task(self.unmute(member, mute_role, duration*60*60, roles))

        if type == "дни":
    
            await ctx.response.send_message(f"{member.mention} был замучен на {duration} дня(я) по причине: {reason if reason else 'не указано'}")

            await member.send(f"{member.mention}, ты был замучен на {duration} день(я) по причине: {reason if reason else 'не указано'}")

            asyncio.create_task(self.unmute(member, mute_role, duration*60*60*24, roles))


    async def unmute(self, member: disnake.Member, mute_role: disnake.Role, duration: int, roles):
        """rols = []
        for role in roles:
            print(roles)
            if "@everyone" == role or "Muted" == role:
                pass
            else:
                print(role)
                print(rolen)
                rolen = disnake.utils.get(member.guild.roles, name=role)

                await member.remove_roles(rolen)
                rols.append(role)"""

        await asyncio.sleep(duration)
        await member.remove_roles(mute_role)
    

def setup(bot):
    bot.add_cog(TempMuteCog(bot))
