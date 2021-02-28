# This Python file uses the following encoding: utf-8
from AbstractObject import *

class ObjectAbsCommand:
    def __init__(self, object):
        self.object = object

    def execute(self):
        if self.object != None:
            AbstractObject(self.object.requestToDo())

