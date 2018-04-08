# imports
import flask
from flask import render_template
from flask import request
from flask import url_for
from pymongo import MongoClient

# Set the location for Flask to look for necessary files
app = flask.Flask(__name__, static_folder="static", template_folder="templates")

# Get the MongoDB client
client = MongoClient('mongodb://138.197.205.128:27017/')

# Get the MongoDB database we are using
db = client.whitebird

# Get the MongoDB database collection we are using
orgs = db.organizations

#Testing Suite
"""
category1 = "hello"
category2 = "bye"
state = None
city = "howdy"
company = "yes"
"""

class CreateDictionary:
	"""
	A class that creates a dictionary with set keys initialized to None. Provides an easy and streamlined way to create a 
	dictionary that is in the correct format to be used to search in the MongoDB database. 
	"""
	def __init__(self, category1=None, category2=None, city=None, company=None):
		self.cat1 = category1
		self.cat2 = category2
		self.city = city
		self.company = company
		self.current_dict = {"category1": self.cat1, "category2": self.cat2, "city": self.city, "company": self.company}

	def __repr__(self):
		# How the object will be printed
		return '{}'.format(self.current_dict)

	def update_dictionary(self):
		# Update the dictionary in order to get rid of empty string and 'N/A' values and keys from the webpage
		for k, v in list(self.current_dict.items()):
			if v == 'N/A':
				del self.current_dict[k]
			elif v == '':
				del self.current_dict[k]

	def get_dictionary(self):
		# Return the dictionary in the format to search the database
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
	# Request the information from the webpage that the user entered/selected
	category1 = flask.request.form.get("formInputCategory1")
	category2 = flask.request.form.get("formInputCategory2")
	city = flask.request.form.get("formInputCity")
	company = flask.request.form.get("formInputCompany")
	# Put the entered information into a CreateDictionary class for easy manipulation
	diction = CreateDictionary(category1, category2, city, company)
	# Update the dictionary to get rid of any values and keys that weren't entered
	diction.update_dictionary()
	orgs_list = []
	# Search the database for data that matches the new dictionary
	for i in orgs.find(diction.get_dictionary()):
		# Append any found database entries into an empty list
		orgs_list.append(i)
	# Loop through the list of database entries
	for i in orgs_list:
		# Get rid of all the '_id' key since we won't use it in on the webpage
		del i['_id']
	# Create a new empty list that we'll append entries to only once so we don't have duplicates
	orgs_list2 = []
	flag = 0
	# Loop through the list of database entries
	for i in orgs_list:
		# Loop through the list of database entries without duplicates
		for j in orgs_list2:
			# If the company name of the ith database entry matches the company name of the jth
			if i.get('company') == j.get('company'):
				# Set a flag indicating these are duplicate companies
				flag = 1
				# Break out of the loop
				break
		# Check if the flag is set indicating a duplicate
		if flag == 1:
			# If it is, reset the flag
			flag = 0
			# Move to the next iteration of the outer loop
			continue
		# If the flag wasn't set, append the new database entry into the list without duplicates
		orgs_list2.append(i)
	# Send an empty string variable to the HTML file for comparisons
	flask.g.empty_str = ''
	# Send the list of unduplicated database entries to the HTML file
	flask.g.orgs_list = orgs_list2
	# Send the amount of entries found to the HTML file
	flask.g.org_count = len(orgs_list2)
	# For debugging: shows the contents of the list of dictionaries
	print("orgslist = " + str(orgs_list2))
	# Refresh the page with the new information
	return flask.render_template("index.html")
