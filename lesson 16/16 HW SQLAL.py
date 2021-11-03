from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Text, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'sqlite:///Sportmansqlalchemy.db', echo=True)

Base = declarative_base()



class Sportsman(Base):
    __tablename__ = 'sportsman'
    sportsman_id = Column(Integer, primary_key=True)
    sportsman_name = Column(Text)
    sportsman_rank = Column(Text)
    year_of_birth = Column(Integer)
    personal_record = Column(Integer)
    country = Column(Text)

    def __init__(self, sportsman_id, sportsman_name, sportsman_rank, year_of_birth, personal_record, country):
        self.sportsman_id = sportsman_id
        self.sportsman_name = sportsman_name
        self.sportsman_rank = sportsman_rank
        self.year_of_birth = year_of_birth
        self.personal_record = personal_record
        self.country = country

    def __repr__(self):
        return 'Sportsman {}, {} sportsman rank:{} year of birth:{} personal record:{} country:{}'.format(self.sportsman_id, self.sportsman_name, self.sportsman_rank, self.year_of_birth, self.personal_record, self.country)


class Competition(Base):
    __tablename__ = 'competition'
    competition_id = Column(Integer, primary_key=True)
    competition_name = Column(Text)
    world_record = Column(Integer)
    set_date = Column(Text)

    def __init__(self, competition_id, competition_name, world_record, set_date):
        self.competition_id = competition_id
        self.competition_name = competition_name
        self.world_record = world_record
        self.set_date = set_date

    def __repr__(self):
        return ' Competition {}, {}  world record: {} set date:{}'.format(self.competition_id, self.competition_name, self.world_record, self.set_date)


class ResultCompetition(Base):
    __tablename__ = 'result_competition'
    res_id = Column(Integer, primary_key=True)
    competition_id = Column(Integer, ForeignKey('competition.competition_id'))
    sportsman_id = Column(Integer, ForeignKey('sportsman.sportsman_id'))
    result_sportsman = Column(Integer)
    city = Column(Text)
    hold_date = Column(Text)

    def __init__(self, res_id, competition_id, sportsman_id, result_sportsman, city, hold_date):
        self.res_id = res_id
        self.competition_id = competition_id
        self.sportsman_id = sportsman_id
        self.result_sportsman = result_sportsman
        self.city = city
        self.hold_date = hold_date

    def __repr__(self):
        return 'Result of Competition {}  Competition id: {} sportsman id: {} result sportsman:{} city: {} hold date: {}'.format(self.res_id, self.competition_id, self.sportsman_id, self.result_sportsman, self.city, self.hold_date)

Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

sportsman1 = Sportsman(1, 'Роман Романович', '2', 1990, 78, 'Россия')
sportsman2 = Sportsman(2, 'Морти Сандерс', '3', 1992, 80, 'США')
sportsman3 = Sportsman(3, 'Торонто Токио', '6', 1990, 56, 'Япония')
sportsman4 = Sportsman(4, 'Рик Сандерс', '8', 1990, 99, 'Луна')
sportsman5 = Sportsman(5, 'Василий Сирч', '1', 1990, 68, 'СССР')
sportsman6 = Sportsman(6, 'Джон Блу', '3', 1991, 16, 'Великобритания')
sportsman7 = Sportsman(7, 'Нун Вей', '6', 1993, 50, 'Китай')
sportsman8 = Sportsman(8, 'Синор Сиг', '5', 1994, 30, 'Куба')
sportsman9 = Sportsman(9, 'Вероника Сова', '7', 1990, 90, 'Россия')
session.add(sportsman2)
session.add(sportsman3)
session.add(sportsman4)
session.add(sportsman5)
session.add(sportsman6)
session.add(sportsman7)
session.add(sportsman8)
session.add(sportsman9)


competition1 = Competition(1, 'Бег на 100 метров', 15, '10-02-2002')
competition2 = Competition(2, 'Бег на 500 метров', 10, '10-04-2002')
competition3 = Competition(3, 'Бег на 1000 метров', 20, '12-12-2002')
competition4 = Competition(4, 'Бег на 3000 метров', 40, '12-22-2002')
competition5 = Competition(5, 'Плавание на 500 метров', 50, '12-12-2002')
competition6 = Competition(6, 'Плавание на 1000 метров', 15, '12-12-2002')
competition7 = Competition(7, 'Плавание на 100 метров', 25, '12-12-2002')
competition8 = Competition(8, 'Марафон 3 км', 90, '12-23-2002')
competition9 = Competition(9, 'Марафон 7 км', 70, '12-15-2002')
session.add(competition1)
session.add(competition2)
session.add(competition3)
session.add(competition4)
session.add(competition5)
session.add(competition6)
session.add(competition7)
session.add(competition8)
session.add(competition9)

result1 = ResultCompetition(1, 1, 1, 30, 'Пекин', '05-15-2010')
result2 = ResultCompetition(2, 2, 2, 25, 'Москва', '05-15-2010')
result3 = ResultCompetition(3, 3, 3, 40, 'Истамбул', '05-15-2010')
result4 = ResultCompetition(4, 4, 4, 90, 'Токио', '05-15-2010')
result5 = ResultCompetition(5, 5, 5, 24, 'ЛунаСити', '05-15-2010')
result6 = ResultCompetition(6, 6, 6, 55, 'Москва', '05-15-2010')
result7 = ResultCompetition(7, 7, 7, 38, 'Пекин', '05-15-2010')
result8 = ResultCompetition(8, 8, 8, 26, 'Токио', '05-15-2010')
result9 = ResultCompetition(9, 9, 9, 82, 'Москва', '05-15-2010')
session.add(result1)
session.add(result2)
session.add(result3)
session.add(result4)
session.add(result5)
session.add(result6)
session.add(result7)
session.add(result8)
session.add(result9)


session.commit()



print('Выдайте наименование и мировые результаты по всем соревнованиям')
result_of_competition = session.query(Competition).all()
for i in result_of_competition:
    print(i)

print('Выберите дату проведения всех соревнований, проводившихся в Москве и полученные '
              'на них результаты равны 10 секунд.')
for i in session.query(ResultCompetition.hold_date).filter(ResultCompetition.city=='Москва').filter(ResultCompetition.result_sportsman > 50):
    print(i)


print('Выберите наименование и мировые результаты по всем соревнованиям, установленные 10-04-2002 или 10-25-2002.')
ourSportsman = session.query(
    ResultCompetition, Competition).filter(ResultCompetition.competition_id == Competition.competition_id).filter((Competition.set_date == '12-05-2010') | (Competition.set_date == '15-05-2010')).all()
for i in ourSportsman:
    print(i)


print('Выдайте всю информацию о спортсменах из таблицы sportsman')
Sportsmans_info = session.query(Sportsman).all()
for i in Sportsmans_info:
    print(i)

print('Выберите имена всех спортсменов, у которых персональный рекорд менее 30 с.')

ourSportsman = session.query(Sportsman).filter(
    Sportsman.personal_record < 30).all()
for i in ourSportsman:
    print(i)

print('Выберите имена всех спортсменов, которые родились в 1990 году')

ourSportsman = session.query(Sportsman).filter(
    Sportsman.year_of_birth == 1990).all()
for i in ourSportsman:
    print(i)

session.close()
