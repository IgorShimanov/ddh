import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QInputDialog, \
    QTextEdit, QLabel, QDesktopWidget


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("DDH")
        self.resize(529, 407)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_export = QtWidgets.QPushButton(self.centralwidget)
        self.btn_export.setMinimumSize(QtCore.QSize(25, 50))
        self.btn_export.setMaximumSize(QtCore.QSize(100, 50))
        self.btn_export.setObjectName("btn_export")
        self.gridLayout.addWidget(self.btn_export, 2, 1, 1, 1)
        self.btn_add_change = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_change.setMinimumSize(QtCore.QSize(25, 50))
        self.btn_add_change.setMaximumSize(QtCore.QSize(100, 50))
        self.btn_add_change.setObjectName("btn_add_change")
        self.gridLayout.addWidget(self.btn_add_change, 0, 1, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setMinimumSize(QtCore.QSize(25, 50))
        self.btn_delete.setMaximumSize(QtCore.QSize(100, 50))
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout.addWidget(self.btn_delete, 1, 1, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.btn_add_change.clicked.connect(self.add_change_delete)

        self.btn_delete.clicked.connect(self.add_change_delete)

        self.btn_export.clicked.connect(self.export)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("DDH", "DDH"))
        self.btn_export.setText(_translate("DDH", "Export"))
        self.btn_add_change.setText(_translate("DDH", "add/change"))
        self.btn_delete.setText(_translate("DDH", "delete"))

    def export(self):
        ans, okPress = QInputDialog.getItem(self, 'select', 'select the export file', ("html", "word"), 0, False)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def add_change_delete(self):
        ans, okPress = QInputDialog.getText(self, 'name function', 'input name function')





app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())