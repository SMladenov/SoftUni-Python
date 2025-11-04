from project.senior_student import SeniorStudent

import unittest

class SeniorStudentTests (unittest.TestCase):

    def setUp(self):
        self.student = SeniorStudent("1234", "Goshko", 1.5)
    
    def test_init_all_valid (self):
        self.assertEqual(self.student.student_id, "1234")
        self.assertEqual(self.student.name, "Goshko")
        self.assertEqual(self.student.student_gpa, 1.5)
        self.assertEqual(self.student.colleges, set())
    
    def test_name_raises (self):
        with self.assertRaises(ValueError) as msg:
            SeniorStudent("1234", "", 1.5)
        self.assertEqual(str(msg.exception), "Student name cannot be null or empty!")
    

    def test_student_gpa_raises (self):
        with self.assertRaises(ValueError) as msg:
            SeniorStudent("1234", "Goshko", 0.9)
        self.assertEqual(str(msg.exception), "Student GPA must be more than 1.0!")

    def test_apply_to_college_unsuccessful (self):
        result = self.student.apply_to_college(2.0, "Botevgrad")
        self.assertEqual(result, "Application failed!")

    def test_apply_to_college_successful (self):
        result = self.student.apply_to_college(1.0, "Botevgrad")
        self.assertEqual(result, f'{self.student.name} successfully applied to Botevgrad.')
        self.assertTrue("BOTEVGRAD" in self.student.colleges)
    
    def test_update_gpa_unsuccessful (self):
        result = self.student.update_gpa(0.9)
        self.assertEqual(result, "The GPA has not been changed!")
        self.assertEqual(self.student.student_gpa, 1.5)

    def test_update_gpa_successful (self):
        result = self.student.update_gpa(2.0)
        self.assertEqual(result, "Student GPA was successfully updated.")
        self.assertEqual(self.student.student_gpa, 2.0)

    def test_students_equal (self):
        student2 = SeniorStudent("5678", "Pesho", 1.5)
        self.assertTrue(self.student == student2)
    
    def test_students_not_equal (self):
        student2 = SeniorStudent("5678", "Pesho", 4.5)
        self.assertFalse(self.student == student2)

if __name__ == '__main__':
    unittest.main()