# from aiogram import Bot, Dispatcher

import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from pymongo import MongoClient 
from bson.objectid import ObjectId
from app.handlers import router

"""Настройки телеграма"""
TOKEN_API = '6383832464:AAGEfozQ4lKYMVRpzXgdfRLoYrwmqu9jdpk'
bot = Bot(token=TOKEN_API)
dp = Dispatcher()

"""Main."""
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
       
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())










# load_dotenv()
# bot = Bot(token=os.getenv('TOKEN'))
# dp = Dispatcher()


# async def main():
#     dp.include_router(router)
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     asyncio.run(main())
