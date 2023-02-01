from src.com.jalasoft.compiler.composite.product import Product


class Software(Product):
    def __init__(self, name, price, type_sof):
        super().__init__(name, price)
        self.type_sof = type_sof

    def get_type_sof(self):
        return self.type_sof
