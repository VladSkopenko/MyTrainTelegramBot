import asyncio
import os

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.client.bot import DefaultBotProperties
from dotenv import load_dotenv

from src.handlers.start import get_start_and_choice_lang
from aiogram.filters import Command

from src.handlers.start import language_callback
from src.utils.commands import set_commands

load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

bot = Bot(token=token, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(admin_id, 'bot running')


dp.startup.register(start_bot)
dp.message.register(get_start_and_choice_lang, Command(commands=['start']))
dp.message.register(get_start_and_choice_lang, Command(commands=['language']))
dp.callback_query.register(language_callback)


async def start():
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
