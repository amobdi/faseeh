import chat2, main
from PyQt4 import QtGui, QtCore


def gochat(MainWindow, MainWindow2):
        MainWindow2.show()
        MainWindow.hide()
def goback(MainWindow, MainWindow2):
        MainWindow2.show()
        MainWindow.close()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = main.Ui_MainWindow()
    ui.setupUi(MainWindow)


    MainWindow2 = QtGui.QMainWindow()
    ui2 = chat2.Ui_MainWindow()
    ui2.setupUi(MainWindow2)

    ui2.pushButton_4.clicked.connect(lambda:goback(MainWindow2,MainWindow))

    ui.pushButton.clicked.connect(lambda:gochat(MainWindow,MainWindow2))
    ui.pushButton_2.clicked.connect(lambda:gochat(MainWindow,MainWindow2))
    MainWindow.show()
    

    sys.exit(app.exec_())

