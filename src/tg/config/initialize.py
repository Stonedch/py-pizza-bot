import logging

from aiogram import Bot, Dispatcher

from .local_settings import TOKEN, LOGGING_LEVEL
from machines import PizzaMachine

logging.basicConfig(level=LOGGING_LEVEL)

bot = Bot(TOKEN)
dp = Dispatcher(bot)

machine = PizzaMachine()
