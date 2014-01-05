#coding=utf-8
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
#from PyQt4 import QtCore
#import ui_10_1,ui_10_2,ui_10_3  
import myrssmain#,check,modify,add,messagebox
import sys  
import model
import os
import datetime
import getdocument
import gettheme_add

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

  
class TestDialog(QMainWindow,QDialog):  
    def __init__(self,parent=None):  
        super(TestDialog,self).__init__(parent) 
        reload(sys)
        sys.setdefaultencoding('utf-8')
        #从网络获取最新数据
        gouke = gettheme_add.guoketheme('http://www.guokr.com/site/all','/site/all','http://www.guokr.com/site/all')
        gouke.getthemelist()
        document = getdocument.dodocument()
        document.inserthead2()
        
        
        self.pageid = 0
        self.query = False#是否点击查询按钮
        self.queryid = 0
        self.mainUi=myrssmain.Ui_MainWindow()
        self.mainUi.setupUi(self) 
        self.db = model.myrss()
        self.themecount = self.db.selectthemecount()[0]-1
        #初始化时间空间数据
        self.initaddtime = self.db.selectinittime()
        self.starttime = datetime.datetime.strptime(self.initaddtime[0][:10],'%Y-%m-%d')
        self.endtime = datetime.datetime.strptime(self.initaddtime[1][:10],'%Y-%m-%d')
#        print type(self.starttime)
        self.mainUi.starttime.setDate(self.starttime)
        self.mainUi.endtime.setDate(self.endtime)
        #加载数据
        self.loadtable()
        #界面操作
        self.mainUi.prepagebut.clicked.connect(self.prepage)
        self.mainUi.nextpagebut.clicked.connect(self.nextpage)
        self.mainUi.startpagebut.clicked.connect(self.startpage)
        self.mainUi.endpagebut.clicked.connect(self.endpage)
        self.mainUi.clearbut.clicked.connect(self.resetcont)
        self.mainUi.selectbut.clicked.connect(self.querycont)
#        print self.mainUi.parttitle.text() is ''
        

    def loadtable(self):
        db = self.db
#        print self.themecount
#       pageid 使用全局变量
#        pageid = self.pageid
        if self.query:
            #传入时间参数 传string类型
#            print self.mainUi.parttitle.text()
            pagedata =  db.selectpagedata(self.queryid,self.mainUi.grouplist.currentText(),\
                        self.mainUi.parttitle.text(),self.mainUi.starttime.text(),self.mainUi.endtime.text())
        else:
            pagedata =  db.selectpagedata(self.pageid)
        for i in xrange(len(pagedata)):

            for x in xrange(len(pagedata[i])-1):
                        
                #解决中文乱码问题，待学习具体原因
                item = u'%s'%pagedata[i][x]
                newItem = QTableWidgetItem(item) 
                self.mainUi.tableWidget.setItem(2*i, x, newItem)  
            item = u'%s'%pagedata[i][-1]
#            print item 
            newItem = QTableWidgetItem(item) 
            self.mainUi.tableWidget.setItem(2*i+1, 0, newItem) 
        if self.query:
            self.queryid  += 10
        else:
            self.pageid += 10

            
    def prepage(self):
        if self.query:
            if self.queryid==10:
                print u'没有上一页'
            else:
                self.queryid -= 20
                self.mainUi.tableWidget.clearContents()            
                self.loadtable()
        else:
            if self.pageid==10:
                print u'没有上一页'
            #显示上一页 既显示前十条 开始id应该从前二十开始
            else:
                self.pageid -= 20
                self.mainUi.tableWidget.clearContents()            
                self.loadtable()
        

    def nextpage(self):
        #bug4 查询后点击下一页无响应
        if self.query:
            if self.queryid >= self.themecount:
                print u'没有下一页'
            else:
                self.mainUi.tableWidget.clearContents()
                self.loadtable()
        else:
            if self.pageid >= self.themecount:
                print u'没有下一页'
            else:
                self.mainUi.tableWidget.clearContents()
                self.loadtable()

    def startpage(self):
        if self.query:
            self.queryid = 0
        else:
            self.pageid  = 0
        self.mainUi.tableWidget.clearContents()
        self.loadtable()


    def endpage(self):
        if self.query:
            #计算末页从哪个项目开始
            self.queryid  = self.themecount-self.themecount%10
        else:
            self.pageid  = self.themecount-self.themecount%10
        #清空列表数据 解决末页数据不刷新问题
        self.mainUi.tableWidget.clearContents()
        self.loadtable()


    def resetcont(self):
        #bug5 增加判断条件，解决非首页，直接点击重置跳页问题
        if self.query:
            self.mainUi.starttime.setDate(self.starttime)
            self.mainUi.endtime.setDate(self.endtime)
            self.mainUi.parttitle.clear()
            self.mainUi.grouplist.clear()
            self.mainUi.tableWidget.clearContents()

            self.themecount = self.db.selectthemecount()[0]-1
            self.queryid = 0#bug4
            #保持查询前的数据
            self.pageid -=10
            self.query = False
            self.loadtable()
        else:
            return

    def querycont(self):
        self.query = True
        self.queryid = 0
        self.mainUi.tableWidget.clearContents()
        self.themecount = self.db.selectthemecount(self.mainUi.grouplist.currentText(),\
                        self.mainUi.parttitle.text(),self.mainUi.starttime.text(),self.mainUi.endtime.text())[0]-1
                        #,self.mainUi.starttime.text(),self.mainUi.endtime.text())[0]-1
        self.loadtable()
        
        
        
        
        
        
    def getcurrentdata(self):
            currentrow = self.mainUi.tableWidget.selectedItems()
    
            if currentrow==[]:
                print 'no data'
                return False
            else:
                db = self.db
                selectrule =  db.selectrule(currentrow[0].text())
                return selectrule
    
        
        

    
        

    
            

        
        

if __name__ == "__main__":          
    app=QApplication(sys.argv)  
    myapp=TestDialog()  
    myapp.show()  
    sys.exit(app.exec_())  







