import logging

from aiogram import Bot, Dispatcher

from .local_settings import TOKEN, LOGGING_LEVEL

logging.basicConfig(level=LOGGING_LEVEL)

bot = Bot(TOKEN)
dp = Dispatcher(bot)
