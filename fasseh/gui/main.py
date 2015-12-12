# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(798, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Myriad Pro"))
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/LOGO.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("background-color: #00aced;\n"
"\n"
""))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.centralwidget.setFont(font)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(_fromUtf8("QPushButton#pushButton_2,QPushButton#pushButton{    \n"
"color:#ffffff;\n"
"border-radius: 10;\n"
"background-color:#00acee;\n"
"border: 3px solid #ffffff;\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover,QPushButton#pushButton:hover {    \n"
"border-radius:15;\n"
"color:#00acee;\n"
"background-color:#ffffff;\n"
"}\n"
"QPushButton#pushButton_2:pressed,QPushButton#pushButton:pressed {    \n"
"color:#ffffff;\n"
"background-color:#00acee;\n"
"\n"
"}\n"
"QPushButton#pushButton_3{    \n"
"border:none;\n"
"image: url(\"img/go2.png\"); \n"
"background-color: #00acee;\n"
"}\n"
"QPushButton#pushButton_3:hover{    \n"
"border:none;\n"
"image: url(\"img/go.png\"); \n"
"background-color: #00acee;\n"
"}\n"
"QPushButton#pushButton_3:pressed{    \n"
"image: url(\"img/go2.png\"); \n"
"}\n"
"\n"
"\n"
"QLineEdit#lineEdit{\n"
"background-color:#00acee;\n"
"color:#ffffff;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border: 2 solid white;\n"
"}\n"
""))
        self.centralwidget.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 30, 281, 311))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("img/logo_300.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 420, 181, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Myriad Pro"))
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(64, 64))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 420, 181, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Myriad Pro"))
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8(""))
        self.pushButton_2.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 340, 91, 51))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(510, 500, 251, 51))
        self.lineEdit.setMaxLength(15)
        self.lineEdit.setFrame(False)
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(729, 516, 21, 21))
        self.pushButton_3.setStyleSheet(_fromUtf8(""))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(520, 560, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(650, 560, 82, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))     
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Fasseh", None))
        self.pushButton.setText(_translate("MainWindow", "Human", None))
        self.pushButton_2.setText(_translate("MainWindow", "Machine", None))
        self.radioButton.setText(_translate("MainWindow", "Client", None))
        self.radioButton_2.setText(_translate("MainWindow", "Server", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Please, Enter the machine IP ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

