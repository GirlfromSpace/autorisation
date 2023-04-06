from PyQt5 import QtCore, QtGui, QtWidgets
from handler.db_handler import *

class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def thr_login(self, username, password):
        login(username, password, self.mysignal)