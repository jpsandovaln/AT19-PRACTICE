from src.com.jalasoft.compiler.observer.client import Client


class Company(Client):
    def __init__(self, name, cell_phone):
        self.name = name
        self.cell_phone = cell_phone

    def get_name(self):
        return self.name

    def get_cell_phone(self):
        return self.cell_phone

    def send_message(self, message):
        print("------------------------------")
        print("Sending message to company: " + self.name)
        print("Whatsapp: " + str(self.cell_phone))
        print("message: " + message)
