from PyQt5 import QtWidgets, QtCore, QtGui
class Ui_amigos_potenciales(object):
    def setupUi(self, amigos_potenciales):
        amigos_potenciales.setObjectName("Amigos potenciales")
        amigos_potenciales.resize(1300, 800)
        amigos_potenciales.setStyleSheet("background-color: rgb(10, 125, 208);")

        self.btnBuscar = QtWidgets.QPushButton(amigos_potenciales)
        self.btnBuscar.setGeometry(QtCore.QRect(1040, 160, 101, 35))
        self.btnBuscar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBuscar.setStyleSheet("background-color: rgb(19, 44, 74);\n" "font: 12pt \"Inter\";\n" "color: rgb(255, 255, 255);\n""border-color: rgb(10, 125, 208);")
        self.btnBuscar.setObjectName("btnBuscar")

        self.titulo = QtWidgets.QLabel(amigos_potenciales)
        self.titulo.setGeometry(QtCore.QRect(330, 10, 691, 121))
        self.titulo.setStyleSheet("font: 700 35pt \"Manrope\";\n" "color: rgb(255, 255, 255);")
        self.titulo.setObjectName("titulo")

        self.btnExit = QtWidgets.QPushButton(amigos_potenciales)
        self.btnExit.setGeometry(QtCore.QRect(110, 40, 71, 61))
        self.btnExit.setStyleSheet("font: 700 20pt \"Manrope\";\n" "color: rgb(19, 44, 74);\n" "background-color: rgb(0, 148, 255);")
        self.btnExit.setObjectName("btnExit")

        self.comboBox = QtWidgets.QComboBox(amigos_potenciales)
        self.comboBox.setGeometry(QtCore.QRect(120, 160, 241, 31))
        self.comboBox.setStyleSheet("font: 400 12pt \"Manrope\";")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")

        items = [
            "Nombre", "Comida favorita", "Pelicula favorita", "Lugar favorito",
            "Hobby", "Fobia", "Carrera", "Numero de hermanos", "Ciclo de estudios",
            "Donde vive", "Tiene novia"
        ]
        self.comboBox.addItems(items)

        self.inputFiltro = QtWidgets.QLineEdit(amigos_potenciales)
        self.inputFiltro.setGeometry(QtCore.QRect(470, 150, 460, 41))
        self.inputFiltro.setStyleSheet("background-color: rgb(255, 255, 255);\n" "font: 14pt \"Segoe UI\";")
        self.inputFiltro.setObjectName("inputFiltro")

        self.frame = QtWidgets.QFrame(amigos_potenciales)
        self.frame.setGeometry(QtCore.QRect(230, 270, 821, 491))
        self.frame.setStyleSheet("background-color: rgb(9, 118, 195);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.lblGrafoGenerado = QtWidgets.QLabel(amigos_potenciales)
        self.lblGrafoGenerado.setGeometry(QtCore.QRect(570, 230, 141, 31))
        self.lblGrafoGenerado.setStyleSheet("font: 200 12pt \"Manrope\";\n" "color: rgb(255, 255, 255);")
        self.lblGrafoGenerado.setObjectName("lblGrafoGenerado")

        self.line = QtWidgets.QFrame(amigos_potenciales)
        self.line.setGeometry(QtCore.QRect(20, 10, 1261, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(amigos_potenciales)
        self.line_2.setGeometry(QtCore.QRect(20, 770, 1261, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(amigos_potenciales)
        QtCore.QMetaObject.connectSlotsByName(amigos_potenciales)

        #Asignacion de funciones a los botones
        self.btnExit.clicked.connect(self.cerrar_ventana)


    def retranslateUi(self, amigos_potenciales):
        _translate = QtCore.QCoreApplication.translate
        amigos_potenciales.setWindowTitle(_translate("amigos_potenciales", "Amigos potenciales"))
        self.btnBuscar.setText(_translate("amigos_potenciales", "Buscar"))
        self.titulo.setText(_translate("amigos_potenciales", "AMIGOS POTENCIALES"))
        self.btnExit.setText(_translate("amigos_potenciales", "<-"))
        self.lblGrafoGenerado.setText(_translate("amigos_potenciales", "Grafo generado"))
    
    def cerrar_ventana(self):
        self.close()

class Ui_amigos_potencialesV(QtWidgets.QDialog, Ui_amigos_potenciales):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
