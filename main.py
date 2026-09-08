#Modulos
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QComboBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout

#Class
class Home(QWidget):

    #Construtor
    def __init__(self):
        super().__init__()
        self.initUI()

    #Objeto e Design
    def initUI(self):
        self.title = QLabel("Streaks")
        self.input_box = QTextEdit()
        self.output_box = QTextEdit()
        self.button1 = QPushButton("HEY CLICK ME")
        self.input_option = QComboBox()

        self.master = QHBoxLayout()

        coluna1 = QVBoxLayout()
        coluna2 = QVBoxLayout()
        coluna3 = QVBoxLayout()

        coluna1.addWidget(self.title)

        coluna2.addWidget(self.input_box)
        coluna2.addWidget(self.output_box)
        coluna2.addWidget(self.button1)

        coluna3.addWidget(self.input_option)

        self.master.addLayout(coluna1, 20)
        self.master.addLayout(coluna2, 60)
        self.master.addLayout(coluna3, 20)

        self.setLayout(self.master)


    #App Settings
    def settings(self):
        pass

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