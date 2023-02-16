import sys
from PySide6.QtCore import *
from PySide6.QtWidget import *
from PySide6.QtGui import *

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Github Drawing")
        self.doraemon = QPixmap("image/doraemon.png")

    def paintEvent(self,e):
        p = QPainter()
        p.begin()

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint(70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
        ])

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawpie(50, 150, 100, 100, 0,  180*16)

        p.drawPolygon(
            [QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),]
        )

        p.drawPixmap(QRect(200, 100, 320, 320), self.doraemon)


def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window1()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())