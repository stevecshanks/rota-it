import unittest
import python_glasgow.rota_it as rota_it
from datetime import date
from python_glasgow.person import Person
from python_glasgow.task import Task


class TestRotaIt(unittest.TestCase):

    def test_get_eligible_people_returns_empty_list_if_no_people(self):
        task = Task( date(2018, 1, 1), 'A skill')
        self.assertEqual(rota_it.get_eligible_people(task, []), [])

    def test_get_eligible_people_returns_empty_list_if_no_skills_match(self):
        task = Task(date(2018, 1, 1), 'A skill')
        person = Person('A Name', ['Another skill'], [])
        self.assertEqual(rota_it.get_eligible_people(task, [person]), [])

    def test_get_eligible_people_returns_person_if_skills_match(self):
        task = Task(date(2018, 1, 1), 'A skill')
        person = Person('A Name', ['A skill'], [])
        self.assertEqual(rota_it.get_eligible_people(task, [person]), [person])

        # TODO vacation

    def test_get_assigned_tasks_returns_empty_list_if_no_assigned_tasks(self):
        task = Task(date(2018, 1, 1), 'A skill')
        person = Person('A Name', ['A skill'], [])
        self.assertEqual(rota_it.get_assigned_tasks([task], person), [])

    def test_get_assigned_tasks_returns_assigned_tasks(self):
        person = Person('A Name', ['A skill'], [])
        task = Task(date(2018, 1, 1), 'A skill', person)
        self.assertEqual(rota_it.get_assigned_tasks([task], person), [task])

    def test_get_least_busy_person_returns_none_if_no_people(self):
        task = Task(date(2018, 1, 1), 'A skill')
        self.assertIsNone(rota_it.get_least_busy_person([task], []))

    def test_get_least_busy_person_returns_person_with_fewest_tasks(self):
        lazy_person = Person('Lazy', ['A skill'], [])
        busy_person = Person('Busy', ['A skill'], [])
        task = Task(date(2018, 1, 1), 'A skill', busy_person)
        self.assertEqual(
            rota_it.get_least_busy_person([task], [busy_person, lazy_person]),
            lazy_person)
