import telebot
from telebot import types



bot = telebot.TeleBot("5378684550:AAFMxFRn8d8LyOpFcfcqrxZ3WcWjp2SkNg0")



@bot.message_handler(commands=["start"])
def start(message):

    mess = f"Здравствуйте  <b>{message.from_user.first_name},  <u>{message.from_user.last_name},  используйте  коману  /help  чтобы  узнать  что  я  умею</u> </b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["новости"])
def news_ru(message):


    # текст "новости"
    news_texts = "Выберите одну страну из 'СНГ'"


    # новости мира
    news = types.InlineKeyboardMarkup(row_width=1)
    news.add(types.InlineKeyboardButton("новости Мира", url="https://ria.ru/world/"))
    
    # новости от "forbes"
    news.add(types.InlineKeyboardButton("новости от 'forbes'", url="https://www.forbes.ru/"))


    # новости России
    news.add(types.InlineKeyboardButton("новости России", url="https://www.rbc.ru/short_news"))


    # новости Украины
    news.add(types.InlineKeyboardButton("новости Украины", url="https://www.ukr.net/"))


    # новости Кыргызстана
    news.add(types.InlineKeyboardButton("новости Кыргызстана", url="https://kloop.kg/blog/category/lenta/"))


    # новости Казахстана
    news.add(types.InlineKeyboardButton("новости Казахстана", url="https://tengrinews.kz/kazakhstan_news/"))

    
    # новости Узбекистана
    news.add(types.InlineKeyboardButton("новости Узбекистана", url="https://www.gazeta.uz/ru/list/news/"))


    # новости Таджикистана
    news.add(types.InlineKeyboardButton("новости Таджикистана", url="https://asiaplustj.info/ru/news/all"))



    # новости Молдовы
    news.add(types.InlineKeyboardButton("новости Молдовы", url="https://www.kp.md/online/"))


    # новости белоруссии
    news.add(types.InlineKeyboardButton("новости Беларусии", url="https://www.belta.by/all_news"))

    
    # новости Армении
    news.add(types.InlineKeyboardButton("новости Армении", url="https://rg.ru/tema/mir/sodrugestvo/armenia/"))


    # новости Азербайджан
    news.add(types.InlineKeyboardButton("новости Азербайджан", url="https://ria.ru/location_Azerbajjdzhan/"))


    # новости о космосе
    

    #__________________#
    bot.send_message(message.chat.id, news_texts, reply_markup=news)


@bot.message_handler(commands=["help"])
def knopka(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1=types.KeyboardButton("новости")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)


@bot.message_handler(content_types="text")
def buttons(message):
    if message.text == "новости":
        return news_ru(message)
    else:
        bot.send_message(message.chat.id, "я не понял что вы имели ввиду,  используйте  коману  /help  чтобы  узнать  что  я  умею")


bot.polling(non_stop=True)
    








"""еще один способ"""
#     # новости России
#     Russian_news = types.InlineKeyboardMarkup(row_width=1)
#     Russian_news.add(types.InlineKeyboardButton("новости России", url="https://www.rbc.ru/short_news"))
#     bot.send_message(message.chat.id, news_texts, reply_markup=Russian_news)
    
#     # новости Украины
#     Ukraine_news = types.InlineKeyboardMarkup(row_width=1)
#     Ukraine_news.add(types.InlineKeyboardButton("новости Украины", url="https://www.ukr.net/"))
#     bot.send_message(message.chat.id, news_texts, reply_markup=Ukraine_news)
    
#     # новости Кыргызстана
#     Kyrgyzstan_news = types.InlineKeyboardMarkup(row_width=1)
#     Kyrgyzstan_news.add(types.InlineKeyboardButton("новости Кыргызстана", url="https://kloop.kg/blog/category/lenta/"))
#     bot.send_message(message.chat.id, "новости Кыргызстана", reply_markup=Kyrgyzstan_news)

#     # новости Казахстана
#     Kazakhstan_news = types.InlineKeyboardMarkup(row_width=1)
#     Kazakhstan_news.add(types.InlineKeyboardButton("новости Казахстана", url="https://tengrinews.kz/kazakhstan_news/"))
#     bot.send_message(message.chat.id, "новости Казахстана", reply_markup=Kazakhstan_news)


# @bot.message_handler(commands=["help"])
# def knopka(message):
#     markup=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     item1=types.KeyboardButton("новости")
#     markup.add(item1)
#     bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)


# @bot.message_handler(content_types="text")
# def buttons(message):
#     if message.text == "новости":
#         return news_ru(message)
#     else:
#         bot.send_message(message.chat.id, "я не понял что вы имели ввиду,  используйте  коману  /help  чтобы  узнать  что  я  умею")


# bot.polling(non_stop=True)