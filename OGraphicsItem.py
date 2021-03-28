# This Python file uses the following encoding: utf-8
from PySide2 import QWidgets
from QWidget import QGraphicsItem
from PySide2.QtCore import Qt, QRectF, QPointF, QTimer, Signal, Slot
from PySide2.QtGui import QPen, QColor
from OGlobalDefine import GlobalDefine

class OGraphicsItem(QGraphicsItem):

    #____
    def __init__(self, parent = None):
        QGraphicsItem.__init__(self, parent)
        self.positionX = 0
        self.positionY = 0
        self.width = 0
        self.height = 0

        self.backColor = None
        self.foreColor = Qt.GlobalColor.black
        self.backImageStr = None

        self.paintPen = QPen(self.foreColor)
        self.paintPen.setWidth(4)

        self.processEventTimer = QTimer()
        self.movingStep = 10
        self.targetX = 0
        self.targetY = 0

    #____
    def paint(self, painter, styleOptionItem, parent):
        painter.setPen(self.paintPen)
        painter.drawEllipse(self.positionX + 6, self.positionY + 6, self.width - 10, self.height - 10)

    #____
    def boundingRect(self):
        return QRectF(0, 0, 50, 50)

    #____
    # In demo version, no need to overload this method
    #def shape(self):
    #    pass

    #____
    def setSize(self, width, height):
        self.width = width
        self.height = height

    #____
    def setPosition(self, pointX, pointY):
        self.positionX = pointX * GlobalDefine.mapBlockWidth
        self.positionY = pointY * GlobalDefine.mapBlockHeight

    #____
    def moving(self, targetPosition):
        self.targetX = targetPosition[GlobalDefine.xIndex]
        self.targetY = targetPosition[GlobalDefine.yIndex]
        self.movingStep = 10

        self.processEventTimer.timeout.connect(self.slotProcessMovingEvent)
        self.processEventTimer.start(1000)

    #____
    @Slot()
    def slotProcessMovingEvent(self):
        print ("we are here and the step is :", self.movingStep)
        if (self.movingStep > 0):
            deltaX = (self.targetX - self.positionX) / self.movingStep
            deltaY = (self.targetY - self.positionY) / self.movingStep

            self.positionX += deltaX
            self.positionY += deltaY
            self.movingStep -= 1

            print ("inside A : ", deltaX, "   ", deltaY)
        else :
            self.processEventTimer.disconnect(self.processEventTimer)
            self.processEventTimer.stop()
            print ("inside B")





