# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2.QtCore import QObject


class AbstractMap(QtCore.QObject):
    def __init__(self):        
        QObject.__init__(self)
        #we are using Qt x.y coordinate
        self.xRange = 2
        self.yRange = 2
        self.worldMap = [ [ 0 for i in range(self.xRange) ] for j in range(self.yRange) ]

    def isPositionLegal(self, position):
        isLegal = True

        if (position[0] >= self.xRange) or (position[1] >= self.yRange) :
            isLegal = False

        return isLegal

    def getRange(self):
        return (self.xRange, self.yRange)

    def setRange(self, xRange, yRange):
        self.xRange = xRange
        self.yRange = yRange
