from src.com.jalasoft.compiler.memento.caretaker import Caretaker
from src.com.jalasoft.compiler.memento.computer import Computer

if __name__ == "__main__":
    computer1 = Computer("unix", "16GB", "1TB")
    computer1.to_string()

    computer1.os = "win"
    computer1.memory = "512MB"
    computer1.hdd = "512GB"

    computer1.to_string()

    computer2 = Computer("win", "16GB", "512GB")
    computer2.to_string()

    print("************************************")
    computer3 = Computer("unix", "16GB", "1TB")
    computer3.to_string()
    caretaker = Caretaker()
    caretaker.add_computer(1, computer3.backup())
    print("-------------------")
    computer3.os = "win"
    computer3.memory = "128MB"
    computer3.hdd = "512GB"
    computer3.to_string()
    caretaker.add_computer(2, computer3.backup())

    print("-----------------------")
    computer3.restore(caretaker.get_computer(1))
    computer3.to_string()

    print("-----------------------")
    computer3.restore(caretaker.get_computer(2))
    computer3.to_string()
