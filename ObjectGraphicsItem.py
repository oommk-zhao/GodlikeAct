# This Python file uses the following encoding: utf-8
from PySide2 import QtWidgets
from PySide2.QtWidgets import QGraphicsItem

class ObjectGraphicsItem(QGraphicsItem):
    def __init__(self, parent = None):
        QGraphicsItem.__init__(self)

    def paint(self, painter, styleOptionItem, parent):
        painter.drawText(-200,-30, ("i am the item"))

    def boundingRect(self):
        pass
