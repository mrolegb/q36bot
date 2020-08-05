from db_manager import DatabaseManager


def create_update_user(user_id, status):
    db = DatabaseManager('db.db')
    db.query('''INSERT OR REPLACE INTO users (user_id, status)
                    VALUES (%d, '%s')''' % (user_id, status))


def create_update_project():
    pass


def get_user_status(user_id):
    db = DatabaseManager('db.db')
    return db.query('''SELECT status FROM users WHERE user_id = %d''' % user_id).fetchall()


def get_question(question_id=None):
    db = DatabaseManager('db.db')
    result = db.query('''SELECT * FROM questions''')
    if question_id:
        return result.fetchall()[question_id][1]
    else:
        q = u'''*Вопросы:*\n'''
        for question in c.fetchall():
            q += (str(question[0]) + '. ' + question[1] + '\n')
        return q


def get_all_users():
    db = DatabaseManager('db.db')
    return db.query('''SELECT * FROM users''').fetchall()
