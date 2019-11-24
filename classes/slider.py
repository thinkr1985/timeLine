"""Creating Slider for timeLine"""
from PyQt5 import QtWidgets, QtCore, QtGui

from classes import tick, logger


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
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)

    def boundingRect(self):
        """This method creats bounding rectangle for this widget.
        Returns:
            (QtCore.QRectF): Returns QRectF object.
        """
        return QtCore.QRectF(-40, 10, 75, 10)

    def removeTicks(self):
        """This method removes all tick frames in this widget.
        Returns:
            (None): Returns None.
        """
        if not self.ticks:
            return
        for tick_item in self.ticks:
            self.ticks.remove(tick_item)
            if tick_item in self.scene.items():
                self.scene.removeItem(tick_item)

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
        # clearing all the ticks
        self.removeTicks()

        tick_separator_length = slider_width / (
                (self.framerange[1] - self.framerange[0]) + 2)
        separator_length = tick_separator_length

        for num in range(self.framerange[0], self.framerange[1] + 1):
            tick_object = tick.Tick(self, framenumber=num, slider=self)
            self.ticks.append(tick_object)
            tick_object.setPos(-slider_width + separator_length, 0)
            separator_length = separator_length + tick_separator_length

    def removeFrame(self, frame_number):
        """This method remove frame tick from the slider.
        Args:
            frame_number (int): Frame number.
        Returns:
            (list): Returns list containing all frame ticks items.
        """
        if self.ticks:
            for tick_item in self.ticks:
                if tick_item.frameNumber == frame_number:
                    tick_item.remove()
                    self.ticks.remove(tick_item)
                    return self.ticks

    def removeFrames(self, frame_numbers):
        """This method removes given frame ticks from the slider.
        Args:
            frame_numbers (list): List containing frame numbers.
        Returns:
            (list): Returns list containing all frame ticks items.
        """
        if self.ticks:
            for tick_item in self.ticks:
                if tick_item.frameNumber in frame_numbers:
                    tick_item.remove()
                    self.ticks.remove(tick_item)
        return self.ticks

    def setFrameRange(self, frame_range):
        """This method sets frame range of slider.
        Args:
            frame_range (list): List contaning start and end frame integers.
        Returns:
            (list): Returns list of Tick items.
        """
        if frame_range[0] <= frame_range[1]:
            logger.log(msg="Setting frame range to [{}-{}]".format(
                frame_range[0], frame_range[1]))
            self.framerange = frame_range
            self.scene.update()
            return self.ticks
        else:
            logger.log(
                typ="ERROR",
                msg="Set Frame range Error,"
                    " start frame cannot be greater than end frame")