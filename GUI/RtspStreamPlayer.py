import socket
from .GuiCore import *
from vlc import Instance
from PyQt5.QtWidgets import QMainWindow, QFrame, QLineEdit, QPushButton
from PyQt5.uic import loadUi


class RtspStreamPlayer(QMainWindow):
    def __init__(self):
        super(RtspStreamPlayer,self).__init__()

        gui = Ui_PlayerMainWindow()
        gui.setupUi(self)

        self.tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)

        self.video_frame = self.findChild(QFrame, 'videoFrame')
        self.line_edit_rtsp_addr = self.findChild(QLineEdit, 'lineEditRtspAddress')
        self.push_button_control_stream = self.findChild(QPushButton, 'pushButtonControlStream')

        self.line_edit_ip_addr = self.findChild(QLineEdit,'lineEditIPAddr')
        self.line_edit_ip_port = self.findChild(QLineEdit,'lineEditIPPort')
        self.push_button_connect = self.findChild(QPushButton,'pushButtonConnect')

        self.push_button_control_stream.clicked.connect(self.control_stream)
        self.push_button_connect.clicked.connect(self.connect_socket)

        self.vlc_instance = Instance()
        self.player = self.vlc_instance.media_player_new()
        self.player.set_hwnd(self.video_frame.winId())

    def control_stream(self):
        self.player.set_media(self.vlc_instance.media_new(self.line_edit_rtsp_addr.text()))
        self.player.play()

    def connect_socket(self):
        try:
            self.tcp_client.connect(('192.168.249.208',8000))
        except socket.error as error:
            print('Error')