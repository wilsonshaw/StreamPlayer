# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_core.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_StreamPlayer(object):
    def setupUi(self, StreamPlayer):
        if not StreamPlayer.objectName():
            StreamPlayer.setObjectName(u"StreamPlayer")
        StreamPlayer.resize(1280, 841)
        StreamPlayer.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        StreamPlayer.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.actionTCP_Connect = QAction(StreamPlayer)
        self.actionTCP_Connect.setObjectName(u"actionTCP_Connect")
        self.centralwidget = QWidget(StreamPlayer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBoxStreamPlayer = QGroupBox(self.centralwidget)
        self.groupBoxStreamPlayer.setObjectName(u"groupBoxStreamPlayer")
        self.groupBoxStreamPlayer.setGeometry(QRect(0, 0, 1280, 771))
        self.frameVideo = QFrame(self.groupBoxStreamPlayer)
        self.frameVideo.setObjectName(u"frameVideo")
        self.frameVideo.setGeometry(QRect(0, 50, 1280, 720))
        self.frameVideo.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frameVideo.setFrameShape(QFrame.Shape.NoFrame)
        self.frameVideo.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEditRtspUrl = QLineEdit(self.groupBoxStreamPlayer)
        self.lineEditRtspUrl.setObjectName(u"lineEditRtspUrl")
        self.lineEditRtspUrl.setGeometry(QRect(190, 20, 1081, 20))
        self.pushButtonPlay = QPushButton(self.groupBoxStreamPlayer)
        self.pushButtonPlay.setObjectName(u"pushButtonPlay")
        self.pushButtonPlay.setEnabled(True)
        self.pushButtonPlay.setGeometry(QRect(10, 20, 75, 20))
        self.pushButtonPlay.setStyleSheet(u"background-color: rgb(227, 227, 227);")
        self.pushButtonStop = QPushButton(self.groupBoxStreamPlayer)
        self.pushButtonStop.setObjectName(u"pushButtonStop")
        self.pushButtonStop.setEnabled(False)
        self.pushButtonStop.setGeometry(QRect(100, 20, 75, 20))
        self.pushButtonStop.setStyleSheet(u"background-color: rgb(227, 227, 227);")
        self.groupBoxTCP = QGroupBox(self.centralwidget)
        self.groupBoxTCP.setObjectName(u"groupBoxTCP")
        self.groupBoxTCP.setGeometry(QRect(0, 770, 1280, 51))
        self.lineEditIP = QLineEdit(self.groupBoxTCP)
        self.lineEditIP.setObjectName(u"lineEditIP")
        self.lineEditIP.setGeometry(QRect(630, 20, 480, 20))
        self.lineEditPort = QLineEdit(self.groupBoxTCP)
        self.lineEditPort.setObjectName(u"lineEditPort")
        self.lineEditPort.setGeometry(QRect(1150, 20, 120, 20))
        self.labelIP = QLabel(self.groupBoxTCP)
        self.labelIP.setObjectName(u"labelIP")
        self.labelIP.setGeometry(QRect(610, 20, 20, 20))
        self.labePort = QLabel(self.groupBoxTCP)
        self.labePort.setObjectName(u"labePort")
        self.labePort.setGeometry(QRect(1120, 20, 30, 20))
        self.pushButtonConnect = QPushButton(self.groupBoxTCP)
        self.pushButtonConnect.setObjectName(u"pushButtonConnect")
        self.pushButtonConnect.setEnabled(True)
        self.pushButtonConnect.setGeometry(QRect(10, 20, 75, 20))
        self.pushButtonConnect.setStyleSheet(u"background-color: rgb(227, 227, 227);")
        self.pushButtonDisconnect = QPushButton(self.groupBoxTCP)
        self.pushButtonDisconnect.setObjectName(u"pushButtonDisconnect")
        self.pushButtonDisconnect.setEnabled(False)
        self.pushButtonDisconnect.setGeometry(QRect(100, 20, 75, 20))
        self.pushButtonDisconnect.setStyleSheet(u"background-color: rgb(227, 227, 227);")
        StreamPlayer.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(StreamPlayer)
        self.statusbar.setObjectName(u"statusbar")
        StreamPlayer.setStatusBar(self.statusbar)

        self.retranslateUi(StreamPlayer)

        QMetaObject.connectSlotsByName(StreamPlayer)
    # setupUi

    def retranslateUi(self, StreamPlayer):
        StreamPlayer.setWindowTitle(QCoreApplication.translate("StreamPlayer", u"StreamPlayer", None))
        self.actionTCP_Connect.setText(QCoreApplication.translate("StreamPlayer", u"TCP Connect", None))
        self.groupBoxStreamPlayer.setTitle(QCoreApplication.translate("StreamPlayer", u"StreamPlayer", None))
        self.pushButtonPlay.setText(QCoreApplication.translate("StreamPlayer", u"Play", None))
        self.pushButtonStop.setText(QCoreApplication.translate("StreamPlayer", u"Stop", None))
        self.groupBoxTCP.setTitle(QCoreApplication.translate("StreamPlayer", u"TCP", None))
        self.lineEditIP.setText(QCoreApplication.translate("StreamPlayer", u"localhost", None))
        self.lineEditPort.setText(QCoreApplication.translate("StreamPlayer", u"8000", None))
        self.labelIP.setText(QCoreApplication.translate("StreamPlayer", u"IP:", None))
        self.labePort.setText(QCoreApplication.translate("StreamPlayer", u"Port:", None))
        self.pushButtonConnect.setText(QCoreApplication.translate("StreamPlayer", u"Connect", None))
        self.pushButtonDisconnect.setText(QCoreApplication.translate("StreamPlayer", u"Disconnect", None))
    # retranslateUi

