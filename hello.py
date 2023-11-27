from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/index')
def index():
    return 'Index Page'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'    

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/Apple')
def Apple():
    return render_template('Apple.html')

@app.route('/page/app')
def pageAppInfo():
    appInfo = { # dict
        'id': 5,
        'name': 'Python - Flask',
        'version': '1.0.1',
        'author': 'Enoxs',
        'remark': 'Python - Web Framework'
    }
    return render_template('page.html', appInfo=appInfo, text="Python Flask !")

@app.route('/x')
def xInfo():
    xInfo = { # dict
        'name': 'John',
        'age': 30,
        'city': 'New York',
    }
    return render_template('x.html', appInfo=xInfo)