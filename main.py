from db import get_question
from secure import API_KEY
from aiogram import Bot, Dispatcher, executor, types

import logging


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_KEY)

dp = Dispatcher(bot)


@dp.message_handler(commands=['questions'])
async def echo(message: types.Message):
    await message.answer(get_question(), parse_mode='Markdown')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
