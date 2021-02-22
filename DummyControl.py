# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2.QtCore import QObject, Signal, Slot

from MainWidget import *
from AbstractObject import *
from AbstractMap import *


class DummyControl(QtCore.QObject):
    def __init__(self):
        QObject.__init__(self)
        self.mainWidget_ = MainWidget()
        self.worldMap = AbstractMap()
        self.objectList = []

    def showTheWorld(self):
        self.mainWidget_.show()

    @Slot()
    def generateSingleObject(self):
        singleObject = AbstractObject()
        singleObject.setRange(self.worldMap.getRange()[0], self.worldMap.getRange()[1])
        singleObject.generatePosition(self.worldMap.getRange()[0], self.worldMap.getRange()[1])
        self.objectList.append(singleObject)
        print (singleObject.where())
