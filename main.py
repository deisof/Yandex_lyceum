from sys import argv, exit
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.event = False
        self.pushButton.clicked.connect(self.change)

    def change(self):
        self.event = True
        if self.event:
            self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        if self.event:
            self.x = randint(0, self.width())
            self.y = randint(0, self.height())
            r, g, b = 255, 255, 0
            qp.setBrush(QColor(r, g, b))
            r = randint(1, 100)
            qp.drawEllipse(self.x, self.y, r, r)
            self.event = False


if __name__ == '__main__':
    app = QApplication(argv)
    ex = MyWidget()
    ex.show()
    exit(app.exec())
