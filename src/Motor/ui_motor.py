# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_motor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushbutton_connect = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_connect.setObjectName("pushbutton_connect")
        self.horizontalLayout.addWidget(self.pushbutton_connect)
        self.pushbutton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_close.setObjectName("pushbutton_close")
        self.horizontalLayout.addWidget(self.pushbutton_close)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.dblspinbox_set_pos = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dblspinbox_set_pos.setPrefix("")
        self.dblspinbox_set_pos.setMinimum(-180.0)
        self.dblspinbox_set_pos.setMaximum(180.0)
        self.dblspinbox_set_pos.setObjectName("dblspinbox_set_pos")
        self.horizontalLayout_2.addWidget(self.dblspinbox_set_pos)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_current_pos = QtWidgets.QLabel(self.centralwidget)
        self.label_current_pos.setObjectName("label_current_pos")
        self.horizontalLayout_3.addWidget(self.label_current_pos)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dxl Motor"))
        self.pushbutton_connect.setText(_translate("MainWindow", "Connect"))
        self.pushbutton_close.setText(_translate("MainWindow", "Close"))
        self.label.setText(_translate("MainWindow", "Set Position"))
        self.label_current_pos.setText(_translate("MainWindow", "Current Position"))