class Person:

    def __init__(self, name, skills, vacations):
        self.name = name
        self.skills = skills
        self.vacations = vacations

    def has_skill(self, skill):
        return skill in self.skills

    def is_available_on(self, date):
        return date not in self.vacations

    def __repr__(self):
        return f'Person({self.name}, {self.skills}, {self.vacations})'
