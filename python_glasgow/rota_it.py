import pprint
from datetime import date
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


tasks = {
    date(2017, 10, 25): {
        'Driving': None,
        'Shopping': None
    },
    date(2017, 10, 26): {
        'Cleaning': None,
        'Cooking': None,
        'Shopping': None
    },
    date(2017, 10, 27): {
        'Cleaning': None,
        'Cooking': None
    },
    date(2017, 10, 28): {
        'Cleaning': None,
        'Cooking': None,
        'Shopping': None
    },
    date(2017, 10, 29): {
        'Cleaning': None,
        'Cooking': None
    },
    date(2017, 10, 30): {
        'Driving': [ROGER.name]
    },
    date(2017, 10, 31): {
        'Driving': [ROGER.name]
    }
}

workload = {
    GORDON.name: 0,
    ERFAN.name: 0,
    ROGER.name: 0,
    YURI.name: 0
}

for task in TASKS:
    assignee = task.assignee.name if task.assignee is not None else 'UNASSIGNED'
    print(f'{task.date} - {task.skill}: {assignee}')


def assign_tasks(tasks, people):
    pass


def get_eligible_people(task, people):
    return [person for person in people
            if person.has_skill(task.skill)
            and person.is_available_on(task.date)]


def get_least_busy_person(tasks, people):
    if len(people) == 0:
        return None
    return sorted(people,
                  key=lambda person: len(get_assigned_tasks(tasks, person)))[0]


def get_assigned_tasks(tasks, person):
    return [task for task in tasks if task.assignee == person]


if __name__ == '__main__':
    for task in TASKS:
        if task.assignee is None:
            continue
        eligible_people = get_eligible_people(task, PEOPLE)
        task.assignee = get_least_busy_person(TASKS, eligible_people)

    for task in TASKS:
        assignee = task.assignee.name if task.assignee is not None else 'UNASSIGNED'
        print(f'{task.date} - {task.skill}: {assignee}')
    exit(0)

    max_length = 0
    for task in TASKS:
        eligible_people = [person.name for person
                           in PEOPLE
                           if person.has_skill(task.skill)
                           and person.is_available_on(task.date)]
        todos[todo] = eligible_people
        if (len(eligible_people) > max_length):
            max_length = len(eligible_people)

    for i in range(1, max_length + 1):
        for (date, todos) in tasks.items():
            for (todo, assignments) in todos.items():
                # Assign tasks with the fewest number of eligible people first
                if not isinstance(assignments, list) or len(assignments) != i: continue
                (_, assignee) = sorted([(numTasks, person) for person, numTasks in workload.items() if person in assignments])[0]
                workload[assignee] += 1
                todos[todo] = assignee

    pprint.pprint(tasks)
    pprint.pprint(workload)
