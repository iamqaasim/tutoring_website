# Blueprint is used to sort our routes
from flask import Blueprint

views = Blueprint('views',__name__)

# Create routes

# Create Home route
@views.route('/')
def home():
  return "<h1>test</h1>"