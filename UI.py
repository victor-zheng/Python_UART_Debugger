# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_params = QtWidgets.QWidget(self.centralwidget)
        self.widget_params.setGeometry(QtCore.QRect(10, 10, 171, 521))
        self.widget_params.setObjectName("widget_params")
        self.comboBox_port = QtWidgets.QComboBox(self.widget_params)
        self.comboBox_port.setGeometry(QtCore.QRect(10, 30, 151, 22))
        self.comboBox_port.setObjectName("comboBox_port")
        self.comboBox_baudrate = QtWidgets.QComboBox(self.widget_params)
        self.comboBox_baudrate.setGeometry(QtCore.QRect(10, 90, 151, 22))
        self.comboBox_baudrate.setObjectName("comboBox_baudrate")
        self.comboBox_bytesize = QtWidgets.QComboBox(self.widget_params)
        self.comboBox_bytesize.setGeometry(QtCore.QRect(10, 150, 151, 22))
        self.comboBox_bytesize.setObjectName("comboBox_bytesize")
        self.comboBox_parity = QtWidgets.QComboBox(self.widget_params)
        self.comboBox_parity.setGeometry(QtCore.QRect(10, 210, 151, 22))
        self.comboBox_parity.setObjectName("comboBox_parity")
        self.comboBox_stopbits = QtWidgets.QComboBox(self.widget_params)
        self.comboBox_stopbits.setGeometry(QtCore.QRect(10, 270, 151, 22))
        self.comboBox_stopbits.setObjectName("comboBox_stopbits")
        self.label = QtWidgets.QLabel(self.widget_params)
        self.label.setGeometry(QtCore.QRect(10, 10, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_params)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_params)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_params)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_params)
        self.label_5.setGeometry(QtCore.QRect(10, 250, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_params)
        self.label_6.setGeometry(QtCore.QRect(10, 310, 72, 15))
        self.label_6.setObjectName("label_6")
        self.comboBox_timeout = QtWidgets.QComboBox(self.widget_params)
        self.comboBox_timeout.setGeometry(QtCore.QRect(10, 330, 151, 22))
        self.comboBox_timeout.setObjectName("comboBox_timeout")
        self.label_7 = QtWidgets.QLabel(self.widget_params)
        self.label_7.setGeometry(QtCore.QRect(10, 370, 72, 15))
        self.label_7.setObjectName("label_7")
        self.comboBox_xonxoff = QtWidgets.QComboBox(self.widget_params)
        self.comboBox_xonxoff.setGeometry(QtCore.QRect(10, 390, 151, 22))
        self.comboBox_xonxoff.setObjectName("comboBox_xonxoff")
        self.label_8 = QtWidgets.QLabel(self.widget_params)
        self.label_8.setGeometry(QtCore.QRect(10, 430, 72, 15))
        self.label_8.setObjectName("label_8")
        self.comboBox_rtscts = QtWidgets.QComboBox(self.widget_params)
        self.comboBox_rtscts.setGeometry(QtCore.QRect(10, 450, 151, 22))
        self.comboBox_rtscts.setObjectName("comboBox_rtscts")
        self.pushButton_openport = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_openport.setGeometry(QtCore.QRect(240, 450, 111, 28))
        self.pushButton_openport.setObjectName("pushButton_openport")
        self.textBrowser_receive = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_receive.setGeometry(QtCore.QRect(240, 111, 511, 141))
        self.textBrowser_receive.setObjectName("textBrowser_receive")
        self.textEdit_transmit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_transmit.setGeometry(QtCore.QRect(240, 300, 511, 131))
        self.textEdit_transmit.setObjectName("textEdit_transmit")
        self.lcdNumber_rx = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rx.setGeometry(QtCore.QRect(240, 90, 64, 23))
        self.lcdNumber_rx.setObjectName("lcdNumber_rx")
        self.lcdNumber_tx = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_tx.setGeometry(QtCore.QRect(240, 280, 64, 23))
        self.lcdNumber_tx.setObjectName("lcdNumber_tx")
        self.textBrowser_sysinf = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_sysinf.setGeometry(QtCore.QRect(240, 40, 511, 31))
        self.textBrowser_sysinf.setObjectName("textBrowser_sysinf")
        self.pushButton_receive = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_receive.setGeometry(QtCore.QRect(370, 450, 111, 28))
        self.pushButton_receive.setObjectName("pushButton_receive")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(630, 450, 111, 28))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send.setGeometry(QtCore.QRect(500, 450, 111, 28))
        self.pushButton_send.setObjectName("pushButton_send")
        self.pushButton_cmd1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cmd1.setGeometry(QtCore.QRect(240, 500, 111, 28))
        self.pushButton_cmd1.setObjectName("pushButton_cmd1")
        self.pushButton_cmd2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cmd2.setGeometry(QtCore.QRect(370, 500, 111, 28))
        self.pushButton_cmd2.setObjectName("pushButton_cmd2")
        self.pushButton_cmd3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cmd3.setGeometry(QtCore.QRect(500, 500, 111, 28))
        self.pushButton_cmd3.setObjectName("pushButton_cmd3")
        self.pushButton_cmd4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cmd4.setGeometry(QtCore.QRect(630, 500, 111, 28))
        self.pushButton_cmd4.setObjectName("pushButton_cmd4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(240, 20, 72, 15))
        self.label_9.setObjectName("label_9")
        self.widget_params.raise_()
        self.pushButton_openport.raise_()
        self.textBrowser_receive.raise_()
        self.textEdit_transmit.raise_()
        self.lcdNumber_rx.raise_()
        self.lcdNumber_tx.raise_()
        self.textBrowser_sysinf.raise_()
        self.pushButton_receive.raise_()
        self.pushButton_clear.raise_()
        self.pushButton_send.raise_()
        self.pushButton_cmd1.raise_()
        self.pushButton_cmd2.raise_()
        self.pushButton_cmd3.raise_()
        self.pushButton_cmd4.raise_()
        self.label_9.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Port"))
        self.label_2.setText(_translate("MainWindow", "BaudRate"))
        self.label_3.setText(_translate("MainWindow", "ByteSize"))
        self.label_4.setText(_translate("MainWindow", "Parity"))
        self.label_5.setText(_translate("MainWindow", "StopBits"))
        self.label_6.setText(_translate("MainWindow", "Timeout"))
        self.label_7.setText(_translate("MainWindow", "XonXoff"))
        self.label_8.setText(_translate("MainWindow", "RtsCts"))
        self.pushButton_openport.setText(_translate("MainWindow", "Open Port"))
        self.pushButton_receive.setText(_translate("MainWindow", "Receive"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_send.setText(_translate("MainWindow", "Send"))
        self.pushButton_cmd1.setText(_translate("MainWindow", "CMD1"))
        self.pushButton_cmd2.setText(_translate("MainWindow", "CMD2"))
        self.pushButton_cmd3.setText(_translate("MainWindow", "CMD3"))
        self.pushButton_cmd4.setText(_translate("MainWindow", "CMD4"))
        self.label_9.setText(_translate("MainWindow", "Information"))

