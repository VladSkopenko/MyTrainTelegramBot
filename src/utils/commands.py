from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description="run bot"
        ),
        BotCommand(
            command="help",
            description="Need help with bot"
        )
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())