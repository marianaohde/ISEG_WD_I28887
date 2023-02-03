from flask import Flask
from flask import make_response, render_template
from flask import request


app = Flask(__name__)

@app.route('/users/<username>')
def show_user(username):
    return f'User: {username}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']
# handle login logic


@app.route('/')
def index():
    response = make_response('Hello World!')
    response.headers['Content-Type'] = 'text/plain'
    return response

@app.route('/')
def index():
    name = request.form['username']
    return render_template ('index.html', name=name)

app.run()
