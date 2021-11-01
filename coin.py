import sys, PyQt5, pykorbit
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType("MainWindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer = QTimer(self)
        self.timer.start(1000)  # interval 1s
        self.timer.timeout.connect(self.inquery)

    def inquery(self):
        current_time = QTime.currentTime()
        str_time = current_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
        price = pykorbit.get_current_price("BTC")
        self.btc_price.setText(str(price))

app = QApplication(sys.argv)
window = MyWindow()
window.show()

app.exec_()