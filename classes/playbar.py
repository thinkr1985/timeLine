"""Creating a playbar widget"""
from PyQt5 import QtCore, QtGui, QtWidgets

from classes import variables


class PlayBar(QtWidgets.QWidget):
    def __init__(self, parent=None, timeslider=None):
        super(PlayBar, self).__init__(parent=parent)
        self.timeSlider = timeslider
        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        # creating buttons
        self.playButton = PlayBarButton(type_="play")
        self.pauseButton = PlayBarButton(type_="pause")
        self.stopButton = PlayBarButton(type_="stop")
        self.backwardButton = PlayBarButton(type_="backward")
        self.forwardButton = PlayBarButton(type_="forward")
        self.prevButton = PlayBarButton(type_="previous")
        self.nextButton = PlayBarButton(type_="next")
        self.layout.addWidget(self.playButton)
        self.layout.addWidget(self.pauseButton)
        self.layout.addWidget(self.stopButton)
        self.layout.addWidget(self.backwardButton)
        self.layout.addWidget(self.forwardButton)
        self.layout.addWidget(self.prevButton)
        self.layout.addWidget(self.nextButton)


class PlayBarButton(QtWidgets.QPushButton):
    def __init__(self, parent=None, type_=None):
        super(PlayBarButton, self).__init__(parent=parent)
        self.type_ = type_
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.setFixedHeight(35)
        self.setFixedWidth(35)
        self.playIcon = QtGui.QIcon(variables.PLAY_ICON)
        self.pauseIcon = QtGui.QIcon(variables.PAUSE_ICON)
        self.stopIcon = QtGui.QIcon(variables.STOP_ICON)
        self.backwardIcon = QtGui.QIcon(variables.BACKWARD_ICON)
        self.forwardIcon = QtGui.QIcon(variables.FORWARD_ICON)
        self.prevKeyIcon = QtGui.QIcon(variables.PREV_KEY_ICON)
        self.nextKeyIcon = QtGui.QIcon(variables.NEXT_KEY_ICON)
        self.setIconSize(QtCore.QSize(35, 35))
        self.set_icon()
        self.setStyleSheet("""
                            PlayBarButton{  
                                            color: white;
                                            border-width: 1px;
                                            border-radius: 10px;
                                            background: transparent;
                                            padding: 4px;
                                         }
                            PlayBarButton:hover{
                                                border-color: black;
                                                border-style: inset;
                                                }
                            PlayBarButton:pressed{
                                                    background: silver;   
                                                 }
                                                 
        """)

    def set_icon(self):
        if self.type_ == "play":
            self.setIcon(self.playIcon)
            self.setToolTip("Play")
        if self.type_ == "pause":
            self.setIcon(self.pauseIcon)
            self.setToolTip("Pause")
        if self.type_ == "stop":
            self.setIcon(self.stopIcon)
            self.setToolTip("Stop")
        if self.type_ == "backward":
            self.setIcon(self.backwardIcon)
            self.setToolTip("Start Frame")
        if self.type_ == "forward":
            self.setIcon(self.forwardIcon)
            self.setToolTip("End Frame")
        if self.type_ == "previous":
            self.setIcon(self.prevKeyIcon)
            self.setToolTip("Previous Key Frame")
        if self.type_ == "next":
            self.setIcon(self.nextKeyIcon)
            self.setToolTip("Next Key Frame")
