#Students

cmd = input().split(':')
#cmd = [i.strip() for i in cmd if i.strip()]
dict = {}

while len(cmd) > 1:
    student = cmd[0] + ' - ' + cmd[1]
    course = cmd[2]
    if course not in dict.keys():
        dict[course] = []
        dict[course].append(student)
    else:
        dict[course].append(student)
    cmd = input().split(':')

cmd[0] = cmd[0].replace("_", " ")

listStudents = dict[cmd[0]]
print ('\n'.join(listStudents))