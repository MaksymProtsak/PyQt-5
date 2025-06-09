import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow
)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("First app")
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("This is base text")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Press on me")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)


    def add_label(self):
        self.new_text.setText("Second text")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
