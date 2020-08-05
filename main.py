# -*- coding: utf-8 -*-

from db_commands import get_question, create_update_user, get_user_status, get_all_users
from secure import API_KEY
from aiogram import Bot, Dispatcher, executor, types

import logging


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_KEY)

dp = Dispatcher(bot)


@dp.message_handler(commands=['questions'])
async def get_questions(message: types.Message):
    await message.answer(get_question(), parse_mode='Markdown')


@dp.message_handler(commands=['new_project'])
async def ready_user(message: types.Message):
    create_update_user(message.from_user.id, 'NEW_PROJECT')
    await message.answer(u'Введите название проекта:', parse_mode='Markdown')


@dp.message_handler()
async def read_input(message: types.Message):
    users = get_user_status(message.from_user.id)
    if users:
        current_status = users[0][0]
        if current_status == 'NEW_PROJECT':
            pass
    else:
        await message.answer(u'Может новый проектик хотите завести?')


@dp.message_handler(commands=['users'])
async def get_users(message: types.Message):
    await message.answer(get_all_users())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
