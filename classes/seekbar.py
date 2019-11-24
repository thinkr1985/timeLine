"""Creating seekbar Graphics item for timeline"""
from PyQt5 import QtWidgets, QtGui, QtCore


class SeekBar(QtWidgets.QGraphicsItem):
    """Creating a SeekBar class by inheriting QGraphicsItem"""
    def __init__(self, parent=None, slider=None, scene=None):
        """Initializing SeekBar class
        Args:
            parent (QtWidgets.QGraphicsItem): Parent Item of this widget.
            slider (slider.Slider): Slider object of this seekbar.
            scene (QtWidgets.QGraphicsScene): Scene for this widget.
        """
        super(SeekBar, self).__init__(parent=parent)
        self.slider = slider
        self.scene = scene

    def boundingRect(self):
        return QtCore.QRectF(1, 1, 1, 1)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        pass
