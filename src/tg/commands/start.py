from aiogram import types

from tg.config import dp, keyboards

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        f'{message.text}',
        reply_markup=keyboards.get_commands(),
    )
