# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Setup.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(601, 427)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(510, 10, 81, 461))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.toolBox = QtGui.QToolBox(Dialog)
        self.toolBox.setGeometry(QtCore.QRect(20, 30, 471, 381))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.label_7 = QtGui.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 141, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.timeEdit_7 = QtGui.QTimeEdit(self.page_3)
        self.timeEdit_7.setGeometry(QtCore.QRect(170, 10, 111, 22))
        self.timeEdit_7.setObjectName(_fromUtf8("timeEdit_7"))
        self.label_8 = QtGui.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(20, 40, 141, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.page_3)
        self.doubleSpinBox.setGeometry(QtCore.QRect(170, 40, 111, 22))
        self.doubleSpinBox.setProperty("value", 22.0)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.label_9 = QtGui.QLabel(self.page_3)
        self.label_9.setGeometry(QtCore.QRect(300, 40, 31, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.toolBox.addItem(self.page_3, _fromUtf8(""))
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.label_6 = QtGui.QLabel(self.page_5)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 141, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.timeEdit_6 = QtGui.QTimeEdit(self.page_5)
        self.timeEdit_6.setGeometry(QtCore.QRect(170, 10, 111, 22))
        self.timeEdit_6.setObjectName(_fromUtf8("timeEdit_6"))
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.page_5)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(170, 40, 111, 22))
        self.doubleSpinBox_2.setProperty("value", 22.0)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.label_10 = QtGui.QLabel(self.page_5)
        self.label_10.setGeometry(QtCore.QRect(20, 40, 141, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.page_5)
        self.label_11.setGeometry(QtCore.QRect(300, 40, 31, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.toolBox.addItem(self.page_5, _fromUtf8(""))
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.label_5 = QtGui.QLabel(self.page_6)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 141, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.timeEdit_5 = QtGui.QTimeEdit(self.page_6)
        self.timeEdit_5.setGeometry(QtCore.QRect(170, 20, 111, 22))
        self.timeEdit_5.setObjectName(_fromUtf8("timeEdit_5"))
        self.label_13 = QtGui.QLabel(self.page_6)
        self.label_13.setGeometry(QtCore.QRect(300, 50, 31, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.page_6)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(170, 50, 111, 22))
        self.doubleSpinBox_3.setProperty("value", 22.0)
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.label_12 = QtGui.QLabel(self.page_6)
        self.label_12.setGeometry(QtCore.QRect(20, 50, 141, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_5.raise_()
        self.timeEdit_5.raise_()
        self.label_13.raise_()
        self.label_12.raise_()
        self.doubleSpinBox_3.raise_()
        self.label_13.raise_()
        self.doubleSpinBox_3.raise_()
        self.label_12.raise_()
        self.toolBox.addItem(self.page_6, _fromUtf8(""))
        self.page_7 = QtGui.QWidget()
        self.page_7.setObjectName(_fromUtf8("page_7"))
        self.label_4 = QtGui.QLabel(self.page_7)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 141, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.timeEdit_4 = QtGui.QTimeEdit(self.page_7)
        self.timeEdit_4.setGeometry(QtCore.QRect(170, 10, 111, 22))
        self.timeEdit_4.setObjectName(_fromUtf8("timeEdit_4"))
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.page_7)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(170, 40, 111, 22))
        self.doubleSpinBox_4.setProperty("value", 22.0)
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))
        self.label_14 = QtGui.QLabel(self.page_7)
        self.label_14.setGeometry(QtCore.QRect(20, 40, 141, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.page_7)
        self.label_15.setGeometry(QtCore.QRect(300, 40, 31, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.toolBox.addItem(self.page_7, _fromUtf8(""))
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.label_3 = QtGui.QLabel(self.page_4)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 141, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.timeEdit_3 = QtGui.QTimeEdit(self.page_4)
        self.timeEdit_3.setGeometry(QtCore.QRect(170, 10, 111, 22))
        self.timeEdit_3.setObjectName(_fromUtf8("timeEdit_3"))
        self.doubleSpinBox_5 = QtGui.QDoubleSpinBox(self.page_4)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(170, 40, 111, 22))
        self.doubleSpinBox_5.setProperty("value", 22.0)
        self.doubleSpinBox_5.setObjectName(_fromUtf8("doubleSpinBox_5"))
        self.label_16 = QtGui.QLabel(self.page_4)
        self.label_16.setGeometry(QtCore.QRect(20, 40, 141, 21))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.page_4)
        self.label_17.setGeometry(QtCore.QRect(300, 40, 31, 21))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.toolBox.addItem(self.page_4, _fromUtf8(""))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 471, 178))
        self.page.setObjectName(_fromUtf8("page"))
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 141, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.timeEdit_2 = QtGui.QTimeEdit(self.page)
        self.timeEdit_2.setGeometry(QtCore.QRect(180, 10, 111, 22))
        self.timeEdit_2.setObjectName(_fromUtf8("timeEdit_2"))
        self.doubleSpinBox_6 = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_6.setGeometry(QtCore.QRect(180, 40, 111, 22))
        self.doubleSpinBox_6.setProperty("value", 22.0)
        self.doubleSpinBox_6.setObjectName(_fromUtf8("doubleSpinBox_6"))
        self.label_18 = QtGui.QLabel(self.page)
        self.label_18.setGeometry(QtCore.QRect(30, 40, 141, 21))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.page)
        self.label_19.setGeometry(QtCore.QRect(310, 40, 31, 21))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 471, 178))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.label = QtGui.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.timeEdit = QtGui.QTimeEdit(self.page_2)
        self.timeEdit.setGeometry(QtCore.QRect(170, 10, 111, 22))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.doubleSpinBox_7 = QtGui.QDoubleSpinBox(self.page_2)
        self.doubleSpinBox_7.setGeometry(QtCore.QRect(170, 40, 111, 22))
        self.doubleSpinBox_7.setProperty("value", 22.0)
        self.doubleSpinBox_7.setObjectName(_fromUtf8("doubleSpinBox_7"))
        self.label_20 = QtGui.QLabel(self.page_2)
        self.label_20.setGeometry(QtCore.QRect(20, 40, 141, 21))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.page_2)
        self.label_21.setGeometry(QtCore.QRect(300, 40, 31, 21))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.toolBox.addItem(self.page_2, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.toolBox.setCurrentIndex(6)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "SetUp", None))
        self.label_7.setText(_translate("Dialog", "Stage Duration", None))
        self.label_8.setText(_translate("Dialog", "Stage Temperature", None))
        self.label_9.setText(_translate("Dialog", "ºC", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Dialog", "Stage 1", None))
        self.label_6.setText(_translate("Dialog", "Stage Duration", None))
        self.label_10.setText(_translate("Dialog", "Stage Temperature", None))
        self.label_11.setText(_translate("Dialog", "ºC", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("Dialog", "Stage 2", None))
        self.label_5.setText(_translate("Dialog", "Stage Duration", None))
        self.label_13.setText(_translate("Dialog", "ºC", None))
        self.label_12.setText(_translate("Dialog", "Stage Temperature", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), _translate("Dialog", "Stage 3", None))
        self.label_4.setText(_translate("Dialog", "Stage Duration", None))
        self.label_14.setText(_translate("Dialog", "Stage Temperature", None))
        self.label_15.setText(_translate("Dialog", "ºC", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), _translate("Dialog", "Stage 4", None))
        self.label_3.setText(_translate("Dialog", "Stage Duration", None))
        self.label_16.setText(_translate("Dialog", "Stage Temperature", None))
        self.label_17.setText(_translate("Dialog", "ºC", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("Dialog", "Stage 5", None))
        self.label_2.setText(_translate("Dialog", "Stage Duration", None))
        self.label_18.setText(_translate("Dialog", "Stage Temperature", None))
        self.label_19.setText(_translate("Dialog", "ºC", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Dialog", "Stage 6", None))
        self.label.setText(_translate("Dialog", "Stage Duration", None))
        self.label_20.setText(_translate("Dialog", "Stage Temperature", None))
        self.label_21.setText(_translate("Dialog", "ºC", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Dialog", "Stage 7", None))

