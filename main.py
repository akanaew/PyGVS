import sys

from PyQt5 import QtWidgets

from Application import Application

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Application()
    application.show()
    sys.exit(app.exec())
