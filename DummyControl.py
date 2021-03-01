# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2.QtCore import QObject, Signal, Slot

from MainWidget import *
from AbstractObject import *
from AbstractMap import *
from ObjectAbsCommand import *
from EventManager import *


class DummyControl(QtCore.QObject):
    def __init__(self, parent = None):
        QObject.__init__(self, parent)

        self.worldMap = AbstractMap(self)
        self.mainWidget_ = MainWidget(self.worldMap)

        self.objectList = []

    def showTheWorld(self):
        self.mainWidget_.showTheWorld()

    def startTheWorld(self):
        self.generateSingleObject()

        for objectIt in self.objectList:
            objectIt.activeObject()

    @Slot()
    def processObjEvent(self):



    @Slot()
    def generateSingleObject(self):
        singleObject = AbstractObject(self.worldMap)
        singleObject.setRange(self.worldMap.getRange()[0], self.worldMap.getRange()[1])
        singleObject.generatePosition(self.worldMap.getRange()[0], self.worldMap.getRange()[1])
        singleObject.signalRequestToDo.connect(self.processObjEvent)

        self.objectList.append(singleObject)

