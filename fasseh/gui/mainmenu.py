import chat, main
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
    ui2 = chat.Ui_MainWindow()
    ui2.setupUi(MainWindow2)

    #Chat_PAGE inputs and buttons
    ###########################
    ui2.pushButton_4.clicked.connect(lambda:goback(MainWindow2,MainWindow)) # back_button
    #ui2.pushButton_3.clicked.connect()                                      # send_button
    #ui2.textEdit.toPlainText()                                              # message_input
    #ui2.add_new_label(direction,mytext)                                     # use it to send your replay :: direction = 1 ,  mytext => string


    #MAIN_PAGE inputs and buttons
    ###########################
    #ui.lineEdit.text()                                                     # ip_input
    ui.pushButton.clicked.connect(lambda:gochat(MainWindow,MainWindow2))    # human_button
    ui.pushButton_2.clicked.connect(lambda:gochat(MainWindow,MainWindow2))  # machine_button
    #ui.pushButton_3.clicked.connect()                                      # ip_go_button
    #ui.radioButton.isChecked()                                                # client radio button
    #ui.radioButton_2.isChecked()                                              # server radio button
    MainWindow.show()                                                       #MAIN PAGE WINDOW
    

    sys.exit(app.exec_())

