#Student Credits

def students_credits (*args):

    dicCourses = {}

    totalCredit = 0
    
    for course in args:
        courseName, credits, maxTestPoints, testPoints = course.split('-')
        
        percentageTest = ((int(testPoints) / int(maxTestPoints))) * 100
        actualCredits = (percentageTest / 100) * int(credits)
        totalCredit += actualCredits
        dicCourses[courseName] = actualCredits

    dicCoursesSorted = dict(sorted(dicCourses.items(), key= lambda x: -x[1]))

    listToPrint = []

    if totalCredit >= 240:
        listToPrint.append(f"Diyan gets a diploma with {totalCredit:.1f} credits.")
    else:
        listToPrint.append(f"Diyan needs {round((240 - totalCredit), 1)} credits more for a diploma.")
        
    for course, credit in dicCoursesSorted.items():
        listToPrint.append (f"{course} - {credit:.1f}")

    return '\n'.join(listToPrint)

# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )

# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
