import unittest
from datetime import date
from python_glasgow.person import Person
from python_glasgow.task import Task
from python_glasgow.workload import Workload


class TestWorkload(unittest.TestCase):

    def test_assign_task_returns_assigned_task(self):
        person = Person('Test', [], [])
        workload = Workload([person])
        task = Task(date(2018, 1, 1), 'Test')

        assigned_task = workload.assign(task, person)
        self.assertEqual(assigned_task.assignee, person)

    def test_get_workload_per_person_defaults_to_zero(self):
        person = Person('Test', [], [])
        workload = Workload([person])

        per_person = workload.get_workload_per_person()

        self.assertEqual(len(per_person), 1)
        self.assertEqual(per_person[person], 0)

    def test_get_workload_per_person_returns_number_of_assigned_tasks(self):
        person = Person('Test', [], [])
        task = Task(date(2018, 1, 1), 'Test')
        workload = Workload([person])
        workload.assign(task, person)

        per_person = workload.get_workload_per_person()

        self.assertEqual(len(per_person), 1)
        self.assertEqual(per_person[person], 1)