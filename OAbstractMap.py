# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2.QtCore import QObject
from OGlobalDefine import Direction, GlobalDefine


class OAbstractMap(QtCore.QObject):
    #----
    def __init__(self, parent = None):
        QObject.__init__(self, parent)
        #we are using Qt x.y coordinate
        self.xMax = 4
        self.yMax = 2
        self.xMin = 0
        self.yMin = 0
        self.worldMap = [ [ 0 for i in range(self.xMax) ] for j in range(self.yMax) ]

    #----
    def isPositionLegal(self, position):
        isLegal = True

        if (position[0] >= self.xMax) or (position[1] >= self.yMax):
            isLegal = False

        return isLegal

    #----
    def getRange(self):
        return [self.xMax, self.yMax]

    #----
    def setRange(self, xMax, yMax):
        self.xMax = xRange
        self.yMax = yRange

    #----
    def getAvailableNextPosition(self, currentPoint):
        nextPointList = []

        for i in Direction:
            nextPoint = []

            for j, k in zip(currentPoint, i.value):
                nextPoint.append(j + k)

            if nextPoint[GlobalDefine.xIndex] > self.xMax:
                nextPoint[GlobalDefine.xIndex] = self.xMin
            elif nextPoint[GlobalDefine.xIndex] < self.xMin:
                nextPoint[GlobalDefine.xIndex] = self.xMax

            if nextPoint[GlobalDefine.yIndex] > self.yMax:
                nextPoint[GlobalDefine.yIndex] = self.yMin
            elif nextPoint[GlobalDefine.yIndex] < self.yMin:
                nextPoint[GlobalDefine.yIndex] = self.yMax

            nextPointList.append(nextPoint)

        return nextPointList
