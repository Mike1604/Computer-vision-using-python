from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Puntaje import Ui_MainWindow
import cv2
import mediapipe as mp
import numpy as np
from math import acos, degrees


class Ui_MenuPrincipal(object):
    pts=0
    activate=False
    indexDes=0 
    puntajetotal=0
    nivel=0
    count=0
    def setupUi(self, MenuPrincipal, cursor, id, Login):
        MenuPrincipal.setObjectName("MenuPrincipal")
        MenuPrincipal.resize(1492, 810)
        MenuPrincipal.setMinimumSize(QtCore.QSize(0, 40))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/appicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MenuPrincipal.setWindowIcon(icon)
        MenuPrincipal.setLayoutDirection(QtCore.Qt.LeftToRight)
        MenuPrincipal.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MenuPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_navbar = QtWidgets.QFrame(self.centralwidget)
        self.frame_navbar.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_navbar.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_navbar.setStyleSheet("background-color: rgb(34, 32, 32);")
        self.frame_navbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_navbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_navbar.setObjectName("frame_navbar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_navbar)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MenuButton = QtWidgets.QPushButton(self.frame_navbar)
        self.MenuButton.setMinimumSize(QtCore.QSize(70, 70))
        self.MenuButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.MenuButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MenuButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.MenuButton.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"    \n"
"    image: url(:/iconos/menuicon.png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"    image: url(:/iconos/menuicon2.png);\n"
"}\n"
"\n"
"")
        self.MenuButton.setText("")
        self.MenuButton.setIconSize(QtCore.QSize(35, 35))
        self.MenuButton.setObjectName("MenuButton")
        self.horizontalLayout_2.addWidget(self.MenuButton)
        spacerItem = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Logo = QtWidgets.QLabel(self.frame_navbar)
        self.Logo.setMinimumSize(QtCore.QSize(70, 50))
        self.Logo.setStyleSheet("image: url(:/icon/appicon.ico);")
        self.Logo.setObjectName("Logo")
        self.horizontalLayout_2.addWidget(self.Logo)
        spacerItem1 = QtWidgets.QSpacerItem(239, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.Username = QtWidgets.QLineEdit(self.frame_navbar)
        self.Username.setMinimumSize(QtCore.QSize(110, 25))
        self.Username.setMaximumSize(QtCore.QSize(150, 25))
        self.Username.setStyleSheet("QLineEdit{\n"
"    background-color: #d9d9d9;\n"
"    border-radius: 10px;\n"
"    color: black;\n"
"}")
        self.Username.setAlignment(QtCore.Qt.AlignCenter)
        self.Username.setReadOnly(True)
        self.Username.setObjectName("Username")
        self.horizontalLayout_2.addWidget(self.Username)
        self.profile_picture_button = QtWidgets.QPushButton(self.frame_navbar)
        self.profile_picture_button.setMinimumSize(QtCore.QSize(70, 65))
        self.profile_picture_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profile_picture_button.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"    image: url(:/user/usericon.png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"    \n"
"    \n"
"    image: url(:/iconos/user.png);\n"
"}\n"
"\n"
"")
        self.profile_picture_button.setText("")
        self.profile_picture_button.setObjectName("profile_picture_button")
        self.horizontalLayout_2.addWidget(self.profile_picture_button)
        self.verticalLayout.addWidget(self.frame_navbar)
        self.frame_contenido = QtWidgets.QFrame(self.centralwidget)
        self.frame_contenido.setEnabled(True)
        self.frame_contenido.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"")
        self.frame_contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contenido.setLineWidth(1)
        self.frame_contenido.setObjectName("frame_contenido")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_contenido)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_menu_desplegable = QtWidgets.QFrame(self.frame_contenido)
        self.frame_menu_desplegable.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_menu_desplegable.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_menu_desplegable.setStyleSheet("QFrame{\n"
"    background-color: rgb(34, 32, 32);\n"
"}\n"
"")
        self.frame_menu_desplegable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu_desplegable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu_desplegable.setObjectName("frame_menu_desplegable")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_menu_desplegable)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(40)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_menu_desplegable)
        self.pushButton_3.setMinimumSize(QtCore.QSize(70, 65))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(34, 32, 32);\n"
"    border: 0px;\n"
"    image: url(:/iconos/home2.png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(34, 32, 32);\n"
"    border: 10px;\n"
"    \n"
"    image: url(:/iconos/home.png);\n"
"}\n"
"\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_menu_desplegable)
        self.pushButton_4.setMinimumSize(QtCore.QSize(70, 65))
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(34, 32, 32);\n"
"    border: 0px;\n"
"    \n"
"    image: url(:/Menu/training2.png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(34, 32, 32);\n"
"    border: 10px;\n"
"    \n"
"    image: url(:/Menu/training.png);\n"
"}\n"
"\n"
"")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_menu_desplegable)
        self.pushButton_5.setMinimumSize(QtCore.QSize(70, 65))
        self.pushButton_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(34, 32, 32);\n"
"    border: 0px;\n"
"    \n"
"    image: url(:/Menu/desafio2.png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(34, 32, 32);\n"
"    border: 10px;\n"
"    \n"
"    image: url(:/Menu/desafio.png);\n"
"}\n"
"\n"
"")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_menu_desplegable)
        self.pushButton_6.setMinimumSize(QtCore.QSize(70, 65))
        self.pushButton_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(34, 32, 32);\n"
"    border: 0px;\n"
"    \n"
"    image: url(:/Menu/Posiciones (1).png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(34, 32, 32);\n"
"    border: 10px;\n"
"    image: url(:/Menu/Posiciones (2).png);\n"
"}\n"
"\n"
"")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_menu_desplegable)
        self.pushButton_8.setMinimumSize(QtCore.QSize(70, 65))
        self.pushButton_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(34, 32, 32);\n"
"    border: 0px;\n"
"    \n"
"    image: url(:/Menu/infoUser (2).png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(34, 32, 32);\n"
"    border: 10px;\n"
"    \n"
"    image: url(:/Menu/infoUser (1).png);\n"
"}\n"
"\n"
"")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_menu_desplegable)
        self.pushButton_9.setMinimumSize(QtCore.QSize(70, 65))
        self.pushButton_9.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(34, 32, 32);\n"
"    border: 0px;\n"
"    image: url(:/Menu/CerrarSesion2.png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(34, 32, 32);\n"
"    border: 10px;\n"
"    \n"
"    image: url(:/Menu/CerrarSesion.png);\n"
"}\n"
"\n"
"")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_3.addWidget(self.pushButton_9)
        spacerItem3 = QtWidgets.QSpacerItem(20, 44, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(self.frame_menu_desplegable)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setStyleSheet("QLabel{\n"
"    font: 87 8pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"    color: rgb(187, 96, 111);\n"
"    font: 87 10pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame_menu_desplegable)
        self.frame_contenedor = QtWidgets.QFrame(self.frame_contenido)
        self.frame_contenedor.setEnabled(True)
        font = QtGui.QFont()
        font.setItalic(False)
        self.frame_contenedor.setFont(font)
        self.frame_contenedor.setAutoFillBackground(False)
        self.frame_contenedor.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.frame_contenedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contenedor.setObjectName("frame_contenedor")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_tipo_app = QtWidgets.QFrame(self.frame_contenedor)
        self.frame_tipo_app.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_tipo_app.setStyleSheet("background-color: rgb(184, 161, 222);")
        self.frame_tipo_app.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tipo_app.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tipo_app.setObjectName("frame_tipo_app")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_tipo_app)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_tipo_app = QtWidgets.QLabel(self.frame_tipo_app)
        self.label_tipo_app.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_tipo_app.setFont(font)
        self.label_tipo_app.setStyleSheet("font: 75 12pt \"Verdana\";\n"
"color: whitesmoke;")
        self.label_tipo_app.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tipo_app.setObjectName("label_tipo_app")
        self.gridLayout.addWidget(self.label_tipo_app, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_tipo_app)
        self.contenedor_paginas = QtWidgets.QFrame(self.frame_contenedor)
        self.contenedor_paginas.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.contenedor_paginas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contenedor_paginas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contenedor_paginas.setObjectName("contenedor_paginas")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.contenedor_paginas)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.contenedor_paginas)
        self.stackedWidget.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.pagina_uno = QtWidgets.QWidget()
        self.pagina_uno.setObjectName("pagina_uno")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pagina_uno)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_content_inicio = QtWidgets.QFrame(self.pagina_uno)
        self.frame_content_inicio.setStyleSheet("background-color: rgb(1, 1, 1);")
        self.frame_content_inicio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content_inicio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_inicio.setObjectName("frame_content_inicio")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_content_inicio)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.frame_content_inicio)
        self.frame.setStyleSheet("background-color: rgb(96, 171, 202);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.Entrenamiento_button_Pag1 = QtWidgets.QPushButton(self.frame)
        self.Entrenamiento_button_Pag1.setMinimumSize(QtCore.QSize(250, 70))
        self.Entrenamiento_button_Pag1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Entrenamiento_button_Pag1.setStyleSheet("QPushButton{\n"
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
        self.Entrenamiento_button_Pag1.setObjectName("Entrenamiento_button_Pag1")
        self.verticalLayout_6.addWidget(self.Entrenamiento_button_Pag1, 0, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 11, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(70, 400))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setStyleSheet("image: url(:/iconos/ejercitandose.png);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem6)
        self.horizontalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.frame_content_inicio)
        self.frame_2.setStyleSheet("background-color: rgb(67, 143, 177);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem7)
        self.Desafios_button_Pag1 = QtWidgets.QPushButton(self.frame_2)
        self.Desafios_button_Pag1.setMinimumSize(QtCore.QSize(250, 70))
        self.Desafios_button_Pag1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Desafios_button_Pag1.setStyleSheet("QPushButton{\n"
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
        self.Desafios_button_Pag1.setObjectName("Desafios_button_Pag1")
        self.verticalLayout_7.addWidget(self.Desafios_button_Pag1, 0, QtCore.Qt.AlignHCenter)
        spacerItem8 = QtWidgets.QSpacerItem(20, 11, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem8)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setMinimumSize(QtCore.QSize(100, 400))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_3.setStyleSheet("image: url(:/iconos/hacer-subir.png);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem9)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.frame_content_inicio)
        self.frame_5.setStyleSheet("background-color: rgb(46, 114, 147);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem10 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem10)
        self.Tabla_button_Pag1 = QtWidgets.QPushButton(self.frame_5)
        self.Tabla_button_Pag1.setMinimumSize(QtCore.QSize(250, 70))
        self.Tabla_button_Pag1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Tabla_button_Pag1.setStyleSheet("QPushButton{\n"
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
        self.Tabla_button_Pag1.setObjectName("Tabla_button_Pag1")
        self.verticalLayout_8.addWidget(self.Tabla_button_Pag1, 0, QtCore.Qt.AlignHCenter)
        spacerItem11 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem11)
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setMinimumSize(QtCore.QSize(100, 400))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_4.setStyleSheet("image: url(:/iconos/yoga.png);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        spacerItem12 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem12)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_4.addWidget(self.frame_content_inicio)
        self.stackedWidget.addWidget(self.pagina_uno)
        self.pagina_dos = QtWidgets.QWidget()
        self.pagina_dos.setObjectName("pagina_dos")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.pagina_dos)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_reloj = QtWidgets.QFrame(self.pagina_dos)
        self.frame_reloj.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_reloj.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_reloj.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_reloj.setObjectName("frame_reloj")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_reloj)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem13 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.Titulo_label_pag2 = QtWidgets.QLabel(self.frame_reloj)
        self.Titulo_label_pag2.setMinimumSize(QtCore.QSize(0, 40))
        self.Titulo_label_pag2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Titulo_label_pag2.setStyleSheet("QLabel{\n"
"    background-color: #c0527a;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #c0527a;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Titulo_label_pag2.setAlignment(QtCore.Qt.AlignCenter)
        self.Titulo_label_pag2.setWordWrap(False)
        self.Titulo_label_pag2.setObjectName("Titulo_label_pag2")
        self.horizontalLayout_4.addWidget(self.Titulo_label_pag2)
        spacerItem14 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.Puntuacion_label_pag2 = QtWidgets.QLabel(self.frame_reloj)
        self.Puntuacion_label_pag2.setMinimumSize(QtCore.QSize(230, 40))
        self.Puntuacion_label_pag2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Puntuacion_label_pag2.setStyleSheet("QLabel{\n"
"    background-color: #5e17eb;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QLabel:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #5e17eb;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.Puntuacion_label_pag2.setAlignment(QtCore.Qt.AlignCenter)
        self.Puntuacion_label_pag2.setWordWrap(False)
        self.Puntuacion_label_pag2.setObjectName("Puntuacion_label_pag2")
        self.horizontalLayout_4.addWidget(self.Puntuacion_label_pag2)
        spacerItem15 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem15)
        self.verticalLayout_9.addWidget(self.frame_reloj)
        self.frame_3 = QtWidgets.QFrame(self.pagina_dos)
        self.frame_3.setMinimumSize(QtCore.QSize(1280, 0))
        self.frame_3.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Label_video = QtWidgets.QLabel(self.frame_3)
        self.Label_video.setMinimumSize(QtCore.QSize(0, 0))
        self.Label_video.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.Label_video.setText("")
        self.Label_video.setObjectName("Label_video")
        self.horizontalLayout_6.addWidget(self.Label_video)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setMaximumSize(QtCore.QSize(170, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem16 = QtWidgets.QSpacerItem(20, 152, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem16)
        self.Num_sentadillas_pag2 = QtWidgets.QLabel(self.frame_4)
        self.Num_sentadillas_pag2.setMinimumSize(QtCore.QSize(100, 40))
        self.Num_sentadillas_pag2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Num_sentadillas_pag2.setStyleSheet("QLabel{\n"
"    background-color: #c0527a;\n"
"    font: 76 16pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #c0527a;\n"
"    font: 76 16pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Num_sentadillas_pag2.setAlignment(QtCore.Qt.AlignCenter)
        self.Num_sentadillas_pag2.setWordWrap(False)
        self.Num_sentadillas_pag2.setObjectName("Num_sentadillas_pag2")
        self.verticalLayout_10.addWidget(self.Num_sentadillas_pag2)
        spacerItem17 = QtWidgets.QSpacerItem(20, 151, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem17)
        self.button_iniciar_pag2 = QtWidgets.QPushButton(self.frame_4)
        self.button_iniciar_pag2.setMinimumSize(QtCore.QSize(100, 40))
        self.button_iniciar_pag2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_iniciar_pag2.setStyleSheet("QPushButton{\n"
"    background-color: #5e17eb;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #5e17eb;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"")
        self.button_iniciar_pag2.setObjectName("button_iniciar_pag2")
        self.verticalLayout_10.addWidget(self.button_iniciar_pag2)
        spacerItem18 = QtWidgets.QSpacerItem(20, 152, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem18)
        self.horizontalLayout_6.addWidget(self.frame_4)
        self.verticalLayout_9.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.pagina_dos)
        self.pagina_tres = QtWidgets.QWidget()
        self.pagina_tres.setObjectName("pagina_tres")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pagina_tres)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_titulo_deafios = QtWidgets.QFrame(self.pagina_tres)
        self.frame_titulo_deafios.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_titulo_deafios.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_titulo_deafios.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_titulo_deafios.setObjectName("frame_titulo_deafios")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_titulo_deafios)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem19 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem19)
        self.label_21 = QtWidgets.QLabel(self.frame_titulo_deafios)
        self.label_21.setMinimumSize(QtCore.QSize(190, 40))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_21.setStyleSheet("QLabel{\n"
"    background-color: #c0527a;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #c0527a;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setWordWrap(False)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_7.addWidget(self.label_21)
        spacerItem20 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem20)
        self.verticalLayout_5.addWidget(self.frame_titulo_deafios)
        self.frame_6 = QtWidgets.QFrame(self.pagina_tres)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_10 = QtWidgets.QFrame(self.frame_7)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Anterior_button_pag3 = QtWidgets.QPushButton(self.frame_10)
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
        self.horizontalLayout_10.addWidget(self.Anterior_button_pag3)
        self.frame_17 = QtWidgets.QFrame(self.frame_10)
        self.frame_17.setMinimumSize(QtCore.QSize(1000, 500))
        self.frame_17.setStyleSheet("QFrame{\n"
"    font: 75 12pt \"Verdana\";\n"
"    color: whitesmoke;\n"
"    \n"
"    \n"
"    background-color: #2E0249;\n"
"    border: 3px solid #F806CC;\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_39 = QtWidgets.QLabel(self.frame_17)
        self.label_39.setMinimumSize(QtCore.QSize(100, 100))
        self.label_39.setMaximumSize(QtCore.QSize(100, 100))
        self.label_39.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_39.setStyleSheet("image: url(:/iconos/reward.png);\n"
"border-color: rgb(255, 255, 255, 0);")
        self.label_39.setText("")
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setWordWrap(False)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_18.addWidget(self.label_39, 0, QtCore.Qt.AlignHCenter)
        self.Ejercicios_label_pag3 = QtWidgets.QFrame(self.frame_17)
        self.Ejercicios_label_pag3.setStyleSheet("background-color: rgb(199, 120, 195);\n"
"border: 3px solid rgb(187, 96, 111, 0);\n"
"font: 87 16pt \"Arial Black\";\n"
"    color: whitesmoke;")
        self.Ejercicios_label_pag3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Ejercicios_label_pag3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Ejercicios_label_pag3.setObjectName("Ejercicios_label_pag3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Ejercicios_label_pag3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_41 = QtWidgets.QLabel(self.Ejercicios_label_pag3)
        self.label_41.setMinimumSize(QtCore.QSize(0, 0))
        self.label_41.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_41.setStyleSheet("background-color:#570A57;\n"
"border-radius: 10px;")
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout_5.addWidget(self.label_41, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.label_40 = QtWidgets.QLabel(self.Ejercicios_label_pag3)
        self.label_40.setMinimumSize(QtCore.QSize(0, 0))
        self.label_40.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_40.setStyleSheet("background-color:#570A57;\n"
"border-radius: 10px;")
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout_5.addWidget(self.label_40, 0, 1, 1, 1, QtCore.Qt.AlignVCenter)
        self.Nombre_label_pag3 = QtWidgets.QLabel(self.Ejercicios_label_pag3)
        self.Nombre_label_pag3.setStyleSheet("")
        self.Nombre_label_pag3.setText("")
        self.Nombre_label_pag3.setAlignment(QtCore.Qt.AlignCenter)
        self.Nombre_label_pag3.setWordWrap(True)
        self.Nombre_label_pag3.setObjectName("Nombre_label_pag3")
        self.gridLayout_5.addWidget(self.Nombre_label_pag3, 1, 0, 1, 1)
        self.Puntos_label_pag3 = QtWidgets.QLabel(self.Ejercicios_label_pag3)
        self.Puntos_label_pag3.setStyleSheet("")
        self.Puntos_label_pag3.setText("")
        self.Puntos_label_pag3.setAlignment(QtCore.Qt.AlignCenter)
        self.Puntos_label_pag3.setWordWrap(True)
        self.Puntos_label_pag3.setObjectName("Puntos_label_pag3")
        self.gridLayout_5.addWidget(self.Puntos_label_pag3, 1, 1, 1, 1)
        self.Descripcion_label_pag3 = QtWidgets.QLabel(self.Ejercicios_label_pag3)
        self.Descripcion_label_pag3.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"")
        self.Descripcion_label_pag3.setText("")
        self.Descripcion_label_pag3.setScaledContents(True)
        self.Descripcion_label_pag3.setWordWrap(True)
        self.Descripcion_label_pag3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Descripcion_label_pag3.setObjectName("Descripcion_label_pag3")
        self.gridLayout_5.addWidget(self.Descripcion_label_pag3, 3, 0, 1, 2)
        self.label_20 = QtWidgets.QLabel(self.Ejercicios_label_pag3)
        self.label_20.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"")
        self.label_20.setText("")
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 5, 0, 1, 2)
        self.label_42 = QtWidgets.QLabel(self.Ejercicios_label_pag3)
        self.label_42.setStyleSheet("background-color:#570A57;\n"
"border-radius: 10px;")
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.gridLayout_5.addWidget(self.label_42, 2, 0, 1, 2, QtCore.Qt.AlignVCenter)
        self.label_43 = QtWidgets.QLabel(self.Ejercicios_label_pag3)
        self.label_43.setStyleSheet("background-color:#570A57;\n"
"border-radius: 10px;")
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.gridLayout_5.addWidget(self.label_43, 4, 0, 1, 2, QtCore.Qt.AlignVCenter)
        self.verticalLayout_18.addWidget(self.Ejercicios_label_pag3)
        self.horizontalLayout_10.addWidget(self.frame_17)
        self.Siguiente_button_pag3 = QtWidgets.QPushButton(self.frame_10)
        self.Siguiente_button_pag3.setMinimumSize(QtCore.QSize(150, 40))
        self.Siguiente_button_pag3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Siguiente_button_pag3.setStyleSheet("QPushButton{\n"
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
        self.Siguiente_button_pag3.setObjectName("Siguiente_button_pag3")
        self.horizontalLayout_10.addWidget(self.Siguiente_button_pag3)
        self.frame_17.raise_()
        self.Siguiente_button_pag3.raise_()
        self.Anterior_button_pag3.raise_()
        self.horizontalLayout_9.addWidget(self.frame_10)
        self.verticalLayout_12.addWidget(self.frame_7)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.stackedWidget.addWidget(self.pagina_tres)
        self.pagina_cuatro = QtWidgets.QWidget()
        self.pagina_cuatro.setObjectName("pagina_cuatro")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.pagina_cuatro)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_titulo_deafios_2 = QtWidgets.QFrame(self.pagina_cuatro)
        self.frame_titulo_deafios_2.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_titulo_deafios_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_titulo_deafios_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_titulo_deafios_2.setObjectName("frame_titulo_deafios_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_titulo_deafios_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem21 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem21)
        self.label_23 = QtWidgets.QLabel(self.frame_titulo_deafios_2)
        self.label_23.setMinimumSize(QtCore.QSize(250, 40))
        self.label_23.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_23.setStyleSheet("QLabel{\n"
"    background-color: #c0527a;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #c0527a;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setWordWrap(False)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_8.addWidget(self.label_23)
        spacerItem22 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem22)
        self.verticalLayout_14.addWidget(self.frame_titulo_deafios_2)
        self.frame_8 = QtWidgets.QFrame(self.pagina_cuatro)
        self.frame_8.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_3.setContentsMargins(5, 10, 5, 10)
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.PosicionesBusqueda = QtWidgets.QLineEdit(self.frame_8)
        self.PosicionesBusqueda.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(208, 208, 208);\n"
"\n"
"border: 1px solid #F806CC;")
        self.PosicionesBusqueda.setObjectName("PosicionesBusqueda")
        self.gridLayout_3.addWidget(self.PosicionesBusqueda, 0, 1, 1, 2)
        self.TablaPosiciones = QtWidgets.QTableWidget(self.frame_8)
        self.TablaPosiciones.setMinimumSize(QtCore.QSize(0, 0))
        self.TablaPosiciones.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.TablaPosiciones.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.TablaPosiciones.setFont(font)
        self.TablaPosiciones.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TablaPosiciones.setStyleSheet("QHeaderView::section{\n"
"    padding: 5px;\n"
"    background-color: #000000;\n"
"    border: 1px solid #F806CC;\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"\n"
"}\n"
"")
        self.TablaPosiciones.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.TablaPosiciones.setObjectName("TablaPosiciones")
        self.TablaPosiciones.setColumnCount(7)
        self.TablaPosiciones.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TablaPosiciones.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TablaPosiciones.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TablaPosiciones.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TablaPosiciones.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TablaPosiciones.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TablaPosiciones.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TablaPosiciones.setHorizontalHeaderItem(6, item)
        self.TablaPosiciones.horizontalHeader().setCascadingSectionResizes(False)
        self.TablaPosiciones.horizontalHeader().setSortIndicatorShown(True)
        self.TablaPosiciones.horizontalHeader().setStretchLastSection(True)
        self.TablaPosiciones.verticalHeader().setVisible(False)
        self.TablaPosiciones.verticalHeader().setHighlightSections(True)
        self.TablaPosiciones.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout_3.addWidget(self.TablaPosiciones, 1, 0, 1, 4)
        self.Buscar_combobox_pag4 = QtWidgets.QComboBox(self.frame_8)
        self.Buscar_combobox_pag4.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: #2E0249;\n"
"color: whitesmoke;\n"
"\n"
"")
        self.Buscar_combobox_pag4.setObjectName("Buscar_combobox_pag4")
        self.Buscar_combobox_pag4.addItem("")
        self.Buscar_combobox_pag4.addItem("")
        self.gridLayout_3.addWidget(self.Buscar_combobox_pag4, 0, 0, 1, 1)
        self.BuscarBotonPosiciones = QtWidgets.QPushButton(self.frame_8)
        self.BuscarBotonPosiciones.setMinimumSize(QtCore.QSize(100, 40))
        self.BuscarBotonPosiciones.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BuscarBotonPosiciones.setStyleSheet("QPushButton{\n"
"    background-color: #2E0249;\n"
"    border: 1px solid #F806CC;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ff0077;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    border-radius: 10px;\n"
"\n"
"}")
        self.BuscarBotonPosiciones.setObjectName("BuscarBotonPosiciones")
        self.gridLayout_3.addWidget(self.BuscarBotonPosiciones, 0, 3, 1, 1)
        self.RefrescarPosiciones = QtWidgets.QPushButton(self.frame_8)
        self.RefrescarPosiciones.setMinimumSize(QtCore.QSize(200, 40))
        self.RefrescarPosiciones.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RefrescarPosiciones.setStyleSheet("QPushButton{\n"
"    background-color: #2E0249;\n"
"    border: 1px solid #F806CC;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ff0077;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    border-radius: 10px;\n"
"\n"
"}")
        self.RefrescarPosiciones.setObjectName("RefrescarPosiciones")
        self.gridLayout_3.addWidget(self.RefrescarPosiciones, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.OrdenarPosicionesBoton = QtWidgets.QComboBox(self.frame_8)
        self.OrdenarPosicionesBoton.setMinimumSize(QtCore.QSize(100, 0))
        self.OrdenarPosicionesBoton.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: #2E0249;\n"
"color: whitesmoke;\n"
"\n"
"")
        self.OrdenarPosicionesBoton.setObjectName("OrdenarPosicionesBoton")
        self.OrdenarPosicionesBoton.addItem("")
        self.OrdenarPosicionesBoton.addItem("")
        self.OrdenarPosicionesBoton.addItem("")
        self.gridLayout_3.addWidget(self.OrdenarPosicionesBoton, 2, 2, 1, 1)
        self.verticalLayout_14.addWidget(self.frame_8)
        self.stackedWidget.addWidget(self.pagina_cuatro)
        self.pagina_cinco = QtWidgets.QWidget()
        self.pagina_cinco.setObjectName("pagina_cinco")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.pagina_cinco)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_titulo_deafios_3 = QtWidgets.QFrame(self.pagina_cinco)
        self.frame_titulo_deafios_3.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_titulo_deafios_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_titulo_deafios_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_titulo_deafios_3.setObjectName("frame_titulo_deafios_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_titulo_deafios_3)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem23 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem23)
        self.label_28 = QtWidgets.QLabel(self.frame_titulo_deafios_3)
        self.label_28.setMinimumSize(QtCore.QSize(300, 40))
        self.label_28.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_28.setStyleSheet("QLabel{\n"
"    background-color:#c0527a;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #c0527a;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setWordWrap(False)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_11.addWidget(self.label_28)
        spacerItem24 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem24)
        self.verticalLayout_17.addWidget(self.frame_titulo_deafios_3)
        self.frame_16 = QtWidgets.QFrame(self.pagina_cinco)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem25 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem25)
        self.frame_11 = QtWidgets.QFrame(self.frame_16)
        self.frame_11.setMinimumSize(QtCore.QSize(1000, 500))
        self.frame_11.setStyleSheet("QFrame{\n"
"    font: 75 12pt \"Verdana\";\n"
"    color: whitesmoke;\n"
"    \n"
"    \n"
"    background-color: #2E0249;\n"
"    border: 3px solid #F806CC;\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_22 = QtWidgets.QLabel(self.frame_11)
        self.label_22.setMinimumSize(QtCore.QSize(100, 100))
        self.label_22.setMaximumSize(QtCore.QSize(100, 100))
        self.label_22.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_22.setStyleSheet("image: url(:/iconos/user.png);\n"
"border-color: rgb(255, 255, 255, 0);")
        self.label_22.setText("")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setWordWrap(False)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_13.addWidget(self.label_22, 0, QtCore.Qt.AlignHCenter)
        self.frame_9 = QtWidgets.QFrame(self.frame_11)
        self.frame_9.setStyleSheet("background-color: #c778c3;\n"
"border: 3px solid rgb(187, 96, 111, 0);\n"
"font: 87 16pt \"Arial Black\";\n"
"    color: whitesmoke;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.frame_9)
        self.label_8.setStyleSheet("background-color:#570A57;\n"
"border-radius: 10px;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.label_14 = QtWidgets.QLabel(self.frame_9)
        self.label_14.setStyleSheet("background-color:#570A57;\n"
"border-radius: 10px;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 7, 1, 1, 1, QtCore.Qt.AlignVCenter)
        self.IMC_label_pag5 = QtWidgets.QLabel(self.frame_9)
        self.IMC_label_pag5.setText("")
        self.IMC_label_pag5.setObjectName("IMC_label_pag5")
        self.gridLayout_2.addWidget(self.IMC_label_pag5, 9, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Peso_label_pag5 = QtWidgets.QLabel(self.frame_9)
        self.Peso_label_pag5.setText("")
        self.Peso_label_pag5.setObjectName("Peso_label_pag5")
        self.gridLayout_2.addWidget(self.Peso_label_pag5, 6, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.Edad_label_pag5 = QtWidgets.QLabel(self.frame_9)
        self.Edad_label_pag5.setText("")
        self.Edad_label_pag5.setObjectName("Edad_label_pag5")
        self.gridLayout_2.addWidget(self.Edad_label_pag5, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(self.frame_9)
        self.label_7.setStyleSheet("background-color:#570A57;\n"
"border-radius: 10px;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.label_30 = QtWidgets.QLabel(self.frame_9)
        self.label_30.setStyleSheet("background-color:#570A57;\n"
"border-radius: 10px;")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 7, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.Nombre_label_pag5 = QtWidgets.QLabel(self.frame_9)
        self.Nombre_label_pag5.setText("")
        self.Nombre_label_pag5.setObjectName("Nombre_label_pag5")
        self.gridLayout_2.addWidget(self.Nombre_label_pag5, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Puntaje_label_pag5 = QtWidgets.QLabel(self.frame_9)
        self.Puntaje_label_pag5.setText("")
        self.Puntaje_label_pag5.setObjectName("Puntaje_label_pag5")
        self.gridLayout_2.addWidget(self.Puntaje_label_pag5, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Sexo_label_pag5 = QtWidgets.QLabel(self.frame_9)
        self.Sexo_label_pag5.setMinimumSize(QtCore.QSize(0, 0))
        self.Sexo_label_pag5.setText("")
        self.Sexo_label_pag5.setObjectName("Sexo_label_pag5")
        self.gridLayout_2.addWidget(self.Sexo_label_pag5, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_29 = QtWidgets.QLabel(self.frame_9)
        self.label_29.setStyleSheet("background-color:#570A57;\n"
"border-radius: 10px;")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 2, 1, 1, 1, QtCore.Qt.AlignVCenter)
        self.Altura_label_pag5 = QtWidgets.QLabel(self.frame_9)
        self.Altura_label_pag5.setText("")
        self.Altura_label_pag5.setObjectName("Altura_label_pag5")
        self.gridLayout_2.addWidget(self.Altura_label_pag5, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_31 = QtWidgets.QLabel(self.frame_9)
        self.label_31.setStyleSheet("background-color:#570A57;\n"
"border-radius: 10px;")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 5, 1, 1, 1, QtCore.Qt.AlignVCenter)
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        self.label_5.setStyleSheet("background-color:#570A57;\n"
"border-radius: 10px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.label_11 = QtWidgets.QLabel(self.frame_9)
        self.label_11.setStyleSheet("background-color:#570A57;\n"
"border-radius: 10px;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1, QtCore.Qt.AlignVCenter)
        self.Level_label_pag5 = QtWidgets.QLabel(self.frame_9)
        self.Level_label_pag5.setText("")
        self.Level_label_pag5.setObjectName("Level_label_pag5")
        self.gridLayout_2.addWidget(self.Level_label_pag5, 9, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_13.addWidget(self.frame_9)
        self.horizontalLayout_12.addWidget(self.frame_11)
        spacerItem26 = QtWidgets.QSpacerItem(51, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem26)
        self.verticalLayout_17.addWidget(self.frame_16)
        self.stackedWidget.addWidget(self.pagina_cinco)
        self.horizontalLayout_5.addWidget(self.stackedWidget)
        self.frame_progressbar = QtWidgets.QFrame(self.contenedor_paginas)
        self.frame_progressbar.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_progressbar.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_progressbar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_progressbar.setStyleSheet("background-color: rgb(105, 86, 143);")
        self.frame_progressbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_progressbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_progressbar.setObjectName("frame_progressbar")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_progressbar)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_xp = QtWidgets.QLabel(self.frame_progressbar)
        self.label_xp.setMinimumSize(QtCore.QSize(120, 50))
        self.label_xp.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_xp.setStyleSheet("QLabel{\n"
"    background-color: #c0527a;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 15px;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #c0527a;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.label_xp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_xp.setWordWrap(False)
        self.label_xp.setObjectName("label_xp")
        self.verticalLayout_11.addWidget(self.label_xp, 0, QtCore.Qt.AlignHCenter)
        self.label_level = QtWidgets.QLabel(self.frame_progressbar)
        self.label_level.setMinimumSize(QtCore.QSize(120, 50))
        self.label_level.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_level.setStyleSheet("QLabel{\n"
"    background-color: #5e17eb;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 15px;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #5e17eb;\n"
"    font: 87 16pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.label_level.setAlignment(QtCore.Qt.AlignCenter)
        self.label_level.setWordWrap(False)
        self.label_level.setObjectName("label_level")
        self.verticalLayout_11.addWidget(self.label_level, 0, QtCore.Qt.AlignHCenter)
        self.barra_xp = QtWidgets.QProgressBar(self.frame_progressbar)
        self.barra_xp.setMinimumSize(QtCore.QSize(170, 20))
        font = QtGui.QFont()
        font.setKerning(True)
        self.barra_xp.setFont(font)
        self.barra_xp.setStyleSheet("QProgressBar\n"
"{\n"
"background-color: ;\n"
"    background-color: rgb(46, 2, 73);\n"
"border : 1px;\n"
"}\n"
"QProgressBar::chunk{\n"
"    \n"
"    background-color: rgb(248, 6, 204);\n"
"}\n"
"")
        self.barra_xp.setProperty("value", 24)
        self.barra_xp.setAlignment(QtCore.Qt.AlignCenter)
        self.barra_xp.setTextVisible(False)
        self.barra_xp.setOrientation(QtCore.Qt.Vertical)
        self.barra_xp.setObjectName("barra_xp")
        self.verticalLayout_11.addWidget(self.barra_xp)
        self.horizontalLayout_5.addWidget(self.frame_progressbar)
        self.verticalLayout_2.addWidget(self.contenedor_paginas)
        self.horizontalLayout.addWidget(self.frame_contenedor)
        self.verticalLayout.addWidget(self.frame_contenido)
        MenuPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(MenuPrincipal)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MenuPrincipal)
        
        """
        Aqui inician las instrucciones a las funciones:
        """
        #Botones menu desplegable
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_uno))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_dos))
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_tres))
        self.pushButton_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_cuatro))
        self.pushButton_8.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_cinco))
        
        #Botones menu principal
        self.Entrenamiento_button_Pag1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_dos))
        self.Desafios_button_Pag1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_tres))
        self.Tabla_button_Pag1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_cuatro))
        self.profile_picture_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_cinco))
        
        #Clickear menu
        self.MenuButton.clicked.connect(lambda: self.desplegarMenu())
        
        #Botones desafios
        cursor.execute("select *from desafios")
        row=cursor.fetchall()
        self.Nombre_label_pag3.setText(str(row[self.indexDes][1]))
        self.Puntos_label_pag3.setText(str(row[self.indexDes][2]))
        self.Descripcion_label_pag3.setText(str(row[self.indexDes][3]))
        self.label_20.setText(str(row[self.indexDes][4]))    
        
        self.Siguiente_button_pag3.clicked.connect(lambda: self.botonSiguienteDesafio(cursor))
        self.Anterior_button_pag3.clicked.connect(lambda: self.botonAnteriorDesafio(cursor))
        
        #Informacion Usuario
        SQL='''select *from jugador where id_jugador='{}' '''.format(id)
        cursor.execute(SQL)
        row=cursor.fetchall()
        self.Username.setText(row[0][1])
        
        self.Nombre_label_pag5.setText(row[0][1])
        self.Sexo_label_pag5.setText(row[0][4])
        self.Edad_label_pag5.setText(str(row[0][3]))
        self.Altura_label_pag5.setText(str(row[0][5]))
        self.Puntaje_label_pag5.setText(str(row[0][6]))
        self.Peso_label_pag5.setText(str(row[0][7]))
        self.IMC_label_pag5.setText(row[0][10])
        self.Level_label_pag5.setText(str(row[0][8]))
        
        #Barra progreso
        self.puntajetotal=int(row[0][6])
        self.nivel = int(row[0][8])
        
        self.label_xp.setText(str(self.puntajetotal)+"XP")
        self.label_level.setText("LVL"+str(self.nivel))
        
        ptjtotal = self.puntajetotal
        
        div = (int(self.nivel)-1) * 3000
        ptjtotal = ptjtotal - div
        
        porcentaje = (ptjtotal*100) / 3000
        self.barra_xp.setValue(porcentaje)
        
        #Cerrar sesion
        self.pushButton_9.clicked.connect(lambda: self.cerrarSesion(MenuPrincipal, cursor, Login))
        
        #Buscar Jugador Posicion
        self.BuscarBotonPosiciones.clicked.connect(lambda: self.buscarPosicion(cursor));
        #Refrescar posiciones
        self.RefrescarPosiciones.clicked.connect(lambda: self.refrescarPosiciones(cursor))
        
        SQL="select *from jugador order by puntaje_total"
        cursor.execute(SQL)
        row=cursor.fetchall()
        if len(row)!=0:
            tablerow = 0
            for rows in row:
                self.TablaPosiciones.setRowCount(tablerow + 1)
                self.TablaPosiciones.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                self.TablaPosiciones.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                self.TablaPosiciones.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                self.TablaPosiciones.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                self.TablaPosiciones.setItem(tablerow,4,QTableWidgetItem(str(rows[4])))
                self.TablaPosiciones.setItem(tablerow,5,QTableWidgetItem(str(rows[8])))
                self.TablaPosiciones.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                tablerow+=1
        #Iniciar y terminar video
        self.button_iniciar_pag2.clicked.connect(lambda: self.startVideo(cursor,id))
        
        
        
        """
        Aqui inician las funciones:
    
        """

    def cerrarSesion(self, MenuPrincipal, cursor, Login):
        MenuPrincipal.close()
        Login.show()
        
        
    def desplegarMenu(self):
        if True:
            width = self.frame_menu_desplegable.width()
            normal = 0
            if width==0:
                extender = 200
            else:
                extender = normal
            
            self.animacion = QtCore.QPropertyAnimation(self.frame_menu_desplegable, b'minimumWidth') 
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width) 
            self.animacion.setEndValue(extender) 
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart) 
            self.animacion.start()
            
    def refrescarPosiciones(self, cursor):
        opc= self.OrdenarPosicionesBoton.currentText()
        if opc == "Ordenar por Nombre":
            sql="select *from jugador order by nombre, puntaje_total"
            cursor.execute(sql)
            row=cursor.fetchall()
            if len(row)!=0:
                tablerow = 0
                for rows in row:
                    self.TablaPosiciones.setRowCount(tablerow + 1)
                    self.TablaPosiciones.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                    self.TablaPosiciones.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                    self.TablaPosiciones.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                    self.TablaPosiciones.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                    self.TablaPosiciones.setItem(tablerow,4,QTableWidgetItem(str(rows[4])))
                    self.TablaPosiciones.setItem(tablerow,5,QTableWidgetItem(str(rows[8])))
                    self.TablaPosiciones.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                    tablerow+=1
        elif opc == "Ordenar por Puntuacion":
            sql="select *from jugador order by puntaje_total"
            cursor.execute(sql)
            row=cursor.fetchall()
            if len(row)!=0:
                tablerow = 0
                for rows in row:
                    self.TablaPosiciones.setRowCount(tablerow + 1)
                    self.TablaPosiciones.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                    self.TablaPosiciones.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                    self.TablaPosiciones.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                    self.TablaPosiciones.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                    self.TablaPosiciones.setItem(tablerow,4,QTableWidgetItem(str(rows[4])))
                    self.TablaPosiciones.setItem(tablerow,5,QTableWidgetItem(str(rows[8])))
                    self.TablaPosiciones.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                    tablerow+=1
        elif opc == "Ordenar por Edad":
            sql="select *from jugador order by edad, puntaje_total"
            cursor.execute(sql)
            row=cursor.fetchall()
            if len(row)!=0:
                tablerow = 0
                for rows in row:
                    self.TablaPosiciones.setRowCount(tablerow + 1)
                    self.TablaPosiciones.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                    self.TablaPosiciones.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                    self.TablaPosiciones.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                    self.TablaPosiciones.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                    self.TablaPosiciones.setItem(tablerow,4,QTableWidgetItem(str(rows[4])))
                    self.TablaPosiciones.setItem(tablerow,5,QTableWidgetItem(str(rows[8])))
                    self.TablaPosiciones.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                    tablerow+=1
            
            
    def buscarPosicion(self, cursor):
        data=self.PosicionesBusqueda.text()
        self.TablaPosiciones.clearContents()
        self.TablaPosiciones.setRowCount(0)
        #Aqui comprueba que se alla escrito en el cuadro
        if len(data)!=0:
            opc=self.Buscar_combobox_pag4.currentText() 
            if opc == "Buscar por Nombre:":
                sql="select *from jugador where nombre_usuario like"
                cursor.execute(sql+"'%"+data+"%'")
                row=cursor.fetchall()
                if len(row)!=0:
                    tablerow = 0
                    for rows in row:
                        self.TablaPosiciones.setRowCount(tablerow + 1)
                        self.TablaPosiciones.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                        self.TablaPosiciones.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                        self.TablaPosiciones.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                        self.TablaPosiciones.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                        self.TablaPosiciones.setItem(tablerow,4,QTableWidgetItem(str(rows[4])))
                        self.TablaPosiciones.setItem(tablerow,5,QTableWidgetItem(str(rows[8])))
                        self.TablaPosiciones.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                        tablerow+=1
                else:
                    self.msgError("Sin coincidencia", "No hay coincidencia con ese USERNAME")
            elif opc == "Buscar por Puntuacion:":
                sql="select *from jugador where puntaje_total="
                cursor.execute(sql+"'"+data+"'")
                row=cursor.fetchall()
                if len(row)!=0:
                    tablerow = 0
                    for rows in row:
                        self.TablaPosiciones.setRowCount(tablerow + 1)
                        self.TablaPosiciones.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                        self.TablaPosiciones.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                        self.TablaPosiciones.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                        self.TablaPosiciones.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                        self.TablaPosiciones.setItem(tablerow,4,QTableWidgetItem(str(rows[4])))
                        self.TablaPosiciones.setItem(tablerow,5,QTableWidgetItem(str(rows[8])))
                        self.TablaPosiciones.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                        tablerow+=1
        else:
            self.msgError("Sin informacion", "Debes ingresar un Username Valido");
    
    def botonSiguienteDesafio(self, cursor):
        
        cursor.execute("select *from desafios")
        row=cursor.fetchall()
        cantidad = len(row)
        
        if (self.indexDes+1) != cantidad:
            self.indexDes+=1
        self.Nombre_label_pag3.setText(str(row[self.indexDes][1]))
        self.Puntos_label_pag3.setText(str(row[self.indexDes][2]))
        self.Descripcion_label_pag3.setText(str(row[self.indexDes][3]))
        self.label_20.setText(str(row[self.indexDes][4]))  
    
    def botonAnteriorDesafio(self, cursor):
        
        cursor.execute("select *from desafios")
        row=cursor.fetchall()
        if (self.indexDes) != 0:
            self.indexDes-=1
        self.Nombre_label_pag3.setText(str(row[self.indexDes][1]))
        self.Puntos_label_pag3.setText(str(row[self.indexDes][2]))
        self.Descripcion_label_pag3.setText(str(row[self.indexDes][3]))
        self.label_20.setText(str(row[self.indexDes][4])) 
        
                    
    def startVideo(self, cursor, id):
        if self.activate == False:
            self.Work = Work()
            self.Work.start()
            self.Work.Imageupd.connect(self.Imageupd_slot)
            self.Work.Labelupd.connect(self.labelUpdate_slot)
            self.activate = True
            self.button_iniciar_pag2.setText("Terminar")
        else:
            self.Work.stop()
            self.button_iniciar_pag2.setText("Iniciar")
            self.activate=False
            self.Label_video.clear()
            self.Label_video.clear()
            self.Num_sentadillas_pag2.setText("N° : ")
            self.Puntuacion_label_pag2.setText("Puntuacion:")
            
            #Conecto al usuario
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window,self.pts, self.nivel, self.count)
            self.window.show()
            
            SQL='''update jugador set nivel='{}' where id_jugador='{}' '''.format(str(self.nivel),str(id))
            print(SQL)
            cursor.execute(SQL)     
            cursor.connection.commit()
            SQL='''update jugador set puntaje_total='{}' where id_jugador='{}' '''.format(str(self.puntajetotal),str(id))
            print(SQL)
            cursor.execute(SQL)     
            cursor.connection.commit()
    
    def Imageupd_slot(self, Image):
        self.Label_video.setPixmap(QPixmap.fromImage(Image))
    
    def labelUpdate_slot(self, count):
        self.count = count
        self.pts= count*100
        self.Num_sentadillas_pag2.setText("N° : "+str(count))
        self.Puntuacion_label_pag2.setText("Puntuacion: "+str(self.pts))
        
        self.puntajetotal+=100
        ptjtotal = self.puntajetotal
        
        
        div = (int(self.nivel)-1) * 3000
        ptjtotal = ptjtotal - div
        
        porcentaje = (ptjtotal*100) / 3000
        self.barra_xp.setValue(porcentaje)

        self.label_xp.setText(str(self.puntajetotal)+"XP")
        if porcentaje >= 100:
            self.nivel+=1        
            self.label_level.setText("LVL"+str(self.nivel))
        
    
    
    def msgError(self,msg1,msg2):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(msg1)
        msg.setText(msg2)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        
        x = msg.exec_()
    def cancel(self):
        self.label.clear()
        self.Work.stop()
 
    
    def msgError(self,msg1,msg2):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(msg1)
        msg.setText(msg2)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        
        x = msg.exec_()
        

    def retranslateUi(self, MenuPrincipal):
        _translate = QtCore.QCoreApplication.translate
        MenuPrincipal.setWindowTitle(_translate("MenuPrincipal", "Menu Principal"))
        self.Logo.setText(_translate("MenuPrincipal", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("MenuPrincipal", "Hecho por Abraham Flores"))
        self.label_tipo_app.setText(_translate("MenuPrincipal", "Aplicación de escritorio para promover el ejercicio haciendo uso de la gamificación"))
        self.Entrenamiento_button_Pag1.setText(_translate("MenuPrincipal", "Entrenamiento"))
        self.label_2.setText(_translate("MenuPrincipal", "<html><head/><body><p><br/></p></body></html>"))
        self.Desafios_button_Pag1.setText(_translate("MenuPrincipal", "Desafios"))
        self.label_3.setText(_translate("MenuPrincipal", "<html><head/><body><p><br/></p></body></html>"))
        self.Tabla_button_Pag1.setText(_translate("MenuPrincipal", "Tabla de posiciones"))
        self.label_4.setText(_translate("MenuPrincipal", "<html><head/><body><p><br/></p></body></html>"))
        self.Titulo_label_pag2.setText(_translate("MenuPrincipal", "Sentadillas"))
        self.Puntuacion_label_pag2.setText(_translate("MenuPrincipal", "Puntuacion:"))
        self.Num_sentadillas_pag2.setText(_translate("MenuPrincipal", "N° : "))
        self.button_iniciar_pag2.setText(_translate("MenuPrincipal", "Iniciar"))
        self.label_21.setText(_translate("MenuPrincipal", "Desafios"))
        self.Anterior_button_pag3.setText(_translate("MenuPrincipal", "Anterior"))
        self.label_41.setText(_translate("MenuPrincipal", "Nombre:"))
        self.label_40.setText(_translate("MenuPrincipal", "Puntos a obtener:"))
        self.label_42.setText(_translate("MenuPrincipal", "Descripcion:"))
        self.label_43.setText(_translate("MenuPrincipal", "Ejercicios:"))
        self.Siguiente_button_pag3.setText(_translate("MenuPrincipal", "Siguiente"))
        self.label_23.setText(_translate("MenuPrincipal", "Tabla de posiciones"))
        item = self.TablaPosiciones.horizontalHeaderItem(0)
        item.setText(_translate("MenuPrincipal", "ID"))
        item = self.TablaPosiciones.horizontalHeaderItem(1)
        item.setText(_translate("MenuPrincipal", "Nombre"))
        item = self.TablaPosiciones.horizontalHeaderItem(2)
        item.setText(_translate("MenuPrincipal", "Username"))
        item = self.TablaPosiciones.horizontalHeaderItem(3)
        item.setText(_translate("MenuPrincipal", "Edad"))
        item = self.TablaPosiciones.horizontalHeaderItem(4)
        item.setText(_translate("MenuPrincipal", "Sexo"))
        item = self.TablaPosiciones.horizontalHeaderItem(5)
        item.setText(_translate("MenuPrincipal", "Level"))
        item = self.TablaPosiciones.horizontalHeaderItem(6)
        item.setText(_translate("MenuPrincipal", "Puntaje Total"))
        self.Buscar_combobox_pag4.setItemText(0, _translate("MenuPrincipal", "Buscar por Nombre:"))
        self.Buscar_combobox_pag4.setItemText(1, _translate("MenuPrincipal", "Buscar por Puntuacion:"))
        self.BuscarBotonPosiciones.setText(_translate("MenuPrincipal", "Buscar"))
        self.RefrescarPosiciones.setText(_translate("MenuPrincipal", "Refrescar"))
        self.OrdenarPosicionesBoton.setItemText(0, _translate("MenuPrincipal", "Ordenar por Nombre"))
        self.OrdenarPosicionesBoton.setItemText(1, _translate("MenuPrincipal", "Ordenar por Puntuacion"))
        self.OrdenarPosicionesBoton.setItemText(2, _translate("MenuPrincipal", "Ordenar por Edad"))
        self.label_28.setText(_translate("MenuPrincipal", "Informacion de usuario"))
        self.label_8.setText(_translate("MenuPrincipal", "Puntaje total"))
        self.label_14.setText(_translate("MenuPrincipal", "Level"))
        self.label_7.setText(_translate("MenuPrincipal", "Edad"))
        self.label_30.setText(_translate("MenuPrincipal", "IMC"))
        self.label_29.setText(_translate("MenuPrincipal", "Altura"))
        self.label_31.setText(_translate("MenuPrincipal", "Peso"))
        self.label_5.setText(_translate("MenuPrincipal", "Nombre:"))
        self.label_11.setText(_translate("MenuPrincipal", "Sexo"))
        self.label_xp.setText(_translate("MenuPrincipal", "00 XP"))
        self.label_level.setText(_translate("MenuPrincipal", " LVL 00"))

          
class Work(QThread):
    Imageupd = pyqtSignal(QImage)
    Labelupd = pyqtSignal(int)
    def run(self):
        count= 0
        self.hilo_corriendo = True
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        cap = cv2.VideoCapture("video_002.mp4")
        up = False
        down = False
        with mp_pose.Pose(
             static_image_mode=False) as pose:
            while self.hilo_corriendo:
                ret, frame = cap.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = cv2.resize(frame,(1280,720),interpolation=cv2.INTER_AREA)
                    #frame = cv2.flip(frame, 1)
                    height, width, _ = frame.shape
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    results = pose.process(frame_rgb)
                    if results.pose_landmarks is not None:
                        x1 = int(results.pose_landmarks.landmark[24].x * width)
                        y1 = int(results.pose_landmarks.landmark[24].y * height)
                        x2 = int(results.pose_landmarks.landmark[26].x * width)
                        y2 = int(results.pose_landmarks.landmark[26].y * height)
                        x3 = int(results.pose_landmarks.landmark[28].x * width)
                        y3 = int(results.pose_landmarks.landmark[28].y * height)
                        p1 = np.array([x1, y1])
                        p2 = np.array([x2, y2])
                        p3 = np.array([x3, y3])
                        l1 = np.linalg.norm(p2 - p3)
                        l2 = np.linalg.norm(p1 - p3)
                        l3 = np.linalg.norm(p1 - p2)
                        # Calcular el ángulo
                        angle = degrees(acos((l1**2 + l3**2 - l2**2) / (2 * l1 * l3)))
                        if angle >= 160:
                            up = True
                        if up == True and down == False and angle <= 100:
                            down = True
                        if up == True and down == True and angle >= 160:
                            count += 1
                            up = False
                            down = False
                            self.Labelupd.emit(count)
                                   
                        #print("count: ", count)
                        # Visualización
                        aux_image = np.zeros(frame.shape, np.uint8)
                        cv2.line(aux_image, (x1, y1), (x2, y2), (0, 193, 208), 20)
                        cv2.line(aux_image, (x2, y2), (x3, y3), (0, 193, 208), 20)
                        cv2.line(aux_image, (x1, y1), (x3, y3), (0, 193, 208), 5)
                        contours = np.array([[x1, y1], [x2, y2], [x3, y3]])
                        cv2.fillPoly(aux_image, pts=[contours], color=(252,70,107))
                        output = cv2.addWeighted(frame, 1, aux_image, 0.8, 0)
                        cv2.circle(output, (x1, y1), 6, (255,5,52), 4)
                        cv2.circle(output, (x2, y2), 6, (230,39,136), 4)
                        cv2.circle(output, (x3, y3), 6, (255,5,52), 4)
                        cv2.putText(output, str(int(angle)), (x2 + 30, y2), 1, 1.5, (0, 193, 208), 2)
                        convertir_QT = QImage(output.data, output.shape[1], output.shape[0], QImage.Format_RGB888)
                        #pic = convertir_QT.scaled(1280, 600, Qt.KeepAspectRatio)
                        pic = convertir_QT.scaled(1920, 1080, Qt.KeepAspectRatio)
        
                        self.Imageupd.emit(pic)
        cap.release()
    def stop(self):
        self.hilo_corriendo = False
        self.quit()


import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuPrincipal = QtWidgets.QMainWindow()
    ui = Ui_MenuPrincipal()
    ui.setupUi(MenuPrincipal)
    MenuPrincipal.show()
    sys.exit(app.exec_())

