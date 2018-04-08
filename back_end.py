import flask
from flask import render_template
from flask import request
from flask import url_for
from pymongo import MongoClient
import pprint

app = flask.Flask(__name__, static_folder="static", template_folder="templates")

client = MongoClient('mongodb://138.197.205.128:27017/')

db = client.whitebird

orgs = db.organizations

pprint.pprint(orgs.find_one())

#Testing Suite
"""
category1 = "hello"
category2 = "bye"
state = None
city = "howdy"
company = "yes"
"""

# set the project root directory as the static folder, you can set others.

class CreateDictionary:

   def __init__(self, category1=None, category2=None, city=None, company=None):
       self.found = 0 #Switch to 1 if result is found
       self.cat1 = category1
       self.cat2 = category2
       self.city = city
       self.company = company
       self.current_dict = {"category1": self.cat1, "category2": self.cat2, 
                            "city": self.city, "company": self.company}

   def __repr__(self):
       return '{}'.format(self.current_dict)

   def update_dictionary(self):
       for k, v in list(self.current_dict.items()):
           if v == 'N/A':
               del self.current_dict[k]
           elif v == '':
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
@app.route("/")
@app.route("/search", methods=['POST'])
def search():
	"""
	The default page which is a search page that allows the client to send various amounts of information 
	to the server in order to check whether or not the requested resource is in the database. Redirects to
	the results page with the specified parameters.
	"""
	print("entering search")
	test = flask.request.form.get("test")
	print("test = " + str(test))
	testselect = flask.request.form.get("testselect")
	print("testselect = " + str(testselect))
	category1 = flask.request.form.get("formInputCategory1")
	print("category 1 = " + str(category1))
	category2 = flask.request.form.get("formInputCategory2")
	state = flask.request.form.get("formInputState")
	print("state = " + str(state))
	city = flask.request.form.get("formInputCity")
	company = flask.request.form.get("formInputCompany")
	diction = CreateDictionary(category1, category2, city, company)
	diction.update_dictionary()
	orgs_list = []
	print("diction = " + str(diction.get_dictionary))
	for i in orgs.find(diction.get_dictionary()):
		orgs_list.append(i)
	for i in orgs_list:
		print("i = " + str(i))
		del i['_id']
	orgs_list2 = []
	flag = 0
	for i in orgs_list:
		for j in orgs_list2:
			if i.get('company') == j.get('company'):
				flag = 1
				break
		if flag == 1:
			flag = 0
			continue
		orgs_list2.append(i)
	empty_str = ''
	flask.g.empty_str = empty_str
	flask.g.orgs_list = orgs_list2
	flask.g.org_count = len(orgs_list2)
	print("orgslist = " + str(orgs_list2))
	return flask.render_template("index.html")

