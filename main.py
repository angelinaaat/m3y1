
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from password import Ui_MainWindow
import random

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_OK.clicked.connect(self.generate)

    def generate(self):
        s_number = '0123456789'
        s_alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        pas = ''
        if self.ui.cb_number.isChecked():
            for i in range(16):
                pas = pas + random.choice(s_number)
        
        if self.ui.cb_alphabet.isChecked():
            for i in range(16):
                pas = pas + random.choice(s_alphabet)


        if self.ui.cb_number.isChecked() and self.ui.cb_alphabet.isClicked():
            for i in range(16):
                pas = pas + random.choice(s_number + s_alphabet)

        self.ui.result.setText(pas)


pushButton.clicked.connect(generation)

app = QApplication([])
ex = Widget()

pushButton.clicked.connect(generation)
 
ex.show()
app.exec_()
