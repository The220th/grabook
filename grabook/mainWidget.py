# -*- coding: utf-8 -*-

# pip3 install PyQt5
# pip3 install pyautogui
# sudo apt install python3-tk python3-dev
# sudo pacman -S tk

from . import SettingWidget
from . import GrabWidget 

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QFrame, QApplication)
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication)



class MainWidget(QWidget):

    __grabWidget = None
    __settingsWidget = None

    __startButton = None

    __grid = None

    def __init__(self):
        super().__init__()

        self.__initUI()


    def __initUI(self):

        self.__startButton = QPushButton("Start")
        self.__grabWidget = GrabWidget()
        self.__settingsWidget = SettingWidget()

        self.__grid = QGridLayout()
        self.__grid.setSpacing(10)

        self.__grid.addWidget(self.__grabWidget, 0, 0, 2, 1)
        self.__grid.addWidget(self.__settingsWidget, 0, 1, 2, 1)
        self.__grid.addWidget(self.__startButton, 2, 0, 1, 2)

        self.setLayout(self.__grid)

        self.__startButton.clicked.connect(lambda:self.__startButton_handler(self.__startButton))

        self.show()

    def __startButton_handler(self, b):
        # https://datatofish.com/images-to-pdf-python/
        viser = self.__grabWidget.getAllFields()
        if(viser == None):
            return
        x_LU, y_LU, x_RD, y_RD = viser

        viser = self.__settingsWidget.getAllFields()
        if(viser == None):
            return
        savePath, key, keyDelay, pagesNum = viser

        from . import StartGrub
        StartGrub(x_LU, y_LU, x_RD, y_RD, savePath, key, keyDelay, pagesNum)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())