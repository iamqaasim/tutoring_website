# Blueprint is used to sort our routes
# Render_template is used to render the html pages
from flask import Blueprint, render_template, jsonify

# Simulating a databse
from .data import *

views = Blueprint('views',__name__)


# Create routes

# Create Home route
@views.route('/')
def home():
  return render_template("home.html", subjects = subjects)

# Create API route
@views.route('/API')
def api():
  return jsonify(subjects, high_school, university_one, university_two, university_three)

# Create all programs route
@views.route('/all')
def all():
  return render_template("all.html")
'''
# Create programing route
@views.route('/all-programs/programing')
def programing():
  return render_template()

# Create specializing route
@views.route('/all-programs/specializing')
def specializing():
  return render_template()
'''