# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2.QtCore import QObject, Signal, Slot, QThread

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

        self.eventManager = EventManager()

        #self.objectEventThread = QThread(self)
        #self.eventManager.moveToThread(self.objectEventThread)


    def showTheWorld(self):
        self.mainWidget_.showTheWorld()

    def startTheWorld(self):
        #self.objectEventThread.start()
        self.generateSingleObject()

        for objectIt in self.objectList:
            objectIt.activeObject()

    @Slot()
    def processObjEvent(self):
        objectCommand = ObjectAbsCommand(self.sender())
        self.eventManager.addObjectEvent(objectCommand)


    @Slot()
    def generateSingleObject(self):
        singleObject = AbstractObject(self.worldMap)
        singleObject.setRange(self.worldMap.getRange()[0], self.worldMap.getRange()[1])
        singleObject.generatePosition(self.worldMap.getRange()[0], self.worldMap.getRange()[1])
        singleObject.signalRequestToDo.connect(self.processObjEvent)

        self.objectList.append(singleObject)

