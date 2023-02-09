class Employee:

    raise_amount = 1.04
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)


emp_1 = Employee('michael', 'dapaah', 400000)
emp_2 = Employee('Henry', 'Dapaah', 230000)

print(emp_1.pay)
print(emp_2.email)
print(emp_1.apply_raise())
print(emp_1.pay)
print(emp_1.fullname())
print(emp_2.fullname())
