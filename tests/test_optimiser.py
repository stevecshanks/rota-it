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

    def test_tasks_are_distributed_fairly(self):
        task1 = Task(date(2018, 1, 1), 'A skill')
        task2 = Task(date(2018, 1, 1), 'A skill')

        person1 = Person('Test 1', ['A skill'], [])
        person2 = Person('Test 2', ['A skill'], [])

        optimiser = Optimiser([task1, task2], [person1, person2])
        optimiser.optimise()

        self.assertIsNotNone(task1.assignee)
        self.assertIsNotNone(task2.assignee)
        self.assertNotEqual(task1.assignee, task2.assignee)

    def test_volunteers_are_taken_into_account(self):
        volunteer = Person('Volunteer', ['A skill'], [])
        other_person = Person('Other', ['A skill'], [])

        volunteered = Task(date(2018, 1, 1), 'A skill', volunteer)
        other_task = Task(date(2018, 1, 1), 'A skill')

        optimiser = Optimiser([volunteered, other_task], [other_person, volunteer])
        optimiser.optimise()

        self.assertEqual(volunteered.assignee, volunteer)
        self.assertEqual(other_task.assignee, other_person)

    def test_hard_to_allocate_tasks_are_distributed_first(self):
        cleaning1 = Task(date(2018, 1, 1), 'Cleaning')
        cleaning2 = Task(date(2018, 1, 1), 'Cleaning')
        driving1 = Task(date(2018, 1, 1), 'Driving')
        driving2 = Task(date(2018, 1, 1), 'Driving')

        cleaner = Person('Cleaner', ['Cleaning'], [])
        cleaner_and_driver = Person('Cleaner and Driver', ['Cleaning', 'Driving'], [])

        optimiser = Optimiser([cleaning1, cleaning2, driving1, driving2],
                              [cleaner, cleaner_and_driver])
        optimiser.optimise()

        self.assertEqual(cleaning1.assignee, cleaner)
        self.assertEqual(cleaning2.assignee, cleaner)
        self.assertEqual(driving1.assignee, cleaner_and_driver)
        self.assertEqual(driving2.assignee, cleaner_and_driver)