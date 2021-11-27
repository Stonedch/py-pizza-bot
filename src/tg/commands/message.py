from aiogram import types
from aiogram.dispatcher.filters import Command

from tg.config import dp, keyboards, machine


@dp.message_handler()
@dp.message_handler(Command(machine.get_triggers(machine.state), ignore_case=True))
async def start(message: types.Message):
    machine.trigger(message.text)
    await message.answer(
        f'{machine.message}',
        reply_markup=keyboards.get_commands(),
    )
