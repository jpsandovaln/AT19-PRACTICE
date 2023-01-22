import math
from src.com.jalasoft.compiler.chain.dispenser import Dispenser


class Dispense20Bs(Dispenser):
    def __init__(self):
        self.next_chain: Dispenser = None

    def set_next_chain(self, next_dispense):
        self.next_chain = next_dispense

    def dispense(self, value):
        if value >= 20:
            num = math.trunc(value / 20)
            remainder = value % 20
            print('Dispensing 20 = ' + str(num) + ' Bs')
            if remainder is not 0:
                self.next_chain.dispense(remainder)
        else:
            self.next_chain.dispense(value)
