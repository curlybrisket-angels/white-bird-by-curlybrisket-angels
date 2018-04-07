import flask
from flask import render_template
from flask import request
from flask import url_for
from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://138.197.205.128:27017/')

db = client.whitebird

orgs = db.organizations

pprint.pprint(orgs.find_one())

@app.route("/")
@app.route("/search", methods=['POST'])

#Check to see if null, if not don't include them
category1 = flask.request.form.get("category1")
category2 = flask.request.form.get("category2")
state = flask.request.form.get("state")
city = flask.request.form.get("city")
company = flask.request.form.get("company")

#Testing Suite
"""
category1 = "hello"
category2 = "bye"
state = None
city = "howdy"
company = "yes"
"""

class CreateDictionary:

   def __init__(self, category1=None, category2=None, state=None, city=None, company=None):
       self.found = 0 #Switch to 1 if result is found
       self.cat1 = category1
       self.cat2 = category2
       self.state = state
       self.city = city
       self.company = company
       self.current_dict = {"category1": self.cat1, "category2": self.cat2, "state": self.state,
                            "city": self.city, "company": self.company}

   def __repr__(self):
       return '{}'.format(self.current_dict)

   def update_dictionary(self):
       for k, v in list(self.current_dict.items()):
           if v == None:
               del self.current_dict[k]

       if bool(self.current_dict) == True:
           self.found = 1
           
   def get_result(self):
       return self.found

   def get_dictionary(self):
       return self.current_dict

#Testing Suite
"""
createdict = CreateDictionary(category1, category2, state, city, company)
print(createdict)
createdict.update_dictionary()
print(createdict)
test = createdict.get_dictionary()
print(test)
"""

def search():
	"""
	The default page which is a search page that allows the client to send various amounts of information 
	to the server in order to check whether or not the requested resource is in the database. Redirects to
	the results page with the specified parameters.
	"""
	category1 = flask.request.form.get("category1")
	category2 = flask.request.form.get("category2")
	state = flask.request.form.get("state")
	city = flask.request.form.get("city")
	company = flask.request.form.get("company")
	diction = new CreateDictionary(category1, category2, state, city, company)
	return flask.render_template("index.html")