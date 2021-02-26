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

        self.worldSceneInstance = WorldScene(self)
        self.worldSceneInstance.setSceneRect(-5, -5, 310, 310)

        self.mainViewerInstance = MainViewer(self)
        self.mainViewerInstance.setGeometry(235, 135, 310,310)
        #self.mainViewerInstance.setGeometry(50, 50, 700,500)
        self.mainViewerInstance.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mainViewerInstance.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mainViewerInstance.setScene(self.worldSceneInstance)

        self.generateMapBlock()

    #____
    def showTheWorld(self):
        self.show()
        self.mainViewerInstance.update()

    #____
    def generateMapBlock(self):

        worldMapRange = self.worldMapObj.getRange()

        for i in range (-1, worldMapRange[GlobalDefine.xIndex]):
            for j in range (-1, worldMapRange[GlobalDefine.yIndex]):
                tempMapBlock = MapBlockGraphicsItem()
                tempMapBlock.setSize(100,100)
                tempMapBlock.setPosition(i, j)
                self.worldSceneInstance.addItem(tempMapBlock)

    #____
    def generateObjects(self):
        tempItem = ObjectGraphicsItem()
