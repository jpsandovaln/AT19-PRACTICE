import abc


class ObservableProductNotification(abc.ABC):
    def notify_all_client(self, product, message):
        """ Implement notify_all_client method """

    def add_observable_client(self, product, client):
        """ Implement add_observable_client """

    def remover_observable_client(self, product, client):
        """ Implement remove_observable_client """
