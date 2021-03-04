# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2.QtCore import QObject, QTimer

from OObjectAbsCommand import *
from OAbstractMap import *
from OAbstractObject import *

class EventManager(QObject):
    def __init__(self, parent = None):
        QObject.__init__(self, parent)
        self.objectEventList = []
        self.objectEventTimer = QTimer()
        self.objectEventTimer.timeout.connect(self.executeObjectEventList)
        self.objectEventTimer.start(500)

    def addObjectEvent(self, objectEvent):
        self.objectEventList.append(OObjectAbsCommand(objectEvent))

    def executeObjectEventList(self):
        for objectIt in self.objectEventList:
            objectIt.execute()

