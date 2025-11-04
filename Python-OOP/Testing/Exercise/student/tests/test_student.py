from project.student import Student
import unittest

class StudentTests (unittest.TestCase):
    

    def test_constructor (self):
        self.student = Student("Kircho")
        self.assertEqual(self.student.name, "Kircho")
        self.assertEqual(self.student.courses, {})

        new_courses = {"Programirane": [], "Linux": [], "DevOps": []}
        self.student2 = Student("Kircho2", new_courses)
        self.assertEqual(self.student2.name, "Kircho2")
        self.assertEqual(self.student2.courses, new_courses)

    def test_enroll_course_present (self):
        new_courses = {"Programirane": [], "Linux": [], "DevOps": []}
        self.student2 = Student("Kircho2", new_courses)

        result = self.student2.enroll("Linux", ['oshte', 'malko', 'i', 'shte', 'stanat', 'neshtata'])
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(self.student2.courses["Linux"], ['oshte', 'malko', 'i', 'shte', 'stanat', 'neshtata'])

    def test_enroll_course_not_present (self):
        self.student = Student("Kircho")
        result = self.student.enroll("Linux", ['oshte', 'malko', 'i', 'shte', 'stanat', 'neshtata'])
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertTrue("Linux" in self.student.courses.keys())

    def test_enroll_course_not_present_no_notes (self):
        self.student = Student("Kircho")
        result = self.student.enroll("Linux", [], "First Course No Notes")
        self.assertEqual(result, "Course has been added.")
        self.assertTrue("Linux" in self.student.courses.keys())
    
    def test_add_notes_cannot_find_course_raises (self):
        self.student = Student("Kircho")
        with self.assertRaises(Exception) as msg:
            self.student.add_notes("Linux", [])
        self.assertEqual(str(msg.exception), "Cannot add notes. Course not found.")
    
    def test_add_notes_all_valid (self):
        new_courses = {"Programirane": [], "Linux": [], "DevOps": []}
        self.student = Student("Kircho", new_courses)

        result = self.student.add_notes("Linux", ['oshte', 'malko', 'i', 'shte', 'stanat', 'neshtata'])
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(self.student.courses["Linux"], [['oshte', 'malko', 'i', 'shte', 'stanat', 'neshtata']])
    
    def test_leave_course_cannot_find_course_raises (self):
        self.student = Student("Kircho")
        with self.assertRaises(Exception) as msg:
            self.student.leave_course("Linux")
        self.assertEqual(str(msg.exception), "Cannot remove course. Course not found.")

    def test_leave_course_all_valid (self):
        new_courses = {"Programirane": [], "Linux": [], "DevOps": []}
        self.student = Student("Kircho", new_courses)

        result = self.student.leave_course("Programirane")
        self.assertEqual(result, "Course has been removed")
        self.assertEqual(self.student.courses, {"Linux": [], "DevOps": []})

if __name__ == '__main__':
    unittest.main()