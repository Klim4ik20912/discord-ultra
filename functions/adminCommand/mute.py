import disnake
from disnake.ext import commands
import asyncio

from config import mute_time


class TempMuteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="vtmute", description="Временный мут")
    @commands.has_any_role("admin", "?")
    async def tempmute(self, ctx, member: disnake.Member, duration: int,
                       type: str = commands.Param(description="Данные в ...", autocomplete=mute_time),
                        *, reason: str = None):
        
        mute_role = disnake.utils.get(ctx.guild.roles, name="voice muted")



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

    

    @commands.slash_command(name="ttmute", description="Временный мут")
    @commands.has_any_role("admin", "?")
    async def tempmute(self, ctx, member: disnake.Member, duration: int,
                       type: str = commands.Param(description="Данные в ...", autocomplete=mute_time),
                        *, reason: str = None):
        
        mute_role = disnake.utils.get(ctx.guild.roles, name="text mute")



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


        await asyncio.sleep(duration)
        await member.remove_roles(mute_role)
    

def setup(bot):
    bot.add_cog(TempMuteCog(bot))
