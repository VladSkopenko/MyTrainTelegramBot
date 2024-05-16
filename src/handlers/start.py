from aiogram import Bot
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.types import Message

from src.key_boadrs.inline import get_callback_buttons


USERS_LANGS = {}
lang_router = Router()


async def get_start_and_choice_lang(message: Message, bot: Bot, ):
    buttons = {"українська": "українська",
               "русский": "русский", }
    keyboard_markup = get_callback_buttons(buttons=buttons, sizes=(5,))

    await bot.send_message(message.from_user.id, "Оберіть мову:", reply_markup=keyboard_markup)


async def language_callback(callback_query: CallbackQuery):
    lang = callback_query.data
    user_id = callback_query.from_user.id
    USERS_LANGS[user_id] = lang
    if lang == "українська":
        lang_message = f"{callback_query.from_user.first_name}, обрано українську мову"
    else:
        lang_message = f"{callback_query.from_user.first_name}, выбран {lang} язык"
    await callback_query.message.answer(f"{lang_message}")
    print(USERS_LANGS)
