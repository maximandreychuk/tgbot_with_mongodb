import pymongo
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from app import keyboards as kb
from app import database_requests
import pprint
import random

"""Сэттингс."""
router = Router()
cluster = pymongo.MongoClient("mongodb://localhost:27017/")
base = cluster.shop
collection = base.registration

"""Хэндлеры."""
@router.message(Command('start'))
async def start_page(message: Message):
   await message.answer(text = 'Выберите',
                        reply_markup = kb.start_page)

@router.callback_query(F.data=='get_one_mov')
async def get_all_movies(callback: CallbackQuery):
   await callback.message.answer(text = f'{database_requests.one_mov}')

@router.callback_query(F.data=='get_quentin_mov')
async def get_all_movies(callback: CallbackQuery):
   await callback.message.answer(f'{[i for i in database_requests.qt_mov]}')


@router.callback_query(F.data=='add_name')
async def get_all_movies(callback: CallbackQuery):
   collection.insert_one({"name": f'{callback.message.chat.id}'})
   collection.insert_one({"name": f'{callback.message.from_user.id}'})
   find_my_name = collection.find({"name": 1}, {f"{callback.message.chat.id}"})
   await callback.message.answer(f'{[i for i in collection.find()]}')


class Reg(StatesGroup):
    time = State()
# @router.message(Command('reg'))
# async def reg_one(message: Message, state: FSMContext):
#     await state.set_state(Reg.time)
#     await message.answer(text="Выберите время", 
#                          reply_markup = await kb.choose_kb(['12','14','16']))


