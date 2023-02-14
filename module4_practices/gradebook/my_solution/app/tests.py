from django.test import TestCase
from app import models as m

# Create your tests here.


class TestGradeBook(TestCase):
    def test_create_grade(self):
        newGrade = m.createGrade('Spelling', 20, 'Joseph', '2023-02-05', 'No Notes')
        newGrade2 = m.createGrade('Math', 12, 'John', '2023-02-15')

        self.assertEqual(newGrade.id, 1)
        self.assertEqual(newGrade.assignmentName, 'Spelling')
        self.assertEqual(newGrade.percentage, 20)
        self.assertEqual(newGrade.studentName, 'Joseph')
        self.assertEqual(newGrade.date, '2023-02-05')
        self.assertEqual(newGrade.notes, "No Notes")

        self.assertEqual(newGrade2.id, 2)
        self.assertEqual(newGrade2.assignmentName, 'Math')
        self.assertEqual(newGrade2.percentage, 12)
        self.assertEqual(newGrade2.studentName, 'John')
        self.assertEqual(newGrade2.date, '2023-02-15')
        self.assertEqual(newGrade2.notes, "")


    def test_find_grade(self):
        newGrade = m.createGrade('Spelling', 20, 'Joseph', '2023-02-05', 'No Notes')
        newGrade2 = m.createGrade('Math', 12, 'John', '2023-02-15')

        foundGrade = m.findGrade(1)
        self.assertEqual(foundGrade.id, 1)
        self.assertEqual(foundGrade.assignmentName, 'Spelling')
        self.assertEqual(foundGrade.studentName, 'Joseph')


    def test_updates(self):
        newGrade = m.createGrade('Spelling', 20, 'Joseph', '2023-02-05', 'No Notes')
        self.assertEqual(newGrade.percentage, 20)
        self.assertEqual(newGrade.notes, 'No Notes')

        newGrade = m.updateGrade(1, 80)
        self.assertEqual(newGrade.percentage, 80)

        newGrade = m.updateNotes(1, 'New Notes')
        self.assertEqual(newGrade.notes, 'New Notes')


    def test_remove_grade(self):
        newGrade = m.createGrade('Spelling', 20, 'Joseph', '2023-02-05', 'No Notes')
        newGrade2 = m.createGrade('Math', 12, 'John', '2023-02-15')

        self.assertEqual(len(m.getAllGrades()), 2)
        m.removeGrade(1)
        self.assertEqual(len(m.getAllGrades()), 1)


    def test_filter_name(self):
        newGrade = m.createGrade('Spelling', 20, 'Joseph', '2023-02-05', 'No Notes')
        newGrade2 = m.createGrade('Math', 12, 'John', '2023-02-15')

        foundGrades = m.filterGradeName('Spelling')
        self.assertEqual(len(foundGrades), 1)


    def test_filter_name_percent(self):
        newGrade = m.createGrade('Spelling', 20, 'Joseph', '2023-02-05', 'No Notes')
        newGrade2 = m.createGrade('Math', 12, 'John', '2023-02-15')
        newGrade = m.createGrade('Spelling', 50, 'Joseph', '2023-02-05', 'No Notes')

        foundGrades = m.filterGradeNamePercent('Spelling', 20)
        self.assertEqual(len(foundGrades), 1)