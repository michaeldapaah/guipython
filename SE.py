# se1 = ["Software Engineer", "Max", 20, "Junior", 5000]
# se2 = ["Software Engineer", "lisa", 25, "Senior", 6000]
# d1 = ["Designer", "Philipp"]
from datetime import datetime, timedelta


today = datetime.now()
print('today is ' + str(today))
# one_day = timedelta(days=1)
# yesterday = today - one_day
# print("yesterday was" + str(yesterday))

one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week was' + str(last_week))

# this line of code does nothing
print("hello is a small world")
firstname = 'christoper'
lastname = 'harrison'

print('hello' + ' ' + firstname.capitalize() + ' ' + lastname.capitalize())
print(f'Helo, {firstname} {lastname}')

firstname = 'christopher'
lastname = 'harrison'
day = 28
print(str(day) + 'th day')

pi = 3.14159
print(pi)

first_num = input("please enter the 1st number")
second_num = input("please enter the 2nd number")
print(int(first_num) + int(second_num))

output = 'hello, {1} {0}'.format(firstname, lastname)
print(output)
class SoftwareEngineer:
    alias = "keyboard Magician "

    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_lang(self, language):
        print(f"{self.name} is writing code in {language}...")

    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def entry_salary(age):
        if age < 25:
            return 50000
        if age < 30:
            return 7000
        return 9000

se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
se2 = SoftwareEngineer("Lisa",25, "Senior", 6000)
se3 = SoftwareEngineer("Max", 20, "Junior", 5000)
se1.code()
se2.code()
se1.code_in_lang("C++")
se2.code_in_lang("python")
# print(se1.information())
print(se1.name, se1.age)
print(SoftwareEngineer.alias)
print(se1)
print(se2 )
print(se1 == se3)
# se1.entry_salary(24)
print(SoftwareEngineer.entry_salary(27))

#recap
#instance method(self)
#can take arguments and return values
#special dunder method(__str__ and __eq__)

