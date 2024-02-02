import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit
from PyQt5.QtGui import QPixmap, QImage
from MapsAPI import create_map_image
from Constants import *


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image = QLabel(self)
        self.setup()

    def setup(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.params = {"ll": ",".join(['0', '0']),
                       "spn": ",".join(['40', '40']),
                       "l": "map"}

        self.image.setText('123')

        self.image.setGeometry(0, 0, *SCREEN_SIZE)
        # создание изображение
        im = create_map_image(self.params)
        print(im.size)
        data = im.tobytes("raw", 'RGB')
        qim = QImage(data, im.size[0], im.size[1], QImage.Format_RGB888)

        qpixmap = QPixmap.fromImage(qim)

        self.image.setPixmap(qpixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapWindow()
    ex.show()
    sys.exit(app.exec())
