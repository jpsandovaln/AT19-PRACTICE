from PyQt5.QtWidgets import QVBoxLayout, QTableWidget, QPushButton


class Result(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(('Percentage', 'Time'))

        self.show_image_button = QPushButton('Show image')
        self.addWidget(self.table)
        self.addWidget(self.show_image_button)
