# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('db.db')

c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS projects''')
c.execute('''DROP TABLE IF EXISTS questions''')
c.execute('''DROP TABLE IF EXISTS answers''')

c.execute('''CREATE TABLE projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                alias TEXT, 
                status TEXT,
                user_id INTEGER, 
                delay INTEGER,
                created TIMESTAMP,
                updated TIMESTAMP
                )''')

c.execute('''CREATE TABLE questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                question TEXT
                )''')

c.execute('''CREATE TABLE answers (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                project_id INTEGER,
                question_id INTEGER,
                answer TEXT,
                created TIMESTAMP
                )''')


c.execute(u'''INSERT INTO questions (question)
VALUES
('Если бы ты мог пригласить кого-нибудь на ужин (близкого человека, умершего родственника, знаменитость), кого бы ты выбрал?'),
('Хотел бы ты быть знаменитым? В чем?'),
('Прежде чем сделать звонок, ты репетируешь свою реплику? Почему?'),
('Каким был бы для тебя «идеальный день»?'),
('Когда ты в последний раз пел в одиночестве? А для кого-нибудь другого?'),
('Если бы ты могли прожить до 90 лет и в последние 60 лет сохранить либо разум, либо тело 30-летнего, что бы ты выбрал?'),
('У тебя есть тайное предчувствие того, как ты умрешь?'),
('Назови три черты, которые, по-твоему, есть и у тебя, и у твоего партнера.'),
('За что ты испытываешь наибольшую благодарность?'),
('Если бы ты мог, что бы ты изменил в том, как тебя воспитывали?'),
('За 4 минуты расскажи партнеру историю твоей жизни настолько подробно, насколько это возможно.'),
('Если бы ты мог проснуться завтра, обладая каким-то умением или способностью, что бы это было?'),
('Если бы магический кристалл мог открыть тебе правду, о чем бы ты хотел узнать?'),
('Есть ли что-то, что ты уже давно мечтаешь сделать? Почему ты еще не сделал этого?'),
('Самое большое достижение в твоей жизни?'),
('Что в дружбе для тебя наиболее ценно?'),
('Какое твое самое дорогое воспоминание?'),
('А самое ужасное воспоминание?'),
('Если бы ты знал, что умрешь через год, что бы ты изменил в том, как ты живете? Почему?'),
('Что для тебя значит дружба?'),
('Какую роль любовь и нежность играют в твоей жизни?'),
('По очереди называй партнеру его положительные черты (обменяйтесь пятью характеристиками).'),
('В твоей семье отношения теплые и близкие?'),
('Что ты чувствуешь в связи с твоими отношениями с матерью?'),
('Составьте каждый по три утверждения, верных для вас обоих. Например, «Мы оба сейчас чувствуем…»'),
('Продолжите фразу: «Я бы хотел, чтобы был кто-то, с кем можно разделить…»'),
('Если ты собирался стать близким другом для твоего партнера, что бы ты ему рассказал прямо сейчас?'),
('Расскажи партнеру, что тебе нравится в нем; говори прямо, произноси вещи, которые ты не мог бы сказать случайному знакомому.'),
('Поделись с парт­нером неприятной ситуацией или смущающим моментом из твоей жизни.'),
('Когда ты в последний раз плакал при ком-нибудь? А в одиночестве?'),
('Расскажи своему партнеру, что ты уже сейчас ценишь в нем (в ней).'),
('По-твоему, какая тема слишком серьезна, чтобы шутить об этом?'),
('Если бы ты должен был умереть сегодня до конца дня, ни с кем не поговорив, о чем несказанном ты бы больше всего жалел? Почему ты еще не сказал этого?'),
('Твой дом со всем имуществом загорелся. После спасения близких и домашних животных у тебя есть время, чтобы забежать в дом и спасти еще что-то. Что бы ты взял? Почему?'),
('Смерть кого из членов твоей семьи расстроила бы тебя больше всего? Почему?'),
('Поделись личной проблемой и спроси партнера, как он бы справился с ней. Затем спроси, что он думает о твоих чувствах по поводу этой проблемы.')
''')


conn.commit()

conn.close()
