#SoftUni Students

def softuni_students (*args, **kwargs):

    dicCourses = {}
    
    for courseId, username in args:
        if courseId not in dicCourses.keys():
            dicCourses[courseId] = [username]
        else:
            dicCourses[courseId].append(username)

    listToPrint = []
    invalidCourseStudents = []

    #for courseId in dicCourses.keys():
    #    dicCourses[courseId] = sorted(dicCourses[courseId])
        
    for courseId, courseName in kwargs.items():
        if courseId in dicCourses.keys():
            listStudents = dicCourses[courseId]
            for student in listStudents:
                messageToAppend = f"*** A student with the username {student} has successfully finished the course {courseName}!"
                listToPrint.append(messageToAppend)
            del dicCourses[courseId]
            
    for students in dicCourses.values():
        invalidCourseStudents.extend(students)
        
    invalidCourseStudents.sort()
    listToPrint.sort()
    
    if invalidCourseStudents:
        return '\n'.join(listToPrint) + f"\n!!! Invalid course students: {', '.join(invalidCourseStudents)}"
    else:
        return '\n'.join(listToPrint)

print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))

print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))

print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
