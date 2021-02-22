# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication

from DummyControl import *


if __name__ == "__main__":
    app = QApplication([])
    dummyControl_ = DummyControl()

    dummyControl_.startTheWorld()
    dummyControl_.showTheWorld()

    sys.exit(app.exec_())
