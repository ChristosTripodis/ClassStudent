from Codes import Employee


class Developer(Employee):

    pay_amt = 10000

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def apply_raise_dev(self):
        self.pay = self.pay + self.pay_amt

print(__name__)