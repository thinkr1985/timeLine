"""Creating Slider for timeLine"""
from PyQt5 import QtWidgets, QtCore, QtGui


class Slider(QtWidgets.QGraphicsItem):
    def __init__(self, parent=None, scene=None):
        super(Slider, self).__init__(parent=parent)
        self.scene = scene

    def boundingRect(self):
        return QtCore.QRectF(-10, 10, 10, 10)

    def paint(self, painter, QStyleWidget, widget=None):
        pass