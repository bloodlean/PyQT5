import sys 
import typing
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QtWidget

class Window(QMainWindow):
    count = 0
    def __init__(self):
        super(Window, self).__init__()
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.bar = self.menuBar()

        file = self.bar.addMenu("File")
        file.addAction("New")
        file.addAction("Cascade")
        file.addAction("Tiled")
        file.addAction("Exit")
        file.triggered[QAction].connect(self.windowaction)
        self.setWindowTitle("PyQt5")

def windowaction(self, q):
    if q.text() == "New":
        Window.count = Window.count+1
        sub = QMdiSubWindow()
        sub.setWidget(QTextEdit())
        sub.setWindowTitle("subwindow"+str(Window.count))
        self.mdi.addSubWindow(sub)
        sub.show()

    if q.text() == "Cascade":
        self.mdi.cascadeSubWindow()

    if q.text() == "Tiled":
        self.mdi.titleSubWindow()

    if q.text == "Exit":
        sys.exit()

def main():
    app = QApplication([])
    project = Window()
    project.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()