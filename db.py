import sqlite3


def get_db():
    conn = sqlite3.connect('db.db')
    return conn.cursor()


def get_question(question_id=None):
    c = get_db()
    c.execute('''SELECT * FROM questions''')
    if question_id:
        return c.fetchall()[question_id][1]
    else:
        q = u'''*Вопросы:*\n'''
        for question in c.fetchall():
            q += (str(question[0]) + '. ' + question[1] + '\n')
        return q
