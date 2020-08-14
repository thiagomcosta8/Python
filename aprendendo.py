from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, 
                            QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, 
                            QVBoxLayout)

import sys

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__()
        self.setWindowTitle("Hello World")
        self.button = QPushButton("Exibir mensagem")
        self.button.clicked.connect(self.exibir) #connection activated
        self.line_edit = QLineEdit()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.layout.addStretch(1)
        self.botao = QPushButton("Teste de QHBox")
        self.layout.addWidget(self.botao)

    def exibir(self):
        self.text = self.line_edit.text()
        self.message_box = QMessageBox.information(self, "Exemplo 1", self.text)

root = QApplication([])
app = Window()
app.show()
sys.exit(root.exec_())

