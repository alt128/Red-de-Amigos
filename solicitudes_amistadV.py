from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QLabel
from usuarioClass import Usuario
from graphClass import Graph
from cuestionario_relacionV import Ui_cuestionario_relacionV

class Ui_solicitudes_amistad(object):
    def setupUi(self, solicitudes_amistad):
        solicitudes_amistad.setObjectName("Solicitudes de amistad")
        solicitudes_amistad.resize(1300, 800)
        solicitudes_amistad.setStyleSheet("background-color: rgb(10, 125, 208);")

        self.btnExit = QtWidgets.QPushButton(solicitudes_amistad)
        self.btnExit.setGeometry(QtCore.QRect(100, 50, 81, 71))
        self.btnExit.setStyleSheet("font: 700 20pt 'Manrope';" "color: rgb(19, 44, 74);" "background-color: rgb(0, 148, 255);")
        self.btnExit.setObjectName("btnExit")

        self.lblNombre = QtWidgets.QLabel(solicitudes_amistad)
        self.lblNombre.setGeometry(QtCore.QRect(420, 150, 500, 31))
        self.lblNombre.setStyleSheet("font: 500 14pt 'Manrope';" "color: rgb(255, 255, 255);")
        self.lblNombre.setObjectName("lblNombre")

        self.titulo = QtWidgets.QLabel(solicitudes_amistad)
        self.titulo.setGeometry(QtCore.QRect(280, 30, 801, 121))
        self.titulo.setStyleSheet("font: 700 35pt 'Manrope';" "color: rgb(255, 255, 255);")
        self.titulo.setObjectName("titulo")

        self.line = QtWidgets.QFrame(solicitudes_amistad)
        self.line.setGeometry(QtCore.QRect(20, 10, 1261, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.scrollArea = QtWidgets.QScrollArea(solicitudes_amistad)
        self.scrollArea.setGeometry(QtCore.QRect(200, 220, 871, 371))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 869, 369))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.scrollAreaWidgetContents_2.setLayout(self.layout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)


        self.line_2 = QtWidgets.QFrame(solicitudes_amistad)
        self.line_2.setGeometry(QtCore.QRect(20, 755, 1261, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        #atributos funcionales
        self.usuarioLogueado = Usuario( 101,"Juan Pérez",[],"password123","Pizza", "Inception","Playa","Leer","Alturas","Ingeniería en Sistemas",2,5,"Ciudad de México","Si",[])
        self.graphUsuarios = Graph()

        self.frame = QtWidgets.QFrame()

        self.retranslateUi(solicitudes_amistad)
        QtCore.QMetaObject.connectSlotsByName(solicitudes_amistad)

        # Asignacion de funciones a los botones
        self.btnExit.clicked.connect(self.cerrar_ventana)

    #metodos
    def setUsuarioLogueado(self, usuario):
        self.usuarioLogueado = usuario

    def setGraphUsuarios(self, graph):
        self.graphUsuarios = graph
    
    def mostrar_solicitudes_amistad(self):
        if not self.usuarioLogueado.solicitudes_amistad:
            # Si no hay solicitudes, mostrar un mensaje indicándolo
            self.frame.setStyleSheet("background-color: rgb(10, 125, 208);" "background-color: rgb(7, 84, 140);" "background-color: rgb(9, 118, 195);")
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setMinimumHeight(100) 
            lblNombrePA = QtWidgets.QLabel("No tienes solicitudes de amistad", self.frame)
            lblNombrePA.setGeometry(QtCore.QRect(40, 20, 400, 31))
            lblNombrePA.setStyleSheet("font: 700 14pt 'Manrope';" "color: rgb(255, 255, 255);")
            self.layout.addWidget(self.frame)
        else:
            # Agregar frames para cada solicitud de amistad
            for solicitud in self.usuarioLogueado.solicitudes_amistad:
                nombre_usuario = solicitud["nombre_usuario"]
                resultado_cuestionario = solicitud["resultado_cuestionario"]
                self.add_request_frame(self.layout, nombre_usuario, resultado_cuestionario)
    
    def aceptar_solicitud_amistad(self, nombre, resultado_cuestionario): #asociada al boton Aceptar solicitud
        window = Ui_cuestionario_relacionV()
        window.setPuerta(False)
        window.setUsuarioLogueado(self.usuarioLogueado)
        usuario_potencial_amigo = self.graphUsuarios.buscar_usuario_bfs(nombre)
        window.setUsuarioAmigo(usuario_potencial_amigo)
        window.setResultadoCuestionarioUsuarioSolicitoAmistad(resultado_cuestionario)
        window.setearComboBoxes()
        print("ventana cuestionario relacion seteado")
        window.exec()
        self.close()



    def retranslateUi(self, solicitudes_amistad):
        _translate = QtCore.QCoreApplication.translate
        solicitudes_amistad.setWindowTitle(_translate("solicitudes_amistad", "Solicitudes de amistad"))
        self.btnExit.setText(_translate("solicitudes_amistad", "<-"))
        self.lblNombre.setText(_translate("solicitudes_amistad", "¿Quiénes te seleccionaron como amigo?"))
        self.titulo.setText(_translate("solicitudes_amistad", "SOLICITUDES DE AMISTAD"))

    def add_request_frame(self, layout, nombre_usuario, resultado_cuestionario):
        frame = QtWidgets.QFrame()
        frame.setStyleSheet("background-color: rgb(10, 125, 208);" "background-color: rgb(7, 84, 140);" "background-color: rgb(9, 118, 195);")
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        frame.setMinimumHeight(100)  # Set a minimum height to ensure proper spacing

        lblNombrePA = QtWidgets.QLabel(nombre_usuario, frame)
        lblNombrePA.setGeometry(QtCore.QRect(40, 20, 191, 31))
        lblNombrePA.setStyleSheet("font: 700 14pt 'Manrope';" "color: rgb(255, 255, 255);")

        btnAceptarSolicitud = QtWidgets.QPushButton("Aceptar solicitud", frame)
        btnAceptarSolicitud.setGeometry(QtCore.QRect(450, 20, 211, 35))
        btnAceptarSolicitud.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btnAceptarSolicitud.setStyleSheet("background-color: rgb(19, 44, 74);" "font: 12pt 'Inter';" "color: rgb(255, 255, 255);" "border-color: rgb(10, 125, 208);")
        print(nombre_usuario)
        # Usar lambda para pasar los argumentos al método aceptar_solicitud_amistad
        btnAceptarSolicitud.clicked.connect(lambda _, nombre=nombre_usuario, resultado=resultado_cuestionario: self.aceptar_solicitud_amistad(nombre, resultado))

        layout.addWidget(frame)
    

    def cerrar_ventana(self):
        self.close()

class Ui_solicitudes_amistadV(QtWidgets.QDialog, Ui_solicitudes_amistad):
    def _init_(self):
        super()._init_()
        self.setupUi(self)
