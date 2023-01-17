from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout

from src.com.jalasoft.compiler.view.result import Result


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("button a")
        # self.button2 = QPushButton("button b")
        self.result = Result()

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.button1, 20)
        self.layout.addLayout(self.result, 70)
        # self.layout.addWidget(self.button2, 80)
        self.setLayout(self.layout)
