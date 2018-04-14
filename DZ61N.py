# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
class Person():
    def __init__(self, firsname, name, sirname):
        self.name = name
        self.sirname = sirname
        self.firsname = firsname
    @property
    def full_name(self):
        return self.firsname + ' ' + self.name + ' ' + self.sirname
class Student(Person):
    def __init__(self, firstname, name, sirname, class_room, parents):
        Person.__init__(self, firstname, name, sirname)
        self.__class_room = class_room
        self.__parents = parents
    @property
    def class_room(self):
        return self.__class_room
    @property
    def parents(self):
        print(f'{Student.full_name} parents: {self.__parents["mother"]}(mother) and {self.__parents["father"]}(father)')
        
class Techer(Person):
    def __init__(self, firstname, name, sirname, subject, class_rooms):
        Person.__init__(self, firstname, name, sirname)
        self.__subject = subject
        self.__class_rooms = class_rooms
    @property
    def subject(self):
        return self.__subject
    @property
    def class_rooms(self):
        return self.__subject
class School_class():
    __list_of_students = []
    __list_of_teachers = []
    __list_of_subjects = []
    def __init__(self, class_room_name):
        self.__class_room_name = class_room_name
    @property
    def class_room_name(self):
        return self.__class_room_name
    def list_constr_st(self, Students):
        listS = []
        for student in Students:
            if self.class_room_name == student.class_room:
                for i in len(Students):
                    listS.append(f'{i + 1}) {student.full_name}')
        self.__list_of_students = listS
    @property
    def list_of_students(self):
        return self.list_of_students
    def list_constr_teach(self, Teachers):
        listS = []
        for teacher in Teachers:
            for k in teacher.class_rooms:
                if self.class_room_name == k:
                    for i in len(Teachers):
                        listS.append(f'{i + 1}) {teacher.full_name}')
        self.__list_of_teachers = listS
    @property
    def list_of_teachers(self):
        return self.__list_of_teachers

    def list_constr_subj(self, Teachers):
        listS = []
        for teacher in Teachers:
            for k in teacher.class_rooms:
                if self.class_room_name == k:
                    for i in len(Teachers):
                        listS.append(f'{i + 1}) {teacher.subject}')
        self.__list_of_subjects = listS

    @property
    def list_of_subjects(self):
        return self.__list_of_subjects

def list_constr_classes(Students):
    listS = []
    for student in Students:
        listS.append(student.class_room)
    new_list = []
    for i in listS:
        if i not in new_list:
            new_list.append(i)
    return new_list
def list_inf_of_studets(clssses, classes, Students):
    for class_sch in classes:
        for student in Students:
            if student.class_room == School_class.class_room_name:
                print(f'{student.full_name} {student.class_room} {class_sch.list_of_teachers} {class_sch.list_of_subjects}')


# Students = [Student(..........
# classes = [7 B,......
# Teachers = [Teacher(.....