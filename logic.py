from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_Project2):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.volume = 0
        self.channel_index = 0
        self.__status = False
        self.__muted = False

        self.channel0.hide()
        self.channel1.hide()
        self.channel2.hide()
        self.channel3.hide()
        self.buttonPower.clicked.connect(lambda: self.power())
        self.buttonMute.clicked.connect(lambda: self.mute())
        self.buttonChannelUp.clicked.connect(lambda: self.channel_up())
        self.buttonChannelDown.clicked.connect(lambda: self.channel_down())
        self.buttonVolumeUp.clicked.connect(lambda: self.volume_up())
        self.buttonVolumeDown.clicked.connect(lambda: self.volume_down())

    def power(self):
        if self.__status:
            self.__status = False
            self.channelOff.show()
            for i in range(4):
                getattr(self, f'channel{i}').hide()
        else:
            self.__status = True
            self.channelOff.hide()
            getattr(self, f'channel{self.channel_index}').show()

    def mute(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.labelVolumeNumber.setText(str(self.volume))
            else:
                self.__muted = True
                self.labelVolumeNumber.setText('0')

    def channel_up(self):
        if self.__status:
            self.channel_index = (self.channel_index + 1) % 4
            self.update_channel()

    def channel_down(self):
        if self.__status:
            self.channel_index = (self.channel_index - 1) % 4
            self.update_channel()

    def update_channel(self):
        for i in range(4):
            getattr(self, f'channel{i}').setVisible(i == self.channel_index)

    def volume_up(self):
        if self.__status:
            if not self.__muted and self.volume < 2:
                self.volume += 1
                self.labelVolumeNumber.setText(str(self.volume))

    def volume_down(self):
        if self.__status:
            if not self.__muted and self.volume > 0:
                self.volume -= 1
                self.labelVolumeNumber.setText(str(self.volume))
