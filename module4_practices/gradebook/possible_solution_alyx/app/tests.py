from django.test import TestCase
from app import models as m

# Create your tests here.
class Test_Gradebook(TestCase):
    # TEsting out notes
    def test_create_grades(self):
        drew_grade = m.create_grade("M4", "Drew", "2010-10-10", 90)

        self.assertEqual(drew_grade.id, 1)
        self.assertEqual(drew_grade.assignment, "M4")
        self.assertEqual(drew_grade.name, "Drew")
        self.assertEqual(drew_grade.date, "2010-10-10")
        self.assertEqual(drew_grade.percentage, 90)
        self.assertIsNone(drew_grade.notes)

        patrick_grade = m.create_grade("M4", "Patrick", "2010-10-10")

        self.assertEqual(patrick_grade.id, 2)
        self.assertEqual(patrick_grade.assignment, "M4")
        self.assertEqual(patrick_grade.name, "Patrick")
        self.assertEqual(patrick_grade.date, "2010-10-10")
        self.assertEqual(patrick_grade.percentage, 0)
        self.assertIsNone(patrick_grade.notes)

    def test_find_grade_by_id(self):
        patrick_grade = m.create_grade("M4", "Patrick", "2010-10-10")
        drew_grade = m.create_grade("M4", "Drew", "2010-10-10", 90)

        grade_search = m.find_grade(2)

        self.assertEqual(drew_grade, grade_search)

    def test_update_grade_drew(self):
        drew_grade_og = m.create_grade("M4", "Drew", "2010-10-10", 90)
        percent_og = drew_grade_og.percentage

        drew_grade_og = m.update_percent(1, 100)

        self.assertEqual(percent_og, 90)
        self.assertEqual(drew_grade_og.percentage, 100)

    def test_update_notes_drew(self):
        drew_grade_og = m.create_grade("M4", "Drew", "2010-10-10", 90)
        notes_og = drew_grade_og.notes

        drew_grade_og = m.update_notes(1, "He did good!")

        self.assertIsNone(notes_og)
        self.assertEqual(drew_grade_og.notes, "He did good!")

    def test_delete_grade(self):
        patrick_grade = m.create_grade("M4", "Patrick", "2010-10-10")
        drew_grade = m.create_grade("M4", "Drew", "2010-10-10", 90)

        self.assertEqual(patrick_grade.id, 1)
        self.assertEqual(drew_grade.id, 2)

        all_objects = m.all_grades()

        self.assertEqual(len(all_objects), 2)

        m.delete_grade(1)

        new_objects = m.all_grades()

        self.assertEqual(len(new_objects), 1)

    def test_filter_by_name_drew(self):
        patrick_grade = m.create_grade("M4", "Patrick", "2010-10-10")
        drew_grade = m.create_grade("M4", "Drew", "2010-10-10", 90)
        drew_grade2 = m.create_grade("M3", "Drew", "2010-10-9")

        all_objects = m.all_grades()

        self.assertEqual(len(all_objects), 3)

        new_objects = m.filter_by_name("Drew")

        self.assertEqual(len(new_objects), 2)

    def test_filter_by_assignment_M3(self):
        patrick_grade = m.create_grade("M4", "Patrick", "2010-10-10")
        drew_grade = m.create_grade("M4", "Drew", "2010-10-10", 90)
        drew_grade2 = m.create_grade("M3", "Drew", "2010-10-9")

        all_objects = m.all_grades()

        self.assertEqual(len(all_objects), 3)

        new_objects = m.filter_by_assignment("M3")

        self.assertEqual(len(new_objects), 1)

    def test_filter_by_pass_assignment_65_M4(self):
        patrick_grade = m.create_grade("M4", "Patrick", "2010-10-10")
        drew_grade = m.create_grade("M4", "Drew", "2010-10-10", 90)
        drew_grade2 = m.create_grade("M3", "Drew", "2010-10-9")

        all_objects = m.all_grades()

        self.assertEqual(len(all_objects), 3)

        new_objects = m.filter_by_pass_assignment("M4", 90)

        self.assertEqual(len(new_objects), 1)
