# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2.QtCore import QObject
from AbstractObject import *

class ObjectAbsCommand(QtCore.QObject):
    def __init__(self, object, parent = None):
        QObject.__init__(self, parent)
        self.object = object

    def execute(self):
        if self.object != None:
            AbstractObject(self.object.requestToDo())

