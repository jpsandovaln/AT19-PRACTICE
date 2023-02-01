from src.com.jalasoft.compiler.composite.composite_product import CompositeProduct
from src.com.jalasoft.compiler.composite.hardware import HardWare
from src.com.jalasoft.compiler.composite.software import Software


class Sales:
    def __init__(self, code):
        self.code = code
        self.product_list = []

    def get_code(self):
        return self.code

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total(self):
        total = 0
        for product in self.product_list:
            total = total + product.get_price()
        return total

    def display(self):
        print("--------------------------")
        print("sales code: " + self.code)
        for product in self.product_list:
            print("Product: " + product.get_name() + " - Price: " + str(product.get_price()))
        print("Total: " + str(self.get_total()))
        print("--------------------------")


if __name__ == '__main__':
    memory = HardWare("memory", 100, "abc")
    hdd = HardWare("hdd", 200, "xyz")
    motherboard = HardWare("motherboard", 300, "asus")

    cd = Software("windows", 30, "os")

    product_pc1 = CompositeProduct("PC Gamer")
    product_pc1.add_product(memory)
    product_pc1.add_product(motherboard)
    product_pc1.add_product(hdd)

    product_pc2 = CompositeProduct("PC Personal")
    product_pc2.add_product(memory)
    product_pc2.add_product(hdd)

    product_pc3 = CompositeProduct("PC PLUS")
    product_pc3.add_product(memory)
    product_pc3.add_product(hdd)
    product_pc3.add_product(motherboard)
    product_pc3.add_product(cd)

    product_pc4 = CompositeProduct("Combo pc")
    product_pc4.add_product(product_pc1)
    product_pc4.add_product(product_pc2)

    product_pc5 = CompositeProduct("Combo pc super")
    product_pc5.add_product(product_pc1)
    product_pc5.add_product(product_pc3)
    product_pc5.add_product(memory)

    sales = Sales("A1")
    sales.add_product(memory)
    sales.add_product(hdd)
    sales.add_product(cd)

    sales.display()

    sales2 = Sales("A2")
    sales2.add_product(product_pc1)
    sales2.display()

    sales3 = Sales("A3")
    sales3.add_product(product_pc5)
    sales3.add_product(product_pc2)
    sales3.add_product(motherboard)
    sales3.display()
