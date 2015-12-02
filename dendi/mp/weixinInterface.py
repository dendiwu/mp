# -*- coding: utf8 -*-
import hashlib
import web
import lxml
import time,os,sys,chardet
import urllib2,json,MySQLdb,MySQLdb.cursors
from lxml import etree

class WeixinInterface:
    
      def __init__(self):
          self.app_root = os.path.dirname(__file__)
          self.templates_root = os.path.join(self.app_root,'templates')
          self.render = web.template.render(self.templates_root)
   
      def POST(self):
          str_xml = web.data()
          xml = etree.fromstring(str_xml)
          content = xml.find("Content").text
          msgType=xml.find("MsgType").text
          fromUser=xml.find("FromUserName").text
          toUser=xml.find("ToUserName").text
          #if type(content).__name__!="unicode":
          #content = content.encode("utf-8")
          #else:
          #   pass
          print content
          conn = MySQLdb.connect(host='localhost', user='root', passwd='',db='dendi',charset='utf8') #,cursorclass=MySQLdb.cursors.DictCursor)
          cursor = conn.cursor()
          cursor.execute("select * from addr where name='" + content + "';")
          content = cursor.fetchall()
          if len(content) == 0:
             ret="call me 666677"
          else:
             ret=""
             for i in content[0]:
                 if i == None:
                      i = " "
                 ret = ret + str(i.encode('utf8')) + "\n"
          return self.render.reply_text(fromUser,toUser,int(time.time()),ret)

      def GET(self):
          data = web.input()
          signature = data.signature
          timestamp=data.timestamp
          nonce=data.nonce
          echostr=data.echostr
          token='dendiwu'
          list=[token,timestamp,nonce]
          list.sort()
          sha1=hashlib.sha1()
          map(sha1.update,list)
          hashcode=sha1.hexdigest()

          if hashcode == signature:
             return echostr



