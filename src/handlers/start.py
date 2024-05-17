from aiogram import Bot
from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.types import Message

from src.key_boadrs.get_number_of_phone import keyboard_get_number
from src.key_boadrs.inline import get_callback_buttons
from src.key_boadrs.register_key_boards import register_keyboard

USERS_LANGS = {}
start_router = Router()
USERS_INFO = []


async def get_start_and_choice_lang(
    message: Message,
    bot: Bot,
):
    buttons = {
        "українська": "українська",
        "русский": "русский",
    }
    keyboard_markup = get_callback_buttons(buttons=buttons, sizes=(2,))

    await bot.send_message(
        message.from_user.id, "Оберіть мову:", reply_markup=keyboard_markup
    )


async def language_callback(callback_query: CallbackQuery):
    lang = callback_query.data
    user_id = callback_query.from_user.id
    USERS_LANGS[user_id] = lang
    if lang == "українська":
        lang_message = f"{callback_query.from_user.first_name}, обрано українську мову"
    else:
        lang_message = f"{callback_query.from_user.first_name}, выбран {lang} язык"
    await callback_query.message.answer(f"{lang_message}")
    await callback_query.message.answer(
        f"Для продовження Авторизуйтесь будь-ласка", reply_markup=register_keyboard
    )


@start_router.message(F.text == "Авторизація")
async def auth_users(message: Message):
    await message.answer(
        "Поділитись номером телефону", reply_markup=keyboard_get_number
    )


@start_router.message(F.contact)
async def get_phone(message: Message):
    if message.contact:
        user_id = message.from_user.id
        phone_number = message.contact.phone_number
        await message.answer(f"Ваш номер телефона: {phone_number}")
        user_dict_with_info = {"user_id": user_id, "phone_number": phone_number}
        USERS_INFO.append(user_dict_with_info)
        print(USERS_INFO)
