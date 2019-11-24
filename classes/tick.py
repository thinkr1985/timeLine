"""Creating Tick Graphics Item"""
from PyQt5 import QtCore, QtGui, QtWidgets

from classes import variables


class Tick(QtWidgets.QGraphicsPolygonItem):
    """Creating a Tick class by inheriting QGraphicsPolygonItem"""
    def __init__(self, parent=None, framenumber=1, slider=None):
        """This method initializes Tick class.
        Args:
            parent (QtWidgets.QGraphicsItem): QGraphicsItem instance.
            framenumber (int): Frame number of the tick.
            slider (slider.Slider): slider object.
        """
        super(Tick, self).__init__(parent=parent)
        self.slider = slider
        self.frameNumber = framenumber
        self.keyed = True
        self.pen = QtGui.QPen(QtCore.Qt.NoPen)
        self.brush = QtGui.QBrush(QtGui.QColor(variables.TICK_COLOR))
        self.keyBrush = QtGui.QBrush(QtGui.QColor(variables.KEY_COLOR))
        self.selectedPen = QtGui.QPen(QtCore.Qt.white)
        self.setToolTip(str(self.frameNumber))
        self.setFlags(QtWidgets.QGraphicsPolygonItem.ItemIsSelectable)

    def boundingRect(self):
        """This method sets bounding rectangle of this widget.
        Returns:
            (QtCore.QRectF): Returns QRectF object.
        """
        return QtCore.QRectF(-variables.TICK_HEIGHT,
                             -variables.TICK_WIDTH,
                             variables.TICK_WIDTH,
                             variables.TICK_HEIGHT)

    def paint(self, painter, QGraphicsStyleOptions, widget=None):
        """This method paints widget on the screen.
        Args:
            painter (QtGui.QPainter): QPainter object.
            QGraphicsStyleOptions (list): Graphics style options.
            widget (QtWidgets.QWidget):

        Returns:
            (None): Returns None.
        """
        # drawing a tick
        if self.isSelected():
            painter.setPen(self.selectedPen)
            self.selectedPen.setWidth(2)
        else:
            painter.setPen(self.pen)
        painter.setBrush(self.brush)

        points = [QtCore.QPointF(-variables.TICK_WIDTH, 0),
                  QtCore.QPointF(-variables.TICK_WIDTH, -variables.TICK_HEIGHT),
                  QtCore.QPointF(variables.TICK_WIDTH, -variables.TICK_HEIGHT),
                  QtCore.QPointF(variables.TICK_WIDTH, variables.TICK_HEIGHT)]
        polygon = QtGui.QPolygonF(points)
        self.setPolygon(polygon)
        painter.drawPolygon(polygon)

        if self.keyed:
            painter.setBrush(self.keyBrush)
            points = [QtCore.QPointF(-(variables.TICK_WIDTH + 1),
                                     variables.TICK_HEIGHT),
                      QtCore.QPointF(-(variables.TICK_WIDTH + 1), 0),
                      QtCore.QPointF(variables.TICK_WIDTH + 1, 0),
                      QtCore.QPointF(variables.TICK_WIDTH + 1,
                                     variables.TICK_HEIGHT)]
            key_polygon = QtGui.QPolygonF(points)
            painter.drawPolygon(key_polygon)

    def remove(self):
        self.slider.scene.removeItem(self)
