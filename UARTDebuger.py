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
        if  length<= 0:
            print("The Serial port can't find!")
        else:
            print(length)
            port_list_0 =list(port_list[0])
            port_serial = port_list_0[0]
            ser = serial.Serial(port_serial,9600,timeout = 60)
            print("check which port was really used >",ser.name)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
