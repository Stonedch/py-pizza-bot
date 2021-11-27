from aiogram import types
from aiogram.dispatcher.filters import Command

from tg.config import dp, keyboards


@dp.message_handler()
async def start(message: types.Message):
    await message.answer(
        f'{message.text}',
        reply_markup=keyboards.get_commands(),
    )
