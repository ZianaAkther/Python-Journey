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

    name = input("Enter name: ")
    students.append(name)
    
    id = int(input("Enter student ID: "))
    students.append(id)

    for m in range(num_of_subjects):
        mark = int(input(f"Enter marks for {subjects[m]}: "))
        marks.append(mark)
    
    students.append(marks) 
    all_students.append(students)

print("--------------Marks--------------")

for student in all_students:
    name, id, mar_ks = student
    print(f"Name: {name}")
    print(f"ID: {id}")

    for i in range(len(subjects)):
        print(f"{subjects[i]}: {mar_ks[i]}")
    
    print("-----------------------------------------")
