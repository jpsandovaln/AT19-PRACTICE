from src.com.jalasoft.compiler.observer.observable_product_notification import ObservableProductNotification


class ProductNotification(ObservableProductNotification):

    def __init__(self):
        self.client_map = {"car": [], "pc": []}

    def add_observable_client(self, product, client):
        client_list = self.client_map.get(product)
        client_list.append(client)

    def remover_observable_client(self, product, client):
        client_list = self.client_map.get(product)
        client_list.remove(client)

    def notify_all_client(self, product, message):
        client_list = self.client_map.get(product)
        for client in client_list:
            client.send_message(message)
