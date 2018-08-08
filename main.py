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
        about_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(about_template.render())



class infoPage(webapp2.RequestHandler):
    def get(self):
        print "====InfoPage (get)===="
        info_template = the_jinja_env.get_template('templates/info.html')
       
    
        question_endpoint_url="http://api.petfinder.com/pet.find?key=24dd34741399125dc8f5c2052ecfd2dc&animal=dog&location=93905&format=json"
        question_response=urlfetch.fetch(question_endpoint_url).content
        question_as_json=json.loads(question_response)
        first_result=question_as_json['petfinder']['pets']['pet']
        self.response.write("recieved a post request")
        dict={"data":first_result}
        self.response.write(info_template.render(dict))
        

class questionPage(webapp2.RequestHandler):
    def post(self):

        print "====InfoPage (get)===="
        info_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(info_template.render())
        
app = webapp2.WSGIApplication([
    ('/', mainPage),
    ("/info", infoPage),
    ("/question",questionPage),
], debug=True)

