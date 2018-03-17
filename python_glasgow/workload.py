from collections import Counter


class Workload:

    def __init__(self):
        self.per_person = Counter()

    def assign(self, task, person):
        task.assignee = person
        self.per_person[person] += 1
        return task

    def assigned_to(self, person):
        return self.per_person[person]