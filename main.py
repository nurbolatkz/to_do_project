# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request
from db_manager import DatabaseManager
import re
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
db = DatabaseManager()

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.


@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        user =  db.get_user(username)
        if user:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            db.create_user(username, password, email)
            db.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(debug=True)
