import sys#系统相关的信息模块

import serial

from PyQt5 import QtWidgets, QtCore, QtSerialPort
from PyQt5.QtCore import QCoreApplication

from UI import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):#继承QWidget
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.pushButton_openport.clicked.connect(self.ButtonHandle)
    def ButtonHandle(self):
        ser = serial.Serial('COM7')
        self.textBrowser_sysinf.setText(ser.name)
        ser.write(b'hello')
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
