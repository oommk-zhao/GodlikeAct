# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2.QtCore import QObject, Signal, Slot, QTimer
import random


class AbstractObject(QtCore.QObject):

    signalRequestToDo = Signal()

    def __init__(self):
        QObject.__init__(self)
        self.position = (0, 0)
        self.signalRequestToDo.connect(self.processObjEvent)
        self.xRange = 0
        self.yRange = 0
        self.eventGenerateTimer = QTimer()
        self.eventGenerateTimer.timeout.connect(self.requestToDo)

    def where(self):
        return self.position

    def setRange(self, xRange, yRange):
        self.xRange = xRange
        self.yRange = yRange

    def generatePosition(self, xRange, yRange):
        self.position = (random.randint(0,xRange), random.randint(0,yRange))

    def activeObject(self):
        self.eventGenerateTimer.start(1000)

    @Slot()
    def requestToDo(self):
        self.signalRequestToDo.emit()

    @Slot()
    def processObjEvent(self):
        print ("we are moving")



