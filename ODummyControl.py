# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2.QtCore import QObject, Signal, Slot, QThread

from OMainWidget import *
from OAbstractObject import *
from OAbstractMap import *
from OObjectAbsCommand import *
from OEventManager import *


class DummyControl(QtCore.QObject):
    def __init__(self, parent = None):
        QObject.__init__(self, parent)

        self.worldMap = OAbstractMap(self)
        self.mainWidget_ = MainWidget(self.worldMap)

        self.objectList = []

        self.eventManager = EventManager()

        self.objectEventThread = QThread(self)
        self.eventManager.moveToThread(self.objectEventThread)


    def showTheWorld(self):
        self.mainWidget_.showTheWorld()

    def startTheWorld(self):
        self.objectEventThread.start()
        self.generateSingleObject()

        for objectIt in self.objectList:
            objectIt.activeObject()

    @Slot()
    def processObjEvent(self):
        objectCommand = OObjectAbsCommand(self.sender())
        self.eventManager.addObjectEvent(objectCommand)


    @Slot()
    def generateSingleObject(self):
        singleObject = OAbstractObject(self.worldMap, self)
        singleObject.setRange(self.worldMap.getRange()[0], self.worldMap.getRange()[1])
        singleObject.generatePosition(self.worldMap.getRange()[0], self.worldMap.getRange()[1])
        singleObject.signalRequestToDo.connect(self.processObjEvent)

        self.objectList.append(singleObject)

