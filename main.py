# -*- coding: utf-8 -*-

import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow ,QTableWidgetItem , QTableView ,QHeaderView,QMessageBox,QMenu,QAction
from mainwindow import Ui_MainWindow
from checkoutdialog import Ui_Dialog
from functools import partial

barcode_recv = ""
lst = []
class CheckoutDialog(QMainWindow):
    def __init__(self, parent=None ):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.mainWin = parent
        self.ui.recvCash.setFocusPolicy(Qt.StrongFocus)
        self.ui.recvCash.setFocus()
        self.onlyFloat = QDoubleValidator()
        self.ui.recvCash.setValidator(self.onlyFloat)
        # print("total pass val="+str(val))
    def insertMoneyBtn(self,note):
        if len(self.ui.recvCash.text()) > 0:
            recv = float(self.ui.recvCash.text())
            recv = recv+note
            print(note)
            self.ui.recvCash.setText(str(recv))
        else:
            self.ui.recvCash.setText(str(float(note)))
    def calChange(self,recv):
        self.ui.lcdNumber_2.display(recv)

        total = float(self.ui.lcdNumber.value())
        if recv < total :
            
            self.ui.lcdNumber_3.display(0.0)
            self.ui.lcdNumber_2.display(0.0)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("จำนวนเงินไม่ถูกต้อง")
            # msg.setInformativeText("Information")
            msg.setWindowTitle("ผิดพลาด")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)            
            retval = msg.exec_()
            # if retval == QMessageBox.Ok:
        else:
            self.ui.lcdNumber_3.display(recv-total)
        
    def keyPressEvent(self, q):
        if q.key()  == QtCore.Qt.Key_Return :
            if len(self.ui.recvCash.text()) >0:
                recv = float(self.ui.recvCash.text())
                if recv > 0:
                    self.calChange(recv)
                    print('return')
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("จำนวนเงินไม่ถูกต้อง")
                    # msg.setInformativeText("Information")
                    msg.setWindowTitle("ผิดพลาด")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)            
                    retval = msg.exec_() 
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("จำนวนเงินไม่ถูกต้อง")
                # msg.setInformativeText("Information")
                msg.setWindowTitle("ผิดพลาด")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)            
                retval = msg.exec_()
        elif q.key() == QtCore.Qt.Key_Escape:
            self.mainWin.clearAllFromDialog()
            self.close()
            print('exit')
        # elif q.key() == QtCore.Qt.Key_F9 :   
        

class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnCount(5) # index | barcode |name | price | amount | total
        self.ui.tableWidget.setHorizontalHeaderLabels(['บาร์โค๊ด', 'ชื่อ', 'ราคา', 'จำนวน', 'ราคารวม'])
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.setSelectionBehavior(QTableView.SelectRows)
        header = self.ui.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        # self.ui.tableWidget.itemChanged.connect(self.tableSignal) 
        self.ui.barcodeText.setFocusPolicy(Qt.StrongFocus)
        self.ui.barcodeText.setFocus()
        # self.ui.barcodeText.setFocus()
        self.ui.barcodeText.textChanged.connect(self.checkBarcode)
        self.ui.amountPlus.clicked.connect(self.plusAmount)
        self.ui.amountMinus.clicked.connect(self.minusAmount)
        self.ui.searchBtn.clicked.connect(self.addProduct)
        self.ui.search_btn2.clicked.connect(self.addProductCustom)
        self.ui.lcdNumber.display(0.0)
        self.onlyFloat = QDoubleValidator()
        self.ui.price_text.setValidator(self.onlyFloat)
        self.ui.price_plus.clicked.connect(self.plusPrice)
        self.ui.price_minus.clicked.connect(self.minusPrice)
        self.ui.pop_product.clicked.connect(self.clearAll)
        self.ui.getTotalBtn.clicked.connect(self.checkout)
        # self.onlyInt = QIntValidator()
        # self.LineEdit.setValidator(self.onlyInt)
        row_position = 0
        # with open('inventory.json') as json_file:  
        #     data = json.load(json_file)
        #     for p in data['data']:
        #         self.rowAppend(p)
    def checkout(self):
        totalPrice = self.ui.lcdNumber.value()
        rowPosition = self.ui.tableWidget.rowCount()
        if rowPosition > 0:
            checkDialog = CheckoutDialog(self)
            checkDialog.ui.lcdNumber.display(totalPrice)
            checkDialog.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ไม่มีรายการสินค้าให้คำนวน")
            # msg.setInformativeText("Information")
            msg.setWindowTitle("ผิดพลาด")
            msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok )    
            msg.setDefaultButton(QMessageBox.Ok)   
            retval = msg.exec_()
        # checkDialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    def clearAllFromDialog(self):
        try:
            self.ui.tableWidget.itemChanged.disconnect()
        except Exception:
            pass
        try:
            self.ui.tableWidget.setRowCount(0)
            # self.ui.tableWidget.setColumnCount(0)
            self.ui.tableWidget.setColumnCount(5) # index | barcode |name | price | amount | total
            self.ui.tableWidget.setHorizontalHeaderLabels(['บาร์โค๊ด', 'ชื่อ', 'ราคา', 'จำนวน', 'ราคารวม'])
            self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.tableWidget.setSelectionBehavior(QTableView.SelectRows)
            self.ui.price_text.setText("0")
            self.ui.productName.setText("")
            self.ui.amountBox.setValue(1)
            self.displayTotalPrice() 
        except:
            pass
    def clearAll(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("ต้องการที่จะลบรายการทั้งหมดหรือไม่")
        # msg.setInformativeText("Information")
        msg.setWindowTitle("ลบรายการทั้งหมด")
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok )    
        msg.setDefaultButton(QMessageBox.Ok)   
        retval = msg.exec_()
        if retval == QMessageBox.Ok:
            print ("value of pressed message box button:", retval)
            try:
                self.ui.tableWidget.itemChanged.disconnect()
            except Exception:
                pass
            self.ui.tableWidget.setRowCount(0)
            # self.ui.tableWidget.setColumnCount(0)
            self.ui.tableWidget.setColumnCount(5) # index | barcode |name | price | amount | total
            self.ui.tableWidget.setHorizontalHeaderLabels(['บาร์โค๊ด', 'ชื่อ', 'ราคา', 'จำนวน', 'ราคารวม'])
            self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.tableWidget.setSelectionBehavior(QTableView.SelectRows)
            self.ui.price_text.setText("0")
            self.ui.productName.setText("")
            self.ui.amountBox.setValue(1)
            self.displayTotalPrice()            
        

    def plusPrice(self):
        price = float(self.ui.price_text.text())
        if price < 50000:
            self.ui.price_text.setText(str(price+1))
            
    def minusPrice(self):
        price = float(self.ui.price_text.text())
        if price > 0:
            self.ui.price_text.setText(str(price-1))
    def addProductCustom(self):
        amount = self.ui.amountBox.value()
        rowPosition = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowPosition)
        self.ui.tableWidget.setItem(rowPosition,0, QTableWidgetItem("000000"))
        self.ui.tableWidget.setItem(rowPosition,1, QTableWidgetItem(str(self.ui.productName.text())))
        self.ui.tableWidget.setItem(rowPosition,2, QTableWidgetItem(str(self.ui.price_text.text())))
        self.ui.tableWidget.setItem(rowPosition,3, QTableWidgetItem(str(amount)))
        self.ui.tableWidget.setItem(rowPosition,4, QTableWidgetItem(str( float(float(self.ui.price_text.text())*amount ))))
        self.ui.price_text.setText("0")
        self.ui.productName.setText("")
        self.ui.amountBox.setValue(1)
        self.displayTotalPrice()
    def priceBtn(self,val):
        price = self.ui.price_text.text()
        self.ui.price_text.setText(str(float(price)+val))
        print("val="+str(val))

    def addProduct(self):
        global barcode_recv
        self.queryFromBarcode(barcode_recv)
    def minusAmount(self):
        amount = self.ui.amountBox.value()
        if amount > 0:
            self.ui.amountBox.setValue(amount-1)
    def plusAmount(self):
        amount = self.ui.amountBox.value()
        if amount < 300:
            self.ui.amountBox.setValue(amount+1)
    def tableSignal(self,event):
        try:
            index = event.row()
            oldPrice = float(self.ui.tableWidget.item(index, 2).text())
            oldAmount = int(self.ui.tableWidget.item(index, 3).text())
            totalPrice = oldPrice*oldAmount
            self.ui.tableWidget.setItem(index,4, QTableWidgetItem(str(totalPrice)))
            self.displayTotalPrice()
            # oldTotal = int(self.ui.tableWidget.item(index, 4).text())
        except:
            print("some error2")

    def openMenu(self,event):
        menu = QMenu()
        deleteAction = menu.addAction("Delete")
        action = menu.exec_(self.ui.tableWidget.mapToGlobal(event))
        if action == deleteAction:
            row = self.ui.tableWidget.rowAt(event.y())
            self.ui.tableWidget.removeRow(row)
            self.displayTotalPrice()
            print(str(row))
            # qApp.quit()

    def db_search(self,bar):
        with open('inventory.json',encoding='utf8') as json_file:  
            data = json.load(json_file)
            for p in data['data']:
                if p['product_NUMBER'] == bar:
                    print("found barcode"+bar)
                    self.rowAppend(p)
                    return None
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ไม่พบสินค้า")
            msg.setInformativeText("Information")
            msg.setWindowTitle("ผิดพลาด")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)            
            retval = msg.exec_()
            print ("value of pressed message box button:", retval)
            return None
                    
                    
    def queryFromBarcode(self,bar):
        self.ui.barcodeText.setText("")
        global barcode_recv
        barcode_recv = ""
        print("query "+bar)
        self.db_search(bar)

    def keyPressEvent(self, q):
        self.ui.barcodeText.setFocus()
        if q.key()  == QtCore.Qt.Key_Return :
            global barcode_recv
            self.queryFromBarcode(barcode_recv)
            print('return')
        elif q.key() == QtCore.Qt.Key_Enter :   
            print('enter')
        elif q.key() == QtCore.Qt.Key_F9 :   
            self.plusAmount()
            self.ui.barcodeText.setFocus()
        elif q.key() == QtCore.Qt.Key_F10 :  
            self.minusAmount() 
        elif q.key() == QtCore.Qt.Key_F1 :  
            self.clearAll() 
        elif q.key() == QtCore.Qt.Key_F12 :  
            self.checkout()
    def checkBarcode(self,text):
        global barcode_recv
        barcode_recv = text
        print(text)
    def displayTotalPrice(self):
        try:
            total = 0.0
            rowPosition = self.ui.tableWidget.rowCount()
            for index in range(rowPosition):
                total += float(self.ui.tableWidget.item(index, 4).text())
            self.ui.lcdNumber.display(float(total))
        except:
            print("some error1")

    def rowAppend(self,p):
        try:
            self.ui.tableWidget.itemChanged.disconnect() 
        except Exception:
            pass
        items = []
        rowPosition = self.ui.tableWidget.rowCount()
        print("row position = "+str(rowPosition))
        amount = self.ui.amountBox.value()
        if rowPosition > 0:
            for index in range(rowPosition):
                item = self.ui.tableWidget.item(index, 0)
                print(item.text())
                if item.text() == str(p['product_NUMBER']):
                    print("product concoerency at position ="+str(index))
                    oldAmount = int(self.ui.tableWidget.item(index, 3).text())
                    print("old amount = "+str(oldAmount))
                    amount = oldAmount+amount
                    totalPrice = float(p['price'])*int(amount)
                    self.ui.tableWidget.setItem(index,0, QTableWidgetItem(str(p['product_NUMBER'])))
                    self.ui.tableWidget.setItem(index,1, QTableWidgetItem(str(p['product_NAME'])))
                    self.ui.tableWidget.setItem(index,2, QTableWidgetItem(str(float(p['price']))))
                    self.ui.tableWidget.setItem(index,3, QTableWidgetItem(str(amount)))
                    self.ui.tableWidget.setItem(index,4, QTableWidgetItem(str(totalPrice)))
                    self.ui.amountBox.setValue(1)
                    self.displayTotalPrice()
                    return None
            self.ui.tableWidget.insertRow(rowPosition)
            self.ui.tableWidget.setItem(rowPosition,0, QTableWidgetItem(str(p['product_NUMBER'])))
            self.ui.tableWidget.setItem(rowPosition,1, QTableWidgetItem(str(p['product_NAME'])))
            self.ui.tableWidget.setItem(rowPosition,2, QTableWidgetItem(str(float(p['price']))))
            self.ui.tableWidget.setItem(rowPosition,3, QTableWidgetItem(str(amount)))
            self.ui.tableWidget.setItem(rowPosition,4, QTableWidgetItem(str( float(p['price'])*amount )))
            self.ui.amountBox.setValue(1)
            self.displayTotalPrice()
        else:
            self.ui.tableWidget.insertRow(rowPosition)
            self.ui.tableWidget.setItem(rowPosition,0, QTableWidgetItem(str(p['product_NUMBER'])))
            self.ui.tableWidget.setItem(rowPosition,1, QTableWidgetItem(str(p['product_NAME'])))
            self.ui.tableWidget.setItem(rowPosition,2, QTableWidgetItem(str(float(p['price']))))
            self.ui.tableWidget.setItem(rowPosition,3, QTableWidgetItem(str(amount)))
            self.ui.tableWidget.setItem(rowPosition,4, QTableWidgetItem(str( float(p['price'])*amount )))
        self.ui.tableWidget.itemChanged.connect(self.tableSignal) 
            
        self.ui.amountBox.setValue(1)
        self.displayTotalPrice()
    
                
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())