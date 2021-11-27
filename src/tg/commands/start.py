from aiogram import types

from tg.config import dp, keyboards, machine


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        f'{machine.message}',
        reply_markup=keyboards.get_commands(),
    )
