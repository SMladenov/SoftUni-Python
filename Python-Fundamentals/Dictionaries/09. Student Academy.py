#Student Academy

numberStudents = int(input())

dicGrades = {}

for i in range (numberStudents):
    student = input()
    grade = float(input())
    if student not in dicGrades.keys():
        dicGrades[student] = []
        dicGrades[student].append(grade)
    else:
        dicGrades[student].append(grade)

for key, value in dicGrades.items():
    average = sum(value) / len(value)
    if average >= 4.50:
        print (f"{key} -> {average:.2f}")