from PyQt5 import QtWidgets, QtCore, QtGui

class Ui_agregar_amigos(object):
    def setupUi(self, agregar_amigos):
        agregar_amigos.setObjectName("Agregar amigos")
        agregar_amigos.resize(1300, 800)
        agregar_amigos.setStyleSheet("background-color: rgb(10, 125, 208);")
        self.btnExit = QtWidgets.QPushButton(agregar_amigos)
        self.btnExit.setGeometry(QtCore.QRect(110, 40, 81, 71))
        self.btnExit.setStyleSheet("font: 700 20pt \"Manrope\";\n" "color: rgb(19, 44, 74);\n" "background-color: rgb(0, 148, 255);")
        self.btnExit.setObjectName("btnExit")
        
        self.lblNombre = QtWidgets.QLabel(agregar_amigos)
        self.lblNombre.setGeometry(QtCore.QRect(240, 160, 111, 31))
        self.lblNombre.setStyleSheet("font: 700 14pt \"Manrope\";\n" "color: rgb(255, 255, 255);")
        self.lblNombre.setObjectName("lblNombre")
        
        self.titulo = QtWidgets.QLabel(agregar_amigos)
        self.titulo.setGeometry(QtCore.QRect(420, 10, 551, 121))
        self.titulo.setStyleSheet("font: 700 35pt \"Manrope\";\n" "color: rgb(255, 255, 255);")
        self.titulo.setObjectName("titulo")
        
        self.frame = QtWidgets.QFrame(agregar_amigos)
        self.frame.setGeometry(QtCore.QRect(470, 280, 341, 291))
        self.frame.setStyleSheet("background-color: rgb(9, 118, 195);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.lblEncontrado = QtWidgets.QLabel(self.frame)
        self.lblEncontrado.setGeometry(QtCore.QRect(90, 240, 211, 31))
        self.lblEncontrado.setStyleSheet("font: 500 14pt \"Manrope\";\n" "color: rgb(255, 255, 255);")
        self.lblEncontrado.setObjectName("lblEncontrado")
        self.lblEncontrado.setEnabled(False)
        
        self.btnBuscar = QtWidgets.QPushButton(agregar_amigos)
        self.btnBuscar.setGeometry(QtCore.QRect(960, 160, 101, 35))
        self.btnBuscar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBuscar.setStyleSheet("background-color: rgb(19, 44, 74);\n" "font: 12pt \"Inter\";\n" "color: rgb(255, 255, 255);\n" "border-color: rgb(10, 125, 208);")
        self.btnBuscar.setObjectName("btnBuscar")
        
        self.line = QtWidgets.QFrame(agregar_amigos)
        self.line.setGeometry(QtCore.QRect(20, 10, 1261, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.btnEnviarSolicitud = QtWidgets.QPushButton(agregar_amigos)
        self.btnEnviarSolicitud.setGeometry(QtCore.QRect(530, 650, 211, 35))
        self.btnEnviarSolicitud.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEnviarSolicitud.setStyleSheet("background-color: rgb(19, 44, 74);\n" "font: 12pt \"Inter\";\n" "color: rgb(255, 255, 255);\n" "border-color: rgb(10, 125, 208);")
        self.btnEnviarSolicitud.setObjectName("btnEnviarSolicitud")
        
        self.inputNombre = QtWidgets.QLineEdit(agregar_amigos)
        self.inputNombre.setGeometry(QtCore.QRect(410, 160, 460, 41))
        self.inputNombre.setStyleSheet("background-color: rgb(255, 255, 255);\n" "font: 14pt \"Segoe UI\";")
        self.inputNombre.setObjectName("inputNombre")
        
        self.line_2 = QtWidgets.QFrame(agregar_amigos)
        self.line_2.setGeometry(QtCore.QRect(20, 760, 1261, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.retranslateUi(agregar_amigos)
        QtCore.QMetaObject.connectSlotsByName(agregar_amigos)

        #Asignacion de funciones a los botones
        self.btnExit.clicked.connect(self.cerrar_ventana)
    
    def retranslateUi(self, agregar_amigos):
        _translate = QtCore.QCoreApplication.translate
        agregar_amigos.setWindowTitle(_translate("agregar_amigos", "Agregar amigos"))
        self.btnExit.setText(_translate("agregar_amigos", "<-"))
        self.lblNombre.setText(_translate("agregar_amigos", "Nombre:"))
        self.titulo.setText(_translate("agregar_amigos", "AGREGAR AMIGOS"))
        self.lblEncontrado.setText(_translate("agregar_amigos", "NO ENCONTRADO"))
        self.btnBuscar.setText(_translate("agregar_amigos", "Buscar"))
        self.btnEnviarSolicitud.setText(_translate("agregar_amigos", "Enviar solicitud"))
    
    #funcion que cierra la ventana
    def cerrar_ventana(self):
        self.close()

class Ui_agregar_amigosV(QtWidgets.QDialog, Ui_agregar_amigos):
    def _init_(self):
        super()._init_()
        self.setupUi(self)

