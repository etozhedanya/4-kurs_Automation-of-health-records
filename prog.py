import sys
import random
import traceback
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QMainWindow, QMenu,  QComboBox
from PyQt5.uic import loadUi
import pymysql
from datetime import datetime
import sys 
import traceback
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PyQt5.QtWidgets import QApplication,QLineEdit, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QComboBox
from PyQt5.QtCore import QSize, Qt
from PyQt5.Qt import QMainWindow, QVBoxLayout, QWidget, QLabel, QAction, Qt, QMessageBox, QApplication
from math import factorial



app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        loadUi("graph.ui",self)

class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        loadUi("otchet.ui",self)

class Login(QDialog):
                    
    def __init__(self):
        super(Login,self).__init__()
        loadUi("inter.ui",self)

        self.pushButton.clicked.connect(self.otch)
        self.pushButton_2.clicked.connect(self.graph)
        self.pushButton_3.clicked.connect(self.raschet)

    def otch(self):
        self.w1 = Window1()
        self.w1.show()

    def graph(self):
        self.w2 = Window2()
        self.w2.show()

    def raschet(self):
        vsch = int(self.lineEdit.text())
        vsagr = int(self.lineEdit_2.text())
        vsneis = int(self.lineEdit_3.text())
        neispagr = []
        for i in range(vsneis):
            number = random.randint(1,vsch)
            neispagr.append(number)
        neispagr.sort()
        intrvl = vsch/10
        mass1 = []
        mass2 = []
        mass3 = []
        mass4 = []
        mass5 = []
        mass6 = []
        mass7 = []
        mass8 = []
        mass9 = []
        mass10 = []
        for i in neispagr:
            if i < intrvl:
                mass1.append(i)
                ser1 = round(intrvl/2)
            if i <= intrvl*2 and i > intrvl:
                mass2.append(i)
                ser2 = round(ser1 + intrvl)
            if i <= intrvl*3 and i > intrvl*2:
                mass3.append(i)
                ser3 = round(ser2 + intrvl)
            if i <= intrvl*4 and i > intrvl*3:
                mass4.append(i)
                ser4 = round(ser3 + intrvl)
            if i <= intrvl*5 and i > intrvl*4:
                mass5.append(i)
                ser5 = round(ser4 + intrvl)
            if i <= intrvl*6 and i > intrvl*5:
                mass6.append(i)
                ser6 = round(ser5 + intrvl)
            if i <= intrvl*7 and i > intrvl*6:
                mass7.append(i)
                ser7 = round(ser6 + intrvl)
            if i <= intrvl*8 and i > intrvl*7:
                mass8.append(i)
                ser8 = round(ser7 + intrvl)
            if i <= intrvl*9 and i > intrvl*8:
                mass9.append(i)
                ser9 = round(ser8 + intrvl)
            if i <= intrvl*10 and i > intrvl*9:
                mass10.append(i)
                ser10 = round(ser9 + intrvl)
        print(neispagr)
        print(mass10)
        
        self.tableWidget.setItem(0, 1, QTableWidgetItem("0 - "+str(round(intrvl))))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(str(round(intrvl))+' - '+str(round(intrvl*2))))
        self.tableWidget.setItem(2, 1, QTableWidgetItem(str(round(intrvl*2))+' - '+str(round(intrvl*3))))
        self.tableWidget.setItem(3, 1, QTableWidgetItem(str(round(intrvl*3))+' - '+str(round(intrvl*4))))
        self.tableWidget.setItem(4, 1, QTableWidgetItem(str(round(intrvl*4))+' - '+str(round(intrvl*5))))
        self.tableWidget.setItem(5, 1, QTableWidgetItem(str(round(intrvl*5))+' - '+str(round(intrvl*6))))
        self.tableWidget.setItem(6, 1, QTableWidgetItem(str(round(intrvl*6))+' - '+str(round(intrvl*7))))
        self.tableWidget.setItem(7, 1, QTableWidgetItem(str(round(intrvl*7))+' - '+str(round(intrvl*8))))
        self.tableWidget.setItem(8, 1, QTableWidgetItem(str(round(intrvl*8))+' - '+str(round(intrvl*9))))
        self.tableWidget.setItem(9, 1, QTableWidgetItem(str(round(intrvl*9))+' - '+str(round(intrvl*10))))

        self.tableWidget.setItem(0, 2, QTableWidgetItem(str(ser1)))
        self.tableWidget.setItem(1, 2, QTableWidgetItem(str(ser2)))
        self.tableWidget.setItem(2, 2, QTableWidgetItem(str(ser3)))
        self.tableWidget.setItem(3, 2, QTableWidgetItem(str(ser4)))
        self.tableWidget.setItem(4, 2, QTableWidgetItem(str(ser5)))
        self.tableWidget.setItem(5, 2, QTableWidgetItem(str(ser6)))
        self.tableWidget.setItem(6, 2, QTableWidgetItem(str(ser7)))
        self.tableWidget.setItem(7, 2, QTableWidgetItem(str(ser8)))
        self.tableWidget.setItem(8, 2, QTableWidgetItem(str(ser9)))
        self.tableWidget.setItem(9, 2, QTableWidgetItem(str(ser10)))

        self.tableWidget.setItem(0, 3, QTableWidgetItem(str(len(mass1))))
        self.tableWidget.setItem(1, 3, QTableWidgetItem(str(len(mass2))))
        self.tableWidget.setItem(2, 3, QTableWidgetItem(str(len(mass3))))
        self.tableWidget.setItem(3, 3, QTableWidgetItem(str(len(mass4))))
        self.tableWidget.setItem(4, 3, QTableWidgetItem(str(len(mass5))))
        self.tableWidget.setItem(5, 3, QTableWidgetItem(str(len(mass6))))
        self.tableWidget.setItem(6, 3, QTableWidgetItem(str(len(mass7))))
        self.tableWidget.setItem(7, 3, QTableWidgetItem(str(len(mass8))))
        self.tableWidget.setItem(8, 3, QTableWidgetItem(str(len(mass9))))
        self.tableWidget.setItem(9, 3, QTableWidgetItem(str(len(mass10))))

        self.tableWidget.setItem(0, 4, QTableWidgetItem(str(round(((len(mass1)/(vsagr*intrvl))*10**4),2))))
        self.tableWidget.setItem(1, 4, QTableWidgetItem(str(round(((len(mass2)/(vsagr*intrvl))*10**4),2))))
        self.tableWidget.setItem(2, 4, QTableWidgetItem(str(round(((len(mass3)/(vsagr*intrvl))*10**4),2))))
        self.tableWidget.setItem(3, 4, QTableWidgetItem(str(round(((len(mass4)/(vsagr*intrvl))*10**4),2))))
        self.tableWidget.setItem(4, 4, QTableWidgetItem(str(round(((len(mass5)/(vsagr*intrvl))*10**4),2))))
        self.tableWidget.setItem(5, 4, QTableWidgetItem(str(round(((len(mass6)/(vsagr*intrvl))*10**4),2))))
        self.tableWidget.setItem(6, 4, QTableWidgetItem(str(round(((len(mass7)/(vsagr*intrvl))*10**4),2))))
        self.tableWidget.setItem(7, 4, QTableWidgetItem(str(round(((len(mass8)/(vsagr*intrvl))*10**4),2))))
        self.tableWidget.setItem(8, 4, QTableWidgetItem(str(round(((len(mass9)/(vsagr*intrvl))*10**4),2))))
        self.tableWidget.setItem(9, 4, QTableWidgetItem(str(round(((len(mass10)/(vsagr*intrvl))*10**4),2))))

        self.tableWidget.setItem(0, 5, QTableWidgetItem(str(round(((vsagr-len(mass1))/vsagr),3))))
        self.tableWidget.setItem(1, 5, QTableWidgetItem(str(round(((vsagr-len(mass2))/vsagr),3))))
        self.tableWidget.setItem(2, 5, QTableWidgetItem(str(round(((vsagr-len(mass3))/vsagr),3))))
        self.tableWidget.setItem(3, 5, QTableWidgetItem(str(round(((vsagr-len(mass4))/vsagr),3))))
        self.tableWidget.setItem(4, 5, QTableWidgetItem(str(round(((vsagr-len(mass5))/vsagr),3))))
        self.tableWidget.setItem(5, 5, QTableWidgetItem(str(round(((vsagr-len(mass6))/vsagr),3))))
        self.tableWidget.setItem(6, 5, QTableWidgetItem(str(round(((vsagr-len(mass7))/vsagr),3))))
        self.tableWidget.setItem(7, 5, QTableWidgetItem(str(round(((vsagr-len(mass8))/vsagr),3))))
        self.tableWidget.setItem(8, 5, QTableWidgetItem(str(round(((vsagr-len(mass9))/vsagr),3))))
        self.tableWidget.setItem(9, 5, QTableWidgetItem(str(round(((vsagr-len(mass10))/vsagr),3))))

        self.tableWidget.setItem(0, 6, QTableWidgetItem(str((round(((len(mass1)/(vsagr*intrvl))*10**4),2))/1)))
        self.tableWidget.setItem(1, 6, QTableWidgetItem(str(round((round(((len(mass2)/(vsagr*intrvl))*10**4),2))/(round(((vsagr-len(mass1))/vsagr),3)),2))))
        self.tableWidget.setItem(2, 6, QTableWidgetItem(str(round((round(((len(mass3)/(vsagr*intrvl))*10**4),2))/(round(((vsagr-len(mass2))/vsagr),3)),2))))
        self.tableWidget.setItem(3, 6, QTableWidgetItem(str(round((round(((len(mass4)/(vsagr*intrvl))*10**4),2))/(round(((vsagr-len(mass3))/vsagr),3)),2))))
        self.tableWidget.setItem(4, 6, QTableWidgetItem(str(round((round(((len(mass5)/(vsagr*intrvl))*10**4),2))/(round(((vsagr-len(mass4))/vsagr),3)),2))))
        self.tableWidget.setItem(5, 6, QTableWidgetItem(str(round((round(((len(mass6)/(vsagr*intrvl))*10**4),2))/(round(((vsagr-len(mass5))/vsagr),3)),2))))
        self.tableWidget.setItem(6, 6, QTableWidgetItem(str(round((round(((len(mass7)/(vsagr*intrvl))*10**4),2))/(round(((vsagr-len(mass6))/vsagr),3)),2))))
        self.tableWidget.setItem(7, 6, QTableWidgetItem(str(round((round(((len(mass8)/(vsagr*intrvl))*10**4),2))/(round(((vsagr-len(mass7))/vsagr),3)),2))))
        self.tableWidget.setItem(8, 6, QTableWidgetItem(str(round((round(((len(mass9)/(vsagr*intrvl))*10**4),2))/(round(((vsagr-len(mass8))/vsagr),3)),2))))
        self.tableWidget.setItem(9, 6, QTableWidgetItem(str(round((round(((len(mass10)/(vsagr*intrvl))*10**4),2))/(round(((vsagr-len(mass9))/vsagr),3)),2))))

        srnarnaotk_1 = (1/110)*sum(18*i for i in range(1, 110 + 1))
        print(srnarnaotk_1)

        self.tableWidget.setItem(0, 3, QTableWidgetItem(str(  )))
        
        
        


mainwindow = Login()
widget.addWidget(mainwindow)
widget.setFixedWidth(1117)
widget.setFixedHeight(562)
widget.show()
widget.setWindowTitle('Шеметов РГ')
app.exec_()
