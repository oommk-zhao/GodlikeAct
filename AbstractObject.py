# This Python file uses the following encoding: utf-8
from PySide2 import QtCore pyqtSignal pyqtSlot
import random


class AbstractObject(QtCore.QObject):

    signalRequestToDo = pyqtSignal()

    def __init__(self):
        self.position = (random.randint(0,2), random.randint(0,2))

    def where(self):
        return self.position

    @pyqtSlot()
    def requestToDo(self):
        pass

    @pyqtSlot()
    def processObjEvent(self):
        pass



