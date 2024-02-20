from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Uzbek', callback_data='uzbek'),InlineKeyboardButton(text='Turk', callback_data='turk')],

])
