# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPalette, QColor

from MapBlockGraphicsItem import *
from ObjectGraphicsItem import *
from MainViewer import *
from WorldScene import *


class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setGeometry(0, 0, 800, 600)

        tempPalette = self.palette()
        tempPalette.setColor(QPalette.ColorRole.Background, QtCore.Qt.GlobalColor.darkGreen)
        self.setPalette(tempPalette)

        self.WorldSceneInstance = WorldScene(self)

        tempItem = ObjectGraphicsItem(self)
        self.WorldSceneInstance.addItem(tempItem)

        self.MainViewerInstance = MainViewer(self)
        self.MainViewerInstance.setGeometry(50,50,500,500)
        self.MainViewerInstance.setScene(self.WorldSceneInstance)

    def showTheWorld(self):
        self.show()
