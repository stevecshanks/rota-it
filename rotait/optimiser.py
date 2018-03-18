from rotait.workload import Workload


class Optimiser:

    def __init__(self, tasks, people):
        self.tasks = tasks
        self.people = people
        self.workload = Workload(tasks)

    def optimise(self):
        for task in self._sort_by_difficulty(self._get_unassigned()):
            eligible_people = self._get_eligible_people(task)
            best_person = self.workload.get_least_busy_person(eligible_people)
            if best_person:
                self.workload.assign(task, best_person)

    def _get_unassigned(self):
        return [task for task in self.tasks if task.assignee is None]

    def _sort_by_difficulty(self, tasks):
        return sorted(tasks,
                      key=lambda task: len([p for p in self._get_eligible_people(task)]))

    def _get_eligible_people(self, task):
        return [person for person in self.people
                if person.has_skill(task.skill)
                and person.is_available_on(task.date)]