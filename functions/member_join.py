import disnake
from disnake.ext import commands
from config import start_role,hi_msg


class MemberJoin(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member:disnake.Member):
        role = disnake.utils.get(member.guild.roles, name=start_role)
        await member.add_roles(role)

        embed=disnake.Embed(title=f"Новый участник {member.mention}", description=f"{hi_msg}", color=0xff0000)

        channel = self.bot.get_channel(1089273266843172977)

        await channel.send(embed=embed)

        
            



def setup(bot):
    bot.add_cog(MemberJoin(bot))

