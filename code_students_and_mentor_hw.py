class Student:

# Конструктор класса Student.  
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Метод выставления оценок студентов лекторам за лекции.  
    def rate_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'
        
    # Метод вычисления средней оценки студента за домашнии работы.  
    def get_average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)
    
    # Магический метод сравнения студентов по средней оценке за домашние задания.  
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

    # Магический метод вывода на печать экземпляра класса в виде строки.  
    def __str__(self) -> str:
        print_courses_in_progress = ', '.join(self.courses_in_progress)
        print_finished_courses = ', '.join(self.finished_courses)
        average_grade = round(self.get_average_grade(), 1)
        return f"Студент\n\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {print_courses_in_progress}\nЗавершенные курсы: {print_finished_courses}\n"
        

class Mentor:

    # Конструктор класса Mentor.  
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    # Магический метод вывода на печать экземпляра класса в виде строки.  
    def __str__(self) -> str:
        return f"Ментор\n\nИмя: {self.name}\nФамилия: {self.surname}\n"
    
        
class Lecturer(Mentor):

    # Конструктор дочернего класса Lecturer.  
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    # Метод вычисления средней оценки лектора за лекцию.  
    def get_average_grade(self):
        all_grades = []
        for grades in self.lecturer_grades.values():
            all_grades.extend(grades)
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)
    
    # Магический метод сравнения лекторов по средней оценке за лекцию.  
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

    # Магический метод вывода на печать экземпляра класса в виде строки.  
    def __str__(self) -> str:
        average_grade = round(self.get_average_grade(), 1)
        return f"Лектор\n\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}\n"
    

class Reviewer(Mentor):

    # Конструктор дочернего класса Reviewer.  
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Магический метод вывода на печать экземпляра класса в виде строки.  
    def __str__(self) -> str:
        return f"\nПроверяющий\n\nИмя: {self.name}\nФамилия: {self.surname}\n"
    
    # Метод выставление оценки проверяющим студенту.  
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        

# Создание первого экземляра класса Studеnt.  
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

# Создание второго экземляра класса Student.  
some_student1 = Student('Ivan', 'Belov', 'your_gender')
some_student1.courses_in_progress += ['Python', 'Git']
some_student1.finished_courses += ['Введение в программирование']

# Создание первого экземляра класса Mentor.  
some_mentor = Mentor('Some', 'Buddy')
some_mentor.courses_attached += ['Python']

# Создание второго экземляра класса Mentor.  
some_mentor1 = Mentor('Mark', 'Grizzly')
some_mentor1.courses_attached += ['Python']

# Создание первого экземляра дочернего класса Lecturer.  
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

# Создание второго экземляра дочернего класса Lecturer.  
some_lecturer1 = Lecturer('Mark', 'Grizzly')
some_lecturer1.courses_attached += ['Python']

# Вызов метода rate_lecturers для первого экземпляра в дочернем классе Lecturer.  
some_student.rate_lecturers(some_lecturer, 'Python', 10)
some_student.rate_lecturers(some_lecturer, 'Python', 10)
some_student.rate_lecturers(some_lecturer, 'Python', 10)

# Вызов метода rate_lecturers для второго экземпляра в дочернем классе Lecturer.  
some_student1.rate_lecturers(some_lecturer1, 'Python', 9)
some_student1.rate_lecturers(some_lecturer1, 'Python', 9)
some_student1.rate_lecturers(some_lecturer1, 'Python', 9)

# Создание первого экземляра дочернего класса Reviewer.  
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

# Создание второго экземляра дочернего класса Reviewer.  
some_reviewer1 = Reviewer('Petr', 'Sidorof')
some_reviewer1.courses_attached += ['Python']

# Вызов метода rate_hw для первого экземпляра в классе Student.  
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)

# Вызов метода rate_hw для второго экземпляра в классе Student.  
some_reviewer1.rate_hw(some_student1, 'Python', 10)
some_reviewer1.rate_hw(some_student1, 'Python', 10)
some_reviewer1.rate_hw(some_student1, 'Python', 10)

# Печать результатов.  
print(some_reviewer)
print(some_reviewer1)
print(some_lecturer)
print(some_lecturer1)
print(some_student)
print(some_student1)
print(some_mentor)
print(some_mentor1)

# Вычисление и сортировка по убыванию средней оценки за домашнее задание студентов и лекторов по средней оценке за лекцию.  
students = [some_student, some_student1]
lecturers = [some_lecturer, some_lecturer1]

sorted_students = sorted(students, reverse=True)
sorted_lecturers = sorted(lecturers, reverse=True)

# Вывод на печать результатов.  
print("Студенты, упорядоченные по средней оценке за домашние задания (по убыванию):\n")
for student in sorted_students:
    print(student)

print("Лекторы, упорядоченные по средней оценке за лекции (по убыванию):\n")
for lecturer in sorted_lecturers:
    print(lecturer)


# Функция - вычисление и вывод на печать средней оценки за домашнее задание студентов одного курса.  
def calculate_course_average(students, course_name):
    total_grades = []
    for student in students:
        if course_name in student.grades:
            total_grades.extend(student.grades[course_name])

    if not total_grades:
        average_grade = 0
    else:
        average_grade = sum(total_grades) / len(total_grades)

    print(f'Курс: {course_name}\nСредняя оценка за домашние задания: {average_grade:.1f}\n')

# Вызов функции calculate_course_average.  
students_list = [some_student, some_student1]
calculate_course_average(students_list, 'Python')


# Функция - вычисление и вывод на печать средней оценки за лекции лекторов одного курса.  
def calculate_lectors_course_average(lectors, course_name):
    total_grades_lectors = []
    for lector in lectors:
        if course_name in student.grades:
            total_grades_lectors.extend(student.grades[course_name])

    if not total_grades_lectors:
        average_grade = 0
    else:
        average_grade = sum(total_grades_lectors) / len(total_grades_lectors)

    print(f'Курс: {course_name}\nСредняя оценка за лекции: {average_grade:.1f}')

# Вызов функции calculate_lectors_course_average.  
lecturers_list = [some_lecturer, some_lecturer1]
calculate_lectors_course_average(lecturers_list, 'Python')  