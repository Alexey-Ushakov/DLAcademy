# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.
class School:
    def __init__(self, teachers, students):
        self.teachers = teachers
        self.students = students

    def get_classes(self):
        list_classes = []
        for students in self.students:
            list_classes.append("{} {}".format(students._class_room["class_num"], students._class_room['class_char']))
        print(list(sorted(set(list_classes))))

    def get_all_students(self, a):
        list_of_name = []
        for student in self.students:
            if ("{} {}".format(student._class_room["class_num"], student._class_room['class_char'])) == a:
                list_of_name.append(student.get_full_name())
        print(list_of_name)

    def get_subject(self,f_name):
        for student in self.students:
            if f_name == student.get_full_name():
                # Разобрать разобрал сам я это конечно не повторю сразу класс в классе и из класса
                teachers = [teachers.get_full_name() for teachers in self.teachers
                            if student._class_room in teachers.teach_classes ]
                subject = [teachers.get_sub() for teachers in self.teachers
                           if student._class_room in teachers.teach_classes]
                print("{} Класс: {} {} Преподаватель: {} Предмет: {}".format
                      (student.get_full_name(), student._class_room["class_num"],
                       student._class_room['class_char'], teachers,subject))
    def get_teachers(self):
        for teachers in self.teachers:
            print(teachers.get_full_name(),teachers.get_sub())

    def get_parents_for_student(self, f_name):
        for student in self.students:
            if f_name == student.get_full_name():
                print(student._parents['Mother'],student._parents["Father"])


class Person:
    def __init__(self, name, surname, middle_name):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name

    def get_full_name(self):
        return self.surname + " " + self.name[:1] + "." + " " + self.middle_name[:1] + "."

    def set_name(self, new_name):
        self.name = new_name


class Teacher(Person, School):
    def __init__(self, name, surname, middle_name, teach_classes, subject):
        Person.__init__(self, name, surname, middle_name)
        self.teach_classes = list(map(self.convert_class, teach_classes))
        self.subject = subject

    def convert_class(self, class_room):
        return {"class_num": int(class_room.split()[0]),
                "class_char": class_room.split()[1]}
    def get_sub(self):
        return self.subject

class Student(Person, School):
    def __init__(self, name, surname, middle_name, class_room, mother, father):
        Person.__init__(self, name, surname, middle_name)
        self._parents = {'Mother': mother,
                         "Father": father }

        # Уникальный атрибут
        # self._class_room = class_room
        self._class_room = {"class_num": int(class_room.split()[0]),
                            "class_char": class_room.split()[1]}

    @property
    def get_parents(self):
        return self._parents

    @property
    def get_class_room(self):
        return "{} {}".format(self._class_room["class_num"],
                               self._class_room["class_char"])

    def next_class(self):
        self._class_room["class_num"] += 1

    def get_parants(self):
        return self._parents


# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе



teachers = [
    Teacher('Maria', 'Bogdanova', 'Vasilievna', ["6 Б", "9 B"], "Math"),
    Teacher('Андрей','Lin','Jonson',['5 А', '7 А'], "History")
    ]


students = [Student('Василий', 'Быков', 'Романов', '5 А', "R. G. None", "A. B. None" ),
    Student('Александр', 'Топов', 'Викторович', '7 А', "F. T. Ray", "M. N. Ray"),
    Student('Анатолий', 'Логинов', 'Васильевич', '6 Б', " G. S. Gas", "N. Y. Gas"),
    Student('Роман', 'Попов', 'Анатольевич', '6 Б', "T. G. Nith", "B. O. Nith"),
    Student('Павел', 'Радов', 'Радович', '5 А', "T. G. Sons", "B. A. Sons"),
    Student('Антон', 'Саланец', 'Питонович', '9 В', "T. A. Nitho", "B. U. Nitho")
    ]
school = School(teachers, students)


school.get_classes()
school.get_all_students("5 А")
school.get_subject("Быков В. Р.")
school.get_teachers()
school.get_parents_for_student("Быков В. Р.")
