# main.py
import sys
import random
from PyQt5 import QtWidgets, uic, QtGui, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("qt.ui", self)
        self.pushButton.clicked.connect(self.draw_circle)
        self.circles = []

    def draw_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.centralwidget.width())
        y = random.randint(0, self.centralwidget.height())
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setBrush(QtGui.QBrush(QtGui.QColor("yellow")))
        painter.setPen(QtCore.Qt.NoPen)
        for x, y, diameter in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())