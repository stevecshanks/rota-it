import unittest
from datetime import date
from rotait.person import Person


class TestPerson(unittest.TestCase):

    def test_has_skill_returns_true_if_person_has_skill(self):
        person = Person('Gordon', ['Cooking', 'Driving'], [])
        self.assertTrue(person.has_skill('Cooking'))

    def test_has_skill_returns_false_if_person_does_not_have_skill(self):
        person = Person('Gordon', ['Cooking', 'Driving'], [])
        self.assertFalse(person.has_skill('Cleaning'))

    def test_is_available_on_returns_true_if_person_not_on_vacation(self):
        person = Person('Yuri', [], [])
        self.assertTrue(person.is_available_on(date(2018, 1, 1)))

    def test_is_available_on_returns_false_if_person_on_vacation(self):
        person = Person('Yuri', [], [date(2018, 1, 1)])
        self.assertFalse(person.is_available_on(date(2018, 1, 1)))