# This Python file uses the following encoding: utf-8
from PySide2 import QtWidgets
from PySide2.QtWidgets import QGraphicsItem
from PySide2.QtCore import Qt, QRectF
from PySide2.QtGui import QPen, QColor
from OGlobalDefine import GlobalDefine

class MapBlockGraphicsItem(QGraphicsItem):

    #____
    def __init__(self, parent = None):
        QGraphicsItem.__init__(self, parent)

        self.positionX = 0
        self.positionY = 0
        self.width = 0
        self.height = 0
        self.paintPen = QPen(Qt.GlobalColor.lightGray)
        self.paintPen.setWidth(5)

        self.backColor = Qt.GlobalColor.lightGray
        self.backImageStr = None

    #____
    def paint(self, painter, styleOptionItem, parent):
        painter.setPen(self.paintPen)
        painter.fillRect(self.positionX, self.positionY, self.width, self.height, self.backColor)

    #____
    def boundingRect(self):
        return QRectF(0,0,0,0)

    #____
    # In demo version, no need to overload this method
    #def shape(self):
    #    pass

    #____
    def setSize(self, width, height):
        self.width = width
        self.height = height

    #____
    def setBackColor(self, qtColor):
        self.backColor = qtColor

    #____
    def setBackImage(self, imageStr):
        self.backImageStr = imageStr

    #____
    def setPosition(self, pointX, pointY):
        self.positionX = pointX
        self.positionY = pointY
        self.setPos(self.positionX * GlobalDefine.mapBlockWidth, self.positionY* GlobalDefine.mapBlockHeight)

    #____
    def setMargin(self, value):
        self.leftMargin = value
        self.rightMargin = value
        self.topMargin = value
        self.bottomMargin = value
