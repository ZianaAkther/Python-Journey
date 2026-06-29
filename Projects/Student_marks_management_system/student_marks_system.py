#student marks management system basic

all_students = []
num_of_students = int(input("Enter no of students: "))

subjects = []
num_of_subjects = int(input("Enter no of subjects: "))


for s in range(num_of_subjects):
    subject = input("Enter the subject title: ")
    subjects.append(subject)

for each_student in range(num_of_students):
    
    students = []
    marks = []
    totals = []
    avg = []
    grades = []
    total = 0

    name = input("Enter name: ")
    students.append(name)
    
    id = int(input("Enter student ID: "))
    students.append(id)

    for m in range(num_of_subjects):
        mark = int(input(f"Enter marks for {subjects[m]}: "))
        marks.append(mark)
        total += mark

    totals.append(total)
    for i in totals:
        average = i//num_of_subjects

        if average >= 93:
            grade = 'A'
            grades.append(grade)
        elif average >= 82 and average < 93:
            grade = 'B'
            grades.append(grade)
        elif average >= 69 and average < 82:
            grade = 'C'
            grades.append(grade)
        elif average >= 60 and average < 69:
            grade = 'D'
            grades.append(grade)
        else:
            grade = 'F'
            grades.append(grade)

        avg.append(average)

    students.append(marks) 
    students.append(totals)
    students.append(avg)
    students.append(grades)
    all_students.append(students)

print("--------------Marks--------------")

for student in all_students:
    name, id, mar_ks, Total, ave_rage, Grade = student
    print(f"Name: {name}")
    print(f"ID: {id}")

    for i in range(len(subjects)):
        print(f"{subjects[i]}: {mar_ks[i]}")

    print()
    print(f"Total marks obtained: {Total}")
    print(f"Average: {ave_rage}")
    print(f"Grade obtained: {Grade}")
    print("-----------------------------------------")
