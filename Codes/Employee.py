class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {} earns {}'.format(self.first, self.last, self.pay)

    def apply_raise(self, pay_amt):
        self.pay = self.pay + pay_amt
