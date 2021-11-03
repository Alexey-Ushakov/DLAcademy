import sqlite3

databaseFile = "E:/PycharmProjects/DlAcademy/lesson 16/Sport.db"  # Путь до нашей базы данных

with sqlite3.connect(databaseFile) as conn:  # Подключение с оператором контекста чтобы сразу закрыть присоединение
    cursor = conn.cursor()  # Создание курсора для работы с базой данных
    try:
        cursor.executescript("""CREATE TABLE sportsman (
  	        sportsman_id integer PRIMARY KEY,
  	        sportsman_name TEXT,
  	        sportsman_rank TEXT,
            year_of_birth INTEGER,
  	        personal_record NUMERIC(100),
  	        country TEXT
            );        

            INSERT INTO sportsman VALUES (1, 'Роман Романович', '2', 1990, 78, 'Россия'),
            (2, 'Морти Сандерс', '3', 1992, 80, 'США'),
            (3, 'Торонто Токио', '6', 1990, 56, 'Япония'),
            (4, 'Рик Сандерс', '8', 1990, 99, 'Луна'),
            (5, 'Василий Сирч', '1', 1990, 68, 'СССР'),
            (6, 'Джон Блу', '3', 1991, 16, 'Великобритания'),
            (7, 'Нун Вей', '6', 1993, 50, 'Китай'),
            (8, 'Синор Сиг', '5', 1994, 30, 'Куба'),
            (9, 'Вероника Сова', '7', 1990, 90, 'Россия');
        """)

    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    else:
        conn.commit()
    finally:
        print('Таблица спортсменов создана')

with sqlite3.connect(databaseFile) as conn:
    cursor = conn.cursor()
    try:
        cursor.executescript("""CREATE TABLE result_competition(
                 res_id int PRIMARY key,
                 competition_id int NOT NULL,
                 sportsman_id int NOT NULL,
                 result_sportsman int NOT NULL check(result_sportsman > 0),
                 city TEXT,
                 hold_date DATE,
                 FOREIGN key(competition_id) REFERENCES competition,
                 FOREIGN key(sportsman_id) REFERENCES sportsman,
                 UNIQUE(competition_id, sportsman_id) );


                INSERT INTO result_competition VALUES (1, 1, 1, 30, 'Пекин', '05-15-2010'),
                (2, 2, 2, 25, 'Москва', '05-15-2010'),
                (3, 3, 3, 40, 'Истамбул', '05-15-2010'),
                (4, 4, 4, 90, 'Токио', '05-15-2010'),
                (5, 5, 5, 24, 'ЛунаСити', '05-15-2010'),
                (6, 6, 6, 55, 'Москва', '05-15-2010'),
                (7, 7, 7, 38, 'Пекин', '05-15-2010'),
                (8, 8, 8, 26, 'Токио', '05-15-2010'),
                (9, 9, 9, 82, 'Москва', '05-15-2010');
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    else:
        conn.commit()
    finally:
        print('Таблица результатов соревнований создана')

with sqlite3.connect(databaseFile) as conn:
    cursor = conn.cursor()
    try:
        cursor.executescript("""CREATE TABLE competition (
            competition_id integer PRIMARY key,
            competition_name TEXT,
            world_record numeric (100, 0),
            set_date DATE
            );

            INSERT INTO competition VALUES (1, 'Бег на 100 метров', 15, '10-02-2002');

            INSERT INTO competition VALUES (2, 'Бег на 500 метров', 10, '10-04-2002'),
            (3, 'Бег на 1000 метров', 20, '12-12-2002'),
            (4, 'Бег на 3000 метров', 40, '12-22-2002'),
            (5, 'Плавание на 500 метров', 50, '12-12-2002'),
            (6, 'Плавание на 1000 метров', 15, '12-12-2002'),
            (7, 'Плавание на 100 метров', 25, '12-12-2002'),
            (8, 'Марафон 3 км', 90, '12-23-2002'),
            (9, 'Марафон 7 км', 70, '12-15-2002'),
            (10, 'Марафон 21 км', 80, '10-11-2002'),
            (11, 'Марафон 30 км', 65, '12-05-2002');

        """)

    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    else:
        conn.commit()
    finally:
        print('Таблица Соревнований создана')