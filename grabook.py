# -*- coding: utf-8 -*-

from grabook import MainWidget

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QFrame, QApplication)
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())
