import sys
from StreamControl import StreamControl
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = StreamControl()
    player.show()
    sys.exit(app.exec_())
