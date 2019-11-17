"""Creating a timeLine widget"""
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

from classes import view, playbar, variables


class TimeLine(QtWidgets.QWidget):
    """Creating a TimeLine widget by inheriting QWidget"""
    def __init__(self, parent=None, frameRange=[1, 50]):
        """Initializing TimeLine class
        Args:
            parent (QtWidget.QWidget): Parent widget of this class.
            frameRange (list): List containing start and end frame.
        """
        super(TimeLine, self).__init__(parent=parent)
        self.frameRange = frameRange
        self.startFrame = self.frameRange[0]
        self.endFrame = self.frameRange[1]
        self.duration = (self.endFrame - self.startFrame) + 1
        self.setContentsMargins(5, 0, 5, 0)
        self.setFixedHeight(variables.SLIDER_WIDTH)

        # setting up main layout
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        self.sliderLayout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.sliderLayout)

        # adding view to the widget
        self.view = view.View(framerange=self.frameRange)
        self.sliderLayout.addWidget(self.view)

        # adding playback buttons to the slider
        self.playbarLayout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.playbarLayout)
        self.startField = FrameField(frameNumber=self.startFrame)
        self.playbarLayout.addWidget(self.startField)
        self.startSpacer = QtWidgets.QSpacerItem(
            0,
            10,
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.Expanding)
        self.playbarLayout.addItem(self.startSpacer)
        self.playbar = playbar.PlayBar()
        self.playbarLayout.addWidget(self.playbar)
        self.endSpacer = QtWidgets.QSpacerItem(
            0, 10,
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.Expanding)
        self.playbarLayout.addItem(self.endSpacer)
        self.currentFrameField = FrameField(frameNumber=self.startFrame)
        self.playbarLayout.addWidget(self.currentFrameField)
        self.endField = FrameField(frameNumber=self.endFrame)
        self.playbarLayout.addWidget(self.endField)
        self.setStyleSheet("""
                            TimeLine{
                                        background-color: darkgray;
                                    }
                            """.replace("darkgray",
                                        variables.TIMELINE_BACKGROUND))

    def setFrameRange(self, framerange):
        """This method sets frame range of this widget.
        Args:
            framerange (list): List containing start and end frame.
        Returns:
            (None): Returns None.
        """
        self.frameRange = framerange
        self.startFrame = framerange[0]
        self.endFrame = framerange[1]
        self.duration = (self.endFrame - self.startFrame) + 1


class FrameField(QtWidgets.QLineEdit):
    def __init__(self, parent=None, frameNumber=1):
        super(FrameField, self).__init__(parent=parent)
        self.frameNumber = frameNumber
        self.validator = QtGui.QIntValidator()
        self.setValidator(self.validator)
        self.setText(str(self.frameNumber))
        self.setFixedWidth(50)
        self.setFixedHeight(30)
        self.setStyleSheet("""
                            FrameField{
                                        color: white;
                                        background: transparent;
                                        border: 1px solid grey;
                                        border-radius: 5px;
                                        font-size: 12px;
                                      }
        """)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = TimeLine()
    win.show()
    app.exec_()
