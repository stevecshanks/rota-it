from collections import Counter


class Workload:

    def __init__(self, tasks):
        self.per_person = Counter(task.assignee for task in tasks)

    def assign(self, task, person):
        task.assignee = person
        self.per_person[person] += 1
        return task

    def assigned_to(self, person):
        return self.per_person[person]

    def get_least_busy_person(self, people):
        if not people:
            return None
        return sorted(people, key=lambda person: self.assigned_to(person))[0]