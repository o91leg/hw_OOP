class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.ave_grades = 0

    def __str__(self):
        if not isinstance(self, Student):
             print('Not a Student!')
             return
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнии задания: {self.ave_grades}\n' \
               f'Курсы в процесе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                if grade > 1 and grade < 10:
                    lecturer.grades[course] += [grade]
                else:
                    return 'Оценка должнабыть от 1 до 10'
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def raiting(self):
        if not isinstance(self, Student):
            print('Not a Student!')
            return
        for v in self.grades.values():
            self.ave_grades = round(sum(v) / len(v), 1)
        return self.ave_grades

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        if self.ave_grades > other.ave_grades:
            return f'Средняя оценка {self.ave_grades} {self.name} больше оценки {other.ave_grades} {other.name}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.ave_grades = 0

    def __str__(self):
        if not isinstance(self, Lecturer):
             print('Not a Lecturer!')
             return
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.ave_grades}'

    def raiting(self):
        for v in self.grades.values():
            self.ave_grades = round(sum(v) / len(v), 1)

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Student!')
            return
        if self.ave_grades > other.ave_grades:
            return f'Средняя оценка {self.ave_grades} {self.name} больше оценки {other.ave_grades} {other.name}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        if not isinstance(self, Reviewer):
             print('Not a Reviewer!')
             return
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                if grade > 1 and grade < 10:
                    student.grades[course] += [grade]
                else:
                    return 'Оценка должнабыть от 1 до 10'
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

student1 = Student('Oleg', 'Polovinkin', 'Male')
student1.finished_courses += ['Ruby']
student1.courses_in_progress += ['Python']

student2 = Student('Masha', 'Polovinkina', 'Female')
student2.finished_courses += ['Ruby']
student2.courses_in_progress += ['Python']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']
reviewer1.rate_hw(student1, 'Python', 3)
reviewer1.rate_hw(student1, 'Python', 6)
reviewer1.rate_hw(student1, 'Python', 7)

reviewer1.rate_hw(student2, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 5)

lectur1 = Lecturer('Ben', 'Aflic')
lectur1.courses_attached +=['Python']
lectur2 = Lecturer('Peter', 'Parker')
lectur2.courses_attached +=['Python']

student1.rate_lecturer(lectur1, 'Python', 3)
student1.rate_lecturer(lectur1, 'Python', 6)
student1.rate_lecturer(lectur1, 'Python', 7)

student2.rate_lecturer(lectur2, 'Python', 9)
student2.rate_lecturer(lectur2, 'Python', 3)
student2.rate_lecturer(lectur2, 'Python', 1)

student1.raiting()
print(student1)
print('')
student2.raiting()
print(student2)
print(student1 < student2)
print('______________')
lectur1.raiting()
print(lectur1)
print('')
lectur2.raiting()
print(lectur2)
print(lectur1 < lectur2)
print('_________________')
all_students = []
all_students.append(student1.__dict__)
all_students.append(student2.__dict__)

def grades(all_students, course):
    all_grades = []
    for val in all_students:
        all_grades.extend(val['grades'][course])
    print(f'Средняя оценка {round(sum(all_grades) / len(all_grades), 1)} студентов по курсу {course}')

grades(all_students, 'Python')

all_lectur = []
all_lectur.append(lectur1.__dict__)
all_lectur.append(lectur2.__dict__)

def grades(all_lectur, course):
    all_grades = []
    for val in all_lectur:
        all_grades.extend(val['grades'][course])
    print(f'Средняя оценка {round(sum(all_grades) / len(all_grades), 1)} лекторов по курсу {course}')

grades(all_lectur, 'Python')
