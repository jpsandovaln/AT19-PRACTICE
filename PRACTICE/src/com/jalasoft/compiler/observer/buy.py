from src.com.jalasoft.compiler.observer.product_notification import ProductNotification
from src.com.jalasoft.compiler.observer.company import Company
from src.com.jalasoft.compiler.observer.consumer import Consumer


if __name__ == "__main__":
    ob1 = ProductNotification()

    ob1.add_observable_client("pc", Consumer("Maria", "Arce", "maria.arce@gamil.com"))
    ob1.add_observable_client("pc", Consumer("Carlos", "Lima", "carlos.lima@gmail.com"))

    ob1.add_observable_client("car", Consumer("pepe", "lucho", "pepe.lucho@gmail.com"))
    ob1.add_observable_client("car", Company("Toyota", "451266548"))

    new_product = input("Add product: ")
    ob1.notify_all_client(new_product, "The product is available")
