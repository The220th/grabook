# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QFrame, QApplication, QMessageBox)
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication)

import threading
import time
import pyautogui

class GrabWidget(QWidget):

    __setButtonLU = None
    __setButtonRD = None

    __coordLabelLU = None
    __coordLabelRD = None

    __delayLabel = None
    __delayTextLine = None

    __counterLabel = None

    __grid = None

    #__th = None
    #__th_stop = False

    __buttonLU_pressed = False
    __buttonRD_pressed = False

    __updateInterval = None
    __count_LU = None
    __count_RD = None

    __x_LU = None
    __y_LU = None
    __x_RD = None
    __y_RD = None

    def __init__(self):
        super().__init__()

        self.__initUI()

        #self.setMouseTracking(True)

        #self.__th = threading.Thread(target=self.lupdate)
        #self.__th.start()
        self.__updateInterval = 100
        self.__count_LU = -1
        self.__count_RD = -1
        self.startTimer(self.__updateInterval)


    def __initUI(self):

        self.__setButtonLU = QPushButton("set LU coord")
        self.__setButtonRD = QPushButton("set RD coord")

        self.__coordLabelLU = QLabel("")
        self.__coordLabelRD = QLabel("")
        self.__counterLabel = QLabel("")

        labelEditW = 200
        self.__coordLabelLU.setFixedWidth(labelEditW)
        self.__coordLabelRD.setFixedWidth(labelEditW)
        self.__counterLabel.setFixedWidth(labelEditW)

        self.__delayLabel = QLabel("Set delay: ")
        self.__delayTextLine = QLineEdit("")
        self.__delayTextLine.textChanged[str].connect(self.__setDelay)
        self.__delayTextLine.setText("5")

        self.__grid = QGridLayout()
        self.__grid.setSpacing(10)

        self.__grid.addWidget(self.__setButtonLU, 0, 0)
        self.__grid.addWidget(self.__setButtonRD, 1, 1)
        self.__grid.addWidget(self.__coordLabelLU, 0, 1)
        self.__grid.addWidget(self.__coordLabelRD, 1, 0)
        self.__grid.addWidget(self.__counterLabel, 2, 1)
        buffWidget = QWidget()
        buffGrid = QGridLayout()
        buffGrid.addWidget(self.__delayLabel, 0, 0)
        buffGrid.addWidget(self.__delayTextLine, 1, 0)
        buffWidget.setLayout(buffGrid)
        self.__grid.addWidget(buffWidget, 2, 0)

        self.setLayout(self.__grid)

        self.__setButtonLU.clicked.connect(lambda:self.__buttonHundler(self.__setButtonLU))
        self.__setButtonRD.clicked.connect(lambda:self.__buttonHundler(self.__setButtonRD))

        #self.show()

    def getAllFields(self) -> tuple:
        '''
        0 - x LU
        1 - y LU
        2 - x RD
        3 - y RD
        '''
        if(self.__x_LU == None or self.__y_LU == None or self.__x_RD == None or self.__y_RD == None):
            self.__ifError("Not all field is filled. Press \"set LU coord\" and \"set RD coord\"")
            return
        if((self.__x_LU >= self.__x_RD) or (self.__y_LU >= self.__y_RD)):
            self.__ifError("The LU should be higher and to the left than the RD. ")
            return
        res = (self.__x_LU, self.__y_LU, self.__x_RD, self.__y_RD)
        return res

    #def lupdate(self):
    #    li = 0
    #    while(True):
    #        #p = self.pos()
    #        p = pyautogui.position()
    #        li+=1
    #        
    #        #self.__coordLabelLU.setText('Mouse coords: ( %d : %d )' % (event.x(), event.y()))
    #        self.__coordLabelRD.setText('%d: Mouse coords: ( %d : %d )' % (li, p.x, p.y))
    #        time.sleep(0.1)
    #        if(self.__th_stop == True):
    #            break

    #def __del__(self):
    #    self.__th_stop = True

    def timerEvent(self, qte):
        # https://www.cyberforum.ru/qt/thread754318.html
        #p = self.pos()
        p = pyautogui.position()
        #if(self.__buttonLU_pressed == False):
        self.__coordLabelLU.setText('Mouse coords: ( %d : %d )' % (p.x, p.y))
        #if(self.__buttonRD_pressed == False):
        self.__coordLabelRD.setText('Mouse coords: ( %d : %d )' % (p.x, p.y))

        if(self.__buttonLU_pressed and self.__count_LU > 0):
            self.__count_LU -= self.__updateInterval
            self.__counterLabel.setText(str(self.__count_LU))
            if(self.__count_LU <= 0):
                self.__count_LU = -1
                self.__buttonLU_pressed = False
                self.__setButtonLU.setStyleSheet("background-color: green")
                p = pyautogui.position()
                self.__x_LU = p.x
                self.__y_LU = p.y
                self.__setButtonLU.setText(f"{self.__x_LU} {self.__y_LU}")
                #self.__counterLabel.setText(self.__delayTextLine.text())
                self.__setDelay(self.__delayTextLine.text())

        if(self.__coordLabelRD and self.__count_RD > 0):
            self.__count_RD -= self.__updateInterval
            self.__counterLabel.setText(str(self.__count_RD))
            if(self.__count_RD <= 0):
                self.__count_RD = -1
                self.__buttonLU_pressed = False
                self.__setButtonRD.setStyleSheet("background-color: green")
                p = pyautogui.position()
                self.__x_RD = p.x
                self.__y_RD = p.y
                self.__setButtonRD.setText(f"{self.__x_RD} {self.__y_RD}")
                #self.__counterLabel.setText(self.__delayTextLine.text())
                self.__setDelay(self.__delayTextLine.text())


    def __ifError(self, text : str):
        #https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text + "\nCheck README.md: https://github.com/The220th/grabook")
        msg.setWindowTitle("Syntax error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setModal(True)
        msg.exec()


    def __setDelay(self, text):
        #self.__counterLabel.setText(f"{self.__delayTextLine.text()}")
        #print(text)
        if(text.isdigit()):
            self.__counterLabel.setText(text)
        else:
            self.__ifError("Counter must be number. ")
            return
        #self.__counterLabel.adjustSize()
    #def mouseMoveEvent(self, event):
    #    p = self.pos()
    #    
    #    self.__coordLabelLU.setText('Mouse coords: ( %d : %d )' % (event.x(), event.y()))
    #    self.__coordLabelRD.setText('Mouse coords: ( %d : %d )' % (p.x(), p.y()))

    def __buttonHundler(self, b):
        if(self.__setButtonLU == b):
            #time.sleep(5)
            self.__buttonLU_pressed = True
            b.setStyleSheet("background-color: white")
            self.__count_LU = int(self.__counterLabel.text())*1000
        elif(self.__setButtonRD == b):
            self.__buttonRD_pressed = True
            b.setStyleSheet("background-color: white")
            self.__count_RD = int(self.__counterLabel.text())*1000

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = GrabWidget()
    sys.exit(app.exec_())