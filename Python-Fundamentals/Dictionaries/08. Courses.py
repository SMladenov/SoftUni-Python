#Courses

cmd = input()

dicCourses = {}

while cmd != "end":
    cmdSplit = cmd.split(':')
    cmdSplit = [i.strip() for i in cmdSplit if i.strip()]
    course = cmdSplit[0]
    student = cmdSplit[1]
    if course not in dicCourses.keys():
        dicCourses[course] = []
        dicCourses[course].append(student)
    else:
        dicCourses[course].append(student)
    cmd = input()

for key, value in dicCourses.items():
    print (f"{key}: {len(value)}")
    print ('\n'.join(f"-- {i}" for i in value))