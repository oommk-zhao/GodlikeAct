# This Python file uses the following encoding: utf-8
from enum import Enum

class Direction(Enum):
    North = [0, -1]
    NorthEast = [1, -1]
    East = [1, 0]
    SouthEast = [1, 1]
    South = [0, 1]
    SouthWest = [-1, 1]
    West = [-1, 0]
    NorthWest = [-1, -1]
    InSitu = [0, 0]

class GlobalDefineClass():
    xIndex = 0
    yIndex = 1
