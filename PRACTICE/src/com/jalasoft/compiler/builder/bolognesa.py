from src.com.jalasoft.compiler.builder.builder_pizza import BuilderPizza
from src.com.jalasoft.compiler.builder.pizza import Pizza


class Bolognesa(BuilderPizza):

    def __init__(self):
        self.pizza = Pizza()
        self.pizza.set_dough("soft")
        self.pizza.set_sauce("sweet")
        self.pizza.set_cheese("mozarella")

    def with_meat(self, meat):
        self.pizza.set_meat(meat)
        return self

    def with_corn(self, corn):
        self.pizza.set_corn(corn)
        return self

    def build(self):
        return self.pizza