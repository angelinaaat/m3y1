from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from password import Ui_MainWindow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

pushButton.clicked.connect(generation)

app = QApplication([])
ex = Widget()

def generation():
    digital = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letter = ['g', 'l', 'm', 'q', 'w', 't', 'r', 'g', 'y', 'p']



pushButton.clicked.connect(generation)
 
ex.show()
app.exec_()
