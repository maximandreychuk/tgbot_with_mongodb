from aiogram.types import (ReplyKeyboardMarkup,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton,
                           KeyboardButton
                           )
from datetime import datetime


go_to_reg = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Погнали')]],resize_keyboard=True)

start_page = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'Погнали! Сегодня запись на {datetime.now().day+1}-{datetime.now().month}-{datetime.now().year}',
                          callback_data='go_to_reg')],
])
yes_is_my_username = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'Да',
                          callback_data='yes_is_my_username')],
])
reg_time = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='10:00', callback_data='10')],
    [InlineKeyboardButton(text='14:00', callback_data='14')],
    [InlineKeyboardButton(text='18:00', callback_data='18')],
])
main_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Показать первый фильм', callback_data='get_one_mov')],
    [InlineKeyboardButton(text='Фильмы Квентина', callback_data='get_quentin_mov')],
    [InlineKeyboardButton(text='Удалить все записи', callback_data='delete_all')],
    [InlineKeyboardButton(text='Узнать дату записи', callback_data='find_name_collection')],
])

async def choose_kb(lst):
    kb=[KeyboardButton(text=item) for item in lst]
    return ReplyKeyboardMarkup(keyboard=[kb], resize_keyboard=True)