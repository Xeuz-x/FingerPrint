from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(493, 544)
        MainWindow.setMaximumSize(QSize(493, 544))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.PasswordEntry = QPlainTextEdit(self.centralwidget)
        self.PasswordEntry.setObjectName(u"PasswordEntry")
        self.PasswordEntry.setGeometry(QRect(250, 440, 221, 41))
        font = QFont()
        font.setPointSize(11)
        self.PasswordEntry.setFont(font)
        self.PasswordEntry.setInputMethodHints(Qt.ImhNone)
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)

        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 20, 451, 361))
        self.tableWidget.setStyleSheet(u"QTableView::item:focus{selection-background-color: white;}")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(200, 410, 61, 16))
        self.EditButton = QPushButton(self.centralwidget)
        self.EditButton.setObjectName(u"EditButton")
        self.EditButton.setGeometry(QRect(20, 490, 211, 41))
        self.EditButton.setFont(font)
        self.AppendButton = QPushButton(self.centralwidget)
        self.AppendButton.setObjectName(u"AppendButton")
        self.AppendButton.setGeometry(QRect(250, 490, 221, 41))
        self.AppendButton.setFont(font)
        self.GenerateButton = QPushButton(self.centralwidget)
        self.GenerateButton.setObjectName(u"GenerateButton")
        self.GenerateButton.setGeometry(QRect(310, 390, 161, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.GenerateButton.setFont(font1)
        self.Length = QSpinBox(self.centralwidget)
        self.Length.setObjectName(u"Length")
        self.Length.setGeometry(QRect(260, 410, 41, 20))
        self.Length.setMaximum(20)
        self.Length.setValue(6)
        self.s_char_checkBox = QCheckBox(self.centralwidget)
        self.s_char_checkBox.setObjectName(u"s_char_checkBox")
        self.s_char_checkBox.setGeometry(QRect(200, 390, 111, 17))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(410, 0, 61, 16))
        self.UsernameEntry = QPlainTextEdit(self.centralwidget)
        self.UsernameEntry.setObjectName(u"UsernameEntry")
        self.UsernameEntry.setGeometry(QRect(20, 440, 211, 41))
        self.UsernameEntry.setFont(font)
        self.UsernameEntry.setInputMethodHints(Qt.ImhNone)
        self.WebsiteEntry = QPlainTextEdit(self.centralwidget)
        self.WebsiteEntry.setObjectName(u"WebsiteEntry")
        self.WebsiteEntry.setGeometry(QRect(20, 390, 171, 41))
        self.WebsiteEntry.setFont(font)
        self.WebsiteEntry.setInputMethodHints(Qt.ImhNone)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(210, 440, 61, 91))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Window Manager", None))
        self.PasswordEntry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Website", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.EditButton.setText(QCoreApplication.translate("MainWindow", u"Delete Selected", None))
        self.AppendButton.setText(QCoreApplication.translate("MainWindow", u"Append", None))
        self.GenerateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.s_char_checkBox.setText(QCoreApplication.translate("MainWindow", u"Special Character", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Version: 1", None))
        self.UsernameEntry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.WebsiteEntry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Website", None))
    # retranslateUi



