"""Creating Tick Graphics Item"""
from PyQt5 import QtCore, QtGui, QtWidgets


class Tick(QtWidgets.QGraphicsItem):
    def __init__(self, parent=None, frameNumber=1):
        super(Tick, self).__init__(parent=parent)
        self.frameNumber = frameNumber
        self.keyed = True
        self.pen = QtGui.QPen(QtCore.Qt.NoPen)
        self.brush = QtGui.QBrush(QtCore.Qt.black)
        self.keyBrush = QtGui.QBrush(QtCore.Qt.red)
        self.keyPen = QtGui.QPen(QtCore.Qt.NoPen)

    def boundingRect(self):
        return QtCore.QRectF(
            -10, 10, 10, 10
        )

    def paint(self, painter, QGraphicsStyleOptions, widget=None):
        pass
