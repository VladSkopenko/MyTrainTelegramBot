from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup

register_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Авторизація"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Для продовження натисніть кнопку",
)
