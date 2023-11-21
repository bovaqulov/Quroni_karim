
from telebot.types import Message, ReplyKeyboardRemove


from loader import bot
from text import *
from keyboard import *
from keyboard.command_list import *



class TextMessage():
    def __init__(s, msg: Message):
        s.chat_id = msg.chat.id
        s.text = msg.text
        s.name = msg.chat.first_name
        s.user_id = msg.from_user.id
        s.msg = msg
        s.msg_id = msg.message_id

    def text_kalima(s):
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
    def manager(s):
        text = s.text

        if text == "/start":
            bot.send_message(s.chat_id, start_text, reply_markup=generate_btn(categories))
            return

        if text == "Quron Karim 🌙":
            bot.send_message(s.chat_id, text_quron, reply_markup=generate_btn(quroni_karim))
            return




        if text == "Audio 🎧":
            bot.send_message(s.chat_id, text_audio, reply_markup=generate_btn(audio))
            return

        if text == "O'zbek tilidagi Qur'oni Karim 🇺🇿":
            bot.send_message(s.chat_id, text=(s.text_kalima()), reply_markup=ReplyKeyboardRemove())
            bot.send_message(s.chat_id, text_audio_uzbek, reply_markup=audio_and_matn(text_call=uzbek_audio_btn, lst=quron_suralar))
            return

        if text == "Arab tilidagi Qur'oni Karim 🇸🇦":
            bot.send_message(s.chat_id, text=(s.text_kalima()), reply_markup=ReplyKeyboardRemove())
            bot.send_message(s.chat_id, text_audio_arab, reply_markup=audio_and_matn(text_call=arab_audio_btn, lst=quron_suralar))
            return




        if text == "Matn 📝":
            return bot.send_message(s.chat_id, text_matn, reply_markup=generate_btn(matn))

        if text == "O'zbek tilidagi Qur'oni Karim (matn) 🇺🇿":
            bot.send_message(s.chat_id, text=(s.text_kalima()), reply_markup=ReplyKeyboardRemove())
            bot.send_message(s.chat_id, text_matn_uzbek, reply_markup=audio_and_matn(text_call=uzbek_matn_btn, lst=quron_suralar))
            return

        if text == "Arab (lotin) tilidagi Qur'oni Karim (matn) 🇸🇦":
            bot.send_message(s.chat_id, text=(s.text_kalima()), reply_markup=ReplyKeyboardRemove())
            bot.send_message(s.chat_id, text_matn_uzbek, reply_markup=audio_and_matn(text_call=arab_matn_lotin_btn, lst=quron_suralar))
            return

        if text == "Arab tilidagi Qur'oni Karim (matn) 🇸🇦":
            bot.send_message(s.chat_id, text=(s.text_kalima()), reply_markup=ReplyKeyboardRemove())
            bot.send_message(s.chat_id, text_matn_uzbek, reply_markup=audio_and_matn(text_call=arab_matn_btn, lst=quron_suralar))
            return




        if text == "Taklif yuborish 📝":
            return bot.send_message(s.chat_id, text_taklif)

        if text == "Orqaga 🔙":
            return


@bot.message_handler(content_types=['text'])
def main(msg: Message):
    try:
        TextMessage(msg).manager()
        print(msg.text)
    except Exception as e:
        bot.send_message(TextMessage(msg).chat_id, f"ERROR: {e}")
        print(f"ERROR: {e}")