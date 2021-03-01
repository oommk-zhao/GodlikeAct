# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2.QtCore import QObject, QTimer

from ObjectAbsCommand import *

class EventManager(QObject):
    def __init__(self, parent = None):
        QObject.__init__(self, parent)
        self.objectEventList = []
        self.objectEventTimer = QTimer(self)
        self.objectEventTimer.timeout.connect(self.executeObjectEventList())
        self.objectEventTimer.start(250)

    def addObjectEvent(self, objectEvent):
        self.objectEventList.append(objectEvent)

    def executeObjectEventList(self):
        print ("inside execute")
        #for objectIt in self.objectEventList:
         #   ObjectAbsCommand(objectIt).execute()

