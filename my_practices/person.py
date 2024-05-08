class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # public method
    def print_person(self):
        print(f"Person: {self.name}, Age: {self.age}")
        self.__print_person3();    

    # protected method
    def _print_person2(self):
        print(f"Protected method: Person: {self.name}, Age: {self.age}")
    
    # private method
    def __print_person3(self):
        print(f"Private method: Person: {self.name}, Age: {self.age}")
