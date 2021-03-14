# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2.QtCore import QObject, Signal, Slot, QTimer
import random

from OAbstractMap import *


class OAbstractObject(QtCore.QObject):

    signalRequestToDo = Signal()
    signalMoving = Signal(list, list)

    def __init__(self, mapInstance, parent = None):
        QObject.__init__(self, parent)
        self.position = [0, 0]
        self.xRange = 0
        self.yRange = 0
        self.eventGenerateTimer = QTimer()
        self.eventGenerateTimer.timeout.connect(self.requestToDo)

        self.testValue = 1

        self.worldMapInstance = OAbstractMap(mapInstance)

    def where(self):
        return self.position

    def setRange(self, xRange, yRange):
        self.xRange = xRange
        self.yRange = yRange

    def generatePosition(self, xRange, yRange):
        self.position = [random.randint(0,xRange), random.randint(0,yRange)]

    def activeObject(self):
        self.eventGenerateTimer.start(1000)

    @Slot()
    def requestToDo(self):
        self.signalRequestToDo.emit()

    @Slot()
    def processTheEvent(self):
        availablePointList = self.worldMapInstance.getAvailableNextPosition(self.position)

        targetIndex = random.randint(0, (len(availablePointList) - 1))
        originalPosition = self.position

        print ("we are moving from :", self.position)
        self.position = availablePointList[targetIndex]
        print ("and the target is :", self.position)

        self.signalMoving.emit(originalPosition, targetIndex)




