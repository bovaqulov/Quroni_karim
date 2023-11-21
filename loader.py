from telebot import TeleBot, custom_filters
from telebot.storage import StateMemoryStorage
from telebot.types import BotCommand

from config import *



bot = TeleBot(TOKEN, state_storage=StateMemoryStorage(), use_class_middlewares=True, parse_mode='html')

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.set_my_commands(commands=[
    BotCommand('start', 'Botni qayta ishga tushirish')
])


bot.add_custom_filter(custom_filters.ChatFilter())