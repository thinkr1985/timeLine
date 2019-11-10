"""Creating View for timeSlider"""
from PyQt5 import QtGui, QtCore, QtWidgets

from classes import scene


class View(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super(View, self).__init__(parent=parent)
        self.scene = scene.Scene(view=self)
        self.setScene(self.scene)
        self.setMinimumWidth(200)
        self.setRenderHints(
                            QtGui.QPainter.Antialiasing |
                            QtGui.QPainter.HighQualityAntialiasing |
                            QtGui.QPainter.TextAntialiasing |
                            QtGui.QPainter.SmoothPixmapTransform
                            )
        self.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
        self.setStyleSheet("""
                            View{
                                    border-color:transparent;
                                }
                            """)

