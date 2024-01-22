from aiogram.dispatcher.filters.state import State, StatesGroup


class UploadPhotoStates(StatesGroup):
    WAITING_FOR_PHOTOS = State()
    WAITING_FOR_CONFIRM = State()
