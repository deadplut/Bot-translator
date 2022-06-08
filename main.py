from telebot import types
import telebot
from googletrans import Translator
import config

bot = telebot.TeleBot(config.tok)


def translater(text, lang='en'):
    translator = Translator()
    return translator.translate(text, dest=lang).text


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("английский")
    btn2 = types.KeyboardButton("французский")
    btn3 = types.KeyboardButton("русский")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Давай что-нибудь переведём! Выбери язык".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):

    languages = {
        "английский": 'en',
        "французский": 'fr',
        "русский": 'ru',
    }

    if (message.text in languages.keys()):
        global language
        language = languages[message.text]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться к выбору языка")
        markup.add(back)
        bot.send_message(message.chat.id, text="Выбран {}!".format(message.text), reply_markup=markup)



    elif (message.text == "Вернуться к выбору языка"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("английский")
        btn2 = types.KeyboardButton("французский")
        btn3 = types.KeyboardButton("русский")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         text="И снова ты, {0.first_name}! Давай ещё что-нибудь переведём! Выбери язык".format(
                             message.from_user), reply_markup=markup)

    else:
        bot.send_message(message.chat.id, text=translater(message.text, language))


if __name__ == '__main__':
    bot.infinity_polling()
