class Student:
    def __init__(self, name, surname, gender):
        # print('Student init is called!')
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self) -> str:
        print_courses_in_progress = ', '.join(self.courses_in_progress)
        print_finished_courses = ', '.join(self.finished_courses)
        return f"Студент\n\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:\nКурсы в процессе изучения: {print_courses_in_progress}\nЗавершенные курсы: {print_finished_courses}\n"
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # print('Lecturer init is called!')
        self.lecturer_grades = {}
    def __str__(self) -> str:
        return f"Лектор\n\nИмя: {self.name}\nФамилия: {self.surname}\n"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # print('Reviewer init is called!')
    def __str__(self) -> str:
        return f"\nПроверяющий\n\nИмя: {self.name}\nФамилия: {self.surname}\n"
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(some_lecturer, 'Python', 9)
some_student.rate_hw(some_lecturer, 'Python', 8)

# print(some_lecturer.lecturer_grades)

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)

print(some_reviewer)
print(some_lecturer)
print(some_student)

# print(some_student.grades)