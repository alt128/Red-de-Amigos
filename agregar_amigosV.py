from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from graphClass import Graph
from usuarioClass import Usuario
from cuestionario_relacionV import Ui_cuestionario_relacionV

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
        self.btnEnviarSolicitud.setEnabled(False)
        
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
        self.btnBuscar.clicked.connect(self.buscar_amigo)
        self.btnEnviarSolicitud.clicked.connect(self.cuestionario_relacion_amigo)

        #atributos funcionales
        self.usuarioLogueado = Usuario( 101,"Juan Pérez",[],"password123","Pizza", "Inception","Playa","Leer","Alturas","Ingeniería en Sistemas",2,5,"Ciudad de México","Si",[])
        self.graphUsuarios = Graph()
        self.usuarioAmigo = Usuario( 101,"Juan Pérez",[],"password123","Pizza", "Inception","Playa","Leer","Alturas","Ingeniería en Sistemas",2,5,"Ciudad de México","Si",[])

    #metodos
    def setUsuarioLogueado(self, usuario):
        self.usuarioLogueado = usuario

    def setGraphUsuarios(self, graph):
        self.graphUsuarios = graph
        
    def buscar_amigo(self):
        nombre = self.inputNombre.text()
        self.usuarioAmigo = self.graphUsuarios.buscar_usuario_bfs(nombre)
        if isinstance(self.usuarioAmigo, Usuario):
            self.btnEnviarSolicitud.setEnabled(True) #activa el boton Enviar Solicitud
            label = QLabel()

            image_path = "user.png"
            pixmap = QtGui.QPixmap(image_path)
            label.setPixmap(pixmap)
            label.resize(pixmap.width(), pixmap.height())
            
            layout = QVBoxLayout()
            layout.addWidget(label)
            self.frame.setLayout(layout)
        else:
            QtWidgets.QMessageBox.information(self, "Aviso", "Usuario no encontrado")
    
    def cuestionario_relacion_amigo(self):
        #eliminar la imagen del frame
        label = self.frame.findChild(QLabel)
        label.clear()
        self.frame.layout().deleteLater()
        window = Ui_cuestionario_relacionV()
        window.setPuerta(True)
        window.setUsuarioLogueado(self.usuarioLogueado)
        window.setUsuarioAmigo(self.usuarioAmigo)
        window.setearComboBoxes()
        window.exec()

    def retranslateUi(self, agregar_amigos):
        _translate = QtCore.QCoreApplication.translate
        agregar_amigos.setWindowTitle(_translate("agregar_amigos", "Agregar amigos"))
        self.btnExit.setText(_translate("agregar_amigos", "<-"))
        self.lblNombre.setText(_translate("agregar_amigos", "Nombre:"))
        self.titulo.setText(_translate("agregar_amigos", "AGREGAR AMIGOS"))
        self.btnBuscar.setText(_translate("agregar_amigos", "Buscar"))
        self.btnEnviarSolicitud.setText(_translate("agregar_amigos", "Enviar solicitud"))
    
    #funcion que cierra la ventana
    def cerrar_ventana(self):
        self.close()

class Ui_agregar_amigosV(QtWidgets.QDialog, Ui_agregar_amigos):
    def _init_(self):
        super()._init_()
        self.setupUi(self)
