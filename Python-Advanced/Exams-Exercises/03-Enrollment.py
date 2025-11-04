#Enrollment

def gather_credits(*args):
    
    listCoursesEnrolled = []
    
    creditsNeeded = int(args[0])
    creditsGathered = 0
    courses = args[1:]

    if creditsNeeded == 0:
        return f"Enrollment finished! Maximum credits: 0.\nCourses: "

    for courseName, credits in courses:
        credits = int(credits)
        
        if creditsGathered < creditsNeeded and courseName not in listCoursesEnrolled:
            listCoursesEnrolled.append(courseName)
            creditsGathered += credits
                
            if creditsGathered >= creditsNeeded:
                sortedCourses = sorted(listCoursesEnrolled)
                return f"Enrollment finished! Maximum credits: {creditsGathered}.\nCourses: {', '.join(sortedCourses)}"
                    
    creditShortage = creditsNeeded - creditsGathered
    return f"You need to enroll in more courses! You have to gather {creditShortage} credits more."

print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

print(gather_credits(0, ("Math", 40), ("Science", 50)))
