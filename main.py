import telebot
import texts
import keyboards
from telebot import types

from database import create_tables
import dao

create_tables()

bot = telebot.TeleBot('7812813901:AAHO55hPIA3WmaBVSO2W6_JV5nkbXlscADk')


def product_post(message, product):
    bot.send_photo(message.chat.id, caption=f'{product.name}\n\n'
                                            f'{product.description}\n\n'
                                            f'{product.price}\n\n'
                                            f'Для замовлення пишіть до @DmytroChagayda. \n'
                                            f'Є можливіть отримати знижку!!!',
                   photo=product.image)


@bot.message_handler(commands=['start'])
def hello_user(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, text=texts.hello_text, reply_markup=keyboards.keyboard1)


@bot.message_handler(content_types=['text'])
def his_prod_med(message):
    if message.text == 'Історія створення':
        bot.send_message(message.chat.id, text=texts.history, reply_markup=keyboards.keyboard_back_1)
        bot.register_next_step_handler(message, his_prod_med)

    if message.text == 'Пошук товарів':
        bot.send_message(message.chat.id, text=texts.help_or_self, reply_markup=keyboards.keyboard_2)
        bot.register_next_step_handler(message, help_or_self)

    if message.text == 'Наші соціальні мережі':
        bot.send_message(message.chat.id, text=texts.media_text, reply_markup=keyboards.keyboard_back_1)
        bot.register_next_step_handler(message, his_prod_med)

    if message.text == 'На попередню сторінку':
        bot.send_message(message.chat.id, text=texts.hello_text, reply_markup=keyboards.keyboard1)
        bot.register_next_step_handler(message, his_prod_med)


def help_or_self(message):
    if message.text == 'Самостійно':
        bot.send_message(message.chat.id, text=texts.all_or_search, reply_markup=keyboards.keyboard_3)
        bot.register_next_step_handler(message, search_or_all)

    if message.text == 'Допомога продавця':
        bot.send_message(message.chat.id, text=texts.help_text, reply_markup=keyboards.keyboard_back)
        bot.register_next_step_handler(message, help_or_self)

    if message.text == 'На попередню сторінку':
        bot.send_message(message.chat.id, text=texts.help_or_self, reply_markup=keyboards.keyboard_2)
        bot.register_next_step_handler(message, help_or_self)

    if message.text == 'На головну':
        bot.send_message(message.chat.id, text=texts.hello_text, reply_markup=keyboards.keyboard1)
        bot.register_next_step_handler(message, his_prod_med)


def search_or_all(message):
    if message.text == 'Всі товари':
        products = dao.get_all_product()
        for product in products:
            product_post(message, product)
        bot.send_message(message.chat.id, text='Для пошуку окремого виду товару, перейдіть до пошуку',
                         reply_markup=keyboards.keyboard_all_products)
        bot.register_next_step_handler(message, all_products)

    if message.text == 'Пошук':
        bot.send_message(message.chat.id, text=texts.search_text, reply_markup=keyboards.keyboard_search)
        bot.register_next_step_handler(message, search)

    if message.text == 'На попередню сторінку':
        bot.send_message(message.chat.id, text=texts.help_or_self, reply_markup=keyboards.keyboard_2)
        bot.register_next_step_handler(message, help_or_self)

    if message.text == 'На головну':
        bot.send_message(message.chat.id, text=texts.hello_text, reply_markup=keyboards.keyboard1)
        bot.register_next_step_handler(message, his_prod_med)


def all_products(message):
    if message.text == 'Замовити':
        bot.send_message(message.chat.id, text=texts.buy_text, reply_markup=keyboards.buy_keyboard)

    if message.text == 'Пошук':
        bot.send_message(message.chat.id, text=texts.search_text, reply_markup=keyboards.keyboard_search)
        bot.register_next_step_handler(message, search)

    if message.text == 'Допомога':
        bot.send_message(message.chat.id, text=texts.help_text, reply_markup=keyboards.keyboard_back)
        bot.register_next_step_handler(message, help_from_all)

    if message.text == 'На попередню сторінку':
        bot.send_message(message.chat.id, text=texts.all_or_search, reply_markup=keyboards.keyboard_3)
        bot.register_next_step_handler(message, search_or_all)

    if message.text == 'На головну':
        bot.send_message(message.chat.id, text=texts.hello_text, reply_markup=keyboards.keyboard1)
        bot.register_next_step_handler(message, his_prod_med)


def help_from_all(message):
    if message.text == 'На головну':
        bot.send_message(message.chat.id, text=texts.hello_text, reply_markup=keyboards.keyboard1)
        bot.register_next_step_handler(message, his_prod_med)

    if message.text == 'На попередню сторінку':
        products = dao.get_all_product()
        for product in products:
            product_post(message, product)
        bot.send_message(message.chat.id, text='Для пошуку окремого виду товару, перейдіть до пошуку',
                         reply_markup=keyboards.keyboard_all_products)
        bot.register_next_step_handler(message, all_products)


def search(message):
    if message.text == 'На попередню сторінку':
        bot.send_message(message.chat.id, text=texts.all_or_search, reply_markup=keyboards.keyboard_3)
        bot.register_next_step_handler(message, search_or_all)

    if message.text == 'На головну':
        bot.send_message(message.chat.id, text=texts.hello_text, reply_markup=keyboards.keyboard1)
        bot.register_next_step_handler(message, his_prod_med)

    if message.text == 'За брендом':
        bot.send_message(message.chat.id, text=texts.search_by_brand, reply_markup=keyboards.keyboard_back)
        bot.register_next_step_handler(message, search_by_brand)

    if message.text == 'За сезонністю':
        bot.send_message(message.chat.id, text=texts.search_by_season, reply_markup=keyboards.keyboard_back)
        bot.register_next_step_handler(message, search_by_season)

    if message.text == 'За типом одягу':
        bot.send_message(message.chat.id, text=texts.search_by_type, reply_markup=keyboards.keyboard_back)
        bot.register_next_step_handler(message, search_by_type)


def search_by_brand(message):
    if message.text == 'На попередню сторінку':
        bot.send_message(message.chat.id, text=texts.search_text, reply_markup=keyboards.keyboard_search)
        bot.register_next_step_handler(message, search)

    elif message.text == 'На головну':
        bot.send_message(message.chat.id, text=texts.hello_text, reply_markup=keyboards.keyboard1)
        bot.register_next_step_handler(message, his_prod_med)

    else:
        products = dao.get_product_by_brand(message.text)
        if products:
            for product in products:
                product_post(message, product)
            bot.send_message(message.chat.id, text=texts.after_search, reply_markup=keyboards.keyboard_back)
            bot.register_next_step_handler(message, search_by_brand)

        else:
            bot.send_message(message.chat.id, text=texts.negative_search, reply_markup=keyboards.keyboard_back)
            bot.register_next_step_handler(message, search_by_brand)


def search_by_season(message):
    if message.text == 'На попередню сторінку':
        bot.send_message(message.chat.id, text=texts.search_text, reply_markup=keyboards.keyboard_search)
        bot.register_next_step_handler(message, search)

    elif message.text == 'На головну':
        bot.send_message(message.chat.id, text=texts.hello_text, reply_markup=keyboards.keyboard1)
        bot.register_next_step_handler(message, his_prod_med)

    else:
        products = dao.get_product_by_season(message.text)
        if products:
            for product in products:
                product_post(message, product)
            bot.send_message(message.chat.id, text=texts.after_search, reply_markup=keyboards.keyboard_back)
            bot.register_next_step_handler(message, search_by_season)

        else:
            bot.send_message(message.chat.id, text=texts.negative_search, reply_markup=keyboards.keyboard_back)
            bot.register_next_step_handler(message, search_by_season)


def search_by_type(message):
    if message.text == 'На попередню сторінку':
        bot.send_message(message.chat.id, text=texts.search_text, reply_markup=keyboards.keyboard_search)
        bot.register_next_step_handler(message, search)

    elif message.text == 'На головну':
        bot.send_message(message.chat.id, text=texts.hello_text, reply_markup=keyboards.keyboard1)
        bot.register_next_step_handler(message, his_prod_med)

    else:
        products = dao.get_product_by_type(message.text)
        if products:
            for product in products:
                product_post(message, product)
            bot.send_message(message.chat.id, text=texts.after_search, reply_markup=keyboards.keyboard_back)
            bot.register_next_step_handler(message, search_by_season)

        else:
            bot.send_message(message.chat.id, text=texts.negative_search, reply_markup=keyboards.keyboard_back)
            bot.register_next_step_handler(message, search_by_season)


bot.infinity_polling()
