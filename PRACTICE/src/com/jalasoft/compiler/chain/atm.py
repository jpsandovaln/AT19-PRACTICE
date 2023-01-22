from src.com.jalasoft.compiler.chain.dispense_10bs import Dispense10Bs
from src.com.jalasoft.compiler.chain.dispense_20bs import Dispense20Bs
from src.com.jalasoft.compiler.chain.dispense_50bs import Dispense50Bs
from src.com.jalasoft.compiler.chain.dispense_100bs import Dispense100Bs


class ATM:
    def __init__(self, value):
        self.value = value

    def get_money(self):
        """if self.value >= 100:
            data = Dispense100Bs()
            self.value = data.dispense(self.value)
        if self.value >= 50:
            data = Dispense50Bs()
            self.value = data.dispense(self.value)
        if self.value >= 20:
            data = Dispense20Bs()
            self.value = data.dispense(self.value)
        if self.value >= 10:
            data = Dispense10Bs()
            self.value = data.dispense(self.value)
        print("reminder = " + str(self.value))"""
        dispense_100 = Dispense100Bs()
        dispense_50 = Dispense50Bs()
        dispense_20 = Dispense20Bs()
        dispense_10 = Dispense10Bs()

        dispense_100.set_next_chain(dispense_50)
        dispense_50.set_next_chain(dispense_20)
        dispense_20.set_next_chain(dispense_10)

        dispense_100.dispense(self.value)


if __name__ == '__main__':
    atm = ATM(320)
    atm.get_money()
