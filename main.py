# -*- coding: utf-8 -*-

from db_commands import get_question, create_project, get_project, get_all_projects, set_timer, update_status
from secure import API_KEY, ADMIN_ID
from aiogram import Bot, Dispatcher, executor, types

import logging


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_KEY)

dp = Dispatcher(bot)


@dp.message_handler(commands=['questions'])
async def get_questions(message: types.Message):
    await message.answer(get_question(), parse_mode='Markdown')


@dp.message_handler()
async def read_input(message: types.Message):
    if u'-добавить' in message.text:
        name = message.text.split()[-1]
        create_project(message.from_user.id, name)
        await message.answer(u'*Создан проект:* ' + name, parse_mode='Markdown')

    if u'-показать' in message.text:
        if u'все' in message.text:
            projects = get_all_projects()
            await message.answer(u'*Проекты:*\n' + projects, parse_mode='Markdown')
            return
        name = message.text.split()[-1]
        project = get_project(name)
        await message.answer(u'*Проект ' + name + ':*\n' + project, parse_mode='Markdown')

    if u'-таймер' in message.text:
        name = message.text.split()[-2]
        timer = None
        try:
            timer = int(message.text.split()[-1])
        except ValueError:
            await message.answer(u'*Введите число.*', parse_mode='Markdown')
        set_timer(name, timer)
        await message.answer(u'Для проекта ' + name + u' установлен таймер на ' + str(timer) + u' дней.',
                             parse_mode='Markdown')

    if u'-запустить' in message.text:
        name = message.text.split()[-1]
        update_status(name, 'ACTIVE')
        await message.answer(u'*Запущен проект:* ' + name, parse_mode='Markdown')

    if u'-остановить' in message.text:
        name = message.text.split()[-1]
        update_status(name, 'STOPPED')
        await message.answer(u'*Остановлен проект:* ' + name, parse_mode='Markdown')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
