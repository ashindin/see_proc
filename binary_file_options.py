# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 204)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_bd = QtWidgets.QLabel(self.centralwidget)
        self.label_bd.setGeometry(QtCore.QRect(10, 40, 67, 17))
        self.label_bd.setObjectName("label_bd")
        self.label_sr = QtWidgets.QLabel(self.centralwidget)
        self.label_sr.setGeometry(QtCore.QRect(10, 90, 101, 17))
        self.label_sr.setObjectName("label_sr")
        self.label_nch = QtWidgets.QLabel(self.centralwidget)
        self.label_nch.setGeometry(QtCore.QRect(10, 140, 171, 17))
        self.label_nch.setObjectName("label_nch")
        self.lineEdit_bd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_bd.setGeometry(QtCore.QRect(220, 30, 51, 25))
        self.lineEdit_bd.setObjectName("lineEdit_bd")
        self.lineEdit_bd.setText("16")
        self.lineEdit_sr = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sr.setGeometry(QtCore.QRect(190, 90, 113, 25))
        self.lineEdit_sr.setObjectName("lineEdit_sr")
        self.lineEdit_sr.setText("333333")
        self.lineEdit_nch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nch.setGeometry(QtCore.QRect(220, 140, 51, 25))
        self.lineEdit_nch.setObjectName("lineEdit_nch")
        self.lineEdit_nch.setText("1")

        self.cancel_btn = QtWidgets.QPushButton(parent=self.centralwidget, text='Cancel')
        self.cancel_btn.move(20, 175)
        self.cancel_btn.clicked.connect(self.cancel_btn_callback)

        self.apply_btn = QtWidgets.QPushButton(parent=self.centralwidget, text='Apply')
        self.apply_btn.move(200, 175)
        self.apply_btn.clicked.connect(self.apply_btn_callback)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def cancel_btn_callback(self):
        sys.exit(self.lineEdit_bd.getTe)

    def apply_btn_callback(self):
        bd = int(self.lineEdit_bd.text())
        sr = int(self.lineEdit_sr.text())
        nch = int(self.lineEdit_nch.text())
        print(bd, sr, nch)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_bd.setText(_translate("MainWindow", "bit depth:"))
        self.label_sr.setText(_translate("MainWindow", "sample rate:"))
        self.label_nch.setText(_translate("MainWindow", "number of I/Q channels:"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

