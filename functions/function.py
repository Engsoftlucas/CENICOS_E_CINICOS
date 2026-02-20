import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("dashboard/aba_dashboard.ui", self)

app = QApplication(sys.argv)

janela = Dashboard()
janela.show()

sys.exit(app.exec_())