from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

bot = Bot(token=token, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()


async def start_bot(bot: Bot):
    await bot.send_message(admin_id, 'bot running')


dp.startup.register(start_bot)


async def start():
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
