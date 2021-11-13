# -*- coding: utf-8 -*-


import sys


from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter
from PyQt5 import uic


SCREEN_SIZE = [355, 380]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.do_paint = False
        uic.loadUi("UI.ui", self)

        self.setFixedSize(*SCREEN_SIZE)
        self.initUI()

    def initUI(self):
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        from random import randint

        radius = randint(5, 200)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(100, 100, radius, radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
