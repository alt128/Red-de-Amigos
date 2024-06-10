import sys
from PyQt5 import QtWidgets
from inicio_sesionV import Ui_inicio_sesion

class MainWindow(QtWidgets.QWidget, Ui_inicio_sesion):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Aquí puedes agregar tus conexiones de señales y slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

