from PyQt5 import QtWidgets, QtCore, QtGui

class Ui_menu_opciones(object):
    def setupUi(self, menu_opciones):
        menu_opciones.setObjectName("Menu opciones")
        menu_opciones.resize(1300, 800)
        menu_opciones.setEnabled(True)
        menu_opciones.setStyleSheet("background-color: rgb(10, 125, 208);")

        self.btnAmigosPotenciales = QtWidgets.QPushButton(menu_opciones)
        self.btnAmigosPotenciales.setGeometry(QtCore.QRect(100, 230, 270, 35))
        self.btnAmigosPotenciales.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAmigosPotenciales.setStyleSheet("background-color: rgb(19, 44, 74);\nfont: 12pt \"Inter\";\ncolor: rgb(255, 255, 255);\nborder-color: rgb(10, 125, 208);")
        self.btnAmigosPotenciales.setObjectName("btnAmigosPotenciales")

        self.titulo = QtWidgets.QLabel(menu_opciones)
        self.titulo.setGeometry(QtCore.QRect(440, 0, 491, 121))
        self.titulo.setStyleSheet("font: 700 35pt \"Manrope\";\ncolor: rgb(255, 255, 255);")
        self.titulo.setObjectName("titulo")

        self.btnCerrarSesion = QtWidgets.QPushButton(menu_opciones)
        self.btnCerrarSesion.setGeometry(QtCore.QRect(100, 530, 270, 35))
        self.btnCerrarSesion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCerrarSesion.setStyleSheet("background-color: rgb(19, 44, 74);\nfont: 12pt \"Inter\";\ncolor: rgb(255, 255, 255);\nborder-color: rgb(10, 125, 208);")
        self.btnCerrarSesion.setObjectName("btnCerrarSesion")

        self.frame = QtWidgets.QFrame(menu_opciones)
        self.frame.setGeometry(QtCore.QRect(490, 160, 741, 561))
        self.frame.setStyleSheet("background-color: rgb(9, 118, 195);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.btnAgregarAmigos = QtWidgets.QPushButton(menu_opciones)
        self.btnAgregarAmigos.setGeometry(QtCore.QRect(100, 330, 270, 35))
        self.btnAgregarAmigos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAgregarAmigos.setStyleSheet("background-color: rgb(19, 44, 74);\nfont: 12pt \"Inter\";\ncolor: rgb(255, 255, 255);\nborder-color: rgb(10, 125, 208);")
        self.btnAgregarAmigos.setObjectName("btnAgregarAmigos")

        self.btnSolicitudesAmistad = QtWidgets.QPushButton(menu_opciones)
        self.btnSolicitudesAmistad.setGeometry(QtCore.QRect(100, 430, 270, 35))
        self.btnSolicitudesAmistad.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSolicitudesAmistad.setStyleSheet("background-color: rgb(19, 44, 74);\nfont: 12pt \"Inter\";\ncolor: rgb(255, 255, 255);\nborder-color: rgb(10, 125, 208);")
        self.btnSolicitudesAmistad.setObjectName("btnSolicitudesAmistad")

        self.lblGrafoAmigos = QtWidgets.QLabel(menu_opciones)
        self.lblGrafoAmigos.setGeometry(QtCore.QRect(820, 120, 151, 31))
        self.lblGrafoAmigos.setStyleSheet("font: 200 12pt \"Manrope\";\ncolor: rgb(255, 255, 255);")
        self.lblGrafoAmigos.setObjectName("lblGrafoAmigos")

        self.line = QtWidgets.QFrame(menu_opciones)
        self.line.setGeometry(QtCore.QRect(20, 10, 1261, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(menu_opciones)
        self.line_2.setGeometry(QtCore.QRect(20, 770, 1261, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(menu_opciones)
        QtCore.QMetaObject.connectSlotsByName(menu_opciones)
        
        #Asignacion de funciones a los botones
        self.btnAmigosPotenciales.clicked.connect(self.amigos_potenciales)
        self.btnCerrarSesion.clicked.connect(self.cerrar_sesion)
        self.btnAgregarAmigos.clicked.connect(self.agregar_amigos)
        self.btnSolicitudesAmistad.clicked.connect(self.solicitudes_amistad)

    def amigos_potenciales(self):
        print("Amigos potenciales button clicked")

    def cerrar_sesion(self):
        print("Cerrar sesión button clicked")
        self.close()

    def agregar_amigos(self):
        print("Agregar amigos button clicked")

    def solicitudes_amistad(self):
        print("Solicitudes de amistad button clicked")

    def retranslateUi(self, menu_opciones):
        _translate = QtCore.QCoreApplication.translate
        menu_opciones.setWindowTitle(_translate("menu_opciones", "InicioSesion"))
        self.btnAmigosPotenciales.setText(_translate("menu_opciones", "Amigos potenciales"))
        self.titulo.setText(_translate("menu_opciones", "RED DE AMIGOS"))
        self.btnCerrarSesion.setText(_translate("menu_opciones", "Cerrar sesión"))
        self.btnAgregarAmigos.setText(_translate("menu_opciones", "Agregar amigos"))
        self.btnSolicitudesAmistad.setText(_translate("menu_opciones", "Solicitudes de amistad"))
        self.lblGrafoAmigos.setText(_translate("menu_opciones", "Grafo de amigos"))

class Ui_menu_opcionesV(QtWidgets.QDialog, Ui_menu_opciones):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

