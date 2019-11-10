"""Creating a timeLine widget"""
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

from classes import view, playbar


class TimeLine(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TimeLine, self).__init__(parent=parent)
        self.setContentsMargins(10, 0, 10, 0)
        self.setFixedHeight(75)
        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.startField = FrameField(frameNumber=1)
        self.layout.addWidget(self.startField)
        self.view = view.View()
        self.layout.addWidget(self.view)
        self.currentFrameField = FrameField(frameNumber=1)
        self.layout.addWidget(self.currentFrameField)
        self.endField = FrameField(frameNumber=10)
        self.layout.addWidget(self.endField)
        self.playbar = playbar.PlayBar()
        self.layout.addWidget(self.playbar)


class FrameField(QtWidgets.QLineEdit):
    def __init__(self, parent=None, frameNumber=1):
        super(FrameField, self).__init__(parent=parent)
        self.frameNumber = frameNumber
        self.validator = QtGui.QIntValidator()
        self.setValidator(self.validator)
        self.setText(str(self.frameNumber))
        self.setFixedWidth(50)
        self.setFixedHeight(30)
        self.setStyleSheet("""
                            FrameField{
                                        color: black;
                                        background: transparent;
                                        border: 2px solid grey;
                                        border-radius: 5px;
                                      }
        """)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = TimeLine()
    win.show()
    app.exec()
