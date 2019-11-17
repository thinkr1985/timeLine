"""Creating Scene for timeSlider widget"""
from PyQt5 import QtCore, QtGui, QtWidgets

from classes import slider, variables


class Scene(QtWidgets.QGraphicsScene):
    """Creating Scene class by inheriting QGraphicsScene"""
    def __init__(self, parent=None, view=None, framerange=None):
        """Initializing Scene class.
        Args:
            parent (QtWidgets.QGraphicsView): Parent QGraphicsView instance.
            view (QtWidgets.QGraphicsView): Parent QGraphicsView instance.
            framerange (list): List of start and end frame.
        """
        super(Scene, self).__init__(parent=parent)
        self.framerange = framerange
        self.view = view
        self.slider = slider.Slider(framerange=framerange, scene=self)
        self.addItem(self.slider)
        self.setBackgroundBrush(QtGui.QColor(variables.TIMELINE_BACKGROUND))

    def set_scene_rectangle(self):
        """This method sets scene rectangle.
        Returns:
            (None): Returns None.
        """
        self.setSceneRect(-self.view.size().width(),
                          -(self.view.size().height()/2),
                          self.view.size().width(),
                          self.view.size().height())
