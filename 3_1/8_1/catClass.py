class Cat:
    def __init__(self, name, gend, age):
        self.name = name
        self.gend = gend
        self.age = age

    def get_name(self):
        return self.name

    def get_gend(self):
        return self.gend

    def get_age(self):
        return self.age


class Dog(Cat):
    def get_pet(self):
        return f'{self.name}, {self.age}'
