"""Creating a playbar widget"""
from PyQt5 import QtCore, QtGui, QtWidgets

from classes import variables, scene


class PlayBar(QtWidgets.QWidget):
    """Creating PlayBar widget by inheriting QWidget"""
    def __init__(self, parent=None, framerange=None, timelineScene=None):
        """initializing PlayBar class
        Args:
            parent (QtWidgets.QWidget): Parent widget of this class.
            framerange (list): List containing start and end frames integers.
            timelineScene (scene.Scene): Time line scene.
        """
        super(PlayBar, self).__init__(parent=parent)
        self.scene = timelineScene
        self.frameRange = framerange
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
        # adding buttons to layout
        self.layout.addWidget(self.playButton)
        self.layout.addWidget(self.pauseButton)
        self.layout.addWidget(self.stopButton)
        self.layout.addWidget(self.backwardButton)
        self.layout.addWidget(self.forwardButton)
        self.layout.addWidget(self.prevButton)
        self.layout.addWidget(self.nextButton)

        # connecting widgets to their functions

    def connect_(self):
        pass


class PlayBarButton(QtWidgets.QPushButton):
    """Creating PlayBarButton by inheriting QPushButton"""
    def __init__(self, parent=None, type_=None):
        """Initializing PlayBarButton class.
        Args:
            parent (QtWidgets.QWidget): Parent widget of this class.
            type_ (str): Type of the button.
        """
        super(PlayBarButton, self).__init__(parent=parent)
        self.type_ = type_
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.setFixedHeight(30)
        self.setFixedWidth(30)
        self.playIcon = QtGui.QIcon(variables.PLAY_ICON)
        self.pauseIcon = QtGui.QIcon(variables.PAUSE_ICON)
        self.stopIcon = QtGui.QIcon(variables.STOP_ICON)
        self.backwardIcon = QtGui.QIcon(variables.BACKWARD_ICON)
        self.forwardIcon = QtGui.QIcon(variables.FORWARD_ICON)
        self.prevKeyIcon = QtGui.QIcon(variables.PREV_KEY_ICON)
        self.nextKeyIcon = QtGui.QIcon(variables.NEXT_KEY_ICON)
        self.setIconSize(QtCore.QSize(30, 30))
        self.set_icon()
        self.setStyleSheet("""
                            PlayBarButton{  
                                            color: white;
                                            border: 1px solid grey;
                                            border-radius: 10px;
                                            background: transparent;
                                         }
                            PlayBarButton:hover{
                                                border: 1px solid black;
                                                }
                            PlayBarButton:pressed{
                                                    background: silver;
                                                    border: 1px silver;   
                                                 }
                                                 
        """)

    def set_icon(self):
        """This method sets icon of this widget by defined type.
        Returns:
            (None): Returns None.
        """
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
