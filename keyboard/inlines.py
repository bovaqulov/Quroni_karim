from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from .command_list import *
from data.data_matn import GetSurah





def audio_and_matn(lst: list = None, text_call: list = None, page=1):
    """

    @type lst: object
    """
    markup = InlineKeyboardMarkup(row_width=2)
    limit = 6
    count_sura = len(lst)
    max_page = count_sura // limit if count_sura % limit == 0 else count_sura // limit + 1
    offset = (page - 1) * limit
    suralar = lst[offset:][:limit]
    size = 2
    text_chunks = [suralar[i:i + size] for i in range(0, len(suralar), size)]
    for chunk in text_chunks:
        buttons = []
        for item in chunk:
            item_1 = item.split('.')
            buttons.append(InlineKeyboardButton(item, callback_data=f"{text_call[0]}|{item_1[0]}"))
        markup.add(*buttons)
    preview_btn = InlineKeyboardButton("⏮", callback_data=f'{text_call[1]}')
    page_btn = InlineKeyboardButton(page, callback_data=f"{text_call[2]}|{page}")
    next_btn = InlineKeyboardButton("⏭", callback_data=f'{text_call[3]}')
    if page == 1:
        markup.row(page_btn, next_btn)
    elif 1 < page < max_page:
        markup.row(preview_btn, page_btn, next_btn)
    elif page == max_page:
        markup.row(preview_btn, page_btn)

    markup.row(InlineKeyboardButton("🔙 Ortga", callback_data=f'{text_call[4]}'),
               InlineKeyboardButton("Asosiy menyu", callback_data='main_menu'))
    return markup

