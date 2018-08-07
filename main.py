import webapp2
import jinja2
import os

from google.appengine.api import urlfetch
import json


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
    

class mainPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(about_template.render())
    def post(self):
        self.response.write("recieved a post request")   

class questionsPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(about_template.render())
    def post(self):
        self.response.write("recieved answers") 

app = webapp2.WSGIApplication([
    ('/', mainPage),
    ('/questions', questionsPage),
], debug=True)
