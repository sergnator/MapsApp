import sys
import traceback

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

from MapsAPI import create_map_image
from Constants import *


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image = QLabel(self)
        self.x = '178'
        self.y = '0'
        self.delta = '40'
        self.params = {"ll": ",".join([self.y, self.x]),
                       "spn": ",".join([self.delta, self.delta]),
                       "l": "map"}
        self.setup()

    def setup(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)

        self.image.setGeometry(0, 0, *SCREEN_SIZE)
        self.setImage()

    def setImage(self):
        self.params = {"ll": ",".join([self.x, self.y]),
                       "spn": ",".join([self.delta, self.delta]),
                       "l": "map"}
        # создание изображение
        im = create_map_image(self.params)

        data = im.tobytes("raw", 'RGB')
        qim = QImage(data, im.size[0], im.size[1], QImage.Format_RGB888)

        qpixmap = QPixmap.fromImage(qim)

        self.image.setPixmap(qpixmap)

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Left:
            self.x = str((float(self.x) - 0.1 * int(self.delta)))
        elif event.key() == Qt.Key_Right:
            self.x = str((float(self.x) + 0.1 * int(self.delta)))
        elif event.key() == Qt.Key_Down:
            self.y = str((float(self.y) - 0.1 * int(self.delta)))
        elif event.key() == Qt.Key_Up:
            self.y = str((float(self.y) + 0.1 * int(self.delta)))
        if float(self.x) >= 180.0:
            self.x = '-179'
            return
        elif float(self.x) <= -178.0:
            self.x = '179'
            return
        if float(self.y) >= 85.0:
            self.y = '-84'
            return
        elif float(self.y) <= -85.0:
            self.y = '84'
            return
        self.setImage()


def except_hook(exc_type, exc_value, exc_tb):

    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print(tb)




sys.excepthook = except_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapWindow()
    ex.show()
    sys.exit(app.exec())
