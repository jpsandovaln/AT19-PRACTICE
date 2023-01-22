import math
from src.com.jalasoft.compiler.chain.dispenser import Dispenser


class Dispense50Bs(Dispenser):
    def __init__(self):
        self.next_chain = None

    def set_next_chain(self, next_dispense):
        self.next_chain = next_dispense

    def dispense(self, value):
        if value >= 50:
            num = math.trunc(value / 50)
            remainder = value % 50
            print('Dispensing 50 = ' + str(num) + ' Bs')
            if remainder is not 0:
                self.next_chain.dispense(remainder)
            return
        else:
            self.next_chain.dispense(value)
