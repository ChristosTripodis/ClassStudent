from Codes.Employee import Employee
from Codes.Developer import Developer

emp_1 = Employee('Adam', 'Trip', 1000)
dev_1 = Developer('ch', 'trip', 2000, 'python')


def test_apply_raise_dev():
    emp_1.apply_raise(1000)
    assert emp_1.pay == 2000


def test_apply_raise():
    dev_1.apply_raise_dev()
    assert dev_1.pay == 12000
