from src.com.jalasoft.compiler.builder.pizza import Pizza
from src.com.jalasoft.compiler.builder.bolognesa import Bolognesa
from src.com.jalasoft.compiler.builder.napolitana import Napolitana
from src.com.jalasoft.compiler.builder.hawaiana import Hawaiana


def display(pizza):
    print("*****************PIZZA *****************")
    print(pizza.get_dough())
    print(pizza.get_sauce())
    print(pizza.get_cheese())

    print(pizza.get_ham())
    print(pizza.get_pineapple())

    print(pizza.get_olive())
    print(pizza.get_basil())
    print(pizza.get_meat())
    print(pizza.get_corn())
    print(pizza.get_peperoni())
    print("****************************************")


if __name__ == "__main__":
    # pizza = Pizza("soft", "sweet", "mozarella", None, None, None, None, None, None, None)
    # display(pizza)

    # pizza2 = Pizza("soft", "spicy", "cheddar", "1", "1", None, None, None, None, None)
    # display(pizza2)

    """pizza = Pizza()
    pizza.set_dough("soft")
    pizza.set_sauce("sweet")
    pizza.set_cheese("mozarella")
    display(pizza)"""

    hawaiana: Pizza = Hawaiana().with_pineapple("1").with_ham("1").build()
    display(hawaiana)

    napolitana: Pizza = Napolitana().with_ham("2").build()
    display(napolitana)

    bolognesa: Pizza = Bolognesa().with_meat("yes").with_corn("1").build()
    display(bolognesa)
