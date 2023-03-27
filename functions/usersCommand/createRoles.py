import disnake
from disnake.ext import commands


from config import role_colors
from database.db import SQLighter

class PersonalRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="crole", description="Креэйт персонал рол")
    async def create_role(self, ctx, *, role_name: str = commands.Param(description="название роли", name="name"),
                        color: disnake.Colour = commands.Param(name="color", description="цвет роли", autocomplete=role_colors, default="black")):
       

        db = SQLighter("discord.db")
        if db.check_user(ctx.author.id):
            if any(role.name == role_name for role in ctx.guild.roles): # Проверяем, существует ли уже роль с таким именем
                await ctx.send(f"Роль с именем {role_name} уже существует.")
                    
            elif db.get_bal(ctx.author.id) < 20000:
                await ctx.send(f"У тебя недостаточно средств на балансе\nДля создания личной роли нужно ещё {20000 - db.get_bal(ctx.author.id)} климчиков")

            else:
                # Создаем новую роль и назначаем ее пользователю
                db.append_bal(ctx.author.id, -20000)

                new_role = await ctx.guild.create_role(name=role_name, color=color, reason=f"Личная роль для {ctx.author.name}")
                await ctx.author.add_roles(new_role)

                await ctx.send(f"Роль {role_name} успешно создана и назначена.")


        


def setup(bot):
    bot.add_cog(PersonalRoles(bot))