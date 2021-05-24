"""

"""

class Wallet:
    def __init__(self, current_balance):
        if current_balance < 0:
            raise ValueError
        self.current_balance = current_balance

    def get_curret_balance(self):
        current_bal = self.current_balance
        return current_bal

    def add_current_balance(self, a):
        if a < 0:
            raise ValueError
        self.current_balance = self.current_balance + a

    def subtract_current_balance(self, b):
        if b > self.current_balance or b < 0:
            raise ValueError
        self.current_balance = self.current_balance - b




