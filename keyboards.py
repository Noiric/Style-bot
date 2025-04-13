from telebot import types

keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    types.KeyboardButton(text='Історія створення'),
    types.KeyboardButton(text='Пошук товарів'),
    types.KeyboardButton(text='Наші соціальні мережі')
)

keyboard_back_1 = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    types.KeyboardButton(text='На попередню сторінку')
)

keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    types.KeyboardButton(text='Самостійно'),
    types.KeyboardButton(text='Допомога продавця'),
    types.KeyboardButton(text='На головну')
)

keyboard_back = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    types.KeyboardButton(text='На попередню сторінку'),
    types.KeyboardButton(text='На головну')
)

keyboard_back_all = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    types.KeyboardButton(text='До всіх товарів'),
    types.KeyboardButton(text='На попередню сторінку'),
    types.KeyboardButton(text='На головну')
)

keyboard_3 = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    types.KeyboardButton(text='Всі товари'),
    types.KeyboardButton(text='Пошук'),
    types.KeyboardButton(text='На попередню сторінку'),
    types.KeyboardButton(text='На головну')
)
keyboard_search = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    types.KeyboardButton(text='За сезонністю'),
    types.KeyboardButton(text='За типом одягу'),
    types.KeyboardButton(text='За ціною'),
    types.KeyboardButton(text='За брендом'),
    types.KeyboardButton(text='На попередню сторінку'),
    types.KeyboardButton(text='На головну')
)

keyboard_all_products = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
                           types.KeyboardButton(text='Замовити'),
                           types.KeyboardButton(text='Пошук'),
                           types.KeyboardButton(text='Допомога'),
                           types.KeyboardButton(text='На попередню сторінку'),
                           types.KeyboardButton(text='На головну')
)

buy_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    types.KeyboardButton(text='На попередню сторінку'),
    types.KeyboardButton(text='На головну')
)
