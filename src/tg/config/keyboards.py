from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from .initialize import machine


def get_commands():
    commands = ReplyKeyboardMarkup(resize_keyboard=True)

    for command in machine.get_triggers(machine.state):
        commands.add(KeyboardButton(command))

    return commands
