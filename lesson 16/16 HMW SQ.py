import sqlite3
import re

databaseFile = "E:/PycharmProjects/DlAcademy/lesson 16/Sport.db"
with sqlite3.connect(databaseFile) as conn:
    cursor = conn.cursor()

    try:
        print('Выдайте всю информацию о спортсменах из таблицы sportsman\n')
        column_names = cursor.execute("SELECT * FROM sportsman")
        col_name = [i[0] for i in column_names.description]  # Название колонны
        print(col_name)

        cursor.execute('SELECT * FROM sportsman')
        sportsman_info = cursor.fetchall()

        for i in sportsman_info:
            print(*i, sep='  ')

        print('\n')
        print('Выдайте наименование и мировые результаты по всем соревнованиям\n')
        get_column_names = cursor.execute("SELECT * from competition")
        col_name = [i[0] for i in get_column_names.description]  # Название колонны
        print(col_name)

        cursor.execute("""SELECT * from competition ; """)
        result = cursor.fetchall()

        for i in result:
            print(*i, sep='  ')

        print('\n')
        print('Выберите имена всех спортсменов, которые родились в 1990 году\n')
        cursor.execute("""SELECT sportsman_name from Sportsman WHERE year_of_birth = 1990 ; """)
        result = cursor.fetchall()
        for i in result:
            print(*i)

        print('\n')
        print('Выберите наименование и мировые результаты по всем соревнованиям, установленные 10-04-2002 или 10-25-2002.\n')
        cursor.execute("""SELECT competition_name, world_record  from competition WHERE set_date BETWEEN '10-04-2002' and '10-25-2002';""")
        result = cursor.fetchall()
        for i in result:
            print(*i, sep='   ')

        print('\n')
        print('Выберите дату проведения всех соревнований, проводившихся в Москве и полученные '
              'на них результаты равны 10 секунд.')
        cursor.execute("""SELECT hold_date from result_competition WHERE city='Москва' and  result_sportsman > 50;\n""")
        result = cursor.fetchall()
        for i in result:
            print(*i, sep='   ')

        print('\n')
        print('Выберите имена всех спортсменов, у которых персональный рекорд менее 30 с.')
        cursor.execute("""SELECT sportsman_name FROM sportsman WHERE personal_record < 30;\n""")
        result = cursor.fetchall()
        for i in result:
            print(*i, sep='   ')

        print('\n')
        print('Создать таблицу  как результат выполнения команды SELECT '
              '(любую, например, список стран спортсмены в которых никогда не занимали 1-х мест в соревнованиях')
        cursor.execute( """SELECT 
                    sportsman.country
                    from result_competition 
                    left JOIN sportsman on sportsman.sportsman_id=result_competition.sportsman_id
                    WHERE personal_record < 80
                    ;\n""")
        result = cursor.fetchall()
        for i in result:
            print(*i, sep='   ')
    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    else:
        conn.commit()
    finally:
        print(' :) ')