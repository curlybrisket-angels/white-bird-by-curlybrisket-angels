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
def search():
	"""
	The default page which is a search page that allows the client to send various amounts of information 
	to the server in order to check whether or not the requested resource is in the database. Redirects to
	the results page with the specified parameters.
	"""
	name = flask.request.form.get("name")
	category1 = flask.request.form.get("category1")
	category2 = flask.request.form.get("category2")
	state = flask.request.form.get("state")
	city = flask.request.form.get("city")
	return flask.render_template("index.html")