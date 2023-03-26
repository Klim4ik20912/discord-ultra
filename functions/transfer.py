import disnake
from disnake.ext import commands

from database.db import SQLighter

class Transfer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="transfer", description="Перевод валют")
    async def trans(ctx, user: disnake.Member, value: int):
        try:
            db = SQLighter()

            if value < db.get_bal(user.id):
                

        except Exception as e:
            pass
    


