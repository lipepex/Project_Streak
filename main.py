#Modulos
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QComboBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
import Ui

#Class
class Home(QWidget):

    #Construtor
    def __init__(self):
        super().__init__()
        Ui.initUI(self)
        self.settings()

    #App Settings
    def settings(self):
        self.setWindowTitle("Streaks")
        self.setGeometry(250,250,600,500)

    #Button Events
    def button_click(self):
        pass

    #Reset App
    def reset(self):
        pass

#Main Run

if __name__ == '__main__':
    app = QApplication([])
    main = Home()
    main.show()
    app.exec_()