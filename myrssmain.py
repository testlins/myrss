# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myrssmain.ui'
#
# Created: Thu Jan 02 11:22:48 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import datetime
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(678, 752)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 110, 631, 541))
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection) 
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True) 
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.prepagebut = QtGui.QPushButton(self.centralwidget)
        self.prepagebut.setGeometry(QtCore.QRect(220, 680, 75, 23))
        self.prepagebut.setObjectName(_fromUtf8("prepagebut"))
        self.nextpagebut = QtGui.QPushButton(self.centralwidget)
        self.nextpagebut.setGeometry(QtCore.QRect(320, 680, 75, 23))
        self.nextpagebut.setObjectName(_fromUtf8("nextpagebut"))
        self.startpagebut = QtGui.QPushButton(self.centralwidget)        
        self.startpagebut.setGeometry(QtCore.QRect(110, 680, 75, 23))
        self.startpagebut.setObjectName(_fromUtf8("startpagebut"))
        self.endpagebut = QtGui.QPushButton(self.centralwidget)
        self.endpagebut.setGeometry(QtCore.QRect(430, 680, 75, 23))
        self.endpagebut.setObjectName(_fromUtf8("endpagebut"))

        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 638, 80))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.clearbut = QtGui.QPushButton(self.gridLayoutWidget)
        self.clearbut.setObjectName(_fromUtf8("clearbut"))
        self.gridLayout.addWidget(self.clearbut, 1, 8, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.parttitle = QtGui.QLineEdit(self.gridLayoutWidget)
        self.parttitle.setObjectName(_fromUtf8("parttitle"))
        self.gridLayout.addWidget(self.parttitle, 0, 6, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 5, 1, 1)
        self.selectbut = QtGui.QPushButton(self.gridLayoutWidget)
        self.selectbut.setObjectName(_fromUtf8("selectbut"))
        self.gridLayout.addWidget(self.selectbut, 1, 7, 1, 1)
        self.starttime = QtGui.QDateEdit(self.gridLayoutWidget)
        self.starttime.setObjectName(_fromUtf8("starttime"))
        #设置日期显示格式
        self.starttime.setDisplayFormat("yyyy-MM-dd")
        self.starttime.setCalendarPopup(True)
        self.gridLayout.addWidget(self.starttime, 1, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 5, 1, 1)
        self.endtime = QtGui.QDateEdit(self.gridLayoutWidget)
        self.endtime.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.endtime.setObjectName(_fromUtf8("endtime"))
        self.endtime.setDisplayFormat("yyyy-MM-dd")        
        self.endtime.setCalendarPopup(True)
        #设置最大宽度长度 应该有对齐方式的 后面学习
        self.endtime.setMaximumSize(100,50)
        self.gridLayout.addWidget(self.endtime, 1, 6, 1, 1)
        self.grouplist = QtGui.QComboBox(self.gridLayoutWidget)
        self.grouplist.setObjectName(_fromUtf8("grouplist"))
        self.gridLayout.addWidget(self.grouplist, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 678, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        for i in xrange(1,self.tableWidget.rowCount(),2):
            #合并notes单元格 状态设为不能选中
            #self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection) 
            self.tableWidget.setSpan(i, 0, 1, self.tableWidget.columnCount())
        self.tableWidget.setColumnWidth(0,320)
        self.tableWidget.setColumnWidth(2,140)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "主题", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "分类", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "发布时间", None))
        self.prepagebut.setText(_translate("MainWindow", "上一页", None))
        self.nextpagebut.setText(_translate("MainWindow", "下一页", None))
        self.startpagebut.setText(_translate("MainWindow", "首页", None))
        self.endpagebut.setText(_translate("MainWindow", "末页", None))
        
        self.clearbut.setText(_translate("MainWindow", "重置", None))
        self.label_3.setText(_translate("MainWindow", "分类", None))
        self.label.setText(_translate("MainWindow", "发布时间", None))
        self.label_4.setText(_translate("MainWindow", "主题", None))
        self.selectbut.setText(_translate("MainWindow", "查询", None))
        self.label_2.setText(_translate("MainWindow", "到", None))

