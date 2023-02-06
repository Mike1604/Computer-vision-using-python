
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, puntaje, nivel, sentadillas):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 400)
        MainWindow.setMinimumSize(QtCore.QSize(450, 400))
        MainWindow.setMaximumSize(QtCore.QSize(450, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/appicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setMinimumSize(QtCore.QSize(100, 100))
        self.label_39.setMaximumSize(QtCore.QSize(100, 100))
        self.label_39.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_39.setStyleSheet("image: url(:/iconos/reward.png);\n"
"border-color: rgb(255, 255, 255, 0);")
        self.label_39.setText("")
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setWordWrap(False)
        self.label_39.setObjectName("label_39")
        self.verticalLayout.addWidget(self.label_39, 0, QtCore.Qt.AlignHCenter)
        self.Titulo_label_pag2 = QtWidgets.QLabel(self.centralwidget)
        self.Titulo_label_pag2.setMinimumSize(QtCore.QSize(200, 40))
        self.Titulo_label_pag2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Titulo_label_pag2.setStyleSheet("QLabel{\n"
"    background-color: #c0527a;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #c0527a;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Titulo_label_pag2.setAlignment(QtCore.Qt.AlignCenter)
        self.Titulo_label_pag2.setWordWrap(False)
        self.Titulo_label_pag2.setObjectName("Titulo_label_pag2")
        self.verticalLayout.addWidget(self.Titulo_label_pag2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.Puntos_label_pag3 = QtWidgets.QLabel(self.centralwidget)
        self.Puntos_label_pag3.setStyleSheet("QLabel{\n"
"    font: 87 16pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"    color: #c0527a;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Puntos_label_pag3.setAlignment(QtCore.Qt.AlignCenter)
        self.Puntos_label_pag3.setWordWrap(True)
        self.Puntos_label_pag3.setObjectName("Puntos_label_pag3")
        self.verticalLayout.addWidget(self.Puntos_label_pag3)
        self.Anterior_button_pag3 = QtWidgets.QPushButton(self.centralwidget)
        self.Anterior_button_pag3.setMinimumSize(QtCore.QSize(150, 40))
        self.Anterior_button_pag3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Anterior_button_pag3.setStyleSheet("QPushButton{\n"
"    background-color: #5e17eb;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #5e17eb;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    border-radius: 10px;\n"
"\n"
"}\n"
"")
        self.Anterior_button_pag3.setObjectName("Anterior_button_pag3")
        self.verticalLayout.addWidget(self.Anterior_button_pag3, 0, QtCore.Qt.AlignRight)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        msg = '''Has obtenido {} pts  \nTe encuentras en el nivel: {}\nRealizaste {} sentadillas '''.format(puntaje,nivel,sentadillas)
        self.Puntos_label_pag3.setText(msg)
        self.Anterior_button_pag3.clicked.connect(lambda: self.cerrar(MainWindow))
   
    
   
    def cerrar(self, MainWindow):
        MainWindow.close()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Actividad Finalizada"))
        self.Titulo_label_pag2.setText(_translate("MainWindow", "¡Felicidades!"))
        self.Puntos_label_pag3.setText(_translate("MainWindow", "Has obtenido pts  \n"
"Te encuentras en el nivel:\n"
"Realizaste  sentadillas"))
        self.Anterior_button_pag3.setText(_translate("MainWindow", "Aceptar"))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

