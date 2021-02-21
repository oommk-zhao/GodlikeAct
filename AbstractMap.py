# This Python file uses the following encoding: utf-8
from PySide2 import QtCore


class AbstractMap(QtCore.QObject):
    def __init__(self):        
        #we are using Qt x.y coordinate
        self.xRange = 3
        self.yRange = 3
        self.worldMap = [ [ 0 for i in range(self.xRange) ] for j in range(self.yRange) ]

    def isPositionLegal(position):
        isLegal = True

        if(position[0] >= self.xRange || position[1] >= self.yRange)
            isLegal = False

        return isLegal
