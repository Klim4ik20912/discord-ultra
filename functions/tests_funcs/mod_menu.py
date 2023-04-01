import disnake
from disnake.ext import commands
from disnake import ButtonStyle
from disnake.ui import Button, View
from typing import Optional

class ButMenu(disnake.ui.View):
    def __init__(self, user: Optional[disnake.Member] = None):
        super().__init__(timeout=120.0)
        self.user = user
        self.author = author

    @disnake.ui.button(label="Выдать мут", style=disnake.ButtonStyle.green)
    async def mute(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        await inter.response.edit_message("выберите время", view=None)
        time = await inter.client.wait_for("message")
        print(f'автор ебаный {self.author}')
        await inter.followup.send(content=f"ты замутил {self.user.mention} на {time.content}м")
        print("функция мута")

    @disnake.ui.button(label="Снять мут", style=disnake.ButtonStyle.red)
    async def unmute(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        await inter.response.edit_message("вы яйца не сасать", view=None)
        print("функция анмута")
        message = await inter.client.wait_for("message")


    @disnake.ui.button(label="Назад", style=disnake.ButtonStyle.primary)
    async def back(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        await inter.message.delete()
        print("назад")


class ModCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="mod", description="Модераторское меню")
    async def mod(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member):

        view = ButMenu(user=user, author=inter.a)  # передаем объект пользователя (user) в конструктор класса ButMenu
        await inter.response.send_message(f"Меню модератора для {user.mention}", view=view)

def setup(bot: commands.Bot):
    bot.add_cog(ModCog(bot))