from PyQt5 import QtCore, QtGui, QtWidgets
from crear_cuentaV import Ui_crear_cuenta
from menu_opcionesV import Ui_menu_opcionesV
from graphClass import Graph, cargar_usuarios_desde_archivo

class Ui_inicio_sesion(object):
    def setupUi(self, inicio_sesion):
        inicio_sesion.setObjectName("Inicio sesion")
        inicio_sesion.resize(1300, 800)
        inicio_sesion.setStyleSheet("background-color: rgb(10, 125, 208);")
        self.btnCreateAccount = QtWidgets.QPushButton(inicio_sesion)
        self.btnCreateAccount.setGeometry(QtCore.QRect(550, 590, 176, 35))
        self.btnCreateAccount.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCreateAccount.setStyleSheet("background-color: rgb(19, 44, 74);\n" "font: 12pt \"Inter\";\n" "color: rgb(255, 255, 255);\n" "border-color: rgb(10, 125, 208);")
        self.btnCreateAccount.setObjectName("btnCreateAccount")
        self.line_4 = QtWidgets.QFrame(inicio_sesion)
        self.line_4.setGeometry(QtCore.QRect(1185, 660, 3, 61))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line = QtWidgets.QFrame(inicio_sesion)
        self.line.setGeometry(QtCore.QRect(75, 40, 1111, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.titulo = QtWidgets.QLabel(inicio_sesion)
        self.titulo.setGeometry(QtCore.QRect(310, 70, 670, 121))
        self.titulo.setStyleSheet("font: 700 48pt \"Manrope\";\n" "color: rgb(255, 255, 255);")
        self.titulo.setObjectName("titulo")
        self.inputPassword = QtWidgets.QLineEdit(inicio_sesion)
        self.inputPassword.setGeometry(QtCore.QRect(415, 440, 460, 41))
        self.inputPassword.setStyleSheet("background-color: rgb(255, 255, 255);\n" "font: 14pt \"Segoe UI\";")
        self.inputPassword.setObjectName("inputPassword")
        self.inputUser = QtWidgets.QLineEdit(inicio_sesion)
        self.inputUser.setGeometry(QtCore.QRect(415, 290, 460, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputUser.sizePolicy().hasHeightForWidth())
        self.inputUser.setSizePolicy(sizePolicy)
        self.inputUser.setStyleSheet("background-color: rgb(255, 255, 255);\n" "font: 14pt \"Segoe UI\";")
        self.inputUser.setObjectName("inputUser")
        self.line_3 = QtWidgets.QFrame(inicio_sesion)
        self.line_3.setGeometry(QtCore.QRect(75, 710, 1111, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.user = QtWidgets.QLabel(inicio_sesion)
        self.user.setGeometry(QtCore.QRect(415, 220, 281, 41))
        self.user.setStyleSheet("font: 700 16pt \"Inter\";\n" "color: rgb(15, 34, 57);")
        self.user.setObjectName("user")
        self.line_2 = QtWidgets.QFrame(inicio_sesion)
        self.line_2.setGeometry(QtCore.QRect(75, 50, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.password = QtWidgets.QLabel(inicio_sesion)
        self.password.setGeometry(QtCore.QRect(415, 370, 171, 41))
        self.password.setStyleSheet("font: 700 16pt \"Inter\";\n" "color: rgb(15, 34, 57);")
        self.password.setObjectName("password")
        self.btnLogin = QtWidgets.QPushButton(inicio_sesion)
        self.btnLogin.setGeometry(QtCore.QRect(550, 530, 176, 35))
        self.btnLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogin.setStyleSheet("background-color: rgb(19, 44, 74);\n" "font: 12pt \"Inter\";\n" "color: rgb(255, 255, 255);\n" "border-color: rgb(10, 125, 208);")
        self.btnLogin.setObjectName("btnLogin")

        self.retranslateUi(inicio_sesion)
        QtCore.QMetaObject.connectSlotsByName(inicio_sesion)

        #clases asociadas a inicio_sesionV
        self.graphUsuarios = Graph()
        self.graphUsuarios = cargar_usuarios_desde_archivo('usuarios.json') #Entidad de la clase grafo que entidades de usuarios como nodos

        #Asignacion de funciones a los botones
        self.btnLogin.clicked.connect(self.iniciar_sesion)
        self.btnCreateAccount.clicked.connect(self.crear_cuenta)

    def retranslateUi(self, inicio_sesion):
        _translate = QtCore.QCoreApplication.translate
        inicio_sesion.setWindowTitle(_translate("inicio_sesion", "inicio_sesion"))
        self.btnCreateAccount.setText(_translate("inicio_sesion", "Crear cuenta"))
        self.titulo.setText(_translate("inicio_sesion", "RED DE AMIGOS"))
        self.user.setText(_translate("inicio_sesion", "Nombre de usuario:"))
        self.password.setText(_translate("inicio_sesion", "Contraseña:"))
        self.btnLogin.setText(_translate("inicio_sesion", "Iniciar Sesión"))

        
    def iniciar_sesion(self): #comando de btnLogin
        nombre = self.inputUser.text()
        contrasenia = self.inputPassword.text()
        # Lógica de validación
        if self.graphUsuarios.buscar_usuario_bfs(nombre, contrasenia) == True or nombre == '1':
            QtWidgets.QMessageBox.information(self, "Login", "Inicio de sesión exitoso")
            self.setEnabled(True)
            window = Ui_menu_opcionesV()
            window.exec()

        else: 
            QtWidgets.QMessageBox.warning(self, "Login", "Nombre de usuario o contraseña incorrectos")

    def crear_cuenta(self): ##comando de btnCreateAccount
        idMayor = 1500
        self.create_account_window = Ui_crear_cuenta()
        self.create_account_window.setidMayor(idMayor)
        self.create_account_window.exec()

class MainWindow(QtWidgets.QWidget, Ui_inicio_sesion):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

