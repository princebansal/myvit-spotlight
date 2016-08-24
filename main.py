import webapp2, urllib2, sys, urllib, cookielib, json, time, os
from array import *
sys.path.append('libs')
import mechanize
from bs4 import BeautifulSoup
from google.appengine.api import urlfetch, memcache
urlfetch.set_default_fetch_deadline(60)
from PIL import Image

#br.addheaders = [('referer', 'https://academics.vit.ac.in')]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<center><h1><u>!!!Welcome!!!</u></h1><h3>VITIO Spotlight Backend App Engine Console/API</h3></center>')

class VersionDetail(webapp2.RequestHandler):
    def get(self):
        sub = {}
        sub.update({'version': '1.0.0'})
        sub.update({'working website': 'https://academics.vit.ac.in'})
        sub.update({'summary': 'Complete JSON Data'})
        self.response.write(json.dumps(sub))

class Spotlight(webapp2.RequestHandler):
    def get(self):
        br = mechanize.Browser()
        jsonData = []
        r = br.open('https://academics.vit.ac.in/include_spotlight_part02.asp')
        html = r.read()
        soup = BeautifulSoup(html)
        tds = soup.findAll('td', style="text-align: justify;")
        jsonObject = {}
        jsonObject.update({'source': "CoE Spotlight"})
        jsonSubData = []
        jsonSubObject = {}
        for td in tds:
            #Figure out a logic to form an object and then pass message and url key in it.
            if(td.findAll('a')):
                anch = td.findAll('a')
                jsonSubObject.update({'url': anch[0]['href']})
                jsonSubObject.update({'message': anch[0].text})
                jsonSubData.append(jsonSubObject)
                jsonSubObject = {}
            else:
                jsonSubObject.update({'url': "-"})
                jsonSubObject.update({'message': td.text})
                jsonSubData.append(jsonSubObject)
                jsonSubObject = {}
        jsonObject.update({"content": jsonSubData})
        jsonData.append(jsonObject)
        #Academcis Spotlight
        r = br.open('https://academics.vit.ac.in/include_spotlight_part01.asp')
        html = r.read()
        soup = BeautifulSoup(html)
        tds = soup.findAll('td', style="text-align: justify;")
        jsonObject = {}
        jsonObject.update({'source': "Academics/Events Spotlight"})
        jsonSubData = []
        jsonSubObject = {}
        for td in tds:
            #Figure out a logic to form an object and then pass message and url key in it.
            if(td.findAll('a')):
                anch = td.findAll('a')
                jsonSubObject.update({'url': anch[0]['href']})
                jsonSubObject.update({'message': anch[0].text})
                jsonSubData.append(jsonSubObject)
                jsonSubObject = {}
            else:
                jsonSubObject.update({'url': "-"})
                jsonSubObject.update({'message': td.text})
                jsonSubData.append(jsonSubObject)
                jsonSubObject = {}
        jsonObject.update({"content": jsonSubData})
        jsonData.append(jsonObject)
        #Research Spotlight
        r = br.open('https://academics.vit.ac.in/include_spotlight_part03.asp')
        html = r.read()
        soup = BeautifulSoup(html)
        tds = soup.findAll('td', style="text-align: justify;")
        jsonObject = {}
        jsonObject.update({'source': "Research Spotlight"})
        jsonSubData = []
        jsonSubObject = {}
        for td in tds:
            #Figure out a logic to form an object and then pass message and url key in it.
            if(td.findAll('a')):
                anch = td.findAll('a')
                jsonSubObject.update({'url': anch[0]['href']})
                jsonSubObject.update({'message': anch[0].text})
                jsonSubData.append(jsonSubObject)
                jsonSubObject = {}
            else:
                jsonSubObject.update({'url': "-"})
                jsonSubObject.update({'message': td.text})
                jsonSubData.append(jsonSubObject)
                jsonSubObject = {}
        jsonObject.update({"content": jsonSubData})
        jsonData.append(jsonObject)
        self.response.write(json.dumps(jsonData))


app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/version', VersionDetail),
    ('/key/(.*)', Key), ('/rekey/(.*)/(.*)', ReKey),
    ('/login/(.*)/(.*)', performLogin),
    ('/subject/(.*)', SubjectJSON),
    ('/student/(.*)/(.*)', StudentJSON),
    ('/date/(.*)/(.*)', DateJSON),
    ('/attendance/(.*)/(.*)/(.*)', AttenJSON),
    ('/post/(.*)/(.*)/(.*)/(.*)',  Post),
    ('/spotlight',  Spotlight),
], debug=True)