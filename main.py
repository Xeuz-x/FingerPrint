from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import threading

import sys
import os
import platform
import base64
import pyperclip
import time
import secrets
import string

from core.fingerprint import userCheck
from core.main_window import Ui_MainWindow
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

data = ""
timer = None

class Nord():

    def __init__(self, time, row, column, status = False):
        self.name = f"{row}:{column}"
        self.time = time
        self.row = row
        self.column = column
        self.status = status # True if its running
        self.triggered = 0

class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.count = 0
        self.nukes = []
        self.selected = []
        self.passwordLength = 6
        self.bomb()
        self.ui.AppendButton.clicked.connect(self.appendFunction)
        self.ui.tableWidget.cellClicked.connect(self.cellCopy)
        self.ui.EditButton.clicked.connect(self.deleteSelected)  
        self.ui.GenerateButton.clicked.connect(self.generateString)
        self.ui.tableWidget.setMouseTracking(True)
        self.ui.Length.valueChanged.connect(self.updatePasswordL)
        self.ui.tableWidget.cellEntered.connect(self.cellHover)
        self.ui.s_char_checkBox.setCheckState(QtCore.Qt.Unchecked)
        if data:
            self.initFields()
            self.count+= 1
            
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.show() 
        
    def bomb(self):
        
        global timer
        
        timer = threading.Timer(0.00001, self.bomb)
        timer.start()
        
        a_time = time.time()
        for obj in self.nukes:
            if obj.status == True:
                #capture the only runner
                if obj.time < a_time:
                    item = self.ui.tableWidget.item(obj.row, obj.column)
                    item.setBackground(QBrush(QColor('black')))
                    obj.status = False
            
    def updatePasswordL(self, val):
        self.passwordLength = val
        rowPosition = self.ui.tableWidget.rowCount()
        
    def cellHover(self, row, column):
        
        while(True):
            item = self.ui.tableWidget.item(row, column)
            found = False
            a_time = time.time()
            if column == 2:
                for obj in self.nukes:
                    if obj.row == row and obj.column == column:
                        found = True
                        if obj.status == False:
                            obj.time = a_time + 0.5
                            obj.status = True
                            item = self.ui.tableWidget.item(obj.row, obj.column)
                            item.setBackground(QBrush(QColor('white')))
                    
                if not found:
                    self.nukes.append(Nord(a_time + 0.5, row, column, True))
                    item = self.ui.tableWidget.item(row, column)
                    item.setBackground(QBrush(QColor('white')))
                    break;
            break;
        
    def addData(self, username, password, website):
        """ 
        """
        global data
        if self.count == 0:
            data += f"{website}:{username}:{password}"
            self.count+= 1
        else:    
            data += f"|{website}:{username}:{password}"
            
    def updateData(self, arrIndex):
        global data
        dat = data.split('|')
        for index in reversed(arrIndex):
            dat.pop(index)
        data = "|".join(dat) 
            
    def recursiveDel(self, counter):
        rowPosition = self.ui.tableWidget.rowCount()
        while(counter != 0):
            for i in range(rowPosition):
                item = self.ui.tableWidget.item(i, 0)
                try:
                    if item.checkState() == QtCore.Qt.Checked:
                        self.ui.tableWidget.removeRow(item.row())
                        counter -= 1
                        self.recursiveDel(counter)
                        
                except AttributeError:
                    return
        self.resetFields()
            
    def deleteSelected(self, counter = 0):
        rowPosition = self.ui.tableWidget.rowCount()
        arrIndex = []
        if self.ui.checkBox.checkState():
            n = 0
            while(n<rowPosition):
                item = self.ui.tableWidget.item(n, 0)
                if item.checkState() == QtCore.Qt.Checked:
                    counter += 1
                    arrIndex.append(n)
                n+= 1
            self.updateData(arrIndex)
            self.recursiveDel(counter)

        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Confirmation tick not marked!')
            error_dialog.setWindowTitle("Error")
            error_dialog.exec_()
            

    def resetFields(self):
        self.ui.checkBox.setChecked(False)
        self.ui.UsernameEntry.setPlainText("")
        self.ui.PasswordEntry.setPlainText("")
        self.ui.WebsiteEntry.setPlainText("")
            
    def addField(self, username, password, website, reset = False):
                    
        rowPosition = self.ui.tableWidget.rowCount()
        new_row = self.ui.tableWidget.insertRow(rowPosition)
        
        self.ui.tableWidget.setItem(rowPosition , 0, QTableWidgetItem(website))
        self.ui.tableWidget.setItem(rowPosition , 1, QTableWidgetItem(username))
        self.ui.tableWidget.setItem(rowPosition , 2, QTableWidgetItem(password))    
        
        item = self.ui.tableWidget.item(rowPosition, 2)
        
        item.setBackground(QBrush(QColor('black')))
        item.setFlags(Qt.ItemIsEnabled)
        item = self.ui.tableWidget.item(rowPosition, 0)
        item.setCheckState(QtCore.Qt.Unchecked)
        item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        item = self.ui.tableWidget.item(rowPosition, 1)
        item.setFlags(Qt.ItemIsEnabled)
        if reset:
            self.resetFields()
        
    def initFields(self):
        # * After decrypting the file, create fields 
        # * with the read data
        global data
        var = data.split('|')
        for i in var:
            var_i = i.split(':')
            self.addField(var_i[1], var_i[2], var_i[0])
            
    def cellCopy(self, row, column):
        item = self.ui.tableWidget.item(row, column).text()
        pyperclip.copy(item)
        
    def generateString(self, specialString = True):
        if self.ui.s_char_checkBox.checkState():
            # * Allow generation with special characters
            alphabet = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(alphabet) for i in range(self.passwordLength)).replace("|", "#").replace(":", "*")
            self.ui.PasswordEntry.setPlainText(QCoreApplication.translate("MainWindow", password))
            
        else:
            # * Don't generate special characters to password
            alphabet = string.ascii_letters + string.digits
            password = ''.join(secrets.choice(alphabet) for i in range(self.passwordLength))
            self.ui.PasswordEntry.setPlainText(QCoreApplication.translate("MainWindow", password))
        
    def checkFields(self):
        username = self.ui.UsernameEntry.toPlainText()
        password = self.ui.PasswordEntry.toPlainText()
        website = self.ui.WebsiteEntry.toPlainText()
        return username, password, website
    
    def appendFunction(self):
        if self.ui.checkBox.checkState():
            username, password, website = self.checkFields()
            if username and password and website:
                self.addField(username.strip(), password.strip(), website.strip(), True)
                self.addData(username.strip(), password.strip(), website.strip())
            else:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Missing field(s)!')
                error_dialog.setWindowTitle("Error")
                error_dialog.exec_()
        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Confirmation tick not marked!')
            error_dialog.setWindowTitle("Error")
            error_dialog.exec_()
        
if __name__ == "__main__":
    
    try:
        createFile = open("passwords.txt", "x")
        os.system( "attrib +h passwords.txt" )
        createFile.close()
    except:
        pass
        
    userInput = input("Use windows biometrics? Y/N ")
    if userInput.upper() == 'Y':
        if fingerId := userCheck(): fingerId
    else:
        fingerId = input("Enter password")
        
    salt = b'A_Salt'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    with open("passwords.txt", "r+b") as openFile:
        encryptedData = openFile.read()
        
        
    key = base64.urlsafe_b64encode(kdf.derive(fingerId.encode()))
    fer = Fernet(key)
    
    if encryptedData:
        decrypt = fer.decrypt(encryptedData)
        data = decrypt.decode()
    
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(app.exec_())

    except:  
        with open("passwords.txt", "r+b") as openFile:
            openFile.seek(0)
            fer = Fernet(key)
            decrypt = fer.encrypt(data.encode())
            openFile.write(decrypt)
            openFile.truncate()
            openFile.close()         
            timer.cancel()