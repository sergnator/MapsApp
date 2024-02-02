import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image = QLabel()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapWindow()
    ex.show()
    sys.exit(app.exec_())