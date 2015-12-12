# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat2.ui'
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
        self.centralwidget.setStyleSheet(_fromUtf8("QListWidget:item {\n"
"margin : 5;\n"
"padding:5;\n"
"border-radius:15%;\n"
"background-color:white;\n"
"padding:10;\n"
"color:#00acee;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#pushButton_2,QPushButton#pushButton{    \n"
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
"QPushButton#pushButton_4{    \n"
"border:none;\n"
"image: url(\"img/back2.png\"); \n"
"background-color: #00acee;\n"
"}\n"
"QPushButton#pushButton_4:hover{    \n"
"border:none;\n"
"image: url(\"img/back.png\"); \n"
"background-color: #00acee;\n"
"}\n"
"QPushButton#pushButton_4:pressed{    \n"
"image: url(\"img/back2.png\"); \n"
"}\n"
"\n"
"\n"
"QLineEdit#lineEdit,QTextEdit#textEdit{\n"
"background-color:#00acee;\n"
"color:#ffffff;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border: 2 solid white;\n"
"}\n"
""))
        self.centralwidget.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(690, 0, 71, 71))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("img/logo_300.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 486, 51, 41))
        self.pushButton_3.setStyleSheet(_fromUtf8(""))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.textEdit = MessageTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 460, 731, 91))
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setLineWrapMode(QtGui.QTextEdit.FixedPixelWidth)
        self.textEdit.setLineWrapColumnOrWidth(670)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 10, 31, 41))
        self.pushButton_4.setStyleSheet(_fromUtf8(""))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 70, 731, 381))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 710, 408))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))

        #type your code here#
        #self.textEdit.sendMessage.connect(lambda: self.add_new_label(0,"sd"))
        QtCore.QObject.connect(self.textEdit, QtCore.SIGNAL("sendMessage"), lambda: self.add_new_label(0,"sd"))
        #type your code here#
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Semibold"))
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet(_fromUtf8("background-color:white;\n"
"border-radius:30%;\n"
"padding:10;\n"
"color:#00acee;\n"
""))
        self.label_7.setFrameShape(QtGui.QFrame.HLine)
        self.label_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_3.addWidget(self.label_7)

        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.textEdit.raise_()
        self.label.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.verticalLayoutWidget.raise_()
        
        
        #self.pushButton_4.clicked.connect(lambda: self.add_new_label(1))
        self.pushButton_3.clicked.connect(lambda: self.add_new_label(0,"sd")) 
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
        
        self.label_7.setText(_translate("MainWindow", "hi, i'm fasse7", None))    
    def gotoback(self):
        self.label_3.setWordWrap(True);
        self.label_3.setText(self.textEdit.toPlainText())
        self.resizeEvent(self.label_3)
    def resizeEvent(self,lblx):     
        lblx.setWordWrap(True)
        text_width1 = lblx.fontMetrics().boundingRect(lblx.text()).width() + 30
        text_height = lblx.fontMetrics().boundingRect(lblx.text()).height()
        if text_width1 < 90 :
            text_width1 = text_width1 + 30
            text_height = lblx.fontMetrics().boundingRect(lblx.text()).height() +30
            lblx.setFixedHeight(text_height)
        if text_width1 > 600 :
            text_width = 600
            num_lines = text_width1/text_width
            text_width1 = text_width
            text_height = lblx.fontMetrics().boundingRect(lblx.text()).height()*(num_lines+1) +60
            lblx.setFixedHeight(text_height)
        lblx.setFixedWidth(text_width1)
        
        

    def add_new_label(self,direction,mytext):
        if self.textEdit.toPlainText()!= "" or direction == 1:
            label_5 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
            label_5.setFixedWidth(600)
            label_5.setFixedHeight(80)
            label_5.setText(self.textEdit.toPlainText())
            self.textEdit.setText("")
            sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(9)
            sizePolicy.setVerticalStretch(6)
            sizePolicy.setHeightForWidth(label_5.sizePolicy().hasHeightForWidth())
            label_5.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Open Sans Semibold"))
            font.setPointSize(16)
            label_5.setFont(font)
            if direction == 1 :
                label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
                label_5.setText(mytext)
            label_5.setAutoFillBackground(False)
            label_5.setStyleSheet(_fromUtf8("background-color:white;\n"
"border-radius:15%;\n"
"padding:10;\n"
"color:#00acee;\n"
""))
            label_5.setFrameShape(QtGui.QFrame.HLine)
            label_5.setFrameShadow(QtGui.QFrame.Sunken)
            label_5.setTextFormat(QtCore.Qt.RichText)
            label_5.setScaledContents(False)
            label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
            label_5.setObjectName(_fromUtf8("label_5"))
            self.verticalLayout_3.addWidget(label_5)
            self.resizeEvent(label_5)
            
            #self.scrollArea.verticalScrollBar().ensureVisible(0, scrollAreaHeight, 0, 0)
            scrollBar = self.scrollArea.verticalScrollBar()
            scrollBar.setValue(scrollBar.maximum())
            scrollBar.setMaximum(scrollBar.maximum() + 1000)
            xxczczx= scrollBar.value() + 1000
            scrollBar.setValue(xxczczx)
#############################################################################
class MessageTextEdit(QtGui.QTextEdit):
    def __init__(self,  parent):
        super(MessageTextEdit,  self).__init__(parent)

        self.parent = parent
        self.__sendMessageOnReturn = False

    def sendMessageOnreturn(self):
        return self.__sendMessageOnReturn

    def setSendMessageOnReturn(self,  state):
        self.__sendMessageOnReturn = state

    def keyPressEvent(self,  event):
        if event.key() == QtCore.Qt.Key_Return:
            self.emit(QtCore.SIGNAL("sendMessage"))
                
        #self.emit(QtCore.SIGNAL("sendMessage"))
        QtGui.QTextEdit.keyPressEvent(self,  event)
#################################################################################

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

