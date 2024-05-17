from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup


keyboard_get_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Відправити номер телефона"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Для продовження авторизуйтесь",
)
