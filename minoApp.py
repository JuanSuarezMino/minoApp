from flask import Flask, render_template , flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
#from functools import wraps
import pygal # for graphs


app = Flask(__name__)

@app.route('/')
def home():
	return '<h1> I am home <h1>'




if __name__	== '__main__':
	app.run(debug=True, port=9000)

