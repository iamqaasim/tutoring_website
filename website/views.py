# Blueprint is used to sort our routes
# Render_template is used to render the html pages
from flask import Blueprint, render_template

views = Blueprint('views',__name__)

# Create routes

# Create Home route
@views.route('/')
def home():
  return render_template("home.html")