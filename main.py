import sys
from StreamPlayer.StreamControl import StreamControl
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = StreamControl()
    player.show()
    sys.exit(app.exec())
