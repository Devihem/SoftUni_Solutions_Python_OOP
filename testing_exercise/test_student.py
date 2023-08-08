from oop.all_exams.exam_16_august_2020.unit_test.project import Student
from unittest import TestCase


class TestStudent(TestCase):
    def test_entry_data(self):
        student_1 = Student("Devihem")
        student_2 = Student("Ivo", {"Python": ["Test", "Last Task In Judge"]})
        self.assertEqual("Devihem", student_1.name)
        self.assertEqual({}, student_1.courses)
        self.assertEqual({'Python': ['Test', 'Last Task In Judge']}, student_2.courses)

    def test_enroll_1_same_course(self):
        student_2 = Student("Ivo", {"Python": ["Test", "Last Task In Judge"]})
        result = student_2.enroll("Python", "Nothing")
        self.assertEqual('Course already added. Notes have been updated.', result)

    def test_enroll_2_notes_empty_or_y(self):
        student_1 = Student("Devihem")
        student_2 = Student("Ivo")
        result_1 = student_1.enroll("Python", "Some Notes", "Y")
        result_2 = student_2.enroll("Python", "Some Notes", "")
        self.assertEqual('Course and course notes have been added.', result_1)
        self.assertEqual('Course and course notes have been added.', result_2)
        self.assertEqual({'Python': 'Some Notes'}, student_1.courses)
        self.assertEqual({'Python': 'Some Notes'}, student_2.courses)

    def test_enroll_3_notes_bad_text_in_notes(self):
        student_1 = Student("Devihem")
        student_2 = Student("Ivo")
        result_1 = student_1.enroll("Python", "Some Notes", "ADD ME")
        result_2 = student_2.enroll("Python", "Some Notes", " ")
        self.assertEqual('Course has been added.', result_1)
        self.assertEqual('Course has been added.', result_2)
        self.assertEqual({'Python': []}, student_1.courses)
        self.assertEqual({'Python': []}, student_2.courses)

    # skipped clear input in enroll - if judge give some error

    def test_add_notes_1_error_test_no_course(self):
        student_1 = Student("Devihem", {'Python': ['Some Notes']})
        with self.assertRaises(Exception) as error:
            student_1.add_notes('Banana', 'Add this banana')
        self.assertEqual("Cannot add notes. Course not found.", str(error.exception))

    def test_add_notes_2_proper_course(self):
        student_1 = Student("Devihem", {'Python': ['Some Notes']})
        result = student_1.add_notes('Python', 'Add this banana')
        self.assertEqual("Notes have been updated", result)
        self.assertEqual({'Python': ['Some Notes', 'Add this banana']}, student_1.courses)

    def test_leave_course(self):
        student_1 = Student("Devihem", {'Python': ['Some Notes']})
        result = student_1.leave_course("Python")
        self.assertEqual("Course has been removed", result)

    def test_leave_course_2_no_course_in_dict(self):
        student_1 = Student("Devihem", {'Python': ['Some Notes']})
        with self.assertRaises(Exception) as error:
            student_1.leave_course("Banana")
        self.assertEqual("Cannot remove course. Course not found.", str(error.exception))
        self.assertEqual({'Python': ['Some Notes']}, student_1.courses)


if __name__ == "__main__":
    main()
