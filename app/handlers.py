import pymongo
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from app import keyboards as kb
import datetime
import pprint
import random


"""Константы."""
PRETTY_DATE = str(datetime.date.today()+datetime.timedelta(days=2))

"""Сэттингс БД."""
router = Router()
cluster = pymongo.MongoClient("mongodb://localhost:27017/")
base = cluster.shop
collection = base.test_reg_3

"""Состояния."""
class RegToWork(StatesGroup, State):
    name = State()
    time = State()

"""Хэндлеры."""
@router.message(Command('start'))
async def start_page(message: Message):
   await message.answer(text = 'Привет, это бот для записи куда-нибудь. Ты готов?',
                        reply_markup = kb.start_page)

@router.callback_query(F.data=='go_to_reg')
async def get_all_movies(callback: CallbackQuery):
   await callback.message.answer(text = f'Это твой ник? @{callback.from_user.username}', 
                                 reply_markup = kb.yes_is_my_username)
   
"""Проверка наличия юзера в БД."""
@router.callback_query(F.data=='yes_is_my_username')
async def get_all_movies(callback: CallbackQuery):
   lst=[]
   try:
      for dic in [i for i in collection.find()]:
         for i in dic.values():
             if i == callback.from_user.username:
                  lst.append(1)
   except KeyError: pass
   if len(lst) == 0:
      collection.insert_one({"username": callback.from_user.username})
      await callback.message.answer(text = f'Тогда, {callback.from_user.first_name}, выбирай время для записи:', 
                                    reply_markup = kb.reg_time)
   else:
      await callback.message.answer(text = f'Тогда, {callback.from_user.first_name}, выбирай время для записи:', 
                                    reply_markup = kb.reg_time)

"""Выбор времени для записи."""
@router.callback_query(F.data=='10')
async def get_all_movies(callback: CallbackQuery):
   collection.update_one({"username": callback.from_user.username},{'$set': {"date": PRETTY_DATE}})
   collection.update_one({"username": callback.from_user.username}, 
                              {'$set': {'time': '10:00'}})
   await callback.message.answer(text = 'Поздравляю ты записан на 10:00')

@router.callback_query(F.data=='14')
async def get_all_movies(callback: CallbackQuery):
   collection.update_one({"username": callback.from_user.username},{'$set': {"date": PRETTY_DATE}})
   collection.update_one({"username": callback.from_user.username}, 
                              {'$set': {'time': '14:00'}})
   await callback.message.answer(text = 'Поздравляю ты записан на 14:00')

@router.callback_query(F.data=='18')
async def get_all_movies(callback: CallbackQuery):
   collection.update_one({"username": callback.from_user.username},{'$set': {"date": PRETTY_DATE}})
   collection.update_one({"username": callback.from_user.username}, 
                              {'$set': {'time': '18:00'}})
   await callback.message.answer(text = 'Поздравляю ты записан на 18:00')

"""Добавить одну запись."""
@router.message(Command('add_one'))
async def get_all_movies(message: Message):
   collection.insert_one({'username': message.from_user.username})
   await message.answer(f'{[i for i in collection.find()]}')

"""Показать все записи."""
@router.message(Command('get_all'))
async def get_all_movies(message: Message):
   await message.answer(f'{[i for i in collection.find()]}')

"""Удаление всех записей."""
@router.callback_query(F.data=='delete_all')
async def get_all_movies(callback: CallbackQuery):
   collection.delete_many({})
   # collection.insert_one({"name": f'{callback.message.from_user.first_name}'})
   # await callback.message.answer(f'{[i for i in collection.find()]}')
   await callback.message.answer(text = 'Все записи удалены')


class Reg(StatesGroup):
    time = State()
# @router.message(Command('reg'))
# async def reg_one(message: Message, state: FSMContext):
#     await state.set_state(Reg.time)
#     await message.answer(text="Выберите время", 
#                          reply_markup = await kb.choose_kb(['12','14','16']))


