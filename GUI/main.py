from PyQt5.QtWidgets import * 
from PyQt5 import uic 

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('qtdes.ui', self)
        self.show()

def main():
    app = QApplication([])
    window = Window()
    app.exec_()

if __name__ == '__main__':
    main()