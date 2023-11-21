from pprint import pprint

import requests
from .to_lotin import to_latin
from keyboard.command_list import quron_suralar


class GetSurah():
    def __init__(self, language: str = None, sura: int = None, all_ayat: int = None, ayat: int = None):
        self.language = language
        self.sura = sura
        self.all_ayat = all_ayat
        self.ayat = ayat
        self.uzbek = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-alaaudeenmansou.min.json"
        self.arab_lotin = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ara-quran-la1.min.json"
        self.arab = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ara-jalaladdinalmah.min.json"

    def get_url_json(self):
        if self.language == "uzbek":
            get = requests.get(self.uzbek)
        elif self.language == "arab_lotin":
            get = requests.get(self.arab_lotin)
        else:
            get = requests.get(self.arab)
        return get.json()

    def get_sura_text(self):
        get_list = [i for i in self.get_url_json()['quran']]
        get_sura_info = [i['text'] for i in get_list if i['chapter'] == self.sura]
        return get_sura_info

    def get_oyat_text(self):
        sura_len = len(self.get_sura_text())
        if self.all_ayat == True:
            get_ayat =  self.get_sura_text()
            surah = ''
            count = 1
            for i in get_ayat:
                surah += (str(count) + " :  " + to_latin(i) + "\n")
                count += 1
            # SURAH SEND PORT
            get_ayat_1 =  f'<b><i>🌙 {quron_suralar[self.sura]} surasi 🌙 :</i></b>\n\n'\
                   f'{surah}'

        elif self.ayat <= sura_len:
            get_ayat = self.get_sura_text()[self.ayat - 1]
            get_ayat_1 = to_latin(get_ayat)
        else:
            get_ayat_1 = "Xato"

        return get_ayat_1

    def get_count(self):
        return self.get_sura_text()









olish = GetSurah(language ="arab_lotin", sura=114, all_ayat=True).get_sura_text()


# gete = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions.json").json()
#
# pprint(gete)



# def get_surah(self, text:str):
#     response = self.get_link_author(self.author)
#     syn = [':']
#     try:
#         for i in syn:
#             if i in text:
#                 res = text.split(':')
#                 if int(res[0]) <= 114:
#                     ayat = int(res[1])
#                     sura = int(res[0])
#                     get_list = [i for i in response['quran']]
#                     get_sura_info = [i['text'] for i in get_list if i['chapter'] == sura]
#                     sura_len = len(get_sura_info)
#                     if ayat <= sura_len:
#                         get_ayat = get_sura_info[ayat - 1]
#
#                         # SURAH SEND PORT
#
#                         return f'<b><i>🌙  {self.quran_sura_nomlari[sura]} surasi  🌙 </i></b> :\n\n' \
#                                f'<i>✨ {ayat}:  {to_latin(get_ayat)}</i>'
#
#                     else:
#                         text_1 = f'🟢 Siz qidirayotgan Surada <b>{sura_len}</b> ta oyat bor ‼️\n' \
#                                  f'🔴 {sura_len} sonidan  katta son kiritmang. \n\n'
#                         return text_1
#                 else:
#                     text_3 ="☝️<b>Quroni Karim</b>da 114 ta sura bor.\n" \
#                             "❌ Birinchi raqamni 114 dan katta kiritmang ‼️\n\n"
#                     return text_3
#             else:
#
#                 if text.isdigit():
#                     text = int(text)
#                     if text <= 114:
#                         text_num = int(text)
#                         get_list = [i for i in response['quran']]
#                         get_sura_info = (i['text'] for i in get_list if i['chapter'] == text_num)
#                         surah = ''
#                         count = 1
#                         for i in get_sura_info:
#                             surah += (str(count) + " :  " + to_latin(i) + "\n")
#                             count += 1
#
#                         # SURAH SEND PORT
#
#
#                         return f'<b><i>🌙 {self.quran_sura_nomlari[text_num]} surasi 🌙 :</i></b>\n\n'\
#                                f'{surah}'
#                     else:
#                         return '☝️<b>Quroni Karim</b>da 114 ta sura bor.\n' \
#                                '❌ Birinchi raqamni 114 dan katta kiritmang!'
#
#                 text_2 = f"❌ Harflar va so'zlar orqali qidirishga urinmang.\n" \
#                          f"✅ Raqamlardan foydalaning\n" \
#                          f"➡️1\n" \
#                          f"➡️1:1"
#
#                 return text_2
#     except:
#         return f"❌ Harflar va so'zlar orqali qidirishga urinmang.\n" \
#                          f"✅ Raqamlardan foydalaning\n" \
#                          f"➡️1\n" \
#                          f"➡️1:1"
    #
