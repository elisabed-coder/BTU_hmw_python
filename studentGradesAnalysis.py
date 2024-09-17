students = [("Alice", 85), ("Bob", 78), ("Charlie", 92), ("David", 85), ("Eve", 78), ("Frank", 85), ("Mark", 50), ("George", 21)]


# Extract and print all the unique grades from the list of student scores.
def getitem():
    uniqueGrades = {grade for _, grade in students}
    print(uniqueGrades)

#Top Performers:
#Identify and print the names of the top three students with the highest scores.
def highestScore():
    top_students = sorted(students, key=lambda student: student[1], reverse=True)[:3]
    print(f"Top students are:")
    iterateStudents(top_students)

#Failed Students:
#Identify and print the names of students who scored below 51, along with their scores.
def failedStudents():
    failedStudents = [student for student in students if student[1] < 51]

    print("Failed students:")
    iterateStudents(failedStudents)

def iterateStudents(students):
    for name, score in students:
        print(f"Name: {name}, Score:{score}")


getitem()
highestScore()
failedStudents()