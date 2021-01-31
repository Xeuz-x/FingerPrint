from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import sys
import os
import platform

from core.fingerprint import userCheck
from core.ui_Window import Ui_MainWindow
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

class MainWindow(QMainWindow):
    def __init__(self, data):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.data = data
        self.ui.setupUi(self)
        self.ui.AppendButton.clicked.connect(self.appendFunction)
        self.ui.EditButton.clicked.connect(self.resetFields)  
        self.ui.GenerateButton.clicked.connect(self.generateString) 
        self.show()       

    def addField(self, username, password, website):
        # Addfield at the end of the line
        None
        
    def initFields(self, data):
        # * After decrypting the file, create fields 
        # * with the read data
        for username, password, website in data:
            addField(username, password, website)
        
    def resetFields(self):
        None
        
    def generateString(self,specialString = True):
        if specialString:
            # * Allow generation with special characters
            None
        else:
            # * Don't generate special characters to password
            None
        
    def checkFields(self):
        username = self.ui.UsernameEntry.toPlainText()
        password = self.ui.PasswordEntry.toPlainText()
        website = self.ui.WebsiteEntry.toPlainText()
        return username, password, website
    
    def appendFunction(self):
        if checkBox:
            username, password, website = self.checkFields()
            
            if username and password and website:
                addField(username, password, website)

            else:
                print("Missing field")
            
        else:
            print("Confirmation box not accepted")
        
if __name__ == "__main__":
    
    if fingerId := userCheck():
        
        salt = b'A_Salt'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )

        key = base64.urlsafe_b64encode(kdf.derive(fingerId))
        fer = Fernet(key)
        encrypt = fer.encrypt(message)
    
        del f
        del key
        
        try:
            app = QApplication(sys.argv)
            window = MainWindow(encrypted)
            sys.exit(app.exec_())

        except:
            print("Window Crashed")