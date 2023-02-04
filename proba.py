import sys
import requests

from PyQt5 import uic, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PIL import Image
from io import BytesIO


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui_design.ui', self)
        self.left.clicked.connect(self.run_left)
        self.right.clicked.connect(self.run_right)
        self.up.clicked.connect(self.run_up)
        self.down.clicked.connect(self.run_down)
        self.pgdown.clicked.connect(self.Pg_Down)
        self.pgup.clicked.connect(self.Pg_Up)
        self.enter_2.clicked.connect(self.enter)
        self.break_2.clicked.connect(self.sbros)
        self.pixmap = QPixmap()

    def run_left(self):
        pass

    def run_right(self):
        pass

    def run_up(self):
        pass

    def run_down(self):
        pass

    def Pg_Up(self):
        pass

    def Pg_Down(self):
        pass

    def sbros(self):
        pass

    def enter(self):
        s = self.lineEdit.text().split()
        y = s[0].strip()
        x = s[1].strip()
        api_server = "http://static-maps.yandex.ru/1.x/"

        delta = "2"

        params = {
            "ll": ",".join([x, y]),
            "spn": ",".join([delta, delta]),
            "l": "map"
        }
        response = requests.get(api_server, params=params)
        image = Image.open(BytesIO(response.content))
        image.save('xxx.png')
        pixmap = QtGui.QPixmap('xxx.png')
        self.window.setPixmap(pixmap)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
