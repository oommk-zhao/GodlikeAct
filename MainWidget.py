# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget, QAbstractScrollArea
from PySide2.QtGui import QPalette, QColor

from MapBlockGraphicsItem import *
from ObjectGraphicsItem import *
from MainViewer import *
from WorldScene import *
from AbstractMap import *


class MainWidget(QtWidgets.QWidget):
    #____
    def __init__(self, worldMapObj, parent = None):
        QWidget.__init__(self, parent)
        self.setGeometry(0, 0, 800, 600)

        self.leftMargin = 235
        self.rightMargin = 235
        self.topMargin = 135
        self.bottomMargin = 135
        self.worldMapObj = worldMapObj

        tempPalette = self.palette()
        tempPalette.setColor(QPalette.ColorRole.Background, QtCore.Qt.GlobalColor.darkGreen)
        self.setPalette(tempPalette)

        self.WorldSceneInstance = WorldScene(self)

        self.MainViewerInstance = MainViewer(self)
        #self.MainViewerInstance.setGeometry(235, 135, 300,300)
        self.MainViewerInstance.setGeometry(50, 50, 700,500)
        self.MainViewerInstance.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.MainViewerInstance.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.MainViewerInstance.setScene(self.WorldSceneInstance)

        self.generateMapBlock()

    #____
    def showTheWorld(self):
        self.show()
        self.MainViewerInstance.update()

    #____
    def generateMapBlock(self):

        worldMapRange = self.worldMapObj.getRange()

        for i in range (-1, worldMapRange[GlobalDefineClass.xIndex]):
            for j in range (-1, worldMapRange[GlobalDefineClass.yIndex]):
                tempMapBlock = MapBlockGraphicsItem()
                tempMapBlock.setSize(100,100)
                tempMapBlock.setPosition(i, j)
                self.WorldSceneInstance.addItem(tempMapBlock)

    #____
    def generateObjects(self):
        tempItem = ObjectGraphicsItem()
