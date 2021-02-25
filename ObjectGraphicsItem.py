# This Python file uses the following encoding: utf-8
from PySide2 import QtWidgets
from PySide2.QtWidgets import QGraphicsItem
from PySide2.QtCore import QRectF

class ObjectGraphicsItem(QGraphicsItem):
    def __init__(self, parent = None):
        QGraphicsItem.__init__(self, parent)

    def paint(self, painter, styleOptionItem, parent):
        pass
        #painter.drawText(-200,-30, ("i am the item"))

    def boundingRect(self):
        return QRectF(0.0, 0.0, 50, 50)
