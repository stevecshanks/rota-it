import unittest
from datetime import date
from python_glasgow.optimiser import Optimiser
from python_glasgow.person import Person
from python_glasgow.task import Task


class TestOptimiser(unittest.TestCase):

    def test_tasks_remain_unassigned_if_noone_car_perform_them(self):
        task = Task(date(2018, 1, 1), 'A skill')
        optimiser = Optimiser([task], [])
        optimiser.optimise()

        self.assertIsNone(task.assignee)

    def test_tasks_are_assigned_to_people_with_correct_skills(self):
        cleaning = Task(date(2018, 1, 1), 'Cleaning')
        cooking = Task(date(2018, 1, 1), 'Cooking')

        cleaner = Person('Cleaner', ['Cleaning'], [])
        cook = Person('Cook', 'Cooking', [])

        optimiser = Optimiser([cleaning, cooking], [cleaner, cook])
        optimiser.optimise()

        self.assertEqual(cleaning.assignee, cleaner)
        self.assertEqual(cooking.assignee, cook)

    def test_tasks_are_not_assigned_to_people_on_vacation(self):
        task = Task(date(2018, 1, 1), 'A skill')
        person = Person('Test', ['A skill'], [date(2018, 1, 1)])

        optimiser = Optimiser([task], [person])
        optimiser.optimise()

        self.assertIsNone(task.assignee)

    def tests_tasks_are_distributed_fairly(self):
        task1 = Task(date(2018, 1, 1), 'A skill')
        task2 = Task(date(2018, 1, 1), 'A skill')

        person1 = Person('Test 1', ['A skill'], [])
        person2 = Person('Test 2', ['A skill'], [])

        optimiser = Optimiser([task1, task2], [person1, person2])
        optimiser.optimise()

        self.assertIsNotNone(task1.assignee)
        self.assertIsNotNone(task2.assignee)
        self.assertNotEqual(task1.assignee, task2.assignee)