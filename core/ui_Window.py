# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledrXChPx.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
        MainWindow.resize(433, 544)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.UsernameEntry = QPlainTextEdit(self.centralwidget)
        self.UsernameEntry.setObjectName(u"UsernameEntry")
        self.UsernameEntry.setGeometry(QRect(20, 440, 191, 41))
        font = QFont()
        font.setPointSize(11)
        self.UsernameEntry.setFont(font)
        self.PasswordEntry = QPlainTextEdit(self.centralwidget)
        self.PasswordEntry.setObjectName(u"PasswordEntry")
        self.PasswordEntry.setGeometry(QRect(220, 440, 191, 41))
        self.PasswordEntry.setFont(font)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 30, 391, 351))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 400, 61, 16))
        self.EditButton = QPushButton(self.centralwidget)
        self.EditButton.setObjectName(u"EditButton")
        self.EditButton.setGeometry(QRect(20, 490, 191, 41))
        self.EditButton.setFont(font)
        self.AppendButton = QPushButton(self.centralwidget)
        self.AppendButton.setObjectName(u"AppendButton")
        self.AppendButton.setGeometry(QRect(220, 490, 191, 41))
        self.AppendButton.setFont(font)
        self.WebsiteEntry = QPlainTextEdit(self.centralwidget)
        self.WebsiteEntry.setObjectName(u"WebsiteEntry")
        self.WebsiteEntry.setGeometry(QRect(130, 390, 171, 41))
        self.WebsiteEntry.setFont(font)
        self.WebsiteEntry.setStyleSheet(u"text-align: centre;")
        self.WebsiteEntry.setInputMethodHints(Qt.ImhNone)
        self.WebsiteEntry.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.WebsiteEntry.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.WebsiteEntry.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.GenerateButton = QPushButton(self.centralwidget)
        self.GenerateButton.setObjectName(u"GenerateButton")
        self.GenerateButton.setGeometry(QRect(310, 390, 101, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.GenerateButton.setFont(font1)
        self.Length = QSpinBox(self.centralwidget)
        self.Length.setObjectName(u"Length")
        self.Length.setGeometry(QRect(80, 401, 41, 20))
        self.Length.setValue(6)
        self.s_char_checkBox = QCheckBox(self.centralwidget)
        self.s_char_checkBox.setObjectName(u"s_char_checkBox")
        self.s_char_checkBox.setGeometry(QRect(20, 420, 111, 17))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 380, 71, 16))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 10, 61, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Window Manager", None))
        self.UsernameEntry.setPlainText("")
        self.UsernameEntry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.PasswordEntry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Website", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"somesite", None));
        ___qtablewidgetitem5 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"A username", None));
        ___qtablewidgetitem6 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"a password", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.EditButton.setText(QCoreApplication.translate("MainWindow", u"Edit Line", None))
        self.AppendButton.setText(QCoreApplication.translate("MainWindow", u"Append", None))
        self.WebsiteEntry.setPlainText("")
        self.WebsiteEntry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Site name", None))
        self.GenerateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.s_char_checkBox.setText(QCoreApplication.translate("MainWindow", u"Special Character", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Version: 0.1", None))
    # retranslateUi

