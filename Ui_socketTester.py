# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\python\socketTester.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.te_result = QtWidgets.QTextEdit(self.centralWidget)
        self.te_result.setGeometry(QtCore.QRect(40, 270, 721, 291))
        self.te_result.setObjectName("te_result")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(44, 50, 421, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_host = QtWidgets.QLabel(self.layoutWidget)
        self.lb_host.setObjectName("lb_host")
        self.horizontalLayout.addWidget(self.lb_host)
        self.le_host = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_host.setObjectName("le_host")
        self.horizontalLayout.addWidget(self.le_host)
        self.lb_port = QtWidgets.QLabel(self.layoutWidget)
        self.lb_port.setObjectName("lb_port")
        self.horizontalLayout.addWidget(self.lb_port)
        self.le_port = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_port.setObjectName("le_port")
        self.horizontalLayout.addWidget(self.le_port)
        self.pb_connect = QtWidgets.QPushButton(self.layoutWidget)
        self.pb_connect.setObjectName("pb_connect")
        self.horizontalLayout.addWidget(self.pb_connect)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 120, 421, 101))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lb_sendMsg1 = QtWidgets.QLabel(self.layoutWidget1)
        self.lb_sendMsg1.setObjectName("lb_sendMsg1")
        self.gridLayout.addWidget(self.lb_sendMsg1, 0, 0, 1, 1)
        self.le_sendMsg1 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.le_sendMsg1.setObjectName("le_sendMsg1")
        self.gridLayout.addWidget(self.le_sendMsg1, 0, 1, 1, 1)
        self.lb_sendMsg2 = QtWidgets.QLabel(self.layoutWidget1)
        self.lb_sendMsg2.setObjectName("lb_sendMsg2")
        self.gridLayout.addWidget(self.lb_sendMsg2, 1, 0, 1, 1)
        self.le_sendMsg2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.le_sendMsg2.setObjectName("le_sendMsg2")
        self.gridLayout.addWidget(self.le_sendMsg2, 1, 1, 1, 1)
        self.lb_sendMsg3 = QtWidgets.QLabel(self.layoutWidget1)
        self.lb_sendMsg3.setObjectName("lb_sendMsg3")
        self.gridLayout.addWidget(self.lb_sendMsg3, 2, 0, 1, 1)
        self.le_sendMsg3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.le_sendMsg3.setObjectName("le_sendMsg3")
        self.gridLayout.addWidget(self.le_sendMsg3, 2, 1, 1, 1)
        self.pb_sendMsg3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_sendMsg3.setObjectName("pb_sendMsg3")
        self.gridLayout.addWidget(self.pb_sendMsg3, 2, 2, 1, 1)
        self.pb_sendMsg1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_sendMsg1.setObjectName("pb_sendMsg1")
        self.gridLayout.addWidget(self.pb_sendMsg1, 0, 2, 1, 1)
        self.pb_sendMsg2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_sendMsg2.setObjectName("pb_sendMsg2")
        self.gridLayout.addWidget(self.pb_sendMsg2, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_host.setText(_translate("MainWindow", "主机"))
        self.le_host.setText(_translate("MainWindow", "localhost"))
        self.lb_port.setText(_translate("MainWindow", "端口"))
        self.le_port.setText(_translate("MainWindow", "10021"))
        self.pb_connect.setText(_translate("MainWindow", "连接"))
        self.lb_sendMsg1.setText(_translate("MainWindow", "发送区一"))
        self.lb_sendMsg2.setText(_translate("MainWindow", "发送区二"))
        self.lb_sendMsg3.setText(_translate("MainWindow", "发送区三"))
        self.pb_sendMsg3.setText(_translate("MainWindow", "发送"))
        self.pb_sendMsg1.setText(_translate("MainWindow", "发送"))
        self.pb_sendMsg2.setText(_translate("MainWindow", "发送"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

