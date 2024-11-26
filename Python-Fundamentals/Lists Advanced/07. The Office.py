#The Office

employees = input().split(' ')
factor = int(input())
employeesAfter = [int(i) * factor for i in employees]
average = (sum(employeesAfter) / len(employeesAfter))

filter = [i for i in employeesAfter if i >= average]

if len(filter) >= (len(employees) // 2):
    print (f"Score: {len(filter)}/{len(employees)}. Employees are happy!")
else:
    print (f"Score: {len(filter)}/{len(employees)}. Employees are not happy!")
    