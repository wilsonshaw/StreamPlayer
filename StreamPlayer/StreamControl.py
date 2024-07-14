import time
import socket
import keyboard
import struct
from vlc import MediaPlayer
from .GuiCore import Ui_StreamPlayer
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QThread, Slot, Signal


class KeyboardThread(QThread):
    finish_signal = Signal(bool, str)

    def __init__(self, parent=None):
        super(KeyboardThread, self).__init__(parent)
        self.url = None
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        self.isTcpConnected = False
        self.error_time = 0
        self.isRun = False

    def run(self):
        self.isRun = True
        while self.isRun:
            if not self.isTcpConnected:
                try:
                    self.tcp_client.connect(self.url)
                    self.finish_signal.emit(True, 'Success!')
                    self.isTcpConnected = True
                except socket.error:
                    self.tcp_client.close()
                    self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
                    self.finish_signal.emit(True, 'Trying to Reconnect ... ' + str(self.error_time))
                    self.error_time += 1
                    if self.error_time >= 7:
                        self.finish_signal.emit(True, 'Disconnect')
                        self.finish_signal.emit(False, ' ')
            else:
                try:
                    key_tail = 0x0000807F
                    key_mask = 0x00000000
                    if keyboard.is_pressed('w') or keyboard.is_pressed('W'):
                        key_mask |= 0x80000000 >> 0
                    self.tcp_client.sendall(struct.pack('!I I', key_mask, key_tail))
                except socket.error:
                    self.error_time = 0
                    self.isTcpConnected = False
        self.error_time = 0

    def stop_thread(self):
        self.isRun = False
        self.isTcpConnected = False
        self.tcp_client.close()
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)


class StreamControl(QMainWindow, Ui_StreamPlayer):
    def __init__(self, parent=None):
        super(StreamControl, self).__init__(parent)
        self.setupUi(self)

        self.keyboard_thread = KeyboardThread(self)
        self.keyboard_thread.finish_signal['bool', 'QString'].connect(self.on_keyboard_thread_finish_signal)

        self.player = MediaPlayer()
        self.player.set_hwnd(self.frameVideo.winId())

    @Slot()
    def on_pushButtonPlay_clicked(self):
        self.player.set_mrl(self.lineEditRtspUrl.text(),'--network-catching=0')
        self.player.play()
        self.statusbar.showMessage('Play...', 3000)
        for x in range(0, 50):
            time.sleep(1)
            if self.player.is_playing() == 1:
                self.statusbar.showMessage('Play Success!', 3000)
                self.pushButtonPlay.setDisabled(True)
                self.lineEditRtspUrl.setDisabled(True)
                self.pushButtonStop.setEnabled(True)
                return
        self.statusbar.showMessage('Play Failed!', 3000)

    @Slot()
    def on_pushButtonStop_clicked(self):
        self.player.pause()
        self.pushButtonPlay.setEnabled(True)
        self.lineEditRtspUrl.setEnabled(True)
        self.pushButtonStop.setDisabled(True)
        self.statusbar.showMessage('Play Stop', 3000)

    @Slot()
    def on_pushButtonConnect_clicked(self):
        self.pushButtonConnect.setDisabled(True)
        ip, port = str(self.lineEditIP.text()), str(self.lineEditPort.text())
        self.statusbar.showMessage('Connect to ' + ip + ':' + port)
        self.keyboard_thread.url = (ip,int(port))
        self.keyboard_thread.start()

    @Slot()
    def on_pushButtonDisconnect_clicked(self):
        self.pushButtonConnect.setEnabled(True)
        self.pushButtonDisconnect.setDisabled(True)
        self.statusbar.showMessage('Disconnected')
        self.keyboard_thread.stop_thread()

    @Slot(bool, str)
    def on_keyboard_thread_finish_signal(self, msg_flag, msg):
        if msg_flag:
            self.statusbar.showMessage(msg, 3000)
            self.pushButtonConnect.setDisabled(True)
            self.pushButtonDisconnect.setEnabled(True)
        else:
            self.keyboard_thread.stop_thread()
            self.pushButtonConnect.setEnabled(True)
            self.pushButtonDisconnect.setDisabled(True)
