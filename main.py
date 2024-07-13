import sys
from GUI.RtspStreamPlayer import RtspStreamPlayer
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = RtspStreamPlayer()
    main_window.show()
    sys.exit(app.exec_())
