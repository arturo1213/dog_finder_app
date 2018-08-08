import webapp2
import jinja2
import os


#libraries for APIs
from google.appengine.api import urlfetch
import json


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class mainPage(webapp2.RequestHandler):
    def get(self):
        question_endpoint_url="http://api.petfinder.com/pet.find?key=24dd34741399125dc8f5c2052ecfd2dc&animal=dog&location=93905&format=json"
        question_response=urlfetch.fetch(question_endpoint_url).content
        question_as_json=json.loads(question_response)
        first_result=question_as_json['petfinder']['pets']['pet'][0]
        self.response.write("recieved a post request")
        self.response.write(first_result)
        results= {"size":"small",
         "age":"months",
         "location":"Salinas"}
        info_template= the_jinja_env.get_template('templates/index.html')
        
        self.response.write(info_template.render(results))
        size = self.request.get('size')
        
        
        self.response.write(origin)
        
'''
class mainPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(about_template.render())
'''  
       


class infoPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(about_template.render())
    
class ResultsPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/info.html')
        self.response.write("recieved a post request")


app = webapp2.WSGIApplication([
    ('/', mainPage),
    ("/questions", infoPage),
    ("results",ResultsPage),
], debug=True)

