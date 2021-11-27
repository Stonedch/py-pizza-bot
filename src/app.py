from aiogram import executor

from tg.commands import dp


if __name__ == '__main__':
    executor.start_polling(dp)
