from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/users/<username>')
def show_user(username):
    return f'User: {username}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Login com Sucesso"
# handle login logic
    else: 
        return 'Tente outra vez'
        # show login form

from flask import request
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
# handle login logic

from flask import make_response, render_template
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
