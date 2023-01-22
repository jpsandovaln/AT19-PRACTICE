import math
from src.com.jalasoft.compiler.chain.dispenser import Dispenser


class Dispense10Bs(Dispenser):
    def __init__(self):
        self.next_chain = None

    def set_next_chain(self, next_dispense):
        self.next_chain = next_dispense

    def dispense(self, value):
        if value >= 10:
            num = math.trunc(value / 10)
            remainder = value % 10
            print('Dispensing 10 = ' + str(num) + ' Bs')
