from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QComboBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout

#Objeto e Design
def initUI(self):
    
    self.title = QLabel("As tuas streaks")
    self.input_box = QTextEdit()
    self.output_box = QTextEdit()
    self.button1 = QPushButton("Streak 1")
    self.button2 = QPushButton("Streak 2")
    self.button3 = QPushButton("Streak 3")
    self.button4 = QPushButton("Streak 4")
    self.input_option = QComboBox()

    self.master = QVBoxLayout()

    linha1 = QHBoxLayout()
    linha2 = QHBoxLayout()
    linha3 = QHBoxLayout()

    linha1.addWidget(self.title)

    linha2.addWidget(self.button1)
    linha2.addWidget(self.button2)

    linha3.addWidget(self.button3)
    linha3.addWidget(self.button4)

    self.master.addLayout(linha1, 10)
    self.master.addLayout(linha2, 45)
    self.master.addLayout(linha3, 45)

    self.setLayout(self.master)
