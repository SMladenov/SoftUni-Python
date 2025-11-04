#Students' Grades

students = int(input())
dicStudents = {}

for i in range (students):
    name, grade = input().split()
    if name not in dicStudents.keys():
        dicStudents[name] = [float(grade)]
    else:
        dicStudents[name].append(float(grade))

for key, value in dicStudents.items():
    averageGrade = sum(value) / len(value)
    print (f"{key} -> {' '.join([f'{i:.2f}' for i in value])} (avg: {averageGrade:.2f})")
