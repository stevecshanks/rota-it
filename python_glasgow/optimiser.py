from python_glasgow.workload import Workload


class Optimiser:

    def __init__(self, tasks, people):
        self.tasks = tasks
        self.people = people
        self.workload = Workload()

    def optimise(self):
        for task in self._get_tasks_by_difficulty():
            eligible_people = self._get_eligible_people(task)
            best_person = self.workload.get_least_busy_person(eligible_people)
            if best_person:
                self.workload.assign(task, best_person)
                continue

    def _get_tasks_by_difficulty(self):
        return sorted(self.tasks,
                      key=lambda task: len([p for p in self._get_eligible_people(task)]))

    def _get_eligible_people(self, task):
        if task.assignee:
            return [task.assignee]
        return [person for person in self.people
                if person.has_skill(task.skill)
                and person.is_available_on(task.date)]