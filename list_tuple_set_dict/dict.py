count = int(input("how many entries do you want: "))

students = {}

for i in range(count):
    name = input("enter student name:")
    marks = int(input("enter student marks: "))
    students[name] = marks

print(students)

total_marks = sum(students.values())

print("average : {}".format(total_marks/len(students)))
