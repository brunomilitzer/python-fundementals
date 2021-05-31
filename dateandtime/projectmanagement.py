from datetime import date


class Project:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)


class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.resources = []

    def add_resource(self, resource):
        self.resources.append(resource)


class Resource:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill


project = Project("AI", date(2021, 4, 1), date(2022, 3, 31))
task = Task("Create Bot", 90)
project.add_task(task)
resource = Resource("Vanessa", "Python")
task.add_resource(resource)

for each_task in project.tasks:
    print(each_task.name)
    for each_resource in each_task.resources:
        print(each_resource.name)
