# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QFrame, QApplication, QMessageBox)
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication)

class SettingWidget(QWidget):


    __nextKeyLabel = None
    __nextKeyDelayLabel = None
    __saveToLabel = None
    __pagesNumLabel = None

    __nextKeyLineText = None
    __nextKeyDelayText = None
    __saveToLineText = None
    __pagesNumLineText = None

    __grid = None

    def __init__(self):
        super().__init__()

        self.__initUI()


    def __initUI(self):

        self.__nextKeyLabel = QLabel('nextKey')
        self.__nextKeyDelayLabel = QLabel('nextKeyDelay (ms)')
        self.__saveToLabel = QLabel('saveTo')
        self.__pagesNumLabel = QLabel('pagesNum')

        self.__nextKeyLineText = QLineEdit()
        self.__nextKeyDelayText = QLineEdit()
        self.__saveToLineText = QLineEdit()
        self.__pagesNumLineText = QLineEdit()

        '''
        lineEditW = 120
        self.__nextKeyLineText.setFixedWidth(lineEditW)
        self.__nextKeyDelayText.setFixedWidth(lineEditW)
        self.__saveToLineText.setFixedWidth(lineEditW)
        self.__pagesNumLineText.setFixedWidth(lineEditW)
        '''

        self.__grid = QGridLayout()
        self.__grid.setSpacing(10)

        self.__grid.addWidget(self.__nextKeyLabel, 0, 0)
        self.__grid.addWidget(self.__nextKeyDelayLabel, 1, 0)
        self.__grid.addWidget(self.__saveToLabel, 2, 0)
        self.__grid.addWidget(self.__pagesNumLabel, 3, 0)

        self.__grid.addWidget(self.__nextKeyLineText, 0, 1)
        self.__grid.addWidget(self.__nextKeyDelayText, 1, 1)
        self.__grid.addWidget(self.__saveToLineText, 2, 1)
        self.__grid.addWidget(self.__pagesNumLineText, 3, 1)
        
        self.setLayout(self.__grid)
        #self.show()

    def getAllFields(self) -> tuple:
        '''
        0 - savePath
        1 - key
        2 - keyDelay in ms
        3 - pagesNum
        '''
        saveToPath = self.__saveToLineText.text()

        nextKey = self.__nextKeyLineText.text()
        nextKeyDelay = self.__nextKeyDelayText.text()
        if(nextKeyDelay.isdigit()):
            nextKeyDelay = int(nextKeyDelay)
        else:
            self.__ifError("nextKeyDelay must be number")
            return


        pagesNum = self.__pagesNumLineText.text()
        if(pagesNum.isdigit()):
            pagesNum = int(pagesNum)
        else:
            self.__ifError("pagesNum must be number")
            return


        if(saveToPath == "" or nextKey == ""):
            self.__ifError("Not all field is filled. ")
            return
        if(nextKeyDelay <= 0 or pagesNum <= 0 ):
            self.__ifError("nextKeyDelay and pagesNum must be positive. ")
            return

        return (saveToPath, nextKey, nextKeyDelay, pagesNum)


    def __ifError(self, text : str):
        #https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text + "\nCheck README.md: https://github.com/The220th/grabook")
        msg.setWindowTitle("Syntax error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setModal(True)
        msg.exec()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = SettingWidget()
    sys.exit(app.exec_())

    for i in range(10):
        print(i)