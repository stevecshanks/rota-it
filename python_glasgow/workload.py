class Workload:

    def __init__(self, people):
        self.people = people
        self.per_person = {person: 0 for person in people}

    def assign(self, task, person):
        task.assignee = person
        self.per_person[person] += 1
        return task

    def get_workload_per_person(self):
        return self.per_person