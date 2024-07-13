from typing import Union, Type

import keyboard
from struct import pack
from socket import socket, AF_INET, SOCK_STREAM, IPPROTO_TCP, error
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QPushButton


class KeyBoardInputThread(QThread):

    def __init__(self, addr:str, port:int, push_button:QPushButton, parent=None):
        super(KeyBoardInputThread, self).__init__(parent)
        self.addr = addr
        self.port = port
        self.tcp_client = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
        self.pushButtonConnect_2 = push_button

    def run(self):
        try:
            self.tcp_client.connect((self.addr, self.port))
        except error:
            print("error")
            self.pushButtonConnect_2.setEnabled(True)
            self.pushButtonConnect_2.setText('Connect')
        else:
            while True:
                key_body = 0x00000000
                if keyboard.is_pressed('K') or keyboard.is_pressed('k'):
                    print('Key-K is pressed')
                    key_body |= 0x10000000
                try:
                    self.tcp_client.sendall(pack('!I I', key_body, 0x0000807F))
                except error:
                    print("send error! reconnect...")
                    while True:
                        try:
                            self.tcp_client = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
                            self.tcp_client.connect((self.addr, self.port))
                        except error:
                            print('connect error')

    def Stop(self):
        self.tcp_client.close()
        self.terminate()
