import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Doraemon Drawing")
        self.doraemon = QPixmap("image/doraemon.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin()
        p.drawPixmap(QRect(200, 100, 320, 320), self.doraemon)
        p.end()


class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Pikachu Drawing")
        self.pikachu = QPixmap("image/pikachu_dance_37.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(200, 100, 320, 200), self.pikachu)
        p.end()


class Simple_drawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("image/cat5.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(200, 100, 400, 200), self.rabbit)
        p.end()


def main():
    app = QApplication(sys.argv)

    w1 = Simple_drawing_window1()
    w2 = Simple_drawing_window2()
    w3 = Simple_drawing_window3()
    w2.show()
    w1.show()
    w3.show()

    w = Simple_drawing_window2()
    w.show()

    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
