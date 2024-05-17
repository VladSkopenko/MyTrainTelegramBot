from aiogram.fsm.state import StatesGroup, State


class RegisterStart(StatesGroup):
    reg_last_name = State()
    reg_first_name = State()
    reg_email = State()
    reg_password = State()
    reg_confirm = State()

