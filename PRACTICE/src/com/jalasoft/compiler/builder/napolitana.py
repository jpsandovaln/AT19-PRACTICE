from src.com.jalasoft.compiler.builder.builder_pizza import BuilderPizza
from src.com.jalasoft.compiler.builder.pizza import Pizza


class Napolitana(BuilderPizza):

    def __init__(self):
        self.pizza = Pizza()
        self.pizza.set_dough("soft")
        self.pizza.set_sauce("spicy")
        self.pizza.set_cheese("cheddar")
        self.pizza.set_olive("green")
        self.pizza.set_peperoni("1")
        self.pizza.set_ham("1")

    def with_ham(self, ham):
        self.pizza.set_ham(ham)
        return self

    def build(self):
        return self.pizza
