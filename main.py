import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow
)


def add_label():
    print("add")


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("First app")
    window.setGeometry(300, 250, 350, 200)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("This is base text")
    main_text.move(100, 100)
    main_text.adjustSize()

    btn = QtWidgets.QPushButton(window)
    btn.move(70, 150)
    btn.setText("Press on me")
    btn.setFixedWidth(200)
    btn.clicked.connect(add_label)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
