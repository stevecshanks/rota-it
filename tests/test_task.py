import unittest
from datetime import date
from python_glasgow.task import Task


class TestTask(unittest.TestCase):

    def test_it_is_initializable(self):
        task = Task(date(2018, 1, 1), 'Cleaning')
