import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from untitled import *

class MyWindow(QMainWindow,Ui_Dialog):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

    def accept(self):
        print("HI")

    def reject(self):
        print("HI")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())