import sys
from collections import Counter
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from PyQt5 import uic
Ui_MainWindow, QtBaseClass = uic.loadUiType('EditorUI.ui')

class MyApp(QMainWindow):
    def __init__(self):
        self.newLines = 1
        super(MyApp, self).__init__(None)
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')

        # New Action
        self.newAction = QAction('&New', self)
        self.newAction.triggered.connect(self.NewCall)
        fileMenu.addAction(self.newAction)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def NewCall(self):
        print('new')

if __name__ == '__main__':
    pyqtRemoveInputHook()
    app = QApplication(sys.argv)
    window = MyApp()
    window.setWindowTitle('PyEditor')
    window.showMaximized()
    window.show()
    sys.exit(app.exec())
