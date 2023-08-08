from oop.all_exams.exam_retake_22_august_2020.unit_test.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.student_1 = StudentReportCard("Name", 3)

    def test_entry_data(self):
        self.student_1.add_grade("Python", 5.00)
        self.assertEqual("Name", self.student_1.student_name)
        self.assertEqual(3, self.student_1.school_year)
        self.assertEqual({'Python': [5.0]}, self.student_1.grades_by_subject)

    def test_empty_name(self):
        with self.assertRaises(ValueError) as error:
            self.student_1.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(error.exception))

    def test_wrong_school_years_under_1(self):
        with self.assertRaises(ValueError) as error:
            self.student_1.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))

    def test_correct_school_year_1(self):
        self.student_1.school_year = 1
        self.assertEqual(1,self.student_1.school_year)

    def test_correct_school_year_12(self):
        self.student_1.school_year = 12
        self.assertEqual(12,self.student_1.school_year)

    def test_wrong_school_years_over_12(self):
        with self.assertRaises(ValueError) as error:
            self.student_1.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))

    def test_add_grade_dict_proper(self):
        self.assertEqual({}, self.student_1.grades_by_subject)
        self.student_1.add_grade("Python", 5.00)
        self.assertEqual({'Python': [5.0]}, self.student_1.grades_by_subject)
        self.student_1.add_grade("Python", 6.00)
        self.assertEqual({'Python': [5.0, 6.0]}, self.student_1.grades_by_subject)

    def test_average_grade_method_for_subject_on_empty_dict(self):
        result = self.student_1.average_grade_by_subject()
        self.assertEqual('', result)

    def test_average_grade_method_for_subject(self):
        self.student_1.add_grade("Python", 2)
        self.student_1.add_grade("Python", 6.00)
        self.student_1.add_grade("Mython", 4.00)
        self.student_1.add_grade("Mython", 3.00)
        result = self.student_1.average_grade_by_subject()
        self.assertEqual('Python: 4.00\nMython: 3.50', result)

    def test_average_grade_method_for_all(self):
        self.student_1.add_grade("Python", 4.00)
        self.student_1.add_grade("Python", 6.00)
        self.student_1.add_grade("Mython", 5)
        self.student_1.add_grade("Mython", 5)
        result = self.student_1.average_grade_for_all_subjects()
        self.assertEqual('Average Grade: 5.00', result)

    def test_average_grade_method_for_all_with_no_data(self):
        with self.assertRaises(ZeroDivisionError) as error:
            self.student_1.average_grade_for_all_subjects()
        self.assertEqual('division by zero', str(error.exception))

    def test_repr(self):
        self.student_1.add_grade("Python", 5.99)
        self.student_1.add_grade("Python", 6.00)
        self.student_1.add_grade("Mython", 4.00)
        self.student_1.add_grade("Mython", 3.00)
        result = str(self.student_1)
        self.assertEqual('Name: Name\nYear: 3\n----------\nPython: 6.00\nMython: 3.50\n----------\nAverage Grade: 4.75',
                         result)


if __name__ == "__main__":
    main()
