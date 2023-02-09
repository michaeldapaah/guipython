class Dog:
    def __init__(self, name, age):
        self.name = name
        print(name)
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog("Tim", 22)
d.set_age(25)
print(d.get_age())
