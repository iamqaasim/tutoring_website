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

# Create high school route
@views.route('/high_school')
def high_school():
  return render_template("programs.html", subjects = high_school_, heading = "High School Subjects")

# Create University first year route
@views.route('/university1')
def university1():
  return render_template("programs.html", subjects = university_one, heading = "1st year Modules")

# Create University second year route
@views.route('/university2')
def university2():
  return render_template("programs.html", subjects = university_two, heading = "2nd year Modules")

# Create University thirst year route
@views.route('/university3')
def university3():
  return render_template("programs.html", subjects = university_three, heading = "3rd year Modules")

# Create Programing route
@views.route('/programing')
def programing():
  return render_template("programs.html", subjects = programing_, heading = "Programing Topics")