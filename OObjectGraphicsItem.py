# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2.QtCore import QObject, Qt, QRectF, QPointF, QTimer, Signal, Slot
from PySide2.QtGui import QPen, QColor
from OGlobalDefine import GlobalDefine

import time

#This is the "Factor" Class, to only make the QGraphicsItem have the QObject
class OObjectGraphicsItem(QObject):

    #____
    def __init__(self, parent = None):
        QObject.__init__(self, parent)
