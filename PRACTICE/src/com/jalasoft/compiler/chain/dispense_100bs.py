import math
from src.com.jalasoft.compiler.chain.dispenser import Dispenser


class Dispense100Bs(Dispenser):
    def __init__(self):
        self.next_chain = None

    def set_next_chain(self, next_dispense):
        self.next_chain = next_dispense

    def dispense(self, value):
        if value >= 100:
            num = math.trunc(value / 100)
            remainder = value % 100
            print('Dispensing 100 = ' + str(num) + ' Bs')
            if remainder is not 0:
                self.next_chain.dispense(remainder)
        else:
            self.next_chain.dispense(value)
