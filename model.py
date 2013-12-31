#coding=utf-8
import sqlite3
import os
import datetime
#sqlite3.connect(fp,check_same_thread = False)
iddb = sqlite3.connect("db/myrss.db",check_same_thread = False)
#iddb = sqlite3.connect("db/myrss.db")
iddb.text_factory = str
#cu = iddb.cursor()

class myrss(object):
    """docstring for depdb"""
    def __init__(self):
        super(myrss, self).__init__()

    def inserttheme(self,themelist):#初始化主题
#        th_insert = 'insert into theme (title,href) values(%s,%s)%();'
        cu = iddb.cursor()
        for theme in themelist:
#            print theme[0],theme[1]
            cu.execute( 'insert into theme (title,href) values(?,?)',(theme[0],theme[1]))
        iddb.commit()
        cu.close()


    def addtheme(self,theme):#增量增加主题
        cu = iddb.cursor()
        cu.execute( 'insert into theme (title,href) values(?,?)',(theme[0],theme[1]))
        iddb.commit()
        cu.close()

    
    
    def selecttheme(self,theme):
        cu = iddb.cursor()
        cu.execute('select count(href) from theme where href=?',(theme[1],))
        qs =cu.fetchone()
        cu.close()
        return   qs[0]
    
    def selecttop10(self):
        #取出未处理的前十条记录
        cu = iddb.cursor()
        cu.execute('select "href" from theme where "flag"=0 order by "id"  limit 0,20;')
        qs =cu.fetchall()
        cu.close()
        return qs
    
    def updatehead(self,href,headlist):
        cu = iddb.cursor()
        #向theme表中插入head
        cu.execute('update theme set "group"=?,"notes"=?,"addtime"=? ,"flag"=1 where "href"=?',(headlist[0],headlist[1],datetime.datetime.strptime(headlist[2],'%Y-%m-%dT%H:%M:%S'),href))
        iddb.commit()
        cu.close()

    def updateerrorflag(self,href):
        cu = iddb.cursor()
        #向theme表中插入head
        cu.execute('update theme set "flag"=2 where "href"=?',(href,))
        iddb.commit()
        cu.close()

    def updatehead2(self,href,headlist):
        cu = iddb.cursor()
        #向theme表中插入head
        cu.execute('update theme set "group"=(select "id" from gruop where "name" = ?),"notes"=?,"addtime"=? ,"flag"=1 where "href"=?',(headlist[0],headlist[1],datetime.datetime.strptime(headlist[2],'%Y-%m-%dT%H:%M:%S'),href))
        iddb.commit()
        cu.close()
    
    

if __name__ == '__main__':
    themelist =[('test','test1'),('test2','test12')]
    theme ='http://www.guokr.com/article/437787/'
    headlist = ['0','1','2']
    print theme
    x=myrss()
#    print x.selecttheme(theme)
    print x.selecttop10()
    x.updatehead(theme,headlist)

