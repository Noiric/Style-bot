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
    types.KeyboardButton(text='На попередню сторінку')
)

keyboard_back_2 = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    types.KeyboardButton(text='На попередню сторінку'),
    types.KeyboardButton(text='На початок')
)

keyboard_3 = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    types.KeyboardButton(text='Всі товари'),
    types.KeyboardButton(text='Пошук'),
    types.KeyboardButton(text='На попередню сторінку'),
    types.KeyboardButton(text='На початок')
)
# keyboard_search =
# keyboard_all_products =

