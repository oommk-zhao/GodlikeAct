# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2.QtCore import QObject
from OAbstractObject import *
from OAbstractMap import *

class OObjectAbsCommand(QtCore.QObject):
    def __init__(self, object, parent = None):
        QObject.__init__(self, parent)
        self.object = object

    def execute(self):
        if self.object != None:
            self.object.processTheEvent()

