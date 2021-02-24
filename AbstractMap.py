# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2.QtCore import QObject
from GlobalDefine import Direction, GlobalDefineClass


class AbstractMap(QtCore.QObject):
    #----
    def __init__(self, parent = None):
        QObject.__init__(self, parent)
        #we are using Qt x.y coordinate
        self.xMax = 2
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
        return (self.xMax, self.yMax)

    #----
    def setRange(self, xMax, yMax):
        self.xMax = xRange
        self.yMax = yRange

    #----
    def getAvailableNextPositionList(self, currentPoint):
        nextPointList = []

        for i in Direction:
            nextPoint = []

            for j, k in zip(currentPoint, i.value):
                nextPoint.append(j + k)

            if nextPoint[GlobalDefineClass.xIndex] > self.xMax:
                nextPoint[GlobalDefineClass.xIndex] = self.xMin
            elif nextPoint[GlobalDefineClass.xIndex] < self.xMin:
                nextPoint[GlobalDefineClass.xIndex] = self.xMax

            if nextPoint[GlobalDefineClass.yIndex] > self.yMax:
                nextPoint[GlobalDefineClass.yIndex] = self.yMin
            elif nextPoint[GlobalDefineClass.yIndex] < self.yMin:
                nextPoint[GlobalDefineClass.yIndex] = self.yMax

            nextPointList.append(nextPoint)

        return nextPointList
