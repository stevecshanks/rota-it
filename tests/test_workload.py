import unittest
from datetime import date
from python_glasgow.person import Person
from python_glasgow.task import Task
from python_glasgow.workload import Workload


class TestWorkload(unittest.TestCase):

    def test_assign_task_returns_assigned_task(self):
        person = Person('Test', [], [])
        workload = Workload()
        task = Task(date(2018, 1, 1), 'Test')

        assigned_task = workload.assign(task, person)
        self.assertEqual(assigned_task.assignee, person)

    def test_get_workload_per_person_defaults_to_zero(self):
        person = Person('Test', [], [])
        workload = Workload()

        self.assertEqual(workload.assigned_to(person), 0)

    def test_get_workload_per_person_returns_number_of_assigned_tasks(self):
        person = Person('Test', [], [])
        task = Task(date(2018, 1, 1), 'Test')
        workload = Workload()
        workload.assign(task, person)

        self.assertEqual(workload.assigned_to(person), 1)

    def test_get_least_busy_person_returns_none_if_no_people(self):
        workload = Workload()
        self.assertIsNone(workload.get_least_busy_person([]))

    def test_get_least_busy_person_returns_person_with_fewest_tasks(self):
        lazy_person = Person('Lazy', ['A skill'], [])
        busy_person = Person('Busy', ['A skill'], [])
        task = Task(date(2018, 1, 1), 'A skill')

        workload = Workload()
        workload.assign(task, busy_person)

        self.assertEqual(workload.get_least_busy_person([busy_person, lazy_person]), lazy_person)