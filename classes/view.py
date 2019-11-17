"""Creating View for timeSlider"""
from PyQt5 import QtGui, QtCore, QtWidgets

from classes import scene, variables


class View(QtWidgets.QGraphicsView):
    """Creating View class by inheriting QGraphicsView"""
    def __init__(self, parent=None, framerange=None):
        """Initializing View class.
        Args:
            parent (QtWidgets.QWidget): Parent widget of this class.
            framerange (list): List containing start and end frame.
        """
        super(View, self).__init__(parent=parent)
        self.framerange = framerange
        self.setFixedHeight(variables.SLIDER_HEIGHT)
        self.setContentsMargins(0, 0, 0, 0)
        self.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
        self.setStyleSheet("""
                            View{
                                    border-color:transparent;
                                    border-width: 0px;
                                    border-style: solid;
                                }
                            """)
        self.scene = scene.Scene(view=self, framerange=self.framerange)
        self.setScene(self.scene)

    def resizeEvent(self, event):
        """This method sets scene rectangle on resize event.
        Args:
            event (QtGui.QResizeEvent): QEvent object.

        Returns:
            (None): Returns None.
        """
        self.scene.set_scene_rectangle()
        super().resizeEvent(event)
