from PyQt5 import QtCore, QtGui, QtWidgets
from usuarioClass import Usuario, agregar_usuario_a_json

class Ui_crear_cuenta(QtWidgets.QDialog):
    # para añadir un id no existente
    idMayor = 0
    
    def __init__(self, parent=None):
        super(Ui_crear_cuenta, self).__init__(parent)
        self.setupUi(self)
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1300, 800)
        Dialog.setStyleSheet("background-color: rgb(10, 125, 208);")
        
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(100, 50, 81, 71))
        self.btnExit.setStyleSheet("font: 700 20pt 'Manrope';\n"
                                   "color: rgb(19, 44, 74);\n"
                                   "background-color: rgb(0, 148, 255);")
        self.btnExit.setObjectName("btnExit")
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 10, 1261, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 755, 1261, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(300, 30, 840, 121))
        self.titulo.setStyleSheet("font: 700 35pt 'Manrope';\n"
                                  "color: rgb(255, 255, 255);")
        self.titulo.setObjectName("titulo")
        
        self.lblNombre = QtWidgets.QLabel(self.centralwidget)
        self.lblNombre.setGeometry(QtCore.QRect(60, 190, 131, 41))
        self.lblNombre.setStyleSheet("font: 700 16pt 'Inter';\n"
                                     "color: rgb(255, 255, 255);")
        self.lblNombre.setObjectName("lblNombre")
        
        self.inputNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNombre.setGeometry(QtCore.QRect(330, 190, 251, 41))
        self.inputNombre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "font: 14pt 'Segoe UI';")
        self.inputNombre.setObjectName("inputNombre")
        
        self.btnCrearCuenta = QtWidgets.QPushButton(self.centralwidget)
        self.btnCrearCuenta.setGeometry(QtCore.QRect(520, 680, 221, 35))
        self.btnCrearCuenta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCrearCuenta.setStyleSheet("background-color: rgb(19, 44, 74);\n"
                                          "font: 12pt 'Inter';\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-color: rgb(10, 125, 208);")
        self.btnCrearCuenta.setObjectName("btnCrearCuenta")
        
        self.lblContrasenia = QtWidgets.QLabel(self.centralwidget)
        self.lblContrasenia.setGeometry(QtCore.QRect(60, 270, 171, 41))
        self.lblContrasenia.setStyleSheet("font: 700 16pt 'Inter';\n"
                                          "color: rgb(255, 255, 255);")
        self.lblContrasenia.setObjectName("lblContrasenia")
        
        self.lblComidaFavorita = QtWidgets.QLabel(self.centralwidget)
        self.lblComidaFavorita.setGeometry(QtCore.QRect(60, 350, 241, 41))
        self.lblComidaFavorita.setStyleSheet("font: 700 16pt 'Inter';\n"
                                             "color: rgb(255, 255, 255);")
        self.lblComidaFavorita.setObjectName("lblComidaFavorita")
        
        self.lblPeliculaFavorita = QtWidgets.QLabel(self.centralwidget)
        self.lblPeliculaFavorita.setGeometry(QtCore.QRect(60, 430, 241, 41))
        self.lblPeliculaFavorita.setStyleSheet("font: 700 16pt 'Inter';\n"
                                               "color: rgb(255, 255, 255);")
        self.lblPeliculaFavorita.setObjectName("lblPeliculaFavorita")
        
        self.lblLugarFavorito = QtWidgets.QLabel(self.centralwidget)
        self.lblLugarFavorito.setGeometry(QtCore.QRect(60, 510, 211, 41))
        self.lblLugarFavorito.setStyleSheet("font: 700 16pt 'Inter';\n"
                                            "color: rgb(255, 255, 255);")
        self.lblLugarFavorito.setObjectName("lblLugarFavorito")
        
        self.lblHobby = QtWidgets.QLabel(self.centralwidget)
        self.lblHobby.setGeometry(QtCore.QRect(60, 590, 111, 41))
        self.lblHobby.setStyleSheet("font: 700 16pt 'Inter';\n"
                                    "color: rgb(255, 255, 255);")
        self.lblHobby.setObjectName("lblHobby")
        
        self.lblFobia = QtWidgets.QLabel(self.centralwidget)
        self.lblFobia.setGeometry(QtCore.QRect(650, 190, 111, 41))
        self.lblFobia.setStyleSheet("font: 700 16pt 'Inter';\n"
                                    "color: rgb(255, 255, 255);")
        self.lblFobia.setObjectName("lblFobia")
        
        self.lblNumHermanos = QtWidgets.QLabel(self.centralwidget)
        self.lblNumHermanos.setGeometry(QtCore.QRect(650, 350, 311, 41))
        self.lblNumHermanos.setStyleSheet("font: 700 16pt 'Inter';\n"
                                          "color: rgb(255, 255, 255);")
        self.lblNumHermanos.setObjectName("lblNumHermanos")

        self.lblCarrera = QtWidgets.QLabel(self.centralwidget)
        self.lblCarrera.setGeometry(QtCore.QRect(650, 270, 311, 41))
        self.lblCarrera.setStyleSheet("font: 700 16pt 'Inter';\n"
                                          "color: rgb(255, 255, 255);")
        self.lblCarrera.setObjectName("lblCarrera")
        
        self.lblTienesNovia = QtWidgets.QLabel(self.centralwidget)
        self.lblTienesNovia.setGeometry(QtCore.QRect(650, 510, 291, 41))
        self.lblTienesNovia.setStyleSheet("font: 700 16pt 'Inter';\n"
                                          "color: rgb(255, 255, 255);")
        self.lblTienesNovia.setObjectName("lblTienesNovia")
        
        self.lblCiclo = QtWidgets.QLabel(self.centralwidget)
        self.lblCiclo.setGeometry(QtCore.QRect(650, 590, 91, 41))
        self.lblCiclo.setStyleSheet("font: 700 16pt 'Inter';\n"
                                    "color: rgb(255, 255, 255);")
        self.lblCiclo.setObjectName("lblCiclo")
        
        self.LblCiudadDomicilio = QtWidgets.QLabel(self.centralwidget)
        self.LblCiudadDomicilio.setGeometry(QtCore.QRect(650, 430, 281, 41))
        self.LblCiudadDomicilio.setStyleSheet("font: 700 16pt 'Inter';\n"
                                              "color: rgb(255, 255, 255);")
        self.LblCiudadDomicilio.setObjectName("LblCiudadDomicilio")
        
        self.inputContrasenia = QtWidgets.QLineEdit(self.centralwidget)
        self.inputContrasenia.setGeometry(QtCore.QRect(330, 270, 251, 41))
        self.inputContrasenia.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "font: 14pt 'Segoe UI';")
        self.inputContrasenia.setObjectName("inputContrasenia")
        
        self.inputComidaFavorita = QtWidgets.QLineEdit(self.centralwidget)
        self.inputComidaFavorita.setGeometry(QtCore.QRect(330, 350, 251, 41))
        self.inputComidaFavorita.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "font: 14pt 'Segoe UI';")
        self.inputComidaFavorita.setObjectName("inputComidaFavorita")
        
        self.inputPeliculaFavorita = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPeliculaFavorita.setGeometry(QtCore.QRect(330, 430, 251, 41))
        self.inputPeliculaFavorita.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 14pt 'Segoe UI';")
        self.inputPeliculaFavorita.setObjectName("inputPeliculaFavorita")
        
        self.inputLugarFavorito = QtWidgets.QLineEdit(self.centralwidget)
        self.inputLugarFavorito.setGeometry(QtCore.QRect(330, 510, 251, 41))
        self.inputLugarFavorito.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "font: 14pt 'Segoe UI';")
        self.inputLugarFavorito.setObjectName("inputLugarFavorito")
        
        self.inputHobby = QtWidgets.QLineEdit(self.centralwidget)
        self.inputHobby.setGeometry(QtCore.QRect(330, 590, 251, 41))
        self.inputHobby.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 14pt 'Segoe UI';")
        self.inputHobby.setObjectName("inputHobby")
        
        self.inputFobia = QtWidgets.QLineEdit(self.centralwidget)
        self.inputFobia.setGeometry(QtCore.QRect(990, 190, 251, 41))
        self.inputFobia.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 14pt 'Segoe UI';")
        self.inputFobia.setObjectName("inputFobia")

        self.inputCiudadDomicilio = QtWidgets.QLineEdit(self.centralwidget)
        self.inputCiudadDomicilio.setGeometry(QtCore.QRect(990, 430, 251, 41))
        self.inputCiudadDomicilio.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 14pt 'Segoe UI';")
        self.inputCiudadDomicilio.setObjectName("inputCiudadDomicilio")
        
        self.inputNumHermanos = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNumHermanos.setGeometry(QtCore.QRect(990, 350, 251, 41))
        self.inputNumHermanos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "font: 14pt 'Segoe UI';")
        self.inputNumHermanos.setObjectName("inputNumHermanos")

        self.inputCarrera = QtWidgets.QLineEdit(self.centralwidget)
        self.inputCarrera.setGeometry(QtCore.QRect(990, 270, 251, 41))
        self.inputCarrera.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "font: 14pt 'Segoe UI';")
        self.inputCarrera.setObjectName("inputCarrera")
        
        self.inputCiclo = QtWidgets.QLineEdit(self.centralwidget)
        self.inputCiclo.setGeometry(QtCore.QRect(990, 590, 251, 41))
        self.inputCiclo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 14pt 'Segoe UI';")
        self.inputCiclo.setObjectName("inputCiclo")
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(990, 510, 251, 41))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "font: 14pt 'Segoe UI';")
        self.comboBox.setObjectName("comboBox")
        
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        # Asignación de funciones a los botones
        self.btnExit.clicked.connect(self.salir)
        self.btnCrearCuenta.clicked.connect(self.crear_cuenta)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def salir(self):
        QtWidgets.QMessageBox.information(self, "ALERTA", "Su progreso no será guardado")
        self.reject()

    def crear_cuenta(self):
        # Obtener valores de los inputs
        nombre = self.inputNombre.text()
        contrasenia = self.inputContrasenia.text()
        comida_favorita = self.inputComidaFavorita.text()
        pelicula_favorita = self.inputPeliculaFavorita.text()
        lugar_favorito = self.inputLugarFavorito.text()
        hobby = self.inputHobby.text()
        fobia = self.inputFobia.text()
        carrera = self.inputCarrera.text()
        num_hermanos = self.inputNumHermanos.text()
        tienes_novia = self.comboBox.currentText()
        ciclo = self.inputCiclo.text()
        ciudad_domicilio = self.inputCiudadDomicilio.text()
        # Valida que ninguno de los campos este vacio
        if not all([nombre, contrasenia, comida_favorita, pelicula_favorita, lugar_favorito, hobby, fobia, carrera, num_hermanos, tienes_novia, ciclo, ciudad_domicilio]):
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Todos los campos deben estar llenos")
            return
        
        nuevo_usuario = Usuario(
            self.idMayor + 1,
            nombre,
            [],
            contrasenia,
            comida_favorita,
            pelicula_favorita,
            lugar_favorito,
            hobby,
            fobia,
            num_hermanos,
            carrera,
            ciclo,
            ciudad_domicilio,
            tienes_novia,
            []
        )
        # Añadir usuario al archivo JSON
        agregar_usuario_a_json(nuevo_usuario, 'usuarios.json')
        
        QtWidgets.QMessageBox.information(self, "Creación de cuenta", "Cuenta creada y almacenada en la base de datos")
        self.accept()

    # Setter idMayor
    def setidMayor(self, idMayor):
        self.idMayor = idMayor

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Crear cuenta"))
        self.btnExit.setText(_translate("Dialog", "<-"))
        self.titulo.setText(_translate("Dialog", "FORMULARIO DE REGISTRO"))
        self.lblNombre.setText(_translate("Dialog", "Nombre:"))
        self.btnCrearCuenta.setText(_translate("Dialog", "Crear Cuenta"))
        self.lblContrasenia.setText(_translate("Dialog", "Contraseña:"))
        self.lblComidaFavorita.setText(_translate("Dialog", "Comida Favorita:"))
        self.lblPeliculaFavorita.setText(_translate("Dialog", "Película Favorita:"))
        self.lblLugarFavorito.setText(_translate("Dialog", "Lugar Favorito:"))
        self.lblHobby.setText(_translate("Dialog", "Hobby:"))
        self.lblFobia.setText(_translate("Dialog", "Fobia:"))
        self.lblCarrera.setText(_translate("Dialog", "Carrera:"))
        self.lblNumHermanos.setText(_translate("Dialog", "Número de Hermanos:"))
        self.lblTienesNovia.setText(_translate("Dialog", "¿Tienes Novia?:"))
        self.lblCiclo.setText(_translate("Dialog", "Ciclo:"))
        self.LblCiudadDomicilio.setText(_translate("Dialog", "Ciudad de Domicilio:"))
        self.comboBox.setItemText(0, _translate("Dialog", "Si"))
        self.comboBox.setItemText(1, _translate("Dialog", "No"))
