import statistics

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
        # Initialize name and an empty list for grades

    def add_grade(self, grade):
        self.grades.append(grade)
        # Add a new grade to the grades list

    def get_average_grade(self):
        return statistics.mean(self.grades)
        # Return the average of the grades


    def __str__(self):
        return f"name: {self.name}, grades {self.grades}, average grade: {self.get_average_grade()}"
        # Return a string representation of the student

class Classroom:
    def __init__(self):
        self.students = []
        # Initialize an empty list for students

    def add_student(self, student):
        self.students.append(student)
        # Add a student to the classroom

    def get_top_students(self):
        top_students = sorted(self.students, key=lambda student: student.get_average_grade(), reverse=True)[:3]

        return top_students
        # Return the top 3 students based on average grades

    def get_failed_students(self):
        # Return students with an average grade below 51
        failed_students = [student for student in self.students if student.get_average_grade() < 51]
        return failed_students



student1 = Student("John")
student1.add_grade(51)
student1.add_grade(80)

student2 = Student("Nick")
student2.add_grade(55)
student2.add_grade(57)

student3 = Student("Thomas")
student3.add_grade(99)
student3.add_grade(100)

student4 = Student("Theo")
student4.add_grade(49)
student4.add_grade(47)

student5 = Student("Lucas")
student5.add_grade(98)
student5.add_grade(100)




classroom = Classroom()
(classroom.add_student(student1))
(classroom.add_student(student2))
(classroom.add_student(student3))
(classroom.add_student(student4))
(classroom.add_student(student5))


print("top students")
for student in classroom.get_top_students():
    print(student)

print("failed students")
for student in classroom.get_failed_students():
    print(student)