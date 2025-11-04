#SoftUni Reception

employee1PerHour = int(input())
employee2PerHour = int(input())
employee3PerHour = int(input())
students = int(input())

allEfficiency = employee1PerHour + employee2PerHour + employee3PerHour

counter = 0

while students > 0:
    counter += 1
    if counter % 4 != 0:
        students -= allEfficiency

print (f"Time needed: {counter}h.")