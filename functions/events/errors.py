import disnake, sys
from disnake.ext import commands


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_error(self, event, *args, **kwargs):
        _, error = sys.exc_info()
        if isinstance(error, disnake.CommandError):
            await self.handle_command_error(error)

    async def handle_command_error(self, error):
        if isinstance(error, commands.CommandNotFound):
            await error.ctx.send("Команда не найдена.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await error.ctx.send(f"Пропущен обязательный аргумент: {error.param.name}.")
        elif isinstance(error, commands.BadArgument):
            await error.ctx.send("Неправильный аргумент. Проверьте введенные данные.")
        elif isinstance(error, commands.CommandOnCooldown):
            await error.ctx.send(f"Команда на кулдауне. Попробуйте снова через {error.retry_after:.2f} секунд.")
        elif isinstance(error, commands.CheckFailure):
            await error.ctx.send("У вас недостаточно прав для использования этой команды.")
        elif isinstance(error, commands.CommandInvokeError):
            await error.ctx.send("Произошла ошибка при выполнении команды.")
        else:
            await error.ctx.send("Неизвестная ошибка. Обратитесь к администратору.")


def setup(bot):
    bot.add_cog(ErrorHandler(bot))