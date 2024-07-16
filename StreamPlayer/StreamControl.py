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
                    key_head = 0xFFFF
                    key_tail = 0x807F
                    key_mask = 0x00000000
                    if keyboard.is_pressed('w') or keyboard.is_pressed('W'):
                        key_mask |= 0x80000000 >> 0
                    if keyboard.is_pressed('s') or keyboard.is_pressed('S'):
                        key_mask |= 0x80000000 >> 1
                    if keyboard.is_pressed('a') or keyboard.is_pressed('A'):
                        key_mask |= 0x80000000 >> 2
                    if keyboard.is_pressed('d') or keyboard.is_pressed('D'):
                        key_mask |= 0x80000000 >> 3
                    if keyboard.is_pressed('q') or keyboard.is_pressed('Q'):
                        key_mask |= 0x80000000 >> 4
                    if keyboard.is_pressed('e') or keyboard.is_pressed('E'):
                        key_mask |= 0x80000000 >> 5
                    if keyboard.is_pressed('z') or keyboard.is_pressed('Z'):
                        key_mask |= 0x80000000 >> 6
                    if keyboard.is_pressed('c') or keyboard.is_pressed('C'):
                        key_mask |= 0x80000000 >> 7
                    if keyboard.is_pressed('x') or keyboard.is_pressed('X'):
                        key_mask |= 0x80000000 >> 8
                    if keyboard.is_pressed('s') or keyboard.is_pressed('S'):
                        key_mask |= 0x80000000 >> 9
                    if keyboard.is_pressed('i') or keyboard.is_pressed('I'):
                        key_mask |= 0x80000000 >> 10
                    if keyboard.is_pressed('m') or keyboard.is_pressed('M'):
                        key_mask |= 0x80000000 >> 11
                    if keyboard.is_pressed('y') or keyboard.is_pressed('Y'):
                        key_mask |= 0x80000000 >> 12
                    if keyboard.is_pressed('h') or keyboard.is_pressed('H'):
                        key_mask |= 0x80000000 >> 13
                    if keyboard.is_pressed('u') or keyboard.is_pressed('U'):
                        key_mask |= 0x80000000 >> 14
                    if keyboard.is_pressed('o') or keyboard.is_pressed('O'):
                        key_mask |= 0x80000000 >> 15
                    if keyboard.is_pressed('p') or keyboard.is_pressed('P'):
                        key_mask |= 0x80000000 >> 16
                    if keyboard.is_pressed('l') or keyboard.is_pressed('L'):
                        key_mask |= 0x80000000 >> 17
                    if keyboard.is_pressed('g') or keyboard.is_pressed('G'):
                        key_mask |= 0x80000000 >> 18
                    if keyboard.is_pressed('b') or keyboard.is_pressed('B'):
                        key_mask |= 0x80000000 >> 19
                    if keyboard.is_pressed('r') or keyboard.is_pressed('R'):
                        key_mask |= 0x80000000 >> 20
                    self.tcp_client.sendall(struct.pack('!H I H', key_head, key_mask, key_tail))
                    time.sleep(0.01)
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

        self.player = MediaPlayer('--network-caching=0')
        self.player.set_hwnd(self.frameVideo.winId())

    @Slot()
    def on_pushButtonPlay_clicked(self):
        self.player.set_mrl(self.lineEditRtspUrl.text())
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
