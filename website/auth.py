# Blueprint is used to sort our routes
from flask import Blueprint

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
  return "<p> login </p>"

@auth.route('/logout')
def logout():
  return "<p> logout </p>"

@auth.route('/sign-up')
def signup():
  return "<p> signup </p>"