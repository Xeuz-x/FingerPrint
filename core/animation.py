from PySide2.QtGui import (QBrush, QColor)

class Blur:
    
    def __init__(self, cell, row, column, status=False, time=None):
        self.cell = cell
        self.time = time
        self.column = column
        self.row = row
        self.hidden = status

    def hide(self):
        try:
            self.cell.setBackground(QBrush(QColor("black")))
            self.hidden = False
        except:
            raise "Could not hide cell!"

    def show(self):
        try:
            self.cell.setBackground(QBrush(QColor("white")))
            self.hidden = True
        except:
            raise "Could not show cell!"
