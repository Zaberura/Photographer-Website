from aiogram import types
from aiogram.dispatcher import FSMContext

from telegram_bot.keyboards import *
from telegram_bot.states import *
import models


async def menu(message: types.Message):
    await message.answer(text='Select ur next Move', reply_markup=build_menu_keyboard())


async def handle_photo_upload_request(message: types.Message):
    await message.answer(text='Upload ur photo url')
    await UploadPhotoStates.WAITING_FOR_PHOTOS.set()


async def upload_photo(messsage: types.Message):
    print(messsage.text)
    # models.add_photo(messsage.text)


