# This Python file uses the following encoding: utf-8
from PySide2 import QtWidgets
from PySide2.QtWidgets import QGraphicsView, QWidget

class MainViewer(QGraphicsView):
    def __init__(self, parent = None):
        QGraphicsView.__init__(self, parent)
