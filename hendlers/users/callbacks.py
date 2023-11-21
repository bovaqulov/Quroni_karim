from telebot.types import CallbackQuery
from telebot.types import ReplyKeyboardRemove
from loader import *

from keyboard.inlines import *
from keyboard.default import *
from text import *


class CallMessage():
    def __init__(s, call: CallbackQuery):
        s.chat_id = call.message.chat.id
        s.data = call.data
        s.msg_id = call.message.id
        s.key = call.message.reply_markup

    def manager(s):
        def text_kalima():
            from random import choice
            kalima = [
                "🌸🍃Subhanalloh",
                "🌸🍃Alhamdulillah",
                "🌸🍃Laa ilaaha illalloh",
                "🌸🍃Allohu Akbar",
                "🌸🍃Subhanallohi va bihamdihi",
                "🌸🍃Subhanallohil ʼAziym",
                "🌸🍃Astagʻfirullah ʼAziym va atubu ilayh",
                "🌸🍃Laa havla va laa quvvata illaa billah",
                "🌸🍃Allohumma solli ʼala Nabiyyina Muhammad",
                "🌸🍃Laa ilaaha illa anta Subhanaka inniy kuntu minaz - zolimiyn!"]

            return choice(kalima)

        data = s.data
        if data == "main_menu":
            bot.delete_message(s.chat_id, s.msg_id)
            bot.send_message(s.chat_id, start_text, reply_markup=generate_btn(categories))
            return

        if data == "back_categories":
            bot.delete_message(s.chat_id, s.msg_id)
            bot.send_message(s.chat_id, text_audio, reply_markup=generate_btn(audio))
            return




        if "uzbek_audio|" in data:
            audio_id = int(data.split("|")[-1]) + 7
            bot.send_audio(s.chat_id, audio=f"https://t.me/Baza_all/{audio_id}",
                           caption=audio_text,
                           reply_markup=ReplyKeyboardRemove())
            return

        if data == "next":
            keyboard_list = s.key.keyboard[-2]
            for item in keyboard_list:
                if 'page' in item.callback_data:
                    page = int(item.text)
                    print(page)
                    page += 1
                    bot.edit_message_reply_markup(s.chat_id, s.msg_id, reply_markup=audio_and_matn(page=page,
                                                                                                   text_call=uzbek_audio_btn,
                                                                                                   lst=quron_suralar))
            return

        if data == "preview":
            keyboard_list = s.key.keyboard[-2]
            for item in keyboard_list:
                if 'page' in item.callback_data:
                    page = int(item.text)
                    page -= 1
                    bot.edit_message_reply_markup(s.chat_id, s.msg_id,
                                                  reply_markup=audio_and_matn(page=page,
                                                                              text_call=uzbek_audio_btn,
                                                                              lst=quron_suralar))

            return




        if "arab_audio|" in data:
            audio_id = int(data.split("|")[-1]) + 211
            bot.send_audio(s.chat_id, audio=f"https://t.me/Baza_all_2/{audio_id}",
                           caption=audio_text,
                           reply_markup=ReplyKeyboardRemove())
            return

        if data == "next_arab":
            keyboard_list = s.key.keyboard[-2]
            for item in keyboard_list:
                if 'page_arab' in item.callback_data:
                    page = int(item.text)
                    print(page)
                    page += 1
                    bot.edit_message_reply_markup(s.chat_id, s.msg_id, reply_markup=audio_and_matn(page=page,
                                                                                                   text_call=arab_audio_btn,
                                                                                                   lst=quron_suralar))

            return

        if data == "preview_arab":
            keyboard_list = s.key.keyboard[-2]
            for item in keyboard_list:
                if 'page_arab' in item.callback_data:
                    page = int(item.text)
                    page -= 1
                    bot.edit_message_reply_markup(s.chat_id, s.msg_id,
                                                  reply_markup=audio_and_matn(page=page,
                                                                              text_call=arab_audio_btn,
                                                                              lst=quron_suralar))
            return














        # if "uzbek_matn|" in data:
        #     print(data)
        #     sura_id = int(data.split("|")[-2])
        #     matn_name = data.split("|")[-1]
        #     bot.send_message(s.chat_id,
        #                      f"Siz {matn_name} surasini tanladingiz",
        #                      reply_markup=uzbek_matn_btn2(sura_id=sura_id))
        #
        # if data == "matn_next_uz":
        #     keyboard_list = s.key.keyboard[-2]
        #     for item in keyboard_list:
        #         if 'matn_page_uz' in item.callback_data:
        #             page = int(item.text)
        #             page += 1
        #             bot.edit_message_reply_markup(s.chat_id, s.msg_id,
        #                                           reply_markup=uzbek_matn_btn(page))
        #     return
        #
        # if data == "matn_preview_uz":
        #     keyboard_list = s.key.keyboard[-2]
        #     for item in keyboard_list:
        #         if 'matn_page_uz' in item.callback_data:
        #             page = int(item.text)
        #             page -= 1
        #             bot.edit_message_reply_markup(s.chat_id, s.msg_id,
        #                                           reply_markup=uzbek_matn_btn(page))
        #     return
        #
        # if data == "uz_matn_back_categories":
        #     bot.delete_message(s.chat_id, s.msg_id)
        #     bot.send_message(s.chat_id, text_matn, reply_markup=generate_btn(matn))
        #     return
        #
        # if "uz_all_ayat" in data:
        #     # bot.delete_message(s.chat_id, s.msg_id)
        #     sura_id = int(data.split("|")[-1])
        #     size: int = 4000
        #     texts = GetSurah(language="uzbek", sura=sura_id, all_ayat=True).get_oyat_text()
        #     text: list = [texts[i:i + size] for i in range(0, len(texts), size)]
        #     for textr in text:
        #         bot.send_message(s.chat_id, f"<i>{textr}</i>")
        #     bot.send_message(s.chat_id, f"<i><b>{text_kalima()}</b></i>", reply_markup=uzbek_matn_btn(sura_id))
        #
        # if data == "uz_matn_back_categories":
        #     bot.send_message(s.chat_id, text_matn, reply_markup=generate_btn(matn))

        # if "oyat_matn_next_uz" in data:
        #     keyboard_list = s.key.keyboard[-3]
        #     for item in keyboard_list:
        #         if 'oyat_matn_page_uz' in item.callback_data:
        #             page: int = int(item.text.split("-")[0].strip())
        #             page += 1
        #             bot.edit_message_reply_markup(s.chat_id, s.msg_id, reply_markup=uzbek_matn_btn2(page))
        #
        #     return
        #
        # if "oyat_matn_preview_uz" == data:
        #     keyboard_list = s.key.keyboard[-2]
        #     for item in keyboard_list:
        #         if 'oyat_matn_page_uz' in item.callback_data:
        #             page = int(item.text.split("|")[-1])
        #             page -= 1
        #             bot.edit_message_reply_markup(s.chat_id, s.msg_id, reply_markup=uzbek_matn_btn2(page))
        #
        #     return









# @bot.callback_query_handler(func=lambda call: call.data == 'preview')
# def reaction_preview(call: CallbackQuery):
#     chat_id = call.message.chat.id
#     keyboard_list = call.message.reply_markup.keyboard[-2]
#     for item in keyboard_list:
#         if 'page' in item.callback_data:
#             category = item.callback_data.split("|")[1]
#             page = int(item.text)
#             page -= 1
#             bot.edit_message_reply_markup(chat_id, call.message.id,
#                                           reply_markup=products_pagination_btns(category, page))
#
# @bot.callback_query_handler(func=lambda call: 'page' in call.data)
# def reaction_page(call: CallbackQuery):
#     keyboard_list = call.message.reply_markup.keyboard[-2]
#     for item in keyboard_list:
#         if 'page' in item.callback_data:
#             page = item.text
#             bot.answer_callback_query(call.id, f"Siz {page}chi betdasiz!")
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'back_categories')
# def reaction_back_categories(call: CallbackQuery):
#     chat_id = call.message.chat.id
#     bot.delete_message(chat_id, call.message.id)
#     bot.send_message(chat_id, "Kategoriyalar", reply_markup=categories_btn())
#
#
# @bot.callback_query_handler(func=lambda call: 'product' in call.data)
# def reaction_product(call: CallbackQuery):
#     chat_id = call.message.chat.id
#     product_id = call.data.split("|")[1]
#     product = db.get_product_info(product_id)
#     keyboard_list = call.message.reply_markup.keyboard[-2]
#     page = 1
#     for item in keyboard_list:
#         if 'page' in item.callback_data:
#             page = item.text
#     product_name, price, image, link, category_id = product[1:]
#     bot.delete_message(chat_id, call.message.id)
#     bot.send_photo(chat_id, image, caption=f"""{product_name}
# Narxi: {price}
# <a href="{link}">Batafsil ma'lumot</a>""", parse_mode='html', reply_markup=product_btn(category_id, product_id, page))
#
#
# @bot.callback_query_handler(func=lambda call: 'back_cat_id' in  call.data)
# def reaction_back_cat_id(call: CallbackQuery):
#     chat_id = call.message.chat.id
#     page = int(call.message.reply_markup.keyboard[0][1].callback_data.split('|')[1])
#     category_id = call.data.split('|')[1]
#     category = db.get_category_by_id(category_id)
#     bot.delete_message(chat_id, call.message.id)
#     bot.send_message(chat_id, category, reply_markup=products_pagination_btns(category, page))
#
#
# @bot.callback_query_handler(func=lambda call: call.data in ['plus', 'minus'])
# def reaction_plus(call: CallbackQuery):
#     chat_id = call.message.chat.id
#     quantity = int(call.message.reply_markup.keyboard[0][1].text)
#
#     page = int(call.message.reply_markup.keyboard[0][1].callback_data.split('|')[1])
#     category_id = int(call.message.reply_markup.keyboard[-1][0].callback_data.split('|')[1])
#     product_id = int(call.message.reply_markup.keyboard[-2][0].callback_data.split('|')[1])
#     if call.data == 'plus':
#         quantity += 1
#         bot.edit_message_reply_markup(chat_id, call.message.id,
#                                       reply_markup=product_btn(category_id, product_id, page, quantity))
#     else:
#         if quantity > 1:
#             quantity -= 1
#             bot.edit_message_reply_markup(chat_id, call.message.id,
#                                           reply_markup=product_btn(category_id, product_id, page, quantity))
#         else:
#             bot.answer_callback_query(call.id, "Siz eng kamida 1ta mahsulot olishingiz kerak❗️", show_alert=True)
#
#
# @bot.callback_query_handler(func=lambda call: 'quantity' in call.data)
# def reaction_quantity(call: CallbackQuery):
#     quantity = int(call.message.reply_markup.keyboard[0][1].text)
#     bot.answer_callback_query(call.id, f"Mahsulotdan hozircha: {quantity}ta")
#
#
# @bot.callback_query_handler(func=lambda call: 'add_card' in call.data)
# def reaction_add_card(call: CallbackQuery):
#     chat_id = call.message.chat.id
#     user_id = call.from_user.id
#     bot.set_state(user_id, CardState.card, chat_id)
#     product_id = call.data.split('|')[1]
#     product = db.get_product_info(product_id)
#     product_name, price = product[1], product[2]
#     quantity = int(call.message.reply_markup.keyboard[0][1].text)
#     with bot.retrieve_data(user_id, chat_id) as data:
#         if data.get('card'):
#             data['card'][product_name] = {
#                 'product_id': product_id,
#                 'price': price,
#                 'quantity': quantity
#             }
#             bot.answer_callback_query(call.id, "Qo'shildi!")
#         else:
#             data['card'] = {
#                 product_name: {
#                     'product_id': product_id,
#                     'price': price,
#                     'quantity': quantity
#                 }
#             }
#             bot.answer_callback_query(call.id, "Qo'shildi!")
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'show_card')
# def reaction_show_card(call: CallbackQuery):
#     chat_id = call.message.chat.id
#     user_id = call.from_user.id
#     with bot.retrieve_data(user_id, chat_id) as data:
#         res = get_card_text_markup(data)
#         text = res['text']
#         markup = res['markup']
#
#     bot.delete_message(chat_id, call.message.id)
#     bot.send_message(chat_id, text, reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda call: 'remove' in call.data)
# def reaction_remove(call: CallbackQuery):
#     chat_id = call.message.chat.id
#     user_id = call.from_user.id
#     product_id = int(call.data.split('|')[1])
#     with bot.retrieve_data(user_id, chat_id) as data:
#         keys = [item for item in data['card'].keys()]
#         for product_name in keys:
#             if int(data['card'][product_name]['product_id']) == product_id:
#                 del data['card'][product_name]
#     res = get_card_text_markup(data)
#     text = res['text']
#     markup = res['markup']
#     bot.delete_message(chat_id, call.message.id)
#     bot.send_message(chat_id, text, reply_markup=markup)
#
#
# def get_card_text_markup(data: dict):
#     text = "Savatda:\n"
#     total_price = 0
#     for product_name, items in data['card'].items():
#         product_price = items['price']
#         quantity = items['quantity']
#         price = int(product_price) * int(quantity)
#         total_price += price
#         text += f"""{product_name}
# Narxi: {quantity} * {product_price} = {price} so'm\n"""
#
#     if total_price == 0:
#         text = "Savatingiz bo'sh!"
#         markup = main_menu_btn()
#     else:
#         text += f"\nUmumiy narx: {total_price} so'm"
#         markup = card_btns(data['card'])
#     return {'markup': markup, 'text': text}
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'clear_card')
# def reaction_clear_card(call: CallbackQuery):
#     chat_id = call.message.chat.id
#     user_id = call.from_user.id
#     bot.delete_state(user_id, chat_id)
#     bot.delete_message(chat_id, call.message.id)
#     bot.send_message(chat_id, "Savat bo'sh!", reply_markup=main_menu_btn())
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'submit')
# def reaction_submit(call: CallbackQuery):
#     chat_id = call.message.chat.id
#     user_id = call.from_user.id
#     with bot.retrieve_data(user_id, chat_id) as data:
#         bot.send_invoice(chat_id, **generate_product_invoice(data['card']).generate_invoice(),
#                          invoice_payload='shop_bot')


@bot.callback_query_handler(func=lambda call: call.data is not None)
def main(call: CallbackQuery):
    try:
        CallMessage(call).manager()
        print(call.data)
    except Exception as e:
        bot.send_message(CallMessage(call).chat_id, f"ERROR: {e}")