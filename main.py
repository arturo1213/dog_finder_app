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

class questionPage(webapp2.RequestHandler):
    def get(self):
        print "====InfoPage(get)===="
        index_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(index_template.render())

class infoPage(webapp2.RequestHandler):
    def post(self):
        print "====InfoPage (get)===="
        info_template = the_jinja_env.get_template('templates/info.html')
        self.response.write(info_template.render())
       
        question_endpoint_url_sal="http://api.petfinder.com/pet.find?key=24dd34741399125dc8f5c2052ecfd2dc&animal=dog&location=93905&format=json"
        question_response_sal=urlfetch.fetch(question_endpoint_url_sal).content
        question_as_json_sal=json.loads(question_response_sal)
        
        question_endpoint_url_mon="http://api.petfinder.com/pet.find?key=24dd34741399125dc8f5c2052ecfd2dc&animal=dog&location=93940&format=json"
        question_response_mon=urlfetch.fetch(question_endpoint_url_mon).content
        question_as_json_mon=json.loads(question_response_mon)


        list_of_pets_sal=question_as_json_sal['petfinder']['pets']['pet']
        list_of_pets_mon=question_as_json_mon['petfinder']['pets']['pet']
        
        #print "+++++++++++++++++++++++"
       # print len(list_of_pets_sal)
        list_of_pets_sal.extend(list_of_pets_mon)
       # print len(list_of_pets_sal)
        #print type(list_of_pets_sal)
        list_of_pets = list_of_pets_sal
        #self.response.write("recieved a post request")
        
        #print type(list_of_pets_sal)
        #print type(list_of_pets_mon)
        print"**********"
        
        size = self.request.get('size')
        gender = self.request.get('gender')
        age = self.request.get('age')
        location = self.request.get('location')
        myDict={
            'size': size,
            'gender': gender,
            'location': location,
            'age':age,

        }
        best_matches=[]
        for pet in list_of_pets:
            if pet['age']['$t']== age and pet['size']['$t']==size and pet['contact']['city']['$t']==location and pet['sex']['$t']==gender:
                best_matches.append(pet)
                
        #self.response.write(best_matches)
        #self.response.write(len(best_matches))
        #print question_as_json['petfinder']['pets']['pet'][0]


                
        dict={'data': best_matches}
        
        self.response.write(info_template.render(dict))


app = webapp2.WSGIApplication([
    ('/', mainPage),
    ("/question",questionPage),
    ("/info", infoPage),
], debug=True)

