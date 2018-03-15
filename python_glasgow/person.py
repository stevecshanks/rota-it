class Person:

    def __init__(self, name, skills, vacations):
        self.name = name
        self.skills = skills
        self.vacations = vacations

    def has_skill(self, skill):
        return skill in self.skills

    def is_available_on(self, date):
        return True
