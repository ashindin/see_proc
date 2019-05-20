# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lay_plus_buttons.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
#        self.showMaximized()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_open = QtWidgets.QPushButton(self.centralwidget)
        self.Button_open.setGeometry(QtCore.QRect(10, 10, 90, 25))
        self.Button_open.setObjectName("Button_open")
        self.radio_bum = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_bum.setChecked(True)
        self.radio_bum.setGeometry(QtCore.QRect(120, 10, 61, 21))
        self.radio_bum.setObjectName("radio_bum")
        self.radio_2bum = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_2bum.setGeometry(QtCore.QRect(180, 10, 71, 21))
        self.radio_2bum.setObjectName("radio_2bum")
        self.radio_bumd = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_bumd.setGeometry(QtCore.QRect(250, 10, 71, 21))
        self.radio_bumd.setObjectName("radio_bumd")
        self.radio_dm = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_dm.setGeometry(QtCore.QRect(330, 10, 51, 21))
        self.radio_dm.setObjectName("radio_dm")
        
        self.Button_load = QtWidgets.QPushButton(self.centralwidget)
        self.Button_load.setGeometry(QtCore.QRect(450, 10, 90, 25))        
        self.Button_load.setObjectName("Button_load")
                        
        self.Text_box = QtWidgets.QLineEdit(self.centralwidget)
        self.Text_box.setGeometry(QtCore.QRect(540+20, 10, 50, 25))        
        self.Text_box.setObjectName("Text_box")
        
        self.Button_save = QtWidgets.QPushButton(self.centralwidget)
        self.Button_save.setGeometry(QtCore.QRect(630, 10, 90, 25))        
        self.Button_save.setObjectName("Button_save")
        
        
        self.radio_um = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_um.setGeometry(QtCore.QRect(390, 10, 51, 21))
        self.radio_um.setObjectName("radio_um")
        self.graphicsView_lay = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView_lay.setGeometry(QtCore.QRect(0, 40, 1920, 960))
        # ~ self.graphicsView_lay.setGeometry(QtCore.QRect(0, 40, 1280, 740))
        self.graphicsView_lay.setObjectName("graphicsView_lay")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_open.setText(_translate("MainWindow", "Open"))
        self.radio_bum.setText(_translate("MainWindow", "BUM"))
        self.radio_2bum.setText(_translate("MainWindow", "2BUM"))
        self.radio_bumd.setText(_translate("MainWindow", "BUMD"))
        self.radio_dm.setText(_translate("MainWindow", "DM"))
        self.Button_load.setText(_translate("MainWindow", "Load"))
        self.Button_save.setText(_translate("MainWindow", "Save"))
        self.radio_um.setText(_translate("MainWindow", "UM"))
        self.Text_box.setText("10")

from pyqtgraph import GraphicsLayoutWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

