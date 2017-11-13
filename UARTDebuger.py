import sys#系统相关的信息模块
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets, QtCore, QtSerialPort
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QVariant
from UI import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):#继承QWidget
    global ser
    ser = serial.Serial()
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
        self.comboBox_baudrate.setCurrentText("9600")
        ser.baudrate = 9600

        self.comboBox_bytesize.addItem("5 bit",5)
        self.comboBox_bytesize.addItem("6 bit",6)
        self.comboBox_bytesize.addItem("7 bit",7)
        self.comboBox_bytesize.addItem("8 bit",8)
        self.comboBox_bytesize.activated.connect(self.comboBox_bytesize_Selection_Handle)
        self.comboBox_bytesize.setCurrentText("8 bit")
        ser.bytesize = serial.EIGHTBITS
        
        self.comboBox_parity.addItem("NONE",0)
        self.comboBox_parity.addItem("EVEN",1)
        self.comboBox_parity.addItem("ODD",2)
        self.comboBox_parity.activated.connect(self.comboBox_parity_Selection_Handle)
        self.comboBox_parity.setCurrentText("NONE")
        ser.parity = serial.PARITY_NONE

        self.comboBox_stopbits.addItem("1 bit",0)
        self.comboBox_stopbits.addItem("1.5 bit",1)
        self.comboBox_stopbits.addItem("2 bit",2)
        self.comboBox_stopbits.activated.connect(self.comboBox_stopbits_Selection_Handle)
        self.comboBox_stopbits.setCurrentText("1 bit")
        ser.stopbits = serial.STOPBITS_ONE

        self.lineEdit_timeout.textChanged.connect(self.lineEdit_timeout_Input_Handle)
        self.lineEdit_timeout.setText("0")
        ser.timeout = 0

        self.checkBox_xonxoff.stateChanged.connect(self.checkBox_xonxoff_Input_Handle)
        self.checkBox_rtscts.stateChanged.connect(self.checkBox_rtscts_Input_Handle)
        self.checkBox_dsrdtr.stateChanged.connect(self.checkBox_dsrdtr_Input_Handle)
        self.xonxoff  = False
        self.rtscts = False
        self.dsrdtr = False
        
        self.pushButton_openport.clicked.connect(self.pushButton_openport_Handle)
        self.pushButton_closeport.clicked.connect(self.pushButton_closeport_Handle)

    def comboBox_port_Search_Handle(self):
        self.comboBox_port.clear()
        port_list = list(serial.tools.list_ports.comports())
        length = len(port_list)
        if  length > 0:
            for i in range(0,length):
                port_temp = list(port_list[i])
                self.comboBox_port.addItem(port_temp[0])
                
    def comboBox_port_Selection_Handle(self):
        ser.port = self.comboBox_port.currentText()
        print("port=",ser.port)
            
    def comboBox_baudrate_Selection_Handle(self):
        ser.baudrate = self.comboBox_baudrate.currentData()
        print("baudrate=", ser.baudrate)
        if ser.is_open:
            settings = ser.get_settings()
            ser.apply_settings(settings)
            
    def comboBox_bytesize_Selection_Handle(self):
        bytesize = self.comboBox_bytesize.currentData()
        if bytesize == 5:
            ser.bytesize = serial.FIVEBITS
        elif bytesize == 6:
            ser.bytesize = serial.SIXBITS
        elif bytesize == 7:
            ser.bytesize = serial.SEVENBITS
        elif bytesize == 8:
            ser.bytesize = serial.EIGHTBITS
        print("bytesize=", ser.bytesize)
        if ser.is_open:
            settings = ser.get_settings()
            ser.apply_settings(settings)
            
    def comboBox_parity_Selection_Handle(self):
        Parity = self.comboBox_parity.currentData()
        print("parity=", Parity)
        if ser.is_open:
            settings = ser.get_settings()
            ser.apply_settings(settings)
            
    def comboBox_stopbits_Selection_Handle(self):
        StopBits = self.comboBox_stopbits.currentData()
        print("stopbits=", StopBits)
        if ser.is_open:
            settings = ser.get_settings()
            ser.apply_settings(settings)
            
    def lineEdit_timeout_Input_Handle(self):
        str1 = self.lineEdit_timeout.text()
        if str1.isdigit():
            Timeout = float(str1)
            print("timeout=",Timeout," seconds")
        else:
            print("timeout=invalid input")
        if ser.is_open:
            settings = ser.get_settings()
            ser.apply_settings(settings)
            
    def checkBox_xonxoff_Input_Handle(self):
        Xonxoff = self.checkBox_xonxoff.checkState()
        print("xonxoff=", Xonxoff)
        if ser.is_open:
            settings = ser.get_settings()
            ser.apply_settings(settings)
            
    def checkBox_rtscts_Input_Handle(self):
        Rtscts = self.checkBox_rtscts.checkState()
        print("rtscts=", Rtscts)
        if ser.is_open:
            settings = ser.get_settings()
            ser.apply_settings(settings)        
        
    def checkBox_dsrdtr_Input_Handle(self):
        Dsrdtr = self.checkBox_dsrdtr.checkState()
        print("dsrdtr=", Dsrdtr)
        if ser.is_open:
            settings = ser.get_settings()
            ser.apply_settings(settings)
            
    def pushButton_openport_Handle(self):
        if ser.is_open:
            print("serial already opened")
        else:
            ser.open()
            print("opening serial")
    def pushButton_closeport_Handle(self):
        if ser.is_open:
            ser.close()
            print("closing serial")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
