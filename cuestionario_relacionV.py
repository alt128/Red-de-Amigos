import sys
from PyQt5 import QtWidgets, QtCore
from usuarioClass import Usuario
from graphClass import Graph
import random


comida = ["Pizza", "Sushi", "Hamburguesa", "Ensalada", "Pasta", "Tacos", "Sandwich", "Parrillada", "Mariscos", "Helado"]
pelicula = ["El Padrino", "Titanic", "El Senor de los Anillos", "Avatar", "Harry Potter", "Star Wars", "Matrix", "Jurassic Park", "Indiana Jones", "Forrest Gump"]
lugar = ["Playa", "Montana", "Ciudad", "Campo", "Parque", "Bosque", "Desierto", "Lago", "Rio", "Pueblo"]
hobby = ["Deportes", "Leer", "Viajar", "Pintar", "Cocinar", "Bailar", "Fotografia", "Jardineria", "Musica", "Videojuegos"]
fobia = ["Aranas", "Alturas", "Espacios cerrados", "Multitudes", "Insectos", "Serpientes", "Oscuridad", "Agujas", "Perros", "Volar"]
carrera = ["Medicina", "Ingenieria", "Arquitectura", "Derecho", "Psicologia", "Administracion", "Biologia", "Economia", "Diseno", "Educacion"]
ciclo = ["Primer ciclo", "Segundo ciclo", "Tercer ciclo", "Cuarto ciclo", "Quinto ciclo", "Sexto ciclo", "Septimo ciclo", "Octavo ciclo", "Noveno ciclo", "Decimo ciclo"]
vive = ["Ciudad", "Pueblo", "Suburbio", "Campo", "Costa", "Montana", "Interior", "Extranjero", "Otro"]
novia = ["Si", "No"]

class Ui_cuestionario_relacion(object):
    def setupUi(self, cuestionario_relacion):
        self.puerta = False #sirve para activar la interfaz a parti de que ventana se ingresa
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
        self.cbLugarFavorito.setObjectName("cbLugarFavorito")

        self.cbCiclo = QtWidgets.QComboBox(cuestionario_relacion)
        self.cbCiclo.setGeometry(QtCore.QRect(350, 555, 241, 31))
        self.cbCiclo.setStyleSheet("font: 400 12pt 'Manrope'; color: rgb(255, 255, 255);")
        self.cbCiclo.addItems(["Primer ciclo", "Segundo ciclo", "Tercer ciclo", "Cuarto ciclo", "Quinto ciclo", "Sexto ciclo", "Septimo ciclo", "Octavo ciclo", "Noveno ciclo", "Decimo ciclo"])
        self.cbCiclo.setObjectName("cbCiclo")

        self.cbFobia = QtWidgets.QComboBox(cuestionario_relacion)
        self.cbFobia.setGeometry(QtCore.QRect(1000, 205, 241, 31))
        self.cbFobia.setStyleSheet("font: 400 12pt 'Manrope'; color: rgb(255, 255, 255);")
        self.cbFobia.setObjectName("cbFobia")

        self.cbComidaFavorita = QtWidgets.QComboBox(cuestionario_relacion)
        self.cbComidaFavorita.setGeometry(QtCore.QRect(350, 305, 241, 31))
        self.cbComidaFavorita.setStyleSheet("font: 400 12pt 'Manrope'; color: rgb(255, 255, 255);")
        self.cbComidaFavorita.setObjectName("cbComidaFavorita")

        self.line = QtWidgets.QFrame(cuestionario_relacion)
        self.line.setGeometry(QtCore.QRect(20, 20, 1261, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.cbHobby = QtWidgets.QComboBox(cuestionario_relacion)
        self.cbHobby.setGeometry(QtCore.QRect(350, 205, 241, 31))
        self.cbHobby.setStyleSheet("font: 400 12pt 'Manrope'; color: rgb(255, 255, 255);")
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
        self.cbPeliculaFavorita.setObjectName("cbPeliculaFavorita")

        self.cbCiudadDomicilio = QtWidgets.QComboBox(cuestionario_relacion)
        self.cbCiudadDomicilio.setGeometry(QtCore.QRect(1000, 395, 241, 31))
        self.cbCiudadDomicilio.setStyleSheet("font: 400 12pt 'Manrope'; color: rgb(255, 255, 255);")
        self.cbCiudadDomicilio.setObjectName("cbCiudadDomicilio")

        self.cbCarrera = QtWidgets.QComboBox(cuestionario_relacion)
        self.cbCarrera.setGeometry(QtCore.QRect(1000, 555, 241, 31))
        self.cbCarrera.setStyleSheet("font: 400 12pt 'Manrope'; color: rgb(255, 255, 255);")
        self.cbCarrera.setObjectName("Carrera")

        self.lblCarrera = QtWidgets.QLabel(cuestionario_relacion)
        self.lblCarrera.setGeometry(QtCore.QRect(670, 550, 111, 41))
        self.lblCarrera.setStyleSheet("font: 700 16pt 'Inter'; color: rgb(19, 44, 74);")
        self.lblCarrera.setObjectName("lblCarrera")

        self.lblNumHermanos = QtWidgets.QLabel(cuestionario_relacion)
        self.lblNumHermanos.setGeometry(QtCore.QRect(670, 300, 311, 41))
        self.lblNumHermanos.setStyleSheet("font: 700 16pt 'Inter'; color: rgb(19, 44, 74);")
        self.lblNumHermanos.setObjectName("lblNumHermanos")

        self.btnTerminar = QtWidgets.QPushButton(cuestionario_relacion)
        self.btnTerminar.setGeometry(QtCore.QRect(550, 700, 221, 35))
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

        #atributos funcionales
        self.usuarioLogueado = Usuario( 101,"Juan Pérez",[],"password123","Pizza", "Inception","Playa","Leer","Alturas","Ingeniería en Sistemas",2,5,"Ciudad de México","Si",[])
        self.graphUsuarios = Graph()
        self.usuarioAmigo = Usuario( 101,"Juan Pérez",[],"password123","Pizza", "Inception","Playa","Leer","Alturas","Ingeniería en Sistemas",2,5,"Ciudad de México","Si",[])
        self.resultadoCuestionarioUsuarioSolicitoAmistad = 0

        # Asignacion de funciones a los botones
        self.btnExit.clicked.connect(self.cerrar_ventana)

    def setPuerta(self,puerta):
        self.puerta=puerta
        if self.puerta is True:
            self.btnTerminar.clicked.connect(self.modificar_solicitudes_amistad)
        else:
            self.btnTerminar.clicked.connect(self.aceptar_solicitud_amistad)
    #metodos
    def setUsuarioLogueado(self, usuario):
        self.usuarioLogueado = usuario

    def setGraphUsuarios(self, graph):
        self.graphUsuarios = graph
    
    def setUsuarioAmigo(self, usuario):
        self.usuarioAmigo = usuario
    
    def setResultadoCuestionarioUsuarioSolicitoAmistad(self, resultado_cuestionario):
        self.resultadoCuestionarioUsuarioSolicitoAmistad = resultado_cuestionario

    def setearComboBoxes(self):
        _translate = QtCore.QCoreApplication.translate
        nombre = "¿Qué tanto sabes de " + self.usuarioAmigo.nombre + "?"
        self.titulo.setText(_translate("cuestionario_relacion", nombre ))

        # Obtén valores aleatorios y mezcla el valor real del usuarioAmigo
        def obtenerItems(lista, valorReal):
            items = random.sample(lista, 4)  # Obtener 4 items aleatorios
            while valorReal in items:  # Asegurarse de que el valor real no esté en los aleatorios
                items = random.sample(lista, 4)
            items.append(valorReal)
            random.shuffle(items)  # Mezclar los items para que el valor real no esté siempre en la misma posición
            return items

        # Asignar los items a los ComboBoxes
        self.cbComidaFavorita.addItems(obtenerItems(comida, self.usuarioAmigo.comida_favorita))
        self.cbPeliculaFavorita.addItems(obtenerItems(pelicula, self.usuarioAmigo.pelicula_favorita))
        self.cbLugarFavorito.addItems(obtenerItems(lugar, self.usuarioAmigo.lugar_favorito))
        self.cbHobby.addItems(obtenerItems(hobby, self.usuarioAmigo.hobby))
        self.cbFobia.addItems(obtenerItems(fobia, self.usuarioAmigo.fobia))
        self.cbCarrera.addItems(obtenerItems(carrera, self.usuarioAmigo.carrera))
        self.cbCiudadDomicilio.addItems(obtenerItems(vive, self.usuarioAmigo.donde_vive))

    def resultadoCuestionario(self):
        resultado_cuestionario = 0

        hobby = self.cbHobby.currentText()
        fobia = self.cbFobia.currentText()
        comida_favorita = self.cbComidaFavorita.currentText
        num_hermanos = int(self.cbNumHermanos.currentText())
        pelicula_favorita = self.cbPeliculaFavorita.currentText
        ciudad_domicilio = self.cbCiudadDomicilio.currentText()
        lugar_favorito = self.cbLugarFavorito.currentText()
        tiene_novia = self.cbTieneNovia.currentText()
        ciclo = self.cbCiclo.currentText()
        carrera = self.cbCarrera.currentText()

        if hobby == self.usuarioAmigo.hobby: resultado_cuestionario = resultado_cuestionario+1
        if fobia == self.usuarioAmigo.fobia: resultado_cuestionario = resultado_cuestionario+1
        if comida_favorita == self.usuarioAmigo.comida_favorita: resultado_cuestionario = resultado_cuestionario+1
        if num_hermanos == self.usuarioAmigo.numero_hermanos: resultado_cuestionario = resultado_cuestionario+1
        if pelicula_favorita == self.usuarioAmigo.pelicula_favorita: resultado_cuestionario = resultado_cuestionario+1
        if ciudad_domicilio == self.usuarioAmigo.donde_vive: resultado_cuestionario = resultado_cuestionario+1
        if lugar_favorito == self.usuarioAmigo.lugar_favorito: resultado_cuestionario = resultado_cuestionario+1
        if tiene_novia == self.usuarioAmigo.tiene_novia: resultado_cuestionario = resultado_cuestionario+1
        if ciclo == self.usuarioAmigo.ciclo: resultado_cuestionario = resultado_cuestionario+1
        if carrera == self.usuarioAmigo.carrera: resultado_cuestionario = resultado_cuestionario+1

        return resultado_cuestionario


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
        self.lblCarrera.setText(_translate("cuestionario_relacion", "Carrera:"))
    
    def cerrar_ventana(self):
        QtWidgets.QMessageBox.information(self, "Aviso", "Tu progreso no sera guardado. Solicitud de amistad no enviada")
        self.close()

class Ui_cuestionario_relacionV(QtWidgets.QDialog, Ui_cuestionario_relacion):
    def _init_(self):
        super()._init_()
        self.setupUi(self)

if _name_ == "_main_":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_cuestionario_relacionV()
    window.show()
    sys.exit(app.exec_())
