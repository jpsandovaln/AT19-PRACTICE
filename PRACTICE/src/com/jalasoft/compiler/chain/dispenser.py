import abc


class Dispenser(abc.ABC):
    @abc.abstractmethod
    def dispense(self, value):
        """ Dispense must be implemented"""

    def set_next_chain(self, next_dispense):
        """ set_next_chain must be implemented """
