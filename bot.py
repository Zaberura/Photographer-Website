from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
import asyncio
import os
from telegram_bot.logics import *

# Init telegram_bot

load_dotenv()
token = os.getenv('API_KEY_BOT')
bot = Bot(token)
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)


async def run_bot():
    await dispatcher.start_polling()


# Handlers

@dispatcher.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(text='Welcome to Little Bot Web Assistant')


@dispatcher.message_handler(commands='menu')
async def start(message: types.Message):
    await menu(message)


@dispatcher.callback_query_handler(text='Upload photo')
async def photo_upload_request(message: types.CallbackQuery):
    await handle_photo_upload_request(message.message)


@dispatcher.message_handler(state=UploadPhotoStates.WAITING_FOR_PHOTOS)
async def get_photo(message: types.Message, state: FSMContext):
    await upload_photo(message)
    print('STATE: ')
    print(state)


# Run telegram_bot

if __name__ == "__main__":

    asyncio.run(run_bot())
