# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manage.ui'
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
        Dialog.resize(553, 262)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 220, 551, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(-6, -1, 561, 211))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(380, 20, 81, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_8 = QtGui.QLineEdit(self.tab)
        self.lineEdit_8.setGeometry(QtCore.QRect(470, 20, 61, 21))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(150, 20, 61, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(30, 80, 81, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 81, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(380, 50, 151, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.timeEdit = QtGui.QTimeEdit(self.tab)
        self.timeEdit.setGeometry(QtCore.QRect(150, 80, 61, 22))
        self.timeEdit.setTime(QtCore.QTime(3, 38, 3))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.pushButton_10 = QtGui.QPushButton(self.tab)
        self.pushButton_10.setGeometry(QtCore.QRect(30, 120, 151, 51))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_11 = QtGui.QPushButton(self.tab)
        self.pushButton_11.setGeometry(QtCore.QRect(200, 120, 161, 51))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_14 = QtGui.QPushButton(self.tab)
        self.pushButton_14.setGeometry(QtCore.QRect(380, 120, 151, 51))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.lineEdit_13 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(390, 20, 51, 21))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 90, 51, 21))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 50, 51, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(30, 50, 81, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_19 = QtGui.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(30, 120, 81, 21))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.lineEdit_11 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(120, 120, 51, 21))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_10 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(390, 120, 51, 21))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_12 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(390, 50, 51, 21))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.label_18 = QtGui.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(300, 120, 81, 21))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_20 = QtGui.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(300, 20, 81, 21))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_17 = QtGui.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(300, 90, 81, 21))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(30, 90, 81, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_9 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(390, 90, 51, 21))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 20, 51, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_21 = QtGui.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(300, 50, 81, 21))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(30, 20, 81, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 20, 71, 25))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 50, 71, 25))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 90, 71, 25))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 120, 71, 25))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 20, 71, 25))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(460, 50, 71, 25))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(460, 90, 71, 25))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(460, 120, 71, 25))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_10 = QtGui.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 57, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_6 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(380, 20, 51, 21))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_5 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 20, 51, 21))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_14 = QtGui.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(286, 20, 71, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.pushButton_12 = QtGui.QPushButton(self.tab_3)
        self.pushButton_12.setGeometry(QtCore.QRect(180, 20, 71, 25))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_13 = QtGui.QPushButton(self.tab_3)
        self.pushButton_13.setGeometry(QtCore.QRect(450, 20, 71, 25))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.buttonBox.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Manage", None))
        self.label_7.setText(_translate("Dialog", "Next Stage", None))
        self.lineEdit_8.setText(_translate("Dialog", "Stage 3", None))
        self.lineEdit.setText(_translate("Dialog", "Stage 2", None))
        self.label_6.setText(_translate("Dialog", "Remainign", None))
        self.label_5.setText(_translate("Dialog", "Actual Stage", None))
        self.pushButton.setText(_translate("Dialog", "Force Next", None))
        self.pushButton_10.setText(_translate("Dialog", "Pause", None))
        self.pushButton_11.setText(_translate("Dialog", "Restart Stage", None))
        self.pushButton_14.setText(_translate("Dialog", "Force End", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Stage", None))
        self.lineEdit_13.setText(_translate("Dialog", "Closed", None))
        self.lineEdit_4.setText(_translate("Dialog", "Open", None))
        self.lineEdit_3.setText(_translate("Dialog", "Closed", None))
        self.label_12.setText(_translate("Dialog", "Water out", None))
        self.label_19.setText(_translate("Dialog", "Hop in", None))
        self.lineEdit_11.setText(_translate("Dialog", "Closed", None))
        self.lineEdit_10.setText(_translate("Dialog", "Closed", None))
        self.lineEdit_12.setText(_translate("Dialog", "Closed", None))
        self.label_18.setText(_translate("Dialog", "Beer out", None))
        self.label_20.setText(_translate("Dialog", "Hatch", None))
        self.label_17.setText(_translate("Dialog", "Must out", None))
        self.label_13.setText(_translate("Dialog", "Malt in", None))
        self.lineEdit_9.setText(_translate("Dialog", "Closed", None))
        self.lineEdit_2.setText(_translate("Dialog", "Closed", None))
        self.label_21.setText(_translate("Dialog", "Pressure out", None))
        self.label_11.setText(_translate("Dialog", "Water in", None))
        self.pushButton_2.setText(_translate("Dialog", "Toggle", None))
        self.pushButton_3.setText(_translate("Dialog", "Toggle", None))
        self.pushButton_4.setText(_translate("Dialog", "Toggle", None))
        self.pushButton_5.setText(_translate("Dialog", "Toggle", None))
        self.pushButton_6.setText(_translate("Dialog", "Toggle", None))
        self.pushButton_7.setText(_translate("Dialog", "Toggle", None))
        self.pushButton_8.setText(_translate("Dialog", "Toggle", None))
        self.pushButton_9.setText(_translate("Dialog", "Toggle", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Valves", None))
        self.label_10.setText(_translate("Dialog", "Burner", None))
        self.lineEdit_6.setText(_translate("Dialog", "On", None))
        self.lineEdit_5.setText(_translate("Dialog", "Off", None))
        self.label_14.setText(_translate("Dialog", "Mixer", None))
        self.pushButton_12.setText(_translate("Dialog", "Toggle", None))
        self.pushButton_13.setText(_translate("Dialog", "Toggle", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Devices", None))

