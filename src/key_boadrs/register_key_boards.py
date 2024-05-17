from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

register_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Реєстрація"),
            KeyboardButton(text="Авторизація"),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Для продовження натисніть кнопку",
)
