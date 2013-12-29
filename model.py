#coding=utf-8
import sqlite3
import os
iddb = sqlite3.connect("db/myrss.db")
iddb.text_factory = str
cu = iddb.cursor()

class myrss(object):
    """docstring for depdb"""
    def __init__(self):
        super(myrss, self).__init__()

    def inserttheme(self,themelist):#初始化主题
#        th_insert = 'insert into theme (title,href) values(%s,%s)%();'
        for theme in themelist:
#            print theme[0],theme[1]
            cu.execute( 'insert into theme (title,href) values(?,?)',(theme[0],theme[1]))
        iddb.commit()

    def addtheme(self,theme):#增量增加主题
        cu.execute( 'insert into theme (title,href) values(?,?)',(theme[0],theme[1]))
        iddb.commit()

    
    
    def selecttheme(self,theme):
        cu.execute('select count(href) from theme where href=?',(theme[1],))
        qs =cu.fetchone()
        return   qs[0]
    
    def selecttop10(self):
        #取出未处理的前十条记录
        cu.execute('select href from theme where "flag"=0 order by id  limit 0,10;')
        qs =cu.fetchall()
        return qs
    
    def updatehead(self,href,headlist):
        #向theme表中插入head
        cu.execute('update theme set "group"=?,"notes"=?,"addtime"=? ,"flag"=1 where "href"=?',(headlist[0],headlist[1],headlist[2],href))
        iddb.commit()    

if __name__ == '__main__':
    themelist =[('test','test1'),('test2','test12')]
    theme ='http://www.guokr.com/article/437787/'
    headlist = ['0','1','2']
    print theme
    x=myrss()
#    print x.selecttheme(theme)
    print x.selecttop10()
    x.updatehead(theme,headlist)

