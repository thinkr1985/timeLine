"""Creating a timeLine widget"""
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

from classes import view, playbar, variables, logger


class TimeLine(QtWidgets.QWidget):
    """Creating a TimeLine widget by inheriting QWidget"""
    def __init__(self, parent=None, framerange=[1, 50]):
        """Initializing TimeLine class
        Args:
            parent (QtWidget.QWidget): Parent widget of this class.
            framerange (list): List containing start and end frame.
        """
        super(TimeLine, self).__init__(parent=parent)
        self.frameRange = framerange
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
        self.playbar = playbar.PlayBar(timelineScene=self.view.scene,
                                       framerange=framerange)
        self.playbarLayout.addWidget(self.playbar)
        self.endSpacer = QtWidgets.QSpacerItem(
            0, 10,
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.Expanding)
        self.playbarLayout.addItem(self.endSpacer)
        self.currentField = FrameField(frameNumber=self.startFrame)
        self.playbarLayout.addWidget(self.currentField)
        self.endField = FrameField(frameNumber=self.endFrame)
        self.playbarLayout.addWidget(self.endField)
        self.setStyleSheet("""
                            TimeLine{
                                        background-color: darkgray;
                                    }
                            """.replace("darkgray",
                                        variables.TIMELINE_BACKGROUND))
        # connecting widgets to their functions.
        self.connect_()

    def connect_(self):
        """This method connects widgets to its fucntions.
        Returns:
            (None): Returns None.
        """
        self.startField.textEdited.connect(self.onChangeStartField)
        self.currentField.textEdited.connect(self.onChangeCurrentField)
        self.endField.textEdited.connect(self.onChangeEndField)

    def onChangeStartField(self):
        """This method sets time line on start field change.
        Returns:
            (None): Return None
        """
        start_frame = self.startField.text()
        end_frame = self.endField.text()
        if not start_frame.isdigit() or not end_frame.isdigit():
            logger.log(typ="ERROR",
                       msg="start frame must be an integer.")
            self.startField.setText(str(self.startFrame))
            return
        if int(start_frame) > int(end_frame):
            logger.log(typ="ERROR",
                       msg="Start frame cannot be greater than end frame")
            self.startField.setText(str(self.startFrame))
            return

        self.setFrameRange([start_frame, end_frame])

    def onChangeCurrentField(self):
        pass

    def onChangeEndField(self):
        """This method sets the frame-range on end field change.
        Returns:
            (None): Returns None.
        """
        start_frame = self.startField.text()
        end_frame = self.endField.text()
        if not start_frame.isdigit() or not end_frame.isdigit():
            logger.log(typ="ERROR",
                       msg="end frame number must be an integer.")
            self.endField.setText(str(self.endFrame))
            return
        if int(end_frame) < int(start_frame):
            logger.log(typ="ERROR",
                       msg="Start frame cannot be greater than end frame")
            self.endField.setText(str(self.endFrame))
            return

        self.setFrameRange([start_frame, end_frame])

    def setFrameRange(self, framerange):
        """This method sets frame range of this widget.
        Args:
            framerange (list): List containing start and end frame.
        Returns:
            (None): Returns None.
        """
        if not framerange[0].isdigit()\
                or not framerange[1].isdigit():
            logger.log(
                typ="ERROR",
                msg="Frame range must be list of integers {}".format(framerange))
            return
        self.frameRange = [int(framerange[0]), int(framerange[1])]
        self.startFrame = int(framerange[0])
        self.endFrame = int(framerange[1])
        self.duration = (self.endFrame - self.startFrame) + 1
        self.view.scene.slider.setFrameRange(self.frameRange)


class FrameField(QtWidgets.QLineEdit):
    """Creating FrameField class by inheriting QLineEdit"""
    def __init__(self, parent=None, frameNumber=1):
        """Initializing FrameField class.
        Args:
            parent (QtWidgets.QWidget): Parent widget of this class.
            frameNumber (str): Frame number in string format.
        """
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
