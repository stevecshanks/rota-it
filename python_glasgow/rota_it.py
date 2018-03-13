import pprint


tasks = {
    "25/10/2017": {
        "Driving": None,
        "Shopping": None
    },
    "26/10/2017": {
        "Cleaning": None,
        "Cooking": None,
        "Shopping": None
    },
    "27/10/2017": {
        "Cleaning": None,
        "Cooking": None
    },
    "28/10/2017": {
        "Cleaning": None,
        "Cooking": None,
        "Shopping": None
    },
    "29/10/2017": {
        "Cleaning": None,
        "Cooking": None
    },
    "30/10/2017": {
        "Driving": ["Roger"]
    },
    "31/10/2017": {
        "Driving": ["Roger"]
    }
}

skills = {
    "Gordon": ["Cleaning", "Driving", "Shopping"],
    "Erfan": ["Cleaning", "Cooking", "Driving", "Shopping"],
    "Roger": ["Cleaning", "Driving", "Shopping"],
    "Yuri": ["Cooking", "Cleaning", "Shopping"]
}

vacations = {
    "25/10/2017": [],
    "26/10/2017": ["Gordon", "Roger"],
    "27/10/2017": ["Yuri"],
    "28/10/2017": ["Erfan"],
    "29/10/2017": ["Gordon", "Yuri"],
    "30/10/2017": [],
    "31/10/2017": []
}

workload = {
    "Gordon": 0,
    "Erfan": 0,
    "Roger": 0,
    "Yuri": 0
}

max_length = 0
for (date, todos) in tasks.items():
    for todo in todos.keys():
        skilled_people = [person for person, abilities
                          in skills.items()
                          if todo in abilities
                          and person not in vacations[date]]
        todos[todo] = skilled_people
        if (len(skilled_people) > max_length):
            max_length = len(skilled_people)

for i in range(1, max_length + 1):
    for (date, todos) in tasks.items():
        for (todo, assignments) in todos.items():
            if not isinstance(assignments, list) or len(assignments) != i: continue
            (_, assignee) = sorted([(numTasks, person) for person, numTasks in workload.items() if person in assignments])[0]
            workload[assignee] += 1
            todos[todo] = assignee

pprint.pprint(tasks)
pprint.pprint(workload)
