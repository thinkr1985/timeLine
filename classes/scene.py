"""Creating Scene for timeSlider widget"""
from PyQt5 import QtCore, QtGui, QtWidgets

from classes import slider


class Scene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None, view=None):
        super(Scene, self).__init__(parent=parent)
        self.view = view
        self.slider = slider.Slider()
        self.addItem(self.slider)
        self.setBackgroundBrush(QtGui.QColor(QtCore.Qt.transparent))
