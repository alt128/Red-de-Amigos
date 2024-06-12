from PyQt5 import QtWidgets, QtCore

class Ui_cuestionario_relacion(object):
    def setupUi(self, cuestionario_relacion):
        cuestionario_relacion.setObjectName("cuestionario_relacion")
        cuestionario_relacion.resize(1300, 800)
        cuestionario_relacion.setStyleSheet("background-color: rgb(10, 125, 208);")

        self.LblCiudadDomicilio = QtWidgets.QLabel(cuestionario_relacion)
        self.LblCiudadDomicilio.setGeometry(QtCore.QRect(670, 390, 281, 41))
        self.LblCiudadDomicilio.setStyleSheet("font: 700 16pt 'Inter'; color: rgb(19, 44, 74);")
        self.LblCiudadDomicilio.setObjectName("LblCiudadDomicilio")

        self.lblLugarFavorito = QtWidgets.QLabel(cuestionario_relacion)
        self.lblLugarFavorito.setGeometry(QtCore.QRect(80, 470, 231, 41))
        self.lblLugarFavorito.setStyleSheet("font: 700 16pt 'Inter'; color: rgb(19, 44, 74);")
        self.lblLugarFavorito.setObjectName("lblLugarFavorito")

        self.cbNumHermanos = QtWidgets.QComboBox(cuestionario_relacion)
        self.cbNumHermanos.setGeometry(QtCore.QRect(1000, 305, 241, 31))
        self.cbNumHermanos.setStyleSheet("font: 400 12pt 'Manrope'; color: rgb(255, 255, 255);")
        self.cbNumHermanos.addItems(["0", "1", "2", "3", "4", "5", "6"])
        self.cbNumHermanos.setObjectName("cbNumHermanos")

        self.lblComidaFavorita = QtWidgets.QLabel(cuestionario_relacion)
        self.lblComidaFavorita.setGeometry(QtCore.QRect(80, 300, 231, 41))
        self.lblComidaFavorita.setStyleSheet("font: 700 16pt 'Inter'; color: rgb(19, 44, 74);")
        self.lblComidaFavorita.setObjectName("lblComidaFavorita")

        self.cbLugarFavorito = QtWidgets.QComboBox(cuestionario_relacion)
        self.cbLugarFavorito.setGeometry(QtCore.QRect(350, 475, 241, 31))
        self.cbLugarFavorito.setStyleSheet("font: 400 12pt 'Manrope'; color: rgb(255, 255, 255);")
        self.cbLugarFavorito.addItems(["Lugar favorito real", "no", "no", "no", "no", "no"])
        self.cbLugarFavorito.setObjectName("cbLugarFavorito")

        self.cbCiclo = QtWidgets.QComboBox(cuestionario_relacion)
        self.cbCiclo.setGeometry(QtCore.QRect(350, 555, 241, 31))
        self.cbCiclo.setStyleSheet("font: 400 12pt 'Manrope'; color: rgb(255, 255, 255);")
        self.cbCiclo.addItems(["Primer ciclo", "Segundo ciclo", "Tercer ciclo", "Cuarto ciclo", "Quinto ciclo", "Sexto ciclo", "Septimo ciclo", "Octavo ciclo", "Noveno ciclo", "Decimo ciclo"])
        self.cbCiclo.setObjectName("cbCiclo")

        self.cbFobia = QtWidgets.QComboBox(cuestionario_relacion)
        self.cbFobia.setGeometry(QtCore.QRect(1000, 205, 241, 31))
        self.cbFobia.setStyleSheet("font: 400 12pt 'Manrope'; color: rgb(255, 255, 255);")
        self.cbFobia.addItems(["Fobia real", "no", "no", "no", "no", "no"])
        self.cbFobia.setObjectName("cbFobia")

        self.cbComidaFavorita = QtWidgets.QComboBox(cuestionario_relacion)
        self.cbComidaFavorita.setGeometry(QtCore.QRect(350, 305, 241, 31))
        self.cbComidaFavorita.setStyleSheet("font: 400 12pt 'Manrope'; color: rgb(255, 255, 255);")
        self.cbComidaFavorita.addItems(["Comida favorita real", "No", "No", "No", "No", "No"])
        self.cbComidaFavorita.setObjectName("cbComidaFavorita")

        self.line = QtWidgets.QFrame(cuestionario_relacion)
        self.line.setGeometry(QtCore.QRect(20, 20, 1261, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.cbHobby = QtWidgets.QComboBox(cuestionario_relacion)
        self.cbHobby.setGeometry(QtCore.QRect(350, 205, 241, 31))
        self.cbHobby.setStyleSheet("font: 400 12pt 'Manrope'; color: rgb(255, 255, 255);")
        self.cbHobby.addItems(["Hobby real", "Hobby relleno", "Hobby relleno", "Hobby relleno", "Hobby relleno"])
        self.cbHobby.setObjectName("cbHobby")

        self.titulo = QtWidgets.QLabel(cuestionario_relacion)
        self.titulo.setGeometry(QtCore.QRect(230, 30, 1071, 121))
        self.titulo.setStyleSheet("font: 700 28pt 'Manrope'; color: rgb(255, 255, 255);")
        self.titulo.setObjectName("titulo")

        self.lblPeliculaFavorita = QtWidgets.QLabel(cuestionario_relacion)
        self.lblPeliculaFavorita.setGeometry(QtCore.QRect(80, 390, 241, 41))
        self.lblPeliculaFavorita.setStyleSheet("font: 700 16pt 'Inter'; color: rgb(19, 44, 74);")
        self.lblPeliculaFavorita.setObjectName("lblPeliculaFavorita")

        self.line_2 = QtWidgets.QFrame(cuestionario_relacion)
        self.line_2.setGeometry(QtCore.QRect(20, 765, 1261, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.lblHobby = QtWidgets.QLabel(cuestionario_relacion)
        self.lblHobby.setGeometry(QtCore.QRect(80, 200, 121, 41))
        self.lblHobby.setStyleSheet("font: 700 16pt 'Inter'; color: rgb(19, 44, 74);")
        self.lblHobby.setObjectName("lblHobby")

        self.cbTieneNovia = QtWidgets.QComboBox(cuestionario_relacion)
        self.cbTieneNovia.setGeometry(QtCore.QRect(1000, 475, 241, 31))
        self.cbTieneNovia.setStyleSheet("font: 400 12pt 'Manrope'; color: rgb(255, 255, 255);")
        self.cbTieneNovia.addItems(["Si", "No"])
        self.cbTieneNovia.setObjectName("cbTieneNovia")

        self.btnExit = QtWidgets.QPushButton(cuestionario_relacion)
        self.btnExit.setGeometry(QtCore.QRect(40, 50, 81, 71))
        self.btnExit.setStyleSheet("font: 700 20pt 'Manrope'; color: rgb(19, 44, 74); background-color: rgb(0, 148, 255);")
        self.btnExit.setObjectName("btnExit")

        self.lblFobia = QtWidgets.QLabel(cuestionario_relacion)
        self.lblFobia.setGeometry(QtCore.QRect(670, 200, 111, 41))
        self.lblFobia.setStyleSheet("font: 700 16pt 'Inter'; color: rgb(19, 44, 74);")
        self.lblFobia.setObjectName("lblFobia")

        self.cbPeliculaFavorita = QtWidgets.QComboBox(cuestionario_relacion)
        self.cbPeliculaFavorita.setGeometry(QtCore.QRect(350, 395, 241, 31))
        self.cbPeliculaFavorita.setStyleSheet("font: 400 12pt 'Manrope'; color: rgb(255, 255, 255);")
        self.cbPeliculaFavorita.addItems(["Pelicula favorita real", "no", "no", "no", "no"])
        self.cbPeliculaFavorita.setObjectName("cbPeliculaFavorita")

        self.cbCiudadDomicilio = QtWidgets.QComboBox(cuestionario_relacion)
        self.cbCiudadDomicilio.setGeometry(QtCore.QRect(1000, 395, 241, 31))
        self.cbCiudadDomicilio.setStyleSheet("font: 400 12pt 'Manrope'; color: rgb(255, 255, 255);")
        self.cbCiudadDomicilio.addItems(["Ciudad de domicilio real", "no", "no", "no", "no"])
        self.cbCiudadDomicilio.setObjectName("cbCiudadDomicilio")

        self.lblNumHermanos = QtWidgets.QLabel(cuestionario_relacion)
        self.lblNumHermanos.setGeometry(QtCore.QRect(670, 300, 311, 41))
        self.lblNumHermanos.setStyleSheet("font: 700 16pt 'Inter'; color: rgb(19, 44, 74);")
        self.lblNumHermanos.setObjectName("lblNumHermanos")

        self.btnTerminar = QtWidgets.QPushButton(cuestionario_relacion)
        self.btnTerminar.setGeometry(QtCore.QRect(840, 610, 221, 35))
        self.btnTerminar.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnTerminar.setStyleSheet("background-color: rgb(19, 44, 74); font: 12pt 'Inter'; color: rgb(255, 255, 255); border-color: rgb(10, 125, 208);")
        self.btnTerminar.setObjectName("btnTerminar")

        self.lblTieneNovia = QtWidgets.QLabel(cuestionario_relacion)
        self.lblTieneNovia.setGeometry(QtCore.QRect(670, 470, 181, 41))
        self.lblTieneNovia.setStyleSheet("font: 700 16pt 'Inter'; color: rgb(19, 44, 74);")
        self.lblTieneNovia.setObjectName("lblTieneNovia")

        self.lblCiclo = QtWidgets.QLabel(cuestionario_relacion)
        self.lblCiclo.setGeometry(QtCore.QRect(80, 550, 111, 41))
        self.lblCiclo.setStyleSheet("font: 700 16pt 'Inter'; color: rgb(19, 44, 74);")
        self.lblCiclo.setObjectName("lblCiclo")

        self.retranslateUi(cuestionario_relacion)
        self.btnExit.clicked.connect(cuestionario_relacion.close)
        QtCore.QMetaObject.connectSlotsByName(cuestionario_relacion)

        # Asignacion de funciones a los botones
        self.btnExit.clicked.connect(self.cerrar_ventana)

    def retranslateUi(self, cuestionario_relacion):
        _translate = QtCore.QCoreApplication.translate
        cuestionario_relacion.setWindowTitle(_translate("cuestionario_relacion", "Dialog"))
        self.LblCiudadDomicilio.setText(_translate("cuestionario_relacion", "Ciudad de domicilio:"))
        self.lblLugarFavorito.setText(_translate("cuestionario_relacion", "Lugar favorito:"))
        self.lblComidaFavorita.setText(_translate("cuestionario_relacion", "Comida favorita:"))
        self.titulo.setText(_translate("cuestionario_relacion", "¿Qué tanto sabes de User xxxxx?"))
        self.lblPeliculaFavorita.setText(_translate("cuestionario_relacion", "Pelicula favorita:"))
        self.lblHobby.setText(_translate("cuestionario_relacion", "Hobby:"))
        self.btnExit.setText(_translate("cuestionario_relacion", "<-"))
        self.lblFobia.setText(_translate("cuestionario_relacion", "Fobia:"))
        self.lblNumHermanos.setText(_translate("cuestionario_relacion", "Número de hermanos:"))
        self.btnTerminar.setText(_translate("cuestionario_relacion", "Terminar"))
        self.lblTieneNovia.setText(_translate("cuestionario_relacion", "Tiene novia:"))
        self.lblCiclo.setText(_translate("cuestionario_relacion", "Ciclo:"))
    
    def cerrar_ventana(self):
        self.close()

class Ui_cuestionario_relacionV(QtWidgets.QDialog, Ui_cuestionario_relacion):
    def _init_(self):
        super()._init_()
        self.setupUi(self)
