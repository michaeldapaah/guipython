from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Button & Label')
        self.setWindowIcon(QIcon("ballon.png"))
        self.setGeometry(500, 200, 500, 400)
        self.create_widget()

    def create_widget(self):
        btn = QPushButton("click me", self)
        btn.setGeometry(100, 100, 100, 100)
        btn.setStyleSheet("background-color:red")
        btn.setIcon(QIcon('ballon.png'))

        self.label = QLabel("My Label", self)
        self.label.move(100, 200)
        self.label.setStyleSheet('color:green')
        self.label.setFont(QFont('Times New Roman', 15))

    def clicked_btn(self):



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
