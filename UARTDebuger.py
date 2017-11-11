import sys#系统相关的信息模块

import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets, QtCore, QtSerialPort
from PyQt5.QtCore import QCoreApplication

from UI import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):#继承QWidget
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.comboBox_port.mysignal.connect(self.pushButton_openport_Handle)
        self.pushButton_openport.clicked.connect(self.ButtonHandle)
    def ButtonHandle(self):
        ser = serial.Serial('COM7')
        self.textBrowser_sysinf.setText(ser.name)
        ser.write(b'hello')
    def pushButton_openport_Handle(self):
        port_list = list(serial.tools.list_ports.comports())
        length = len(port_list)
        if  length <= 0:
            print("The Serial port can't find!")
        else:
            for i in range(0,length):
                port_temp = list(port_list[i])
                print("check which port was really used >",port_temp[0])
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
