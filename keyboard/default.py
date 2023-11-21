from telebot.types import ReplyKeyboardMarkup, KeyboardButton



def generate_btn(lst: list):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for category in lst:
        markup.add(KeyboardButton(category))
    return markup



