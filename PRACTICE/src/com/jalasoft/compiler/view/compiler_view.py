from PyQt5.QtWidgets import QMainWindow

from src.com.jalasoft.compiler.view.main_widget import MainWidget
from src.com.jalasoft.compiler.view.menu import Menu


class CompilerView(QMainWindow):

    def __init__(self):
        super().__init__()
        self.main_widget = MainWidget()
        self.menu = Menu()
        self.setMenuBar(self.menu)

    def init_ui(self):
        self.setWindowTitle("AT19 Compiler")
        self.setGeometry(1000, 1000, 1000, 1000)
        self.setCentralWidget(self.main_widget)
        self.showMaximized()
        self.show()

    def get_search(self):
        return self.main_widget.button1

    def get_show(self):
        return self.main_widget.result.show_image_button

    def set_table(self):
        return self.main_widget.result.table
