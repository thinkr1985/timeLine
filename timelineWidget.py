"""Creating a timeLine widget"""
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

from classes import view, playbar


class TimeLine(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TimeLine, self).__init__(parent=parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedHeight(75)
        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.view = view.View()
        self.layout.addWidget(self.view)
        self.playbar = playbar.PlayBar()
        self.layout.addWidget(self.playbar)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = TimeLine()
    win.show()
    app.exec()
