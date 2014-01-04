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

#    def selectpagedata(self,pageid):
#        #供界面数据 按时间逆序 每次10个
#        cu = iddb.cursor()
#        cu.execute('select "title","group","addtime","notes" from theme where "flag"=1 order by "addtime" desc limit ?,10',(pageid,))
##        cu.execute('select "title","group","addtime","notes" from theme where "flag"=1 and ("group"= ? or "group" is null) order by "addtime" desc limit ?,10',(group,pageid,))
#
#        qs =cu.fetchall()
#        cu.close()
#        return qs

    def selectpagedata(self,initid,group= '',title= '',starttime= '',endtime= ''):
        #供界面数据 按时间逆序 每次10个 
        exsql = 'select "title","group","addtime","notes" from theme where "flag"=1'
        if group != '':
            exsql += ' and "group"="%s"'%group
        #str(title).strip()清除空格
        elif str(title).strip() != '':
            exsql += ' and "title" like "%%%s%%"'%str(title).strip()
        elif starttime != '' and endtime != '':
#            starttime = datetime.datetime.strftime(starttime,"%Y/%m/%d")+' 00:00'
#            endtime = datetime.datetime.strftime(endtime,"%Y/%m/%d")+' 23:59:59'
            starttime = starttime+' 00:00'
            endtime = endtime+' 23:59:59'
            exsql += ' and "addtime" between "%s" and "%s"'%(starttime,endtime)
        exsql += ' order by "addtime" desc limit %d,10'%initid
        print exsql

        cu = iddb.cursor()
        cu.execute(exsql)
#        cu.execute('select "title","group","addtime","notes" from theme where "flag"=1 and ("group"= ? or "group" is null) order by "addtime" desc limit ?,10',(group,pageid,))

        qs =cu.fetchall()
        cu.close()
        return qs

    def selectinittime(self):
        #供界面时间数据 最大最小有效数据
        cu = iddb.cursor()
        cu.execute('SELECT min(addtime),max(addtime) FROM theme where flag =1')
        qs =cu.fetchone()
        cu.close()
        return qs

    
    def selectthemecount(self,group='',title='',starttime='',endtime=''):
        #计算有效主题数
#        print group,title,starttime,endtime
#        print str(title).strip()
        exsql = 'select count("title") from theme where "flag"=1'
        if group != '':
            exsql += ' and "group"="%s"'%group
        elif str(title).strip() != '':
            exsql += ' and "title" like "%%%s%%"'%str(title).strip()
        elif starttime != '' and endtime != '':
#            starttime = datetime.datetime.strftime(starttime,"%Y/%m/%d")+' 00:00'
#            endtime = datetime.datetime.strftime(endtime,"%Y/%m/%d")+' 23:59:59'   
            starttime = starttime+' 00:00'
            endtime = endtime+' 23:59:59'
            exsql += ' and "addtime" between "%s" and "%s"'%(starttime,endtime)
        cu = iddb.cursor()
        cu.execute(exsql)
        qs =cu.fetchone()
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
#    print x.selecttop10()
    print x.selectpagedata(10,None,'为什么',None,None)

