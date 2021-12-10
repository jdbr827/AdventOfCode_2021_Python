import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from untitled import *
from Day9.day_9 import *

class MyWindow(QMainWindow,Ui_Dialog):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.matrix = read_in_matrix('Day9/day_9_small_input.txt')
        self.tableWidget.setRowCount(len(self.matrix))
        self.tableWidget.setColumnCount(len(self.matrix))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.matrix[i][j])))
                if self.matrix[i][j] == 9:
                    self.tableWidget.item(i, j).setBackground(QtGui.QColor(0, 0, 0))
                else:
                    darkness = int((1 - (self.matrix[i][j] / 8.0)) * 192) + 64
                    print(self.matrix[i][j], darkness)
                    self.tableWidget.item(i, j).setBackground(QtGui.QColor(darkness, darkness, darkness))


    def accept(self):
        print("Yo")

    def reject(self):
        print("HI")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())