#SoftUni Exam Results

cmd = input()

dicStudents = {}
dicSubmissions = {}

while cmd != "exam finished":
    cmdSplit = cmd.split('-')
    if len(cmdSplit) == 3:
        student = cmdSplit[0]
        language = cmdSplit[1]
        score = int(cmdSplit[2])
    
        if language not in dicSubmissions.keys():
            dicSubmissions[language] = 0
    
        if student in dicStudents.keys():
            if language in dicStudents[student].keys():
                if score > dicStudents[student][language]:
                    dicStudents[student][language] = score
                dicSubmissions[language] += 1
            if language not in dicStudents[student].keys():
                dicStudents[student][language] = score
                dicSubmissions[language] += 1
                
        if student not in dicStudents.keys():
            dicStudents[student] = {}
            if language not in dicStudents[student].keys():
                dicStudents[student][language] = score
                dicSubmissions[language] += 1
            #if language in dicStudents[student].keys():
            #    if score > dicStudents[student][language]:
            #        dicStudents[student][language] = score
            #    dicSubmissions[language] += 1
                
    else:
        student = cmdSplit[0]
        dicStudents.pop(student)
    cmd = input()

print (f"Results:")
for key, value in dicStudents.items():
    print (f"{key} | ", end = "")
    for key2, value2 in value.items():
        print (f"{value2}")

print (f"Submissions:")
for key, value in dicSubmissions.items():
    print (f"{key} - {value}")
    