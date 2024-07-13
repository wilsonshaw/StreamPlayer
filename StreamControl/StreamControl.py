from  Input import KeyBoardInputThread
from vlc import Instance
from GUI.GuiCore import Ui_PlayerMainWindow
from PyQt5.QtWidgets import QMainWindow


class StreamControl(QMainWindow, Ui_PlayerMainWindow):
    def __init__(self, parent=None):
        super(StreamControl, self).__init__(parent)
        super(StreamControl, self).__init__()
        self.setupUi(self)
        self.vlc_instance = Instance()

        self.tcp_client = None
        self.player = self.vlc_instance.media_player_new()
        self.player.set_hwnd(self.videoFrame.winId())

        self.pushButtonControlStream.clicked.connect(self.slot_push_button_control_stream)
        self.pushButtonConnect.clicked.connect(self.slot_push_button_connect)
        self.pushButtonConnect_2.clicked.connect(self.slot_push_button_connect_2)

        self.keyboard_thread = None

    def slot_push_button_control_stream(self):
        if self.pushButtonControlStream.text() == 'Play':
            self.pushButtonControlStream.setText('Stop')
            self.lineEditRtspAddress.setDisabled(True)
            self.player.set_media(self.vlc_instance.media_new(self.lineEditRtspAddress.text()))
            self.player.play()
        else:
            self.pushButtonControlStream.setText('Play')
            self.lineEditRtspAddress.setEnabled(True)
            self.player.set_pause(1)

    def slot_push_button_connect(self):
        pass

    def slot_push_button_connect_2(self):
        if self.pushButtonConnect_2.text() == 'Connect':
            port = int(self.lineEditIPPort_2.text())
            addr = self.lineEditIPAddr_2.text()
            self.pushButtonConnect_2.setText('Disconnect')
            self.pushButtonConnect_2.setDisabled(True)
            self.keyboard_thread = KeyBoardInputThread(addr, port,self.pushButtonConnect_2)
            self.keyboard_thread.start()
        else:
            self.keyboard_thread.Stop()
            self.keyboard_thread = None
            self.pushButtonConnect_2.setText('Connect')