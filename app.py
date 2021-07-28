from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required
from models import *

app = Flask(__name__)
app.secret_key = 'super secret string'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:harvest1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

users = {'admin': {'password': 'admin1'}}

class User(UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user



@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template("harvest-login.html")

    email = request.form.get("email")
    if request.form.get("password") == users[email]['password']:
        user = User()
        user.id = email
        login_user(user)
        return redirect(url_for('index'))

@app.route('/')
@login_required
def handle_needs_login():
    flash("You have to be logged in to access this page.")
    return redirect(url_for('harvest-login', next=request.endpoint))

def form():
    return render_template('add-meal.html')

if __name__ == '__main__':
    app.run(debug=True)
