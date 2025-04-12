import telebot
import texts
import keyboards
from telebot import types

from database import create_tables
import dao

create_tables()

bot = telebot.TeleBot('7812813901:AAHO55hPIA3WmaBVSO2W6_JV5nkbXlscADk')


@bot.message_handler(commands=['start'])
def hello_user(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, text=texts.hello_text, reply_markup=keyboards.keyboard1)


@bot.message_handler(content_types=['text'])
def his_prod_med(message):
    if message.text == 'Історія створення':
        bot.send_message(message.chat.id, text=texts.history, reply_markup=keyboards.keyboard_back_1)

    if message.text == 'Пошук товарів':
        bot.send_message(message.chat.id, text=texts.help_or_self, reply_markup=keyboards.keyboard_2)
        bot.register_next_step_handler(message, help_or_self)

    if message.text == 'Наші соціальні мережі':
        bot.send_message(message.chat.id, text=texts.media_text, reply_markup=keyboards.keyboard_back_1)

    if message.text == 'На попередню сторінку':
        bot.send_message(message.chat.id, text=texts.hello_text, reply_markup=keyboards.keyboard1)


def help_or_self(message):
    if message.text == 'Самостійно':
        bot.send_message(message.chat.id, text=texts.all_or_search, reply_markup=keyboards.keyboard_3)

    if message.text == 'Допомога продавця':
        bot.send_message(message.chat.id, text=texts.help_text, reply_markup=keyboards.keyboard_back_2)

    if message.text == 'На попередню сторінку':
        bot.send_message(message.chat.id, text=texts.hello_text, reply_markup=keyboards.keyboard1)
        bot.register_next_step_handler(message, his_prod_med)


bot.infinity_polling()
