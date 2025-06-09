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

        main_text = QtWidgets.QLabel(self)
        main_text.setText("This is base text")
        main_text.move(100, 100)
        main_text.adjustSize()

        btn = QtWidgets.QPushButton(self)
        btn.move(70, 150)
        btn.setText("Press on me")
        btn.setFixedWidth(200)
        btn.clicked.connect(self.add_label)


    @staticmethod
    def add_label():
        print("add")


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
