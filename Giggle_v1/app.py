from flask import Flask, render_template, request, jsonify, session, redirect, url_for
#from functools import wraps
#from flask_sqlalchemy import SQLAlchemy
#import sqlite3
#from flask_login import login_user
#from werkzeug.security import generate_password_hash, check_password_hash
import os
#from app import db

app = Flask(__name__)
app.secret_key = os.urandom(16) # set scret key

'''
class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    employees = db.relationship('User', backref='company', lazy=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(100))
    def check_password(self, password):
        return check_password_hash(self.password, password)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    password = db.Column(db.String(100))
    def check_password(self, password):
        return check_password_hash(self.password, password)

# create a decorator function to check if the user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
'''

#define routes

# serve the login page
@app.route("/")
def index():
    return render_template("login.html")

# if user clicks on login form submission
@app.route("/login", methods=["POST"])
def login():
    # get form data
    username = request.form["username"]
    password = request.form["password"]

    # check if username and password are valid
    # this is where you would use your database to check if the user exists and if the password is correct
    if username == "myusername" and password == "mypassword":
        # store user data in session
        session["username"] = username
        session["email"] = "myemail@example.com"

        # redirect to authenticate page where it determines whether its a user or company
        return redirect(url_for('authenticate'))
    else:
        # show error message
        error_message = "Invalid username or password. Please try again."
        return render_template("login.html", error=error_message)
        
# if user clicks on signup form submission
@app.route("/signup", methods=["POST"])
def signup():
    # once I sign up I am directed to the authenticate page
    return redirect(url_for('authenticate'))
        
# creates new login authentication point
@app.route("/authenticate", methods=["GET","POST"])
def authenticate():
    return redirect(url_for('upload_jobs'))
'''
    email = request.form['email']
    password = request.form['password']
    user_type = request.form['user_type']
    # redirect user to appropriate page based on user type
    if user_type == 'company':
        return redirect(url_for('upload_jobs'))
    else:
        return redirect(url_for('mood'))'''


# serve the upload jobs page
@app.route("/upload_jobs", methods=["GET"])
#@login_required
def upload_jobs():
    #if request.method == "GET":
        #job_title = request.form['job_title']
        #job_description = request.form['job_description']
        #job_payment = request.form['job_payment']
        #job_category = request.form['job_category']
        #job_location = request.form['job_location']
        #add_job(job_title, job_description, job_payment, job_category, job_location)
        #return redirect(url_for('index'))

    return render_template('upload_jobs.html')


# serve the mood page
@app.route("/mood")
#@login_required
def mood():
    return render_template("mood.html")

# call the javascript function jobs to display jobs on mood page
@app.route("/jobs", methods=["POST"])
def getjobs():
    mood = request.json["mood"]
    # perform some logic to get matching jobs based on mood
    matching_jobs = [
        {"title": "Job 1", "description": "This is job 1"},
        {"title": "Job 2", "description": "This is job 2"},
        {"title": "Job 3", "description": "This is job 3"},
    ]
    return jsonify(matching_jobs)


'''
@app.route('/profile')
@login_required
def profile():
    username = current_user.name
    email = current_user.email
    user_type = 'company' if isinstance(current_user, Company) else 'user'
    return render_template('profile.html', username=username, email=email, user_type=user_type)


@app.route('/select-mood', methods=['POST'])
@login_required
def select_mood():
    mood = request.form['mood']
    jobs = fetch_jobs(mood)
    return render_template('mood.html', mood=mood, jobs=jobs)

@app.route('/upload-jobs', methods=['GET', 'POST'])
@login_required
def upload_jobs():
    if request.method == 'POST':
        job_title = request.form['job_title']
        job_description = request.form['job_description']
        job_payment = request.form['job_payment']
        add_job(job_title, job_description, job_payment)
        return redirect(url_for('index'))

    return render_template('upload_jobs.html')

@app.route('/protected')
@login_required
def protected_route():
    return 'This page is protected!'


#initialize database
'''
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
db = SQLAlchemy(app)

def create_tables():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_type TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT,
            job_description TEXT,
            job_pay REAL,
            job_category TEXT,
            job_location TEXT,
            mood TEXT
        )
    """)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    pay = db.Column(db.Float, nullable=False)
    company_name = db.Column(db.String(200), nullable=False)
    company_email = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Job('{self.title}', '{self.company_name}', '{self.pay}')"


'''
if __name__ == "__main__":
    #db.create_all()
    app.run(debug=True)

