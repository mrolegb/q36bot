from datetime import datetime
from db_manager import DatabaseManager


def create_project(user_id, alias):
    db = DatabaseManager('db.db')
    db.query('''INSERT INTO projects (user_id, alias, delay, status, created)
                    VALUES (%d, '%s', 3, 'NEW', '%s')''' % (user_id, alias, datetime.now()))


def update_status(alias, status):
    db = DatabaseManager('db.db')
    db.query('''UPDATE projects SET status = '%s', updated = '%s'
                    WHERE alias = '%s' ''' % (status, datetime.now(), alias))


def set_timer(alias, timer):
    db = DatabaseManager('db.db')
    db.query('''UPDATE projects SET delay = %d, updated = '%s'
                    WHERE alias = '%s' ''' % (timer, datetime.now(), alias))


def get_project(alias):
    db = DatabaseManager('db.db')
    result = db.query('''SELECT * FROM projects
                    WHERE alias = '%s' ''' % alias)
    return u'''*Проект:*''' + str(result.fetchall()[0])


def get_all_projects():
    db = DatabaseManager('db.db')
    result = db.query('''SELECT * FROM projects''')
    all_projects = u''
    for r in result.fetchall():
        all_projects += str(r) + '''\n'''
    return all_projects


def get_question(question_id=None):
    db = DatabaseManager('db.db')
    result = db.query('''SELECT * FROM questions''')
    if question_id:
        return result.fetchall()[question_id][1]
    else:
        q = u'''*Вопросы:*\n'''
        for question in result.fetchall():
            q += (str(question[0]) + '. ' + question[1] + '\n')
        return q
