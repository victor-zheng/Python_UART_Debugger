import sys#系统相关的信息模块

import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets, QtCore, QtSerialPort
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QVariant
from UI import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):#继承QWidget
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        #initialize the UART parameter selection UI
        self.comboBox_port.mysignal.connect(self.comboBox_port_Search_Handle)
        self.comboBox_port.activated.connect(self.comboBox_port_Selection_Handle)

        self.comboBox_baudrate.addItem("600",600)
        self.comboBox_baudrate.addItem("1200",1200)
        self.comboBox_baudrate.addItem("4800",4800)
        self.comboBox_baudrate.addItem("9600",9600)
        self.comboBox_baudrate.addItem("19200",19200)
        self.comboBox_baudrate.addItem("38400",38400)
        self.comboBox_baudrate.addItem("57600",57600)
        self.comboBox_baudrate.addItem("115200",115200)
        self.comboBox_baudrate.activated.connect(self.comboBox_baudrate_Selection_Handle)

        self.comboBox_bytesize.addItem("4 bit",4)
        self.comboBox_bytesize.addItem("5 bit",5)
        self.comboBox_bytesize.addItem("6 bit",6)
        self.comboBox_bytesize.addItem("7 bit",7)
        self.comboBox_bytesize.addItem("8 bit",8)
        self.comboBox_bytesize.activated.connect(self.comboBox_bytesize_Selection_Handle)
        
        self.comboBox_parity.addItem("NONE",0)
        self.comboBox_parity.addItem("EVEN",1)
        self.comboBox_parity.addItem("ODD",2)
        self.comboBox_parity.activated.connect(self.comboBox_parity_Selection_Handle)

        self.comboBox_stopbits.addItem("1 bit",0)
        self.comboBox_stopbits.addItem("1.5 bit",1)
        self.comboBox_stopbits.addItem("2 bit",2)
        self.comboBox_stopbits.activated.connect(self.comboBox_stopbits_Selection_Handle)
        
        self.pushButton_openport.clicked.connect(self.pushButton_openport_Handle)

    def comboBox_port_Search_Handle(self):
        self.comboBox_port.clear()
        port_list = list(serial.tools.list_ports.comports())
        length = len(port_list)
        if  length <= 0:
            print("The Serial port can't find!")
        else:
            for i in range(0,length):
                port_temp = list(port_list[i])
                print("check which port was really used >",port_temp[0])
                self.comboBox_port.addItem(port_temp[0])
                
    def comboBox_port_Selection_Handle(self):
        ActivePortName = self.comboBox_port.currentText()
        print("port=",ActivePortName)
        
    def comboBox_baudrate_Selection_Handle(self):
        BaudRate = self.comboBox_baudrate.currentData()
        print("baudrate=", BaudRate)
        
    def comboBox_bytesize_Selection_Handle(self):
        ByteSize = self.comboBox_bytesize.currentData()
        print("bytesize=", ByteSize)
        
    def comboBox_parity_Selection_Handle(self):
        Parity = self.comboBox_parity.currentData()
        print("parity=", Parity)
        
    def comboBox_stopbits_Selection_Handle(self):
        StopBits = self.comboBox_stopbits.currentData()
        print("stopbits=", StopBits)
        
    def comboBox_timeout_Input_Handle(self):
        print("timeout=")
        
    def pushButton_openport_Handle(self):
        ser = serial.Serial('COM7')
        self.textBrowser_sysinf.setText(ser.name)
        ser.write(b'hello')
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
