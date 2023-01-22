########################################################################################
######################          Import packages      ###################################
########################################################################################
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db

########################################################################################
# our main blueprint
main = Blueprint('main', __name__)

@main.route('/') # home page that return 'index'
@main.route('/index') # home page that return 'index'
def index():
    return render_template('index.html')

@main.route('/home') # home page that return 'index'
def home():
    return render_template('home.html')


@main.route('/profile') # profile page that return 'profile'
@login_required
def profile():
    return render_template('profile.html', Title=current_user.Title)

@main.route('/record') # record page that return 'profile'
@login_required
def record():
    return render_template('record.html', Title=current_user.Title)

app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    with app.app_context():
        db.create_all() # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode
