# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'get_spectrogram.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(10, 10, 89, 25))
        self.btn_open.setObjectName("btn_open")
        self.label_filepath = QtWidgets.QLabel(self.centralwidget)
        self.label_filepath.setGeometry(QtCore.QRect(120, 10, 511, 17))
        self.label_filepath.setObjectName("label_filepath")
        self.label_bd = QtWidgets.QLabel(self.centralwidget)
        self.label_bd.setGeometry(QtCore.QRect(20, 50, 101, 17))
        self.label_bd.setObjectName("label_bd")
        self.label_sr = QtWidgets.QLabel(self.centralwidget)
        self.label_sr.setGeometry(QtCore.QRect(140, 50, 111, 17))
        self.label_sr.setObjectName("label_sr")
        self.label_nch = QtWidgets.QLabel(self.centralwidget)
        self.label_nch.setGeometry(QtCore.QRect(280, 50, 171, 17))
        self.label_nch.setObjectName("label_nch")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Get spectrogram"))
        self.btn_open.setText(_translate("MainWindow", "Open"))
        self.label_filepath.setText(_translate("MainWindow", "Binary filepath should be here..."))
        self.label_bd.setText(_translate("MainWindow", "bit depth: ??"))
        self.label_sr.setText(_translate("MainWindow", "sample rate: ??"))
        self.label_nch.setText(_translate("MainWindow", "number of I/Q channels: ??"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

