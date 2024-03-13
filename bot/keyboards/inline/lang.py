from aiogram import types

langs = types.InlineKeyboardMarkup(one_time_keyboard=True)
langs.add(types.InlineKeyboardButton('🇺🇿UZB', callback_data='uzb'),
         types.InlineKeyboardButton('🇷🇺RUS', callback_data='rus'))