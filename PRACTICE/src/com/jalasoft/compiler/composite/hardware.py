from src.com.jalasoft.compiler.composite.product import Product


class HardWare(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def get_brand(self):
        return self.brand
