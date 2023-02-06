# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
from MenuPrincipal import Ui_MenuPrincipal

class Ui_LogIn(object):
    def setupUi(self, LogIn, cursor):
        LogIn.setObjectName("LogIn")
        LogIn.resize(1498, 944)
        self.centralwidget = QtWidgets.QWidget(LogIn)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pagina1 = QtWidgets.QWidget()
        self.pagina1.setObjectName("pagina1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pagina1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.pagina1)
        self.frame_2.setStyleSheet("background-color: rgb(34, 32, 32);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setMinimumSize(QtCore.QSize(200, 200))
        self.label_15.setStyleSheet("image: url(:/Menu/infoUser (2).png);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.label_18 = QtWidgets.QLabel(self.frame_2)
        self.label_18.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"    color: whitesmoke;")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.label_18)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"    color: whitesmoke;")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(300, 40))
        self.lineEdit_4.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"    color: whitesmoke;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_3.addWidget(self.lineEdit_4, 0, QtCore.Qt.AlignHCenter)
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"    color: whitesmoke;")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(300, 40))
        self.lineEdit_8.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.lineEdit_8.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_8.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"    color: whitesmoke;")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_3.addWidget(self.lineEdit_8, 0, QtCore.Qt.AlignHCenter)
        self.Desafios_button_Pag1_3 = QtWidgets.QPushButton(self.frame_2)
        self.Desafios_button_Pag1_3.setMinimumSize(QtCore.QSize(250, 70))
        self.Desafios_button_Pag1_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Desafios_button_Pag1_3.setStyleSheet("QPushButton{\n"
"    background-color: #c0527a;\n"
"    font: 87 14pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 15px;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #c0527a;\n"
"    font: 87 14pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"")
        self.Desafios_button_Pag1_3.setObjectName("Desafios_button_Pag1_3")
        self.verticalLayout_3.addWidget(self.Desafios_button_Pag1_3, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"    color: whitesmoke;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(250, 70))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: #c0527a;\n"
"    font: 87 14pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 15px;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #c0527a;\n"
"    font: 87 14pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 122, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.pagina1)
        self.pagina2 = QtWidgets.QWidget()
        self.pagina2.setObjectName("pagina2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pagina2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(self.pagina2)
        self.frame.setStyleSheet("background-color: rgb(34, 32, 32);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 50)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_19 = QtWidgets.QLabel(self.frame_3)
        self.label_19.setStyleSheet("image: url(:/Menu/infoUser (1).png);")
        self.label_19.setText("")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_6.addWidget(self.label_19)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setStyleSheet("background-color: rgb(34, 32, 32);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout.setContentsMargins(500, 0, 0, 50)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(241, 40))
        self.lineEdit_5.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(240, 40))
        self.lineEdit_9.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_20 = QtWidgets.QLabel(self.frame_6)
        self.label_20.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(241, 40))
        self.lineEdit_10.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.lineEdit_10.setText("")
        self.lineEdit_10.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 8, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(241, 40))
        self.lineEdit_6.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setStyleSheet("background-color: rgb(34, 32, 32);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_2.setContentsMargins(0, 0, 500, 50)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit.setMinimumSize(QtCore.QSize(241, 40))
        self.lineEdit.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_2.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.gridLayout_2.addWidget(self.frame_7, 5, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setMinimumSize(QtCore.QSize(50, 50))
        self.label_7.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.spinBox = QtWidgets.QSpinBox(self.frame_5)
        self.spinBox.setMinimumSize(QtCore.QSize(240, 0))
        self.spinBox.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 3, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.Desafios_button_Pag1_4 = QtWidgets.QPushButton(self.frame)
        self.Desafios_button_Pag1_4.setMinimumSize(QtCore.QSize(250, 70))
        self.Desafios_button_Pag1_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Desafios_button_Pag1_4.setStyleSheet("QPushButton{\n"
"    background-color: #c0527a;\n"
"    font: 87 14pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 15px;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #c0527a;\n"
"    font: 87 14pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.Desafios_button_Pag1_4.setObjectName("Desafios_button_Pag1_4")
        self.verticalLayout_7.addWidget(self.Desafios_button_Pag1_4, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(250, 70))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: #c0527a;\n"
"    font: 87 14pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 15px;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #c0527a;\n"
"    font: 87 14pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_7.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addWidget(self.frame)
        self.stackedWidget.addWidget(self.pagina2)
        self.verticalLayout_8.addWidget(self.stackedWidget)
        LogIn.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogIn)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LogIn)
        
        """
        Aqui inician las instrucciones a las funciones:
        """
        #Botones registrar e iniciar paginas
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina2))
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina1))
        
        #Botones iniciar y registrar
        self.Desafios_button_Pag1_3.clicked.connect(lambda: self.iniciarSesion(cursor, LogIn))
        self.Desafios_button_Pag1_4.clicked.connect(lambda: self.registrarse(cursor, LogIn))
        
        
        """
        Aqui inician las funciones:
    
        """
        
    def iniciarSesion(self, cursor, LogIn):
        user = self.lineEdit_4.text()
        passw = self.lineEdit_8.text()
        
        sql='''select *from jugador where nombre_usuario='{}' '''.format(user)
        cursor.execute(sql)
        row=cursor.fetchall()
        print(row)
        if len(row)==0:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Sin coincidencia")
            msg.setText("No hay ningun usuario registrado con ese nombre")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            
            x = msg.exec_()
        else:
            for rows in row: 
                if str(rows[9])!=passw:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Contraseña Incorrecta")
                    msg.setText("La contraseña no coincide con el usuario")
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    
                    x = msg.exec_()
                else:
                    id=rows[0]
                    print(id)
                    #Conecto al usuario
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Ui_MenuPrincipal()
                    self.ui.setupUi(self.window,cursor,id,LogIn)
                    LogIn.close()
                    self.lineEdit_4.setText("")
                    self.lineEdit_8.setText("")
                    self.window.show()
                    
    def registrarse(self, cursor, LogIn):
        sex=""
        name = self.lineEdit_5.text()
        username = self.lineEdit.text()
        altura = self.lineEdit_9.text()
        peso = self.lineEdit_6.text()
        passw = self.lineEdit_10.text()
        edad = self.spinBox.text()
        SQL='''select *from jugador where nombre_usuario='{}' '''.format(username)
        cursor.execute(SQL)
        row=cursor.fetchall()
        if self.radioButton.isChecked():
            sex = self.radioButton.text()
        elif self.radioButton_2.isChecked():
            sex = self.radioButton_2.text()     
        if len(name)==0:
            self.msgError("Campo incompleto","Debes ingresar un nombre valido y no dejarlo vacio")
        elif len(username)==0:
            self.msgError("Campo incompleto","Debes ingresar un nombre de usuario valido y no dejarlo vacio")
        elif len(row)!=0:
            self.msgError("Username ya registrado","Ya existe un usuario registrado con dicho nombre, por favor ingresa otro")
        elif (len(altura)==0) or (float(altura)<=1.0) or (float(altura)>=2.5):
            self.msgError("Campo incompleto","Debes ingresar una altura valida en formato (1.50) y no dejarlo vacio")
        elif (len(peso)==0):
            self.msgError("Campo incompleto","Debes ingresar tu peso correctamente y no dejarlo vacio")
        elif (len(passw)==0) or (len(passw)<8):
            self.msgError("Campo incompleto","Debes ingresar una contraseña y esta debe tener al menos 8 caracteres")
        elif (len(edad)==0) or (int(edad)<8):
            self.msgError("Campo incompleto","Para poder jugar necesitas ser mayor de 8 años")
        elif len(sex)==0:
            self.msgError("Campo incompleto","Debes ingresar tu sexo para continuar")
        else:
            alt=float(altura)
            pes=float(peso) 
            IMC = pes / (alt**2)
            
            if IMC<18.5:
                IMCS= str(self.truncate(IMC),2)+" Bajo peso"
            elif (IMC<=24.9) and (IMC>=18.5):
                IMCS= str(self.truncate(IMC,2))+" Peso saludable"
            elif (IMC<=29.9) and (IMC>=25):
                IMCS= str(self.truncate(IMC,2))+" Sobrepeso"  
            elif (IMC>30):
                IMCS= str(self.truncate(IMC,2))++" Obesidad" 
            SQL='''insert into jugador(nombre, nombre_usuario, edad, sexo, altura, puntaje_total, peso, nivel, contraseña, IMC) values
            ('{}','{}',{},'{}',{},0,{},0,'{}','{}') '''.format(name, username, edad, sex, altura, peso, passw, IMCS)
            
            print(SQL)
            
            try:
                cursor.execute(SQL)     
                cursor.connection.commit()
            except Exception as ex:
                self.msgError("Error a la hora de registrar", ex)
            
            self.lineEdit_5.clear()
            self.lineEdit.clear()
            self.lineEdit_9.clear()
            self.lineEdit_6.clear()
            self.lineEdit_10.clear()
            self.spinBox.clear()
            self.stackedWidget.setCurrentWidget(self.pagina1)
            
            #Conecto al usuario
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MenuPrincipal()
            self.ui.setupUi(self.window,cursor,id,LogIn)
            LogIn.close()
            self.window.show()
            
                            
    def msgError(self,msg1,msg2):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(msg1)
        msg.setText(msg2)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        
        x = msg.exec_()
        
    def truncate(self, number: float, max_decimals: int) -> float:
        int_part, dec_part = str(number).split(".")
        return float(".".join((int_part, dec_part[:max_decimals])))
           
    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "MainWindow"))
        self.label_18.setText(_translate("LogIn", "¡Bienvenido a EasyFit! \n"
"Ingresa tus datos para iniciar."))
        self.label_16.setText(_translate("LogIn", "Usuario:"))
        self.label_17.setText(_translate("LogIn", "Contraseña:"))
        self.Desafios_button_Pag1_3.setText(_translate("LogIn", "Iniciar Sesion"))
        self.label.setText(_translate("LogIn", "¿No tienes cuenta aun? \n"
"¡Registrate!"))
        self.pushButton.setText(_translate("LogIn", "Registrarse"))
        self.label_5.setText(_translate("LogIn", "¡Bienvenido!\n"
"Ingresa tus datos para registrarte."))
        self.label_6.setText(_translate("LogIn", "Nombre:"))
        self.label_9.setText(_translate("LogIn", "Altura:"))
        self.label_10.setText(_translate("LogIn", "Peso:"))
        self.label_20.setText(_translate("LogIn", "Password:"))
        self.label_2.setText(_translate("LogIn", "Nombre de usuario:"))
        self.radioButton.setText(_translate("LogIn", "Hombre"))
        self.radioButton_2.setText(_translate("LogIn", "Mujer"))
        self.label_7.setText(_translate("LogIn", "Sexo:"))
        self.label_8.setText(_translate("LogIn", "Edad:"))
        self.Desafios_button_Pag1_4.setText(_translate("LogIn", "Registrar"))
        self.pushButton_2.setText(_translate("LogIn", "O Iniciar Sesion"))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QMainWindow()
    ui = Ui_LogIn()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())

