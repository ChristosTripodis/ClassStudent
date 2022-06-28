from Codes.Employee import Employee
from Codes.Developer import Developer

emp_1 = Employee('Adam', 'Trip', 1000)
print(emp_1.fullname())
emp_1.apply_raise(1000)
print(emp_1.fullname())

dev_1 = Developer('ch', 'trip', 2000, 'python')
print(dev_1.prog_lang)
dev_1.apply_raise_dev()

print('aaaaa')
print('bbbbb')
print('cccc')
