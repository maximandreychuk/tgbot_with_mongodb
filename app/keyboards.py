from aiogram.types import (ReplyKeyboardMarkup,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton,
                           KeyboardButton
                           )

go_to_reg = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Погнали')]],resize_keyboard=True)


start_page = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Показать первый фильм', callback_data='get_one_mov')],
    [InlineKeyboardButton(text='Фильмы Квентина', callback_data='get_quentin_mov')],
    [InlineKeyboardButton(text='Добавить имя', callback_data='add_name')],
    [InlineKeyboardButton(text='year 1999', callback_data='1999')],
])

async def choose_kb(lst):
    kb=[KeyboardButton(text=item) for item in lst]
    return ReplyKeyboardMarkup(keyboard=[kb], resize_keyboard=True)