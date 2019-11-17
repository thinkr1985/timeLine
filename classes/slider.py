"""Creating Slider for timeLine"""
from PyQt5 import QtWidgets, QtCore, QtGui

from classes import tick, variables


class Slider(QtWidgets.QGraphicsItem):
    """Creating Slider class by inheriting QGraphicsItem"""
    def __init__(self, parent=None, scene=None, framerange=None):
        """Initializing Slider class.
        Args:
            parent (QtWidgets.QGraphicsItem): Parent widget of this class.
            scene (QtWidgets.QGraphicsScene): QGraphicsScene instance.
            framerange (list): list containing start and end frame.
        """
        super(Slider, self).__init__(parent=parent)
        self.scene = scene
        self.framerange = framerange
        self.ticks = []

    def boundingRect(self):
        """This method creats bounding rectangle for this widget.
        Returns:
            (QtCore.QRectF): Returns QRectF object.
        """
        return QtCore.QRectF(-40, 10, 75, 10)

    def paint(self, painter, QStyleWidget, widget=None):
        """This method paints widget on the screen.
        Args:
            painter (QtGui.QPainter): QPainter object.
            QStyleWidget (list): List containing graphics options
            widget (QtWidgets.QWidget): QWidget instance.

        Returns:
            (None): Returns None.
        """
        slider_width = self.scene.view.size().width() + 20
        if self.ticks:
            [self.scene.removeItem(x) for x in self.ticks]

        tick_separator_lenth = slider_width / ((self.framerange[1] - self.framerange[0]) + 2)
        separator_length = tick_separator_lenth
        for num in range(self.framerange[0], self.framerange[1] + 1):
            tick_object = tick.Tick(frameNumber=num)
            self.scene.addItem(tick_object)
            self.ticks.append(tick_object)
            tick_object.setPos(-slider_width + separator_length, 0)
            separator_length = separator_length + tick_separator_lenth
