# main.py
import sys
import random
from PyQt5 import QtWidgets, uic, QtGui, QtCore


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self):
        self.setWindowTitle("Random Circles")
        self.setGeometry(100, 100, 800, 600)

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.pushButton = QtWidgets.QPushButton("нажми меня", self.centralwidget)
        self.pushButton.setGeometry(280, 240, 191, 41)


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.pushButton.clicked.connect(self.draw_circle)
        self.circles = []

    def draw_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.centralwidget.width())
        y = random.randint(0, self.centralwidget.height())

        color = QtGui.QColor(random.randint(0,255), random.randint(0,255), random.randint(0,255))

        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(QtCore.Qt.NoPen)
        for x, y, diameter, color in self.circles:
            painter.setBrush(QtGui.QBrush(color))
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())