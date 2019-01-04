# -*- coding: utf-8 -*-

"""
Module implementing socketTester.
"""
import socket
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import   QtWidgets
from Ui_socketTester import Ui_MainWindow


class socketTester(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    obj = socket.socket()
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(socketTester, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pb_connect_clicked(self):
        host = self.le_host.text()
        port = self.le_port.text()
        print("开始建立连接，主机：" + host + "，端口号：" + port)
        self.obj.connect((host,int(port)))
        result = "connect server success"
        self.te_result.setPlainText(result)
        print(result)


    @pyqtSlot()
    def on_pb_sendMsg3_clicked(self):
        send_msg = self.le_sendMsg3.text()
        print("开始发送消息：" + send_msg)
        if send_msg== "bye" :
            self.obj.close();
            sys.exit(0);
        else :
            self.obj.send(send_msg.encode())
            ret = str(self.obj.recv(1024),encoding="utf-8")
            receiveMsg = "receive msg from server:" + ret
            print(receiveMsg)
            self.te_result.setPlainText(self.te_result.toPlainText() +"\n" + receiveMsg)

    @pyqtSlot()
    def on_pb_sendMsg1_clicked(self):
        send_msg = self.le_sendMsg1.text()
        print("开始发送消息：" + send_msg)
        if send_msg== "bye" :
            self.obj.close();
            sys.exit(0);
        else :
            self.obj.send(send_msg.encode())
            ret = str(self.obj.recv(1024),encoding="utf-8")
            receiveMsg = "receive msg from server:" + ret
            print(receiveMsg)
            self.te_result.setPlainText(self.te_result.toPlainText() +"\n" + receiveMsg)

    @pyqtSlot()
    def on_pb_sendMsg2_clicked(self):
        send_msg = self.le_sendMsg2.text()
        print("开始发送消息：" + send_msg)
        if send_msg== "bye" :
            self.obj.close();
            sys.exit(0);
        else :
            self.obj.send(send_msg.encode())
            ret = str(self.obj.recv(1024),encoding="utf-8")
            receiveMsg = "receive msg from server:" + ret
            print(receiveMsg)
            self.te_result.setPlainText(self.te_result.toPlainText() +"\n" + receiveMsg)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    socketTester = socketTester()
    socketTester.show()
    sys.exit(app.exec_())
