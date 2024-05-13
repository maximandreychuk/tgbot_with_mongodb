import pymongo
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from app import keyboards as kb
from app import database_requests
from datetime import datetime
import pprint
import random


"""Константы."""
PRETTY_DATE = datetime.today().strftime('%Y-%m-%d')

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
   await callback.message.answer(text = f'Это твой ник? {callback.from_user.username}', 
                                 reply_markup = kb.yes_is_my_username)
   
@router.callback_query(F.data=='yes_is_my_username')
async def get_all_movies(callback: CallbackQuery):
   try:
      for dic in [i for i in collection.find()]:
         if dic['username'] != callback.from_user.username:
            collection.insert_one({'username': callback.from_user.username})
         else: pass
   except KeyError:
      pass
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


@router.callback_query(F.data=='get_quentin_mov')
async def get_all_movies(callback: CallbackQuery):
   await callback.message.answer(f'{[i for i in database_requests.qt_mov]}')

@router.callback_query(F.data=='find_name_collection')
async def get_all_movies(callback: CallbackQuery):
   await callback.message.answer(text = f'{name_collection}')

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


