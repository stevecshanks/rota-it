import unittest
import python_glasgow.rota_it as rota_it
from datetime import date
from python_glasgow.person import Person
from python_glasgow.task import Task


class TestRotaIt(unittest.TestCase):

    def test_get_eligible_people_returns_empty_list_if_no_people(self):
        task = Task('A skill', date(2018, 1, 1))
        self.assertEqual(rota_it.get_eligible_people(task, []), [])

    def test_get_eligible_people_returns_empty_list_if_no_skills_match(self):
        task = Task('A skill', date(2018, 1, 1))
        person = Person('A Name', ['Another skill'], [])
        self.assertEqual(rota_it.get_eligible_people(task, [person]), [])

    def test_get_eligible_people_returns_person_if_skills_match(self):
        task = Task('A skill', date(2018, 1, 1))
        person = Person('A Name', ['A skill'], [])
        self.assertEqual(rota_it.get_eligible_people(task, [person]), [person])
