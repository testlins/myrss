#coding=utf-8
#抓取分析果壳网新主题
import model
import os
import urllib2
import re
from sgmllib import SGMLParser  
class GetSiteList(SGMLParser):  
    """抓取每页的主题网址 和下一页网址"""
    def reset(self):  
        self.SiteList = []
#        self.subpagelist = []
        self.flag = False  
        self.getsite = False
##        self.subpage = False
#        self.getsubpage = False
#        self.pagekey = '下一页'
        self.verbatim = 0  
        SGMLParser.reset(self)  
          
    def start_div(self, attrs):  
        if self.flag == True:  
            self.verbatim +=1 #进入子层div了，层数加1  
            return  
        for k,v in attrs:#遍历div的所有属性以及其值  
            if k == 'class' and v == 'main':#确定进入了主题页面<div class='main'>  
                self.flag = True  
                return  
  
    def end_div(self):#遇到</div>  
        if self.verbatim == 0:  
            self.flag = False  
        if self.flag == True:#退出子层div了，层数减1  
            self.verbatim -=1  
          
    def start_h3(self, attrs):#主题头 
        if self.flag == False:  
            return  
        self.getsite = True  
          
    def end_h3(self):
        if self.getsite:  
            self.getsite = False 

#    def start_li(self, attrs):#主题头 
#        if self.flag == False:  
#            return  
#        self.subpage = True  
#          
#    def end_li(self):
#        if self.subpage:  
#            self.subpage = False
    
#    def handle_data(self, text):#处理文本  
#        if self.subpage:
#            
#            if text == self.pagekey: #and self.getsubpage ==False:
#                
#                return  True
#                #self.getsubpage =True
#            else:
#                return False
#                #self.getsubpage =False
#            #print text.decode('utf-8').encode('gbk')
#            #print self.pagekey.decode('utf-8').encode('gbk')
#            #return text.decode('utf-8').encode('gbk')



    def start_a(self, attrs):  
        if self.getsite == True:
            href = [v for k, v in attrs if k == "href"][0] #只有一个url和名字
            title = [v for k, v in attrs if k == "title"][0]
            if href and title:
                #print href,title
                self.SiteList.append((title,str(href)))
#                print self.SiteList
        
            
            
                



class guoketheme(object):
    """""" 
    def __init__(self,starturl,oldkey=None,newkey=None):
        self.starturl = starturl
        self.oldkey = oldkey
        self.newkey = newkey
        self.db = model.myrss()
        self.articlelist = []
    def getthemelist(self):
        starturl = self.starturl
        articlelist = self.articlelist
        db = self.db
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

        pagelist = []
        pagelist.append(starturl)
        while len(pagelist)>0:
            #print pagelist.pop()
            page = self.linkstr(pagelist.pop())
            #print page
            req = urllib2.Request(page, headers= headers)
            pagedata = urllib2.urlopen(req).read()
            #正则提取下一页url
            rex =  re.compile(r'<a href="(.*)">下一页</a>')
            connect = re.findall(rex,pagedata)

            lister = GetSiteList()  
            lister.feed(pagedata)  
            db.inserttheme(lister.SiteList)
            #取出子页面重复元素并添加按原来顺序排序pagelist中，即取下一页链接
            #由于首页 上一页 的影响所以最后一个
#            templist = filter((lambda i: lister.subpagelist.count(i)>1),lister.subpagelist)
#            pagelist.append(sorted(set(templist),key=templist.index)[-1])
            pagelist.extend(connect)
#        testfile.close()
#        return articlelist
            
    def linkstr(self,suburl):
        #处理下一页为绝对路径
        starturl = self.starturl
        oldkey = self.oldkey
        newkey = self.newkey
        if oldkey==None or newkey==None or starturl==suburl:
            return suburl
        else:
            return suburl.replace(oldkey,newkey)
        
            
            
        
        
        
                

if __name__ == "__main__":  
    
    gouke = guoketheme('http://www.guokr.com/site/all','/site/all','http://www.guokr.com/site/all')
    gouke.getthemelist()
    




    
    



#
#from sgmllib import SGMLParser  
#class GetIdList(SGMLParser):  
#    def reset(self):  
#        self.IDlist = []  
#        self.flag = False  
#        self.getsite = False  
#        self.verbatim = 0  
#        SGMLParser.reset(self)  
#          
#    def start_div(self, attrs):  
#        if self.flag == True:  
#            self.verbatim +=1 #进入子层div了，层数加1  
#            return  
#        for k,v in attrs:#遍历div的所有属性以及其值  
#            if k == 'class' and v == 'entry-content':#确定进入了<div class='entry-content'>  
#                self.flag = True  
#                return  
#  
#    def end_div(self):#遇到</div>  
#        if self.verbatim == 0:  
#            self.flag = False  
#        if self.flag == True:#退出子层div了，层数减1  
#            self.verbatim -=1  
#  
#    def start_p(self, attrs):  
#        if self.flag == False:  
#            return  
#        self.getsite = True  
#          
#    def end_p(self):#遇到</p>  
#        if self.getsite:  
#            self.getsite = False  
#  
#    def handle_data(self, text):#处理文本  
#        if self.getsite:  
#            self.IDlist.append(text)  
#              
#    def printID(self):  
#        for i in self.IDlist:  
#            print i  
#  
#  
###import urllib2  
###import datetime  
###vrg = (datetime.date(2012,2,19) - datetime.date.today()).days  
###strUrl = 'http://www.nod32id.org/nod32id/%d.html'%(200+vrg)  
###req = urllib2.Request(strUrl)#通过网络获取网页  
###response = urllib2.urlopen(req)  
###the_page = response.read()  
#  
#the_page ='''''<html> 
#<head> 
#<title>test</title> 
#</head> 
#<body> 
#<h1>title</h1> 
#<div class='entry-content'> 
#<div class= 'ooxx'>我是来捣乱的</div> 
#<p>感兴趣内容1</p> 
#<p>感兴趣内容2</p> 
#…… 
#<p>感兴趣内容n</p> 
#<div class= 'ooxx'>我是来捣乱的2<div class= 'ooxx'>我是来捣乱的3</div></div> 
#</div> 
#<div class='content'> 
#<p>内容1</p> 
#<p>内容2</p> 
#…… 
#<p>内容n</p> 
#</div> 
#</body> 
#</html> 
#'''  
#lister = GetIdList()  
#lister.feed(the_page)  
#lister.printID()  
#
#    
