from check_db import *
from autorisation import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Interface(QtWidgets.QWidget):
    def __int__(self):
        super(Interface, self).__init__()
        self.ui = Ui_autorisation()
        self.ui.setupUi(self)
        self.ui.login_btn.connect(self.auth)
        self.base_line_edit = [self.ui.username_value, self.ui.password_value]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

    #Проверка правильности ввода
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
                funct(self)
        return wrapper

    #Обработка сигналов
    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    @check_input
    def auth(self):
        username = self.ui.username_value.text()
        password = self.ui.password_value.text()
        self.check_db.thr_login(username, password)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())
