class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def get_average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

    def __str__(self) -> str:
        print_courses_in_progress = ', '.join(self.courses_in_progress)
        print_finished_courses = ', '.join(self.finished_courses)
        average_grade = round(self.get_average_grade(), 1)
        return f"Студент\n\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {print_courses_in_progress}\nЗавершенные курсы: {print_finished_courses}\n"
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self) -> str:
        return f"Ментор\n\nИмя: {self.name}\nФамилия: {self.surname}\n"
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    def get_average_grade(self):
        all_grades = []
        for grades in self.lecturer_grades.values():
            all_grades.extend(grades)
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

    def __str__(self) -> str:
        average_grade = round(self.get_average_grade(), 1)
        return f"Лектор\n\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}\n"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

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

some_student1 = Student('Ivan', 'Belov', 'your_gender')
some_student1.courses_in_progress += ['Python', 'Git']
some_student1.finished_courses += ['Введение в программирование']

some_mentor = Mentor('Some', 'Buddy')
some_mentor.courses_attached += ['Python']

some_mentor1 = Mentor('Mark', 'Grizzly')
some_mentor1.courses_attached += ['Git']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_lecturer1 = Lecturer('Mark', 'Grizzly')
some_lecturer1.courses_attached += ['Git']

some_student.rate_lecturers(some_lecturer, 'Python', 10)
some_student.rate_lecturers(some_lecturer, 'Python', 9)
some_student.rate_lecturers(some_lecturer, 'Python', 10)

some_student1.rate_lecturers(some_lecturer1, 'Git', 9)
some_student1.rate_lecturers(some_lecturer1, 'Git', 9)
some_student1.rate_lecturers(some_lecturer1, 'Git', 9)

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_reviewer1 = Reviewer('Petr', 'Sidorof')
some_reviewer1.courses_attached += ['Git']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)

some_reviewer1.rate_hw(some_student1, 'Git', 10)
some_reviewer1.rate_hw(some_student1, 'Git', 10)
some_reviewer1.rate_hw(some_student1, 'Git', 10)

print(some_reviewer)
print(some_reviewer1)
print(some_lecturer)
print(some_lecturer1)
print(some_student)
print(some_student1)
# print(some_mentor)
# print(some_mentor1)

students = [some_student, some_student1]
lecturers = [some_lecturer, some_lecturer1]

sorted_students = sorted(students, reverse=True)
sorted_lecturers = sorted(lecturers, reverse=True)

print("Студенты, упорядоченные по средней оценке за домашние задания (убывание):\n")
for student in sorted_students:
    print(student)

print("Лекторы, упорядоченные по средней оценке за лекции (убывание):\n")
for lecturer in sorted_lecturers:
    print(lecturer)