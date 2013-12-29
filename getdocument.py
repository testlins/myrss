#coding=utf-8
#抓取分析果壳网主题内容
import model
import time
import os
import urllib2
import re
from sgmllib import SGMLParser  
class Getdocument(SGMLParser):  
    """抓取主题分组、时间、提示 和 详细内容网址"""
    def reset(self):  
        self.documenthead = []
        self.getheadflag = False  
        self.getupdatetime  = False
        self.getsitename = False
        self.verbatim = 0 
        SGMLParser.reset(self)
          
    def start_head(self, attrs):
        self.getheadflag = True
        return
    
    def end_head(self):
        self.getheadflag = False
        return
        
    def start_meta(self, attrs):
        #获取notes
        if self.getheadflag:
            for k,v in attrs:
                if k=='name' and v =='Description':
                    content = [v for k, v in attrs if k == "content"]
                    self.documenthead.extend(content)
#                    print content
        #获取发表时间
        elif self.getupdatetime:
            content = [v for k, v in attrs if k == "content"][0]
            #
            strp = re.compile('(.*)\+.*')
            updatetime = re.findall(strp,content)
            self.documenthead.extend(updatetime)
#            print content,updatetime
    
    def start_title(self, attrs):
        if self.getheadflag:
            self.getsitename=True
            return
        return
    
    def end_title(self):
        if self.getheadflag and self.getsitename:
            self.getsitename=False
            return
        return
    
    def handle_data(self, text):#处理文本  
        if self.getsitename:
            sitename = re.compile(r'.*\| (.*)主题站 \| .*')
            self.documenthead.extend(re.findall(sitename,text))
            
    
    def start_div(self,attrs):
        if self.getupdatetime:  
            self.verbatim +=1 #进入子层div了，层数加1  
            return  
        for k,v in attrs:#遍历div的所有属性以及其值  
            if k == 'class' and v == 'content-th-info':#
                self.getupdatetime = True  
                return
             
    def end_div(self):#遇到</div>  
        if self.verbatim == 0:  
            self.getupdatetime = False  
        if self.getupdatetime == True:#退出子层div了，层数减1  
            self.verbatim -=1  




class dodocument(object):
    """处理主题信息"""
    def __init__(self):
        self.db = model.myrss()
        
    def inserthead(self):
        #需要改为多线程
        db = self.db
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}        
        sitelist = db.selecttop10()
        while len(sitelist)>0:
            for site in sitelist:
                req = urllib2.Request(site[0], headers= headers)
                pagedata = urllib2.urlopen(req).read()
                lister = Getdocument()
                lister.feed(pagedata)
                db.updatehead(site[0],lister.documenthead)
                print site[0]
#                sitelist.remove(site)
            sitelist = db.selecttop10()
                
                
            
        


if __name__ == "__main__": 
    test1 = dodocument()
    test1.inserthead()
     
#
#starturl = 'http://www.guokr.com/article/437749/'     
#headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
#req = urllib2.Request(starturl, headers= headers)
#pagedata = urllib2.urlopen(req).read()
#
#lister = Getdocument()  
#lister.feed(pagedata)
#print lister.documenthead