from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build_keyboard(buttons):
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 1

    for button in buttons:
        keyboard.add(InlineKeyboardButton(text=button, callback_data=button))

    return keyboard


def build_menu_keyboard():

    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text=' Upload photo ', callback_data='Upload photo')
    keyboard.add(button1)

    return keyboard
