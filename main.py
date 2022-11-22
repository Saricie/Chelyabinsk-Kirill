import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.btn.clicked.connect(self.repaint)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.paint(qp)
        qp.end()

    def paint(self, qp):
        color = QColor('yellow')
        qp.setBrush(color)
        x = random.randint(1, 399)
        y = random.randint(1, 299)
        w = random.randint(10, 300)
        qp.drawEllipse(x, y, w, w)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
