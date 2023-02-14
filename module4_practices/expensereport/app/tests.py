from django.test import TestCase
from app import models as system

# Create your tests here.


class ExpenseTest(TestCase):
    def test_creation(self):
        expenses = system.createExpense(
            "2022-03-13", "Home Town", 30, "It was good pizza"
        )

        self.assertEqual(expenses.date, "2022-03-13")
        self.assertEqual(expenses.location, "Home Town")
        self.assertEqual(expenses.amount, 30)
        self.assertEqual(expenses.notes, "It was good pizza")

    def test_update(self):
        expenses = system.createExpense(
            "2022-03-13", "Home Town", 30, "It was good pizza"
        )

        expenses = system.updateExpense(
            expenses.id, "2022-24-14", "Home Town Pizza", 40, "It was a bit pricey"
        )

        self.assertEqual(expenses.date, "2022-24-14")
        self.assertEqual(expenses.location, "Home Town Pizza")
        self.assertEqual(expenses.amount, 40)
        self.assertEqual(expenses.notes, "It was a bit pricey")

    def test_delete(self):
        expenses = system.createExpense(
            "2022-03-13", "Home Town", 30, "It was good pizza"
        )

        expenses2 = system.createExpense("2023-01-03", "Walmart", 15, "blank")

        self.assertEqual(len(system.getAllExpenses()), 2)
        system.deleteExpense(expenses2.id)
        self.assertEqual(len(system.getAllExpenses()), 1)

    def test_filter(self):
        expenses = system.createExpense(
            "2022-03-13", "Home Town", 30, "It was good pizza"
        )

        expenses2 = system.createExpense("2023-01-03", "Walmart", 15, "blank")

        self.assertEqual(len(system.filterExpensesLocation("Walmart")), 1)
        self.assertEqual(len(system.filterExpensesLocation("Home Town")), 1)

        self.assertEqual(len(system.filterExpensesAmount(30)), 1)
        self.assertEqual(len(system.filterExpensesAmount(15)), 1)

    def test_all(self):
        expenses = system.createExpense(
            "2022-03-13", "Home Town", 30, "It was good pizza"
        )

        self.assertEqual(len(system.getAllExpenses()), 1)

        expenses2 = system.createExpense("2023-01-03", "Walmart", 15, "blank")

        self.assertEqual(len(system.getAllExpenses()), 2)

    def test_getAmount(self):
        expenses = system.createExpense(
            "2022-03-13", "Home Town", 30, "It was good pizza"
        )
        expenses2 = system.createExpense("2023-01-03", "Walmart", 15, "blank")

        foundAmount = system.getAmount(expenses.id)

        self.assertEqual(foundAmount, 30)
