from person import Person

# Class worker extends from class Person
class Worker(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_worker(self):
        self._print_person2()