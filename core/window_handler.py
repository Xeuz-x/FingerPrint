from .main_window import Ui_MainWindow
from .animation import Blur
from .utils import *

import threading
import time
import sys

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

from PySide2.QtCore import QCoreApplication, Qt, SIGNAL
from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import *


FILENAME = None
DATA = None
FER = None


class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Variable definitions
        self.hide_credentials = True
        self.password_length = 8
        self.flag = False
        self.clock = None
        self.cells = []
        # Enable mouse hovering
        self.ui.tableWidget.setMouseTracking(True)
        # Connecting buttons to functions
        self.ui.WebsiteEntry.textChanged.connect(self.website_entry_limiter)
        self.ui.UsernameEntry.textChanged.connect(self.username_entry_limiter)
        self.ui.PasswordEntry.textChanged.connect(self.password_entry_limiter)
        self.ui.AppendButton.clicked.connect(self.append_data)
        self.ui.tableWidget.cellClicked.connect(self.copy_cell)
        self.ui.EditButton.clicked.connect(self.recursive_delete)
        self.ui.GenerateButton.clicked.connect(self.generate_password)
        self.ui.Length.valueChanged.connect(self.update_password_length)
        self.ui.tableWidget.cellEntered.connect(self.cell_hovered)
        self.ui.s_char_checkBox.setCheckState(QtCore.Qt.Unchecked)
        # Auto-resize the table widget to fit the screen    
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # Load current data
        if DATA:
            self.flag = True
            self.init_fields()
        # Show window
        self.show()
        

    def check_cell_state(self):
        for cell in self.cells:
            if cell.hidden is True and cell.time < time.time():
                cell.hide()
            
                
    def start_clock(self):
        self.clock = threading.Timer(0.0001, self.start_clock)
        self.clock.start()
        self.check_cell_state()
        

    def stop_clock(self):
        if self.clock:
            self.clock.cancel()
        else:
            raise "Clock is not running!"


    def update_password_length(self, length):
        self.password_length = length


    def cell_hovered(self, row, column, fade_length=0.35):
        if column != 2: return
        if not self.hide_credentials: return
        while True:
            current_cell = self.ui.tableWidget.item(row, column)
            current_time = time.time()
            for cell in self.cells:
                if cell.row == row and cell.column == column and cell.hidden is False:
                    cell.time = current_time + fade_length
                    cell.show()
            break
        
        
    def website_entry_limiter(self):
        max_length = 19
        entry_window = self.ui.WebsiteEntry.toPlainText()
        if len(entry_window) > max_length:
            text = entry_window[:max_length]
            self.ui.WebsiteEntry.setPlainText(text)
            cursor = self.ui.WebsiteEntry.textCursor().setPosition(max_length)
            self.ui.WebsiteEntry.setTextCursor(cursor)
            
            
    def password_entry_limiter(self):
        max_length = 22
        entry_window = self.ui.PasswordEntry.toPlainText()
        if len(entry_window) > max_length:
            text = entry_window[:max_length]
            self.ui.PasswordEntry.setPlainText(text)
            cursor = self.ui.PasswordEntry.textCursor().setPosition(max_length)
            self.ui.PasswordEntry.setTextCursor(cursor)
        
        
    def username_entry_limiter(self):
        max_length = 22
        entry_window = self.ui.UsernameEntry.toPlainText()
        if len(entry_window) > max_length:
            text = entry_window[:max_length]
            self.ui.UsernameEntry.setPlainText(text)
            cursor = self.ui.UsernameEntry.textCursor().setPosition(max_length)
            self.ui.UsernameEntry.setTextCursor(cursor)


    def show_error(self, message):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(message)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec_()


    def add_data(self, username, password, website):
        global DATA
        DATA += f"|{website}:{username}:{password}" if self.flag else f"{website}:{username}:{password}"
        self.flag = True
        

    def update_data(self, index, name):
        global DATA
        data_list = DATA.split("|")
        del  data_list[index]
        del  self.cells[index]
        DATA = "|".join(data_list)
        for current_index, cell in enumerate(self.cells):
            if cell.row != current_index:
                cell.row = current_index


    def recursive_delete(self):
        if self.ui.checkBox.checkState():
            rowPosition = self.ui.tableWidget.rowCount()
            for index in range(rowPosition -1, -1, -1):
                item = self.ui.tableWidget.item(index, 0)
                if item.checkState() == QtCore.Qt.Checked:
                    self.update_data(index, item.text())
                    self.ui.tableWidget.removeRow(item.row())
            self.reset_fields()
        else:
            self.show_error("Confirmation box not ticked")


    def reset_fields(self):
        self.ui.checkBox.setChecked(False)
        self.ui.UsernameEntry.setPlainText("")
        self.ui.PasswordEntry.setPlainText("")
        self.ui.WebsiteEntry.setPlainText("")


    def add_field(self, username, password, website, reset=False):
        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)
        self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(website))
        self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(username))
        self.ui.tableWidget.setItem(row_position, 2, QTableWidgetItem(password))
        cell = self.ui.tableWidget.item(row_position, 2)
        cell.setFlags(Qt.ItemIsEnabled)
        new_cell = Blur(cell, row_position, 2)
        new_cell.hide() 
        self.cells.append(new_cell)
        cell = self.ui.tableWidget.item(row_position, 0)
        cell.setCheckState(QtCore.Qt.Unchecked)
        cell.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        cell = self.ui.tableWidget.item(row_position, 1)
        cell.setFlags(Qt.ItemIsEnabled)
        if reset:
            self.reset_fields()
            

    def init_fields(self):
        global DATA
        data_list = DATA.split("|")
        for accounts in data_list:
            account_details = accounts.split(":")
            self.add_field(account_details[1], account_details[2], account_details[0])
            

    def copy_cell(self, row, column):
        copy_content(self.ui.tableWidget.item(row, column).text())
        

    def generate_password(self, specialString=True):
        if self.ui.s_char_checkBox.checkState():
            password = generate_specialString(self.password_length)
            self.ui.PasswordEntry.setPlainText(QCoreApplication.translate("MainWindow", password))

        else:
            password = generate_string(self.password_length)
            self.ui.PasswordEntry.setPlainText(QCoreApplication.translate("MainWindow", password))
            

    def check_entries(self):
        username = self.ui.UsernameEntry.toPlainText()
        password = self.ui.PasswordEntry.toPlainText()
        website = self.ui.WebsiteEntry.toPlainText()
        return (
            website, username, password
            if username and password and website
            else False
            )


    def append_data(self):
        if self.ui.checkBox.checkState():
            if details := self.check_entries():
                website, username, password = details
                self.add_field(
                    username.replace(" ", ""),
                    password.replace(" ", ""),
                    website.replace(" ", ""),
                    True,
                )
                self.add_data(
                    username.replace(" ", ""),
                    password.replace(" ", ""),
                    website.replace(" ", ""),
                )
            else:
                self.show_error("Missing field(s)!")
        else:
            self.show_error("Confirmation box not ticked!")
    
    def closeEvent(self, event):
        global FER, DATA, FILENAME
        with open(FILENAME, "r+b") as openFile:
            openFile.seek(0)
            decrypt = FER.encrypt(DATA.encode())
            openFile.write(decrypt)
            openFile.truncate()
        self.stop_clock()


def run_window(fer, filename, initial_data):
    global DATA, FER, FILENAME
    FILENAME = filename
    DATA = initial_data
    FER = fer

    app = QApplication(sys.argv)
    app_window = MainWindow()
    app_window.start_clock()
    sys.exit(app.exec_())
        