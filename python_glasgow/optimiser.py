from python_glasgow.workload import Workload


class Optimiser:

    def __init__(self, tasks, people):
        self.tasks = tasks
        self.people = people
        self.workload = Workload()

    def optimise(self):
        for task in self.tasks:
            eligible_people = [person for person in self.people
                               if person.has_skill(task.skill)
                               and person.is_available_on(task.date)]
            best_person = self.workload.get_least_busy_person(eligible_people)
            if best_person:
                self.workload.assign(task, best_person)
                continue