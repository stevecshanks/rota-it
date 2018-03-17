from datetime import date
from python_glasgow.optimiser import Optimiser
from python_glasgow.person import Person
from python_glasgow.task import Task


GORDON = Person('Gordon',
                ['Cleaning', 'Driving', 'Shopping'],
                [date(2017, 10, 26), date(2017, 10, 29)])
ERFAN = Person('Erfan',
               ['Cleaning', 'Cooking', 'Driving', 'Shopping'],
               [date(2017, 10, 28)])
ROGER = Person('Roger',
               ['Cleaning', 'Driving', 'Shopping'],
               [date(2017, 10, 26)])
YURI = Person('Yuri',
              ['Cooking', 'Cleaning', 'Shopping'],
              [date(2017, 10, 27), date(2017, 10, 29)])

PEOPLE = [GORDON, ERFAN, ROGER, YURI]

TASKS = [Task(date(2017, 10, 25), 'Driving'),
         Task(date(2017, 10, 25), 'Shopping'),
         Task(date(2017, 10, 26), 'Cleaning'),
         Task(date(2017, 10, 26), 'Cooking'),
         Task(date(2017, 10, 26), 'Shopping'),
         Task(date(2017, 10, 27), 'Cleaning'),
         Task(date(2017, 10, 27), 'Cooking'),
         Task(date(2017, 10, 28), 'Cleaning'),
         Task(date(2017, 10, 28), 'Cooking'),
         Task(date(2017, 10, 28), 'Shopping'),
         Task(date(2017, 10, 29), 'Cleaning'),
         Task(date(2017, 10, 29), 'Cooking'),
         Task(date(2017, 10, 30), 'Driving', ROGER),
         Task(date(2017, 10, 31), 'Driving', ROGER)]

optimiser = Optimiser(TASKS, PEOPLE)
optimiser.optimise()

for task in TASKS:
    assignee = task.assignee.name if task.assignee is not None else 'UNASSIGNED'
    print(f'{task.date} - {task.skill}: {assignee}')