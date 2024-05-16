from aiogram import Bot
from aiogram.types import Message

from src.key_boadrs.inline import get_callback_buttons


async def get_start_and_choice_lang(message: Message, bot: Bot, ):
    buttons = {"українська": "ukrainian", "русский": "russian",}
    keyboard_markup = get_callback_buttons(buttons=buttons, sizes=(5,),)

    await bot.send_message(message.from_user.id, "Оберіть мову:", reply_markup=keyboard_markup)
