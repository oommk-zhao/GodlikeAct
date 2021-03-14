# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget, QAbstractScrollArea
from PySide2.QtGui import QPalette, QColor
from PySide2.QtCore import Signal, Slot, Qt

from OMapBlockGraphicsItem import *
from OObjectGraphicsItem import *
from OMainViewer import *
from OWorldScene import *
from OAbstractMap import *
from OGlobalDefine import GlobalDefine



class OMainWidget(QtWidgets.QWidget):
    #____
    def __init__(self, worldMapObj, parent = None):
        QWidget.__init__(self, parent)
        self.setGeometry(0, 0, GlobalDefine.applicationWidth, GlobalDefine.applicationHeight)

        self.worldMapObj = worldMapObj

        tempPalette = self.palette()
        tempPalette.setColor(QPalette.ColorRole.Background, QtCore.Qt.GlobalColor.darkGreen)
        self.setPalette(tempPalette)

        self.worldSceneInstance = WorldScene(self)
        self.worldSceneInstance.setSceneRect(-GlobalDefine.worldSceneHorizontalMargin,
                                             -GlobalDefine.worldSceneVerticalMargin,
                                             GlobalDefine.worldSceneWidth,
                                             GlobalDefine.worldSceneHeight)

        self.mainViewerInstance = MainViewer(self)
        self.mainViewerInstance.setGeometry(GlobalDefine.worldScenePosX,
                                            GlobalDefine.worldScenePosY,
                                            GlobalDefine.worldSceneWidth,
                                            GlobalDefine.worldSceneHeight)

        self.mainViewerInstance.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mainViewerInstance.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mainViewerInstance.setScene(self.worldSceneInstance)

        self.generateMapBlock()

        self.generateObjects()
        self.graphicsItemTest = ObjectGraphicsItem()
        self.graphicsItemTest.setPosition(2, 1)
        self.graphicsItemTest.setSize(200, 200)
        self.worldSceneInstance.addItem(self.graphicsItemTest)

        self.testSceneUpdateTimer = QTimer(self)
        self.testSceneUpdateTimer.timeout.connect(self.letUpdateWorld)



    @Slot()
    def letUpdateWorld(self):
        self.mainViewerInstance.viewport().update()

    #____
    def showTheWorld(self):
        self.show()
        self.mainViewerInstance.update()

        self.testSceneUpdateTimer.start(1000)

        self.graphicsItemTest.moving([1, 1])
        self.mainViewerInstance.viewport().update()

    #____
    def generateMapBlock(self):

        worldMapRange = self.worldMapObj.getRange()

        for i in range (0, (worldMapRange[GlobalDefine.xIndex] + 1)):
            for j in range (0, (worldMapRange[GlobalDefine.yIndex] + 1)):
                tempMapBlock = None
                tempMapBlock = MapBlockGraphicsItem()
                tempMapBlock.setSize(GlobalDefine.mapBlockWidth, GlobalDefine.mapBlockHeight)
                tempMapBlock.setPosition(i, j)
                self.worldSceneInstance.addItem(tempMapBlock)

    #____
    def generateObjects(self):
        pass
        #tempItem = ObjectGraphicsItem()
        #tempItem.setPosition(2, 1)
        #tempItem.setSize(200, 200)
        #self.worldSceneInstance.addItem(tempItem)
