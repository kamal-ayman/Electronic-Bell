import os, sys, urllib.request
from PyQt5.QtWidgets import *
from time import sleep
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from PyQt5.QtGui import *

ui, _ = loadUiType('QtUi\Themes\\themes.ui')


class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.button()

    def button(self):
        self.pushButton.clicked.connect(self.Apply_Light_Style)
        self.pushButton_2.clicked.connect(self.Apply_Dark_Style)

    def Apply_Light_Style(self):
        u = open('QtUi/Themes/Light.ui', 'r')
        m = open('QtUi/main.ui', 'w')
        m.write(u.read())
        QMessageBox.information(self, 'Done!!', 'Done Make Light Mode Please Restart App')
        exit()

    def Apply_Dark_Style(self):
        u = open('QtUi/Themes/Dark.ui', 'r')
        m = open('QtUi/main.ui', 'w')
        m.write(u.read())
        QMessageBox.information(self, 'Done!!', 'Done Make Dark Mode Please Restart App')
        exit()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
